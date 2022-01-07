[comment]: # "Auto-generated SOAR connector documentation"
# OSXCollector

Publisher: Phantom  
Connector Version: 2\.0\.8  
Product Vendor: Yelp  
Product Name: OSXCollector  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 3\.0\.251  

Runs OSXCollector on an endpoint running OS X

[comment]: # "    File: readme.md"
[comment]: # "    Copyright (c) Phantom Cyber Corporation, 2017"
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## Root access permissions

If the user you are logging in is root (or is otherwise configured to not need to use sudo), then be
sure to check the "User is root" box in the asset configuration. Otherwise, you will need to provide
a password if you want to run commands that require root access even if an RSA key is specified, as
required by your sudoers configuration. If you incorrectly specify that the account is root, or if
you incorrectly enter a password in conjunction with an RSA key, then the action may indefinitely
hang.

## Key-based authentication

Refer to the following steps to install the authentication keys. Note that the key pair must be
unencrypted and generated using `     ssh-keygen    ` .

Connect to your Phantom instance and sudo to root, then change to the phantom-worker's home
directory.  

[![](img/1.png)](img/1.png)

Create a directory for the SSH keys (Note: You must give it the name .ssh), then move any private
key files into this directory. In this case, the file `     id_rsa    ` had been added to user's
home directory using scp. It is entirely possible to generate a new key pair from the Phantom VM
using `     ssh-keygen    ` as well.  
[![](img/2.png)](img/2.png)

Once the files are in the correct place, ownership must be set to phantom-worker.  

[![](img/3.png)](img/3.png)

Using the `     chown    ` command:  
[![](img/4.png)](img/4.png)

