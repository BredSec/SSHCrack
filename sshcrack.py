import shodan
import threading
import os
import paramiko
import sys
import getopt

shodanAPIKey = "8t0SrW5P3emGYkm2rvWzQmcDOSdToYUV"
api = shodan.Shodan(shodanAPIKey)

client = paramiko.SSHClient()
client.load_system_host_keys()
#client.look_for_keys(True)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

target = ""
iplist = ""
userlist = ""
passlist = ""
output = ""

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:i:u:p:o:", ["help", "target=", "iplist=", "userlist=", "passlist=", "output="])
    except getopt.GetoptError:
        print("   _____ _____ _    _  _____ _____            _____ _  __")
        print("  / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /")
        print(" | (___| (___ | |__| | |    | |__) |   /  \ | |    | ' / ")
        print("  \___ \___ \ |  __  | |    |  _  /   / /\ \| |    |  <  ")
        print("  ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \ ")
        print(" |_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\  v1.0\n")
        print("              Created by @BredSec")
        print("\n")
        print("       Disclaimer: Developers not liable or responsible")
        print("       for misuse or damage caused by SSHCrack")
        print("\n")
        print("usage: python sshcrack.py [-h --help] [-t --target <target name>] [-i --iplist <ip list>] \n[-u --userlist <username list>] [-p --passlist <password list>] [-o --output <output file name>]")
        print("\n")
        print("-h --help                     | Display help menu of arguments and command use")
        print("\n")
        print("-t --target <target>          | Used to conduct an ssh search with shodan on a specified target")
        print("-i --iplist <ip list>         | Specify a file with a list of IPs to enumerate through and crack")
        print("-u --userlist <username list> | Specify a wordlist of usernames to enermate through (default will be common default ssh logins)")
        print("-p --passlist <password list> | Specify a wordlist of passwords to enumerate through (default will be common default ssh logins)")
        print("-o --output <filename>        | Specify the name of an output file for successful logins")
        print("\n")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("   _____ _____ _    _  _____ _____            _____ _  __")
            print("  / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /")
            print(" | (___| (___ | |__| | |    | |__) |   /  \ | |    | ' / ")
            print("  \___ \___ \ |  __  | |    |  _  /   / /\ \| |    |  <  ")
            print("  ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \ ")
            print(" |_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\  v1.0\n")
            print("              Created by @BredSec")
            print("\n")
            print("       Disclaimer: Developers not liable or responsible")
            print("       for misuse or damage caused by SSHCrack")
            print("\n")
            print("usage: python sshcrack.py [-h --help] [-t --target <target name>] [-i --iplist <ip list>] \n[-u --userlist <username list>] [-p --passlist <password list>] [-o --output <output file name>]")
            print("\n")
            print("-h --help                     | Display help menu of arguments and command use")
            print("\n")
            print("-t --target <target>          | Used to conduct an ssh search with shodan on a specified target")
            print("-i --iplist <ip list>         | Specify a file with a list of IPs to enumerate through and crack")
            print("-u --userlist <username list> | Specify a wordlist of usernames to enermate through (default will be common default ssh logins)")
            print("-p --passlist <password list> | Specify a wordlist of passwords to enumerate through (default will be common default ssh logins)")
            print("-o --output <filename>        | Specify the name of an output file for successful logins")
            print("\n")

#take arguments for target search and ip, username, and password wordlists in a function
#set defaults if none specified and ask for confirmation

#use shodan to perform a search on ssh ports within target location
#add results to a file and ip list to an array

#use multithreading to run multiple instances of sshcracker for the different ips


def SSHConnect(ip, userList, passList):
    #load ip list
    #load username list
    #load password list

    #parse through usernames and try passwords for each ip addr

    #return with correct combination once succeeding to get in and add it to a file
    print("hi")

if __name__ == "__main__":
    main(sys.argv[1:])