# File: osxcollector_consts.py
#
# Copyright (c) 2016-2017 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
OSXC_JSON_DEVICE = "device"
OSXC_JSON_USERNAME = "username"
OSXC_JSON_PASSWORD = "password"
OSXC_JSON_RSA_KEY = "rsa_key_file"
OSXC_JSON_ROOT = "root"

OSXC_JSON_IP_HOSTNAME = "ip_hostname"
OSXC_JSON_SECTIONS = "sections"

OSXC_ERR_CONNECTION_FAILED = "Could not establish ssh connection to server"
OSXC_ERR_READ_FROM_SERVER_FAILED = "Read from device failed"
OSXC_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
OSXC_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
OSXC_ERR_NO_CONNECTION_ABORT = "Couldn't establish connection wtih server. Action aborted"
OSXC_ERR_SHELL_SEND_COMMAND = "On device execution of command '{}' failed"
OSXC_SUCC_CMD_EXEC = "Successfully executed command"
OSXC_ERR_FIREWALL_CMDS_NOT_SUPPORTED = "Firewall actions are not supported for OS X"
OSXC_ERR_NEED_PW_FOR_ROOT = "Unable to run commands that require root without a specified password"

OSXC_UNABLE_TO_PARSE_OUTPUT_OF_CMD = "Could not parse output of command '{}'"
OSXC_SHELL_NO_ERRORS = "Shell returned no errors"
OSXC_ERR_CMD_ERRORS = "Command executed but shell returned errors"
OSXC_SUCC_CMD_SUCCESS = "Command successfully executed and shell returned no errors"

OSXC_VALID_SECTIONS = [ "version",         "system_info",          "kext",
                        "startup",         "launch_agents",       "scripting_additions",
                        "startup_items",   "login_items",         "applications",
                        "install_history", "quarantines",         "downloads",
                        "email_downloads", "old_email_downloads", "chrome",
                        "history",         "archived_history",    "cookies",
                        "login_data",      "top_sites",           "web_data",
                        "databases",       "local_storage",       "preferences",
                        "firefox",         "formhistory",         "signons",
                        "addons",          "extension",           "content_prefs",
                        "health_report",   "webapps_store",       "json_files",
                        "safari",          "databases",           "localstorage",
                        "extension_files", "accounts",            "system_admins",
                        "system_users",    "social_accounts",     "recent_items",
                        "mail",            "full_hash" ]