The RSA key should be ready to use in an SSH asset. Based on the above example, configure this by
specifying id_rsa as the RSA key file.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a OSXCollector asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**username** |  required  | string | Username
**root** |  optional  | boolean | User is root
**password** |  optional  | password | Password
**rsa\_key\_file** |  optional  | string | RSA Key file
**test\_device** |  optional  | string | Device IP/Hostname \(for TEST CONNECTIVITY only\)

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied credentials  
[get system info](#action-get-system-info) - Get information about a system using OSXCollector  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied credentials

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get system info'
Get information about a system using OSXCollector

Type: **investigate**  
Read only: **True**

This action will only work on an endpoint running OS X\.<br>This action will create a copy of the osxcollector\.py file in the endpoint's <code>/tmp/phantom</code> directory\.<br>Sections are a way to filter out the data\. For a list of sections, refer to this link\: <a href="https\://github\.com/Yelp/osxcollector">https\://github\.com/Yelp/osxcollector</a>\.<br>Due to the large amount of data and time involved, this app does not support running with the 'full\_hash' section\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip\_hostname** |  required  | Hostname/IP to investigate | string |  `ip`  `host name` 
**sections** |  optional  | A comma seperated list of sections | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.sections | string | 
action\_result\.parameter\.ip\_hostname | string |  `ip`  `host name` 
action\_result\.id | string | 
action\_result\.data\.\*\.kext\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.kext\.\*\.sha1 | string | 
action\_result\.data\.\*\.kext\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.kext\.\*\.ctime | string | 
action\_result\.data\.\*\.kext\.\*\.mtime | string | 
action\_result\.data\.\*\.kext\.\*\.file\_path | string | 
action\_result\.data\.\*\.kext\.\*\.signature\_chain\.\*\. | string | 
action\_result\.data\.\*\.kext\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.kext\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.kext\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.kext\.\*\.osxcollector\_bundle\_id | string | 
action\_result\.data\.\*\.kext\.\*\.osxcollector\_plist\_path | string | 
action\_result\.data\.\*\.kext\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.mail\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.mail\.\*\.sha1 | string | 
action\_result\.data\.\*\.mail\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.mail\.\*\.ctime | string | 
action\_result\.data\.\*\.mail\.\*\.mtime | string | 
action\_result\.data\.\*\.mail\.\*\.file\_path | string | 
action\_result\.data\.\*\.mail\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.mail\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.mail\.\*\.xattr\-quarantines\.\*\. | string | 
action\_result\.data\.\*\.mail\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.mail\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.mail\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.name | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.path | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.secure | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.host\_key | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.httponly | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.priority | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.persistent | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.expires\_utc | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.has\_expires | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.creation\_utc | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.firstpartyonly | numeric | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.encrypted\_value | string | 
action\_result\.data\.\*\.chrome\.cookies\.\*\.last\_access\_utc | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.id | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.url | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.title | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.hidden | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.favicon\_id | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.typed\_count | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.visit\_count | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.last\_visit\_time | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.from\_visit | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.segment\_id | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.transition | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.visit\_time | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.visit\_duration | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.term | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.url\_id | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.keyword\_id | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.lower\_term | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.etag | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.guid | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.hash | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.state | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.opened | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.tab\_url | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.end\_time | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.referrer | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.site\_url | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.by\_ext\_id | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.mime\_type | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.start\_time | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.by\_ext\_name | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.danger\_type | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.http\_method | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.target\_path | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.total\_bytes | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.current\_path | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.last\_modified | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.received\_bytes | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.interrupt\_reason | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.tab\_referrer\_url | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.original\_mime\_type | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.chain\_index | numeric | 
action\_result\.data\.\*\.chrome\.history\.\*\.name | string | 
action\_result\.data\.\*\.chrome\.history\.\*\.time\_slot | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.id | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.keyword | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.image\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.sync\_guid | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.short\_name | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.favicon\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.instant\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.new\_tab\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.suggest\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.usage\_count | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.date\_created | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.last\_modified | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.alternate\_urls | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.prepopulate\_id | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.input\_encodings | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.originating\_url | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.created\_by\_policy | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.safe\_for\_autoreplace | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.show\_in\_default\_list | numeric | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.image\_url\_post\_params | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.search\_url\_post\_params | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.instant\_url\_post\_params | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.suggest\_url\_post\_params | string | 
action\_result\.data\.\*\.chrome\.web\_data\.\*\.search\_terms\_replacement\_key | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.databases\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.url | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.title | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.at\_top | numeric | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.url\_rank | numeric | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.redirects | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.thumbnail | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.last\_forced | numeric | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.boring\_score | numeric | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.last\_updated | string | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.good\_clipping | numeric | 
action\_result\.data\.\*\.chrome\.top\_sites\.\*\.load\_completed | numeric | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.value | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.login\_data\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://clients2\.google\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://clients2\.googleusercontent\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://csync\.flickr\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://yahoogroups\.tumblr\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://search\.yahoo\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.yahoo\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://s\.yimg\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://geo\.yahoo\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://fonts\.googleapis\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://ssl\.google\-analytics\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://stats\.g\.doubleclick\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://scontent\.fsnc1\-2\.fna\.fbcdn\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://staticxx\.facebook\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://instagramstatic\-a\.akamaihd\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.facebook\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.instagram\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://cm\.g\.doubleclick\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://tpc\.googlesyndication\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://yt3\.ggpht\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://static\.doubleclick\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://pagead2\.googlesyndication\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://s\.ytimg\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.youtube\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://clients1\.google\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://s\.youtube\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://s0\.2mdn\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://ad\.doubleclick\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://accounts\.google\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://accounts\.youtube\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://fonts\.gstatic\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://content\.googleapis\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://googleads\.g\.doubleclick\.net\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://apis\.google\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.gstatic\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://ssl\.gstatic\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.google\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.googletagmanager\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.mozilla\.org\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.servers\.\*\.https\://www\.google\-analytics\.com\.supports\_spdy | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.net\.http\_server\_properties\.version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.apps\.shortcuts\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.media\.device\_id\_salt | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.top | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.left | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.right | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.bottom | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.maximized | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.always\_on\_top | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.work\_area\_top | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.work\_area\_left | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.work\_area\_right | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.browser\.window\_placement\.work\_area\_bottom | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.exit\_type | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.avatar\_index | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.exited\_cleanly | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.managed\_user\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.yahoo\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.yahoo\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.yahoo\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.yahoo\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.google\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.google\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.google\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.google\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.youtube\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.youtube\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.youtube\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.youtube\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.facebook\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.facebook\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.facebook\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.facebook\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.linkedin\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.linkedin\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.linkedin\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.linkedin\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.instagram\.com\:443,\*\.setting\.rawScore | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.instagram\.com\:443,\*\.setting\.pointsAddedToday | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.instagram\.com\:443,\*\.setting\.lastEngagementTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.exceptions\.site\_engagement\.https\://www\.instagram\.com\:443,\*\.setting\.lastShortcutLaunchTime | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.content\_settings\.pref\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.created\_by\_version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.profile\.avatar\_bubble\_tutorial\_shown | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.download\.directory\_upgrade | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.alerts\.initialized | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.app\.launch\.local\_path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.icons\.16 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.container | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.offline\_enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.manifest\.api\_console\_project\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.app\.urls\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.app\.launch\.web\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.icons\.16 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.app\.launch\.local\_path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.icons\.16 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.container | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.offline\_enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.manifest\.api\_console\_project\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.app\.urls\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.app\.launch\.web\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.background\.allow\_js\_access | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.options\_page | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.offline\_enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.granted\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.bepbmhgboaologfdajaanbcjmnhjmhfn\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.bepbmhgboaologfdajaanbcjmnhjmhfn\.disable\_reasons | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.app\.launch\.web\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.app\.launch\.container | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.app\.web\_content\.origin | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.app\.web\_content\.enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.chrome\_url\_overrides\.bookmarks | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.manifest\.content\_security\_policy | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.app\.launch\.local\_path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.icons\.16 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.container | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.offline\_enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.manifest\.api\_console\_project\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.running | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.app\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.app\.content\_security\_policy | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.icons\.32 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.icons\.64 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.display\_in\_launcher | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.manifest\.display\_in\_new\_tab\_page | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.storage\.managed\_schema | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.background\.persistent | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.content\_capabilities\.matches\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.content\_capabilities\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.externally\_connectable\.matches\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.minimum\_chrome\_version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.content\_security\_policy | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.manifest\.web\_accessible\_resources\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.granted\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.background\.persistent | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.permissions\.\*\.usbDevices\.\*\.vendorId | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.permissions\.\*\.usbDevices\.\*\.productId | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.externally\_connectable\.ids\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.externally\_connectable\.matches\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.manifest\.externally\_connectable\.accepts\_tls\_channel\_id | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.active\_permissions\.api\.\*\.usbDevices\.\*\.vendorId | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.active\_permissions\.api\.\*\.usbDevices\.\*\.productId | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.active\_permissions\.api\.\*\.usbDevices\.\*\.interfaceId | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.app\.urls\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.app\.launch\.web\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.manifest\.display\_in\_launcher | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.content\_scripts\.\*\.js\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.content\_scripts\.\*\.run\_at | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.content\_scripts\.\*\.matches\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.content\_scripts\.\*\.all\_frames | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.content\_security\_policy | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.manifest\.web\_accessible\_resources\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.active\_permissions\.scriptable\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.mime\_types\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.offline\_enabled | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.mime\_types\_handler | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.content\_security\_policy | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.manifest\.web\_accessible\_resources\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.background\.persistent | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.tts\_engine\.voices\.\*\.lang | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.tts\_engine\.voices\.\*\.gender | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.tts\_engine\.voices\.\*\.remote | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.tts\_engine\.voices\.\*\.voice\_name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.tts\_engine\.voices\.\*\.event\_types\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.incognito | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.background\.page | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.background\.persistent | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.manifest\.externally\_connectable\.matches\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.events\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.running | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.app\.background\.scripts\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.icons\.16 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.oauth2\.scopes\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.oauth2\.client\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.oauth2\.auto\_approve | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.display\_in\_launcher | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.minimum\_chrome\_version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.manifest\.display\_in\_new\_tab\_page | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.active\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.granted\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.granted\_permissions\.explicit\_host\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.initial\_keybindings\_set | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.path | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.location | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.app\.urls\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.app\.launch\.web\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.app\.launch\.container | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.key | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.icons\.128 | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.update\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.description | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.permissions\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.options\_page | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.current\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.default\_locale | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.manifest\.manifest\_version | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.lastpingday | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.ack\_external | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.install\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.page\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.from\_bookmark | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.from\_webstore | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.creation\_flags | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.active\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.granted\_permissions\.api\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.app\_launcher\_ordinal | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.was\_installed\_by\_oem | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia\.was\_installed\_by\_default | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.autoupdate\.next\_check | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.last\_chrome\_version | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.chrome\_url\_overrides\.bookmarks\.\*\.entry | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.extensions\.chrome\_url\_overrides\.bookmarks\.\*\.active | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.prefs\.preference\_reset\_time | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.google\.services\.username | string |  `user name` 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.google\.services\.account\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.google\.services\.last\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.google\.services\.last\_account\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.browser\.show\_home\_button | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.session\.startup\_urls | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.session\.restore\_on\_startup | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.homepage | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.aapocclcgogkmnckokdopfmhonfmgoek | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.ahfgeienlihckogmohjhadlkjgocpleb | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.aohghmighlieiainnegkcijnfilokake | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.apdfllckaahabafndbhieahigkjlhalf | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.bepbmhgboaologfdajaanbcjmnhjmhfn | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.blpcfgokakmgnkcojhhkbfbldkacnbeo | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.eemcgdkfndhakfknompkggombfjjjeno | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.felcaaldnbdncclmgdcncolpebgiejap | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.gfdkimpbcpahaombhbimeihdjnejgicl | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.ghbmnnjooekpmoecnnnilnnbdlolhkhi | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.kmendfapggjehodndflmmgagdbamhnfd | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.mfehgcgbbipciphmccgaenjidiccnmng | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.mfffpogegjflfpflabcdkioaeobkgjik | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.mhjfbmdgcfjbbpaeojofohoefgiehjai | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.neajdppkdcdipfabeoofebfddakdcjhd | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.nkeimhogjdpnpccoofpliimaahmaaome | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.nmmhkkegccagdldgiimedpiccmgmieda | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.extensions\.settings\.pjkljhegncpnkpknbcohdijeoejaedia | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.pinned\_tabs | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.safebrowsing\.incidents\_sent | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.homepage\_is\_newtabpage | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.default\_search\_provider\.name | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.default\_search\_provider\.keyword | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.default\_search\_provider\.search\_url | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.search\_provider\_overrides | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.protection\.macs\.default\_search\_provider\_data\.template\_url\_data | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.sync\_promo\.startup\_count | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.invalidator\.client\_id | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.last\_update\_date | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_via\_data\_reduction\_proxy\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_via\_data\_reduction\_proxy\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_via\_data\_reduction\_proxy\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_via\_data\_reduction\_proxy\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_via\_data\_reduction\_proxy\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_via\_data\_reduction\_proxy\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_via\_data\_reduction\_proxy\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_via\_data\_reduction\_proxy\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_with\_data\_reduction\_proxy\_enabled\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_https\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_with\_data\_reduction\_proxy\_enabled\_video | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_with\_data\_reduction\_proxy\_enabled\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_unknown\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_with\_data\_reduction\_proxy\_enabled\_unknown | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_original\_length\_with\_data\_reduction\_proxy\_enabled\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_long\_bypass\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_with\_data\_reduction\_proxy\_enabled\_application | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\.daily\_received\_length\_short\_bypass\_with\_data\_reduction\_proxy\_enabled\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.dns\_prefetching\.startup\_list\.\*\. | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.dns\_prefetching\.host\_referral\_list\.\*\. | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.dns\_prefetching\.host\_referral\_list\.\*\.\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.dns\_prefetching\.host\_referral\_list\.\*\.\.\*\.\.\*\. | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.password\_manager\.keychain\_migration | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.countryid\_at\_install | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\_lo\_fi\.was\_used\_this\_session | boolean | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\_lo\_fi\.load\_images\_requests\_per\_session | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.data\_reduction\_lo\_fi\.load\_images\_snackbars\_shown\_per\_session | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.account\_id\_migration\_state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.default\_apps\_install\_state | numeric | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.http\_original\_content\_length | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.http\_received\_content\_length | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.contents\.account\_tracker\_service\_last\_update | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.preferences\.\*\.osxcollector\_json\_file | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.preferences\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.key | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.chrome\.local\_storage\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryURL | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryPath | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryIdentifier | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryBookmarkBlob | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryDateAddedKey | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryDateFinishedKey | string | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryRemoveWhenDoneKey | boolean | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryProgressBytesSoFar | numeric | 
action\_result\.data\.\*\.safari\.downloads\.\*\.DownloadEntryProgressTotalToLoad | numeric | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.key | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.path | string | 
action\_result\.data\.\*\.safari\.localstorage\.\*\.origin | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.id | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.host | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.name | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.path | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.appId | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.expiry | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.isSecure | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.baseDomain | string |  `domain` 
action\_result\.data\.\*\.firefox\.cookies\.\*\.isHttpOnly | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.creationTime | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.lastAccessed | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.inBrowserElement | numeric | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.originAttributes | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.firefox\.cookies\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.id | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.url | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.guid | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.title | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.typed | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.hidden | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.frecency | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.rev\_host | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.favicon\_id | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.visit\_count | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.foreign\_count | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.last\_visit\_date | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.session | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.place\_id | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.from\_visit | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.visit\_date | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.visit\_type | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.host | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.prefix | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.fk | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.type | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.parent | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.position | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.dateAdded | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.keyword\_id | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.folder\_type | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.lastModified | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.data | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.mime\_type | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.expiration | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.name | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.flags | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.content | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.item\_id | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.anno\_attribute\_id | numeric | 
action\_result\.data\.\*\.firefox\.history\.\*\.idx | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.tbl | string | 
action\_result\.data\.\*\.firefox\.history\.\*\.stat | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.id | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.name | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.size | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.type | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.creator\.url | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.creator\.name | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.version | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.reviewURL | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.sourceURI | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.dailyUsers | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.developers\.\*\.url | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.developers\.\*\.name | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.supportURL | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.updateDate | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.description | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.homepageURL | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.reviewCount | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.learnmoreURL | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.averageRating | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.totalDownloads | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.fullDescription | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.weeklyDownloads | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.repositoryStatus | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.isPlatformCompatible | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.icons\.32 | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.icons\.64 | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.schema | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.osxcollector\_json\_file | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.seen | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.active | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.visible | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.location | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.syncGUID | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.bootstrap | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.skinnable | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.descriptor | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.appDisabled | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.installDate | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.softDisabled | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.userDisabled | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.defaultLocale\.name | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.defaultLocale\.description | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.foreignInstall | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.targetApplications\.\*\.id | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.targetApplications\.\*\.maxVersion | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.targetApplications\.\*\.minVersion | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.hasBinaryComponents | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.strictCompatibility | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.applyBackgroundUpdates | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.multiprocessCompatible | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.defaultLocale\.creator | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.icons\.48 | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.internalName | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.addons\.\*\.defaultLocale\.contributors\.\*\. | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.schemaVersion | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.final\-ui\-startup | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.quit\-application | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.profile\-after\-change | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.profile\-before\-change | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.profile\-change\-teardown | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.quit\-application\-granted | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.profile\-change\-net\-teardown | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.sessionstore\-windows\-restored | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.sessionstore\-final\-state\-write\-complete | boolean | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.created | numeric | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.chrome\://browser/content/browser\.xul\.main\-window\.sizemode | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.chrome\://browser/content/browser\.xul\.sidebar\-title\.value | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.chrome\://browser/content/browser\.xul\.navigator\-toolbox\.iconsize | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.chrome\://browser/content/browser\.xul\.titlebar\-placeholder\-on\-TabsToolbar\-for\-captions\-buttons\.width | string | 
action\_result\.data\.\*\.firefox\.json\_files\.\*\.contents\.chrome\://browser/content/browser\.xul\.titlebar\-placeholder\-on\-TabsToolbar\-for\-fullscreen\-button\.width | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.key | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.scope | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.value | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.originKey | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.originAttributes | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.firefox\.webapps\_store\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.sha1 | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.ctime | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.label | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.mtime | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.program | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.file\_path | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.signature\_chain\.\*\. | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.osxcollector\_plist | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.arguments\.\*\. | string | 
action\_result\.data\.\*\.startup\.launch\_agents\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.sha1 | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.ctime | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.mtime | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.file\_path | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.signature\_chain\.\*\. | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.osxcollector\_bundle\_id | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.osxcollector\_plist\_path | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.startup\.scripting\_additions\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.version\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.version\.\*\.osxcollector\_version | string | 
action\_result\.data\.\*\.version\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.gid\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.uid\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.home\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.names\.\*\.name | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.names\.\*\.is\_admin | boolean | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.shell\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.realname\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.generateduid\.\*\.name | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.generateduid\.\*\.is\_admin | boolean | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.accounts\.system\_users\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.accounts\.system\_admins\.\*\.admins\.\*\. | string | 
action\_result\.data\.\*\.accounts\.system\_admins\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.accounts\.system\_admins\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.accounts\.system\_admins\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_PK | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZNAME | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_ENT | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_OPT | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_1ACCESSKEYS | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_4OWNINGACCOUNTTYPES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZDATE | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZACTIVE | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZVISIBLE | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZUSERNAME | string |  `user name` 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZIDENTIFIER | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZACCOUNTTYPE | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZAUTHENTICATED | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZPARENTACCOUNT | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZCREDENTIALTYPE | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZOWNINGBUNDLEID | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZACCOUNTDESCRIPTION | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZAUTHENTICATIONTYPE | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZDATACLASSPROPERTIES | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZSUPPORTSAUTHENTICATION | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZLASTCREDENTIALRENEWALREJECTIONDATE | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_2ENABLEDACCOUNTS | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_7ENABLEDDATACLASSES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_2PROVISIONEDACCOUNTS | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_7PROVISIONEDDATACLASSES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZKEY | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZOWNER | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZVALUE | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZVISIBILITY | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZACCOUNTTYPEDESCRIPTION | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZENCRYPTACCOUNTPROPERTIES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZSUPPORTSMULTIPLEACCOUNTS | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.ZCREDENTIALPROTECTIONPOLICY | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_4SUPPORTEDTYPES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_7SUPPORTEDDATACLASSES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_4SYNCABLETYPES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_7SYNCABLEDATACLASSES | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_MAX | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_NAME | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_SUPER | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_UUID | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_PLIST | string | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_VERSION | numeric | 
action\_result\.data\.\*\.accounts\.social\_accounts\.\*\.Z\_CONTENT | string | 
action\_result\.data\.\*\.warnings\.\*\.osxcollector\_warn | string | 
action\_result\.data\.\*\.warnings\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.warnings\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.warnings\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.warnings\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.downloads\.downloads\.\*\.sha1 | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.downloads\.downloads\.\*\.ctime | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.mtime | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.file\_path | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.downloads\.downloads\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.downloads\.downloads\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.quarantines\.\*\.osxcollector\_db\_path | string | 
action\_result\.data\.\*\.quarantines\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineAgentName | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineTimeStamp | string | 
action\_result\.data\.\*\.quarantines\.\*\.osxcollector\_username | string |  `user name` 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineSenderName | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineTypeNumber | numeric | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineOriginAlias | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineOriginTitle | string | 
action\_result\.data\.\*\.quarantines\.\*\.osxcollector\_table\_name | string | 
action\_result\.data\.\*\.quarantines\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineDataURLString | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineSenderAddress | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineEventIdentifier | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineOriginURLString | string | 
action\_result\.data\.\*\.quarantines\.\*\.LSQuarantineAgentBundleIdentifier | string | 
action\_result\.data\.\*\.quarantines\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.quarantines\.\*\.sha1 | string | 
action\_result\.data\.\*\.quarantines\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.quarantines\.\*\.ctime | string | 
action\_result\.data\.\*\.quarantines\.\*\.mtime | string | 
action\_result\.data\.\*\.quarantines\.\*\.file\_path | string | 
action\_result\.data\.\*\.quarantines\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.quarantines\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.system\_info\.\*\.fde | boolean | 
action\_result\.data\.\*\.system\_info\.\*\.machine | string | 
action\_result\.data\.\*\.system\_info\.\*\.release | string | 
action\_result\.data\.\*\.system\_info\.\*\.sysname | string | 
action\_result\.data\.\*\.system\_info\.\*\.version | string | 
action\_result\.data\.\*\.system\_info\.\*\.nodename | string | 
action\_result\.data\.\*\.system\_info\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.system\_info\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.applications\.applications\.\*\.sha1 | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.sha2 | string |  `sha256` 
action\_result\.data\.\*\.applications\.applications\.\*\.ctime | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.mtime | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.file\_path | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.signature\_chain\.\*\. | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.extra\_data\_check | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.extra\_data\_found | boolean | 
action\_result\.data\.\*\.applications\.applications\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.osxcollector\_bundle\_id | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.osxcollector\_plist\_path | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.applications\.applications\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.date | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.displayName | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.processName | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.displayVersion | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.packageIdentifiers\.\*\. | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.osxcollector\_section | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.osxcollector\_subsection | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.osxcollector\_incident\_id | string | 
action\_result\.data\.\*\.applications\.install\_history\.\*\.contentType | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_entries | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 