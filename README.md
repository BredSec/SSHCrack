# SSHCrack
Tool for cracking into SSH IoT devices with built in Shodan API capabilities for optimal automation. This is essentially my own Hydra clone with psuedo multi threading and Shodan API capabilities to attack large amounts of targets effeciently.

The idea came from a video by David Bombal interviewing with a hacker who's efforts were against the Russian Federation in assistance of Ukraine. He mainly hacked Russia's SCADA systems along with assistance from Shodan. My idea was to basically automate this process by iterating through a large number of targets utilizing python's pseudo multi threading for faster cracking.

Currently this tool is only developed for Windows operating systems and for SSH cracking. Future versions will include Linux compatability as well as other common ports.

**DISCLAIMER: Do Not Use This Tool For Any Illegal Purposes. I Am NOT Liable For Any Damages Caused By Using This Tool. This Is Purely For Educational And Learning Purposes.**

# Usage
Download using `sudo git clone https://github.com/BredSec/SSHCrack.git`

Go to the directory `cd SSHCrack`

Run Python script with `python3 sshcrack.py -h` for the help screen
```
   _____ _____ _    _  _____ _____            _____ _  __
  / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /
 | (___| (___ | |__| | |    | |__) |   /  \ | |    | ' /
  \___ \___ \ |  __  | |    |  _  /   / /\ \| |    |  <
  ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \
 |_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\  v1.0

              Created by @BredSec

       Disclaimer: Developers not liable or responsible
       for misuse or damage caused by SSHCrack


usage: python sshcrack.py [-k --key <api key>] [-t --target <target name>] [-i --iplist <ip list>]
[-u --userlist <username list>] [-p --passlist <password list>] [-a --attack <attack method>]
[-o --output <output file name>] [-m --multi <thread number>] [-x] [-v --verbose]


-h --help                     | Display help menu of arguments and command use


-k --key <api key>            | Enter your Shodan API key here to enable Shodan searches
-t --target <target>          | Used to conduct an ssh search with shodan on a specified target
-i --iplist <ip list>         | Specify a file with a list of IPs to enumerate through and crack
-u --userlist <username list> | Specify a wordlist of usernames to enermate through
                              (default will be common default ssh logins)
-p --passlist <password list> | Specify a wordlist of passwords to enumerate through
                              (default will be common default ssh logins)
-a --attack <attack method>   | Method of attack (ssh, ftp)
-o --output <filename>        | Specify the name of an output file for successful logins
-m --multi <thread number>    | Number of threads to be used during cracking (default is one)
-x                            | X mode - runs cracking on all searched IPs immediately
-v --verbose                  | Verbose mode - display everything going on```
