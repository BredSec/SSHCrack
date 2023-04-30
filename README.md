# SSHCrack
Tool for cracking into SSH IoT devices with built in Shodan API capabilities for optimal automation. This is essentially my own Hydra clone with psuedo multi threading and Shodan API capabilities to attack large amounts of targets effeciently.

The idea came from a video by David Bombal interviewing with a hacker who's efforts were against the Russian Federation in assistance of Ukraine. He mainly hacked Russia's SCADA systems along with assistance from Shodan. My idea was to basically automate this process by iterating through a large number of targets utilizing python's pseudo multi threading for faster cracking.

Currently this tool is only developed for Windows operating systems and for SSH cracking. Future versions will include Linux compatability as well as other common ports.

**DISCLAIMER: Do Not Use This Tool For Any Illegal Purposes. I Am NOT Liable For Any Damages Caused By Using This Tool. This Is Purely For Educational And Learning Purposes.**

# Usage
Download using `sudo git clone https://github.com/BredSec/SSHCrack.git`

`cd SSHCrack`

Run Python script with `python3 sshcrack.py -h` for the help screen

