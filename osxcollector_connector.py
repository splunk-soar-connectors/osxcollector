# File: osxcollector_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2016-2017
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

# Phantom App Imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# Import Local
from osxcollector_consts import *

import os
os.sys.path.insert(0, "{}/paramikossh".format(os.path.dirname(os.path.abspath(__file__))))  # noqa
import paramiko
import socket
import simplejson as json
import time
import tarfile


class OSXCollectorConnector(BaseConnector):

    REMOTE_TMP_PATH = "/tmp/phantom/"
    VAULT_PATH = "/vault/tmp/"

    ACTION_ID_GET_SYSTEM_INFO = "get_system_info"

    def __init__(self):
        super(OSXCollectorConnector, self).__init__()

        self._ssh_client = None
        self._shell_channel = None

    def _start_connection(self, endpoint, action_result):
        """ Start SSH Connection with endpoint
        """
        config = self.get_config()
        user = config[OSXC_JSON_USERNAME]
        password = config.get(OSXC_JSON_PASSWORD, None)
        rsa_key_file = config.get(OSXC_JSON_RSA_KEY, None)
        if rsa_key_file is None and password is None:
            return action_result.set_status(phantom.APP_ERROR, "Need to specify either password or RSA key")
        if rsa_key_file:
            try:
                key = paramiko.RSAKey.from_private_key_file("/home/phantom-worker/.ssh/{}".format(rsa_key_file))
                password = None
            except Exception as e:
                return action_result.set_status(phantom.APP_ERROR, OSXC_ERR_CONNECTION_FAILED, e)
        else:
            key = None

        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.save_progress(phantom.APP_PROG_CONNECTING_TO_ELLIPSES, endpoint)
        try:
            self._ssh_client.connect(hostname=endpoint, username=user, pkey=key,
                    password=password, allow_agent=False, look_for_keys=True,
                    timeout=30)
        except Exception as e:
            return action_result.set_status(phantom.APP_ERROR, OSXC_ERR_CONNECTION_FAILED, e)

        # Mac sure its a mac
        cmd = "uname -a"
        status_code, stdout, exit_status = self._send_command(cmd, action_result)

        # Couldn't send command
        if (phantom.is_fail(status_code)):
            return action_result.set_status(phantom.APP_ERROR, "Unable to verify OS")

        # Some version of mac
        if (exit_status == 0 and stdout.split()[0] != "Darwin"):
            return action_result.set_status(phantom.APP_ERROR, "Need to connect to a Mac")

        return phantom.APP_SUCCESS

    def _send_command(self, command, result, passwd="", timeout=0):
        """
           Args:
               command: command to send
               result:  object used to store the status
               passwd:  password, if command needs to be run with root
        """
        try:
            output = ""
            trans = self._ssh_client.get_transport()
            self._shell_channel = trans.open_session()
            self._shell_channel.get_pty()
            self._shell_channel.set_combine_stderr(True)
            self._shell_channel.exec_command(command)
            result, data, exit_status = self._get_output(result, timeout, passwd)
            if (phantom.is_fail(result.get_status())):
                return (result.set_status(phantom.APP_ERROR, result.get_message()), None, None)
            output += data
            output = self._clean_stdout(output, passwd)
        except Exception as e:
            return (result.set_status(phantom.APP_ERROR, OSXC_ERR_SHELL_SEND_COMMAND, e, command),
                    None, None)

        return (result.set_status(phantom.APP_SUCCESS, OSXC_SUCC_CMD_EXEC),
                output, exit_status)

    def _get_output(self, result, timeout, passwd):
        sendpw = True
        self._shell_channel.settimeout(2)
        output = ""
        i = 1
        stime = int(time.time())
        self.save_progress("Executing command")
        try:
            while True:
                ctime = int(time.time())
                if (self._shell_channel.recv_ready()):
                    output += self._shell_channel.recv(8192)
                    # This is pretty messy but it's just the way it is I guess
                    if (sendpw and passwd):
                        try:
                            self._shell_channel.send("{}\n".format(passwd))
                        except socket.error:
                            pass
                        sendpw = False
                # Exit status AND nothing left in output
                elif (self._shell_channel.exit_status_ready() and not self._shell_channel.recv_ready()):
                    break
                elif (timeout and ctime - stime >= timeout):
                    result.set_status(phantom.APP_ERROR, "Error: Timeout")
                    return (result, None, None)
                else:
                    time.sleep(1)
                    self.send_progress("Executing command" + "." * i)
                    i = i % 5 + 1
        except Exception as e:
            result.set_status(phantom.APP_ERROR, str(e))
            return (result, None, None)
        result.set_status(phantom.APP_SUCCESS)
        return (result, output, self._shell_channel.recv_exit_status())

    def _clean_stdout(self, stdout, passwd):
        if (stdout is None):
            return None

        try:
            lines = stdout.splitlines()
            while (True):
                if (passwd and passwd in lines[0]):
                    lines.pop(0)
                    continue
                if ("[sudo] password for" in lines[0]):
                    lines.pop(0)
                    continue
                if (lines[0] == ""):
                    lines.pop(0)
                    continue
                break
        except:
            return None

        return ('\n'.join(lines))

    def _upload_osxcollector(self, action_result):

        file_path = "{}/osxc/osxcollector/osxcollector.py".format(os.path.dirname(os.path.abspath(__file__)))
        try:
            self._sftp.mkdir(self.REMOTE_TMP_PATH)
        except:
            pass
        try:
            self._sftp.put(file_path, self.REMOTE_TMP_PATH + "osxcollector.py")
        except:
            return action_result.set_status(phantom.APP_ERROR, "Unable to upload osxcollector")
        return phantom.APP_SUCCESS

    def _run_osxcollector(self, action_result):

        # The original osxcollector has been changed to always output in
        #  /tmp/phantom
        # You need to change that file if you want to use a different directory
        cd_cmd = 'cd {} ; '.format(self.REMOTE_TMP_PATH)
        cmd = 'sudo -k python2.7 /tmp/phantom/osxcollector.py {}'.format(self._param_string)
        config = self.get_config()
        passwd = config.get(OSXC_JSON_PASSWORD, None)
        root = config.get(OSXC_JSON_ROOT, False)
        if root:
            passwd = None
        if not root and  passwd is None:
            return action_result.set_status(phantom.APP_ERROR, OSXC_ERR_NEED_PW_FOR_ROOT)

        # Since the output is always in the current working directory, we want to cd into our tmp directory first
        status_code, stdout, exit_status = self._send_command(cd_cmd + cmd, action_result, passwd=passwd)
        if (phantom.is_fail(status_code)):
            return action_result.get_status()
        self.debug_print("STDOUT", stdout)
        # This is a bit cowboyish but I can't think of a better way
        self._out_file = stdout.splitlines()[2].split()[-1]
        return phantom.APP_SUCCESS

    def _get_file(self, action_result):
        remote_file = self.REMOTE_TMP_PATH + self._out_file
        local_file = self.VAULT_PATH + self._out_file
        self.debug_print("FILE", self._out_file)
        try:
            self._sftp.get(remote_file, local_file)
            self._sftp.remove(remote_file)
            tar = tarfile.open(local_file, 'r:gz')
            tar.extractall(path=self.VAULT_PATH)
            tar.close()
        except:
            return action_result.set_status(phantom.APP_ERROR, "Error extracting json file")
        return phantom.APP_SUCCESS

    def _get_contents(self, action_result):
        data = {}
        total_entries = 0
        # data['warnings'] = []  # Create own section for warnings (mostly because warnings will break the code otherwise)
        warnings = []
        base_name = self._out_file.split('.')[0]  # Ignore the .tar.gz
        try:
            with open("{}/{}/{}".format(self.VAULT_PATH, base_name, base_name + ".json"), 'r') as f:
                for line in f.read().splitlines():
                    total_entries += 1
                    j = json.loads(line)
                    section = j['osxcollector_section']
                    # These warnings mean that it couldn't find the the directory that it uses
                    #  for some of the information.
                    if 'osxcollector_warn' in j:
                        warnings.append(j)
                        continue
                    if 'osxcollector_subsection' in j:
                        subsection = j['osxcollector_subsection']
                    else:
                        subsection = None
                    if section not in data:
                        if subsection:
                            data[section] = {}
                        else:
                            data[section] = []
                    if subsection:
                        if subsection not in data[section]:
                            data[section][subsection] = []
                        data[section][subsection].append(j)
                    else:
                        data[section].append(j)
        except:
            # This should /hopefully/ never happen
            return action_result.set_status(phantom.APP_ERROR, "Error parsing json file")
        if warnings:
            data['warnings'] = warnings
        action_result.add_data(data)
        action_result.update_summary({'total_entries': total_entries})
        return action_result.set_status(phantom.APP_SUCCESS, "Successfully parsed json data")

    def _parse_sections(self, param, action_result):
        """ Validate sections """
        """ Ontop of doing something which osxcollector doesn't do, this can stop
            potential string injection vulnerabilities
        """
        invalid_sections = []
        self._param_string = ""
        if OSXC_JSON_SECTIONS not in param:
            return phantom.APP_SUCCESS
        for section in param[OSXC_JSON_SECTIONS].split(','):
            section = section.strip()
            if section in OSXC_VALID_SECTIONS:
                self._param_string += "-s {} ".format(section)
            else:
                invalid_sections.append(section)
        if invalid_sections:
            return action_result.set_status(phantom.APP_ERROR, "Invalid sections: {}".format(", ".join(invalid_sections)))
        else:
            return phantom.APP_SUCCESS

    def _test_connectivity(self, param):

        self.save_progress("Testing SSH connection")

        try:
            endpoint = self.get_config()['test_device']
        except:
            return self.set_status(phantom.APP_ERROR, "Need to specify a hostname or IP to connect to")

        ret_val = self._start_connection(endpoint, ActionResult())
        if (phantom.is_fail(ret_val)):
            return self.set_status_save_progress(phantom.APP_ERROR, OSXC_ERR_CONNECTIVITY_TEST)

        return self.set_status_save_progress(phantom.APP_SUCCESS, OSXC_SUCC_CONNECTIVITY_TEST)

    def _osx_collect(self, param):

        action_result = self.add_action_result(ActionResult(dict(param)))
        endpoint = param[OSXC_JSON_IP_HOSTNAME]
        ret_val = self._start_connection(endpoint, action_result)
        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # OSXcollector doesn't actually care if you put in valid sections
        # So we validate and parse them here
        ret_val = self._parse_sections(param, action_result)
        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Upload the osx collector file
        self._sftp = self._ssh_client.open_sftp()
        ret_val = self._upload_osxcollector(action_result)
        if (phantom.is_fail(ret_val)):
            return action_result.get_status()
        ret_val = self._run_osxcollector(action_result)
        if (phantom.is_fail(ret_val)):
            return action_result.get_status()
        ret_val = self._get_file(action_result)
        if (phantom.is_fail(ret_val)):
            return action_result.get_status()
        ret_val = self._get_contents(action_result)
        return ret_val

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        action_id = self.get_action_identifier()

        if (action_id == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY):
            ret_val = self._test_connectivity(param)
        elif (action_id == self.ACTION_ID_GET_SYSTEM_INFO):
            ret_val = self._osx_collect(param)

        return ret_val

if __name__ == '__main__':

    # import sys
    import pudb
    import sys
    pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))
        connector = OSXCollectorConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
