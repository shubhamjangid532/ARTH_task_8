import getpass
from com_fun import *
import os
def l_ansible_setup():
    while(1):
        os.system("tput setaf 1")
        ansible_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ((("setup" in ch2) or ("Setup" in ch2) or ("SETUP" in ch2)) and (("ansible" in ch2) or ("ANSIBLE" in ch2) or ("Ansible" in ch2))) :
            print("Installation may take 10 to 15 minutes and also depends upon your internet connection ")
            os.system("pip3 install ansible")
            a = os.system("ls /etc/ | grep ip.txt > garbage")
            if a != 0:
                os.system("touch /root/ip.txt")
            a = os.system("ls /etc/ | grep ansible > garbage")
            if a != 0:
                os.system("mkdir /etc/ansible")
                os.system('echo "[defaults]" > /etc/ansible/ansible.cfg')
                os.system('echo "inventory = /root/ip.txt" >> /etc/ansible/ansible.cfg')
                os.system('echo "host_key_checking = false" >> /etc/ansible/ansible.cfg')
            
            

        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) :
            IP = input("Enter IP of target :- ")
            username = input("Enter user Name of target :- ")
            passwd = getpass.getpass("Enter password of target :- ")
            print("Select target system :- ")
            while(1) :
                print("""
                    1. Windows
                    2. Linux

                    """)
                sys = input("Enter Your Choice :- ")
                if (("Win" in sys) or ("win" in sys) or ("WIN" in sys)) :
                    protocol = "winrm"
                    break
                elif (("LINUX" in sys) or ("linux" in sys) or ("Linux" in sys)) :
                    protocol = "ssh"
                    break
                else :
                    print("\t !Please Select A Valied Option! ")

            os.system('echo "{} ansible_user={} ansible_ssh_pass={} ansible_connection={}" >> /root/ip.txt'.format(IP,username,passwd,protocol))

        elif ((("show" in ch2) or ("Show" in ch2) or ("SHOW" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) : 
            cmd = "ansible all --list-hosts"
            os.system(cmd)
            
        elif ((("check" in ch2) or ("Check" in ch2) or ("Check" in ch2)) and (("conn" in ch2) or ("Conn" in ch2) or ("CONN" in ch2))) :     
            cmd = "ansible all -m ping"
            os.system(cmd)
            
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")

def r_ansible_setup(ip_add):
    while(1):
        os.system("tput setaf 1")
        ansible_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ((("setup" in ch2) or ("Setup" in ch2) or ("SETUP" in ch2)) and (("ansible" in ch2) or ("ANSIBLE" in ch2) or ("Ansible" in ch2))) :
            print("Installation may take 10 to 15 minutes and also depends upon your internet connection ")
            os.system("ssh {} pip3 install ansible".format(ip_add))
            a = os.system("ssh {} ls /etc/ | grep ip.txt > garbage".format(ip_add))
            if a != 0:
                os.system("ssh {} touch /root/ip.txt".format(ip_add))
            a = os.system("ssh {} ls /etc/ | grep ansible > garbage".format(ip_add))
            if a != 0:
                os.system("ssh {} mkdir /etc/ansible".format(ip_add))
                os.system('ssh {} echo "[defaults]" > /etc/ansible/ansible.cfg'.format(ip_add))
                os.system('ssh {} echo "inventory = /root/ip.txt" >> /etc/ansible/ansible.cfg'.format(ip_add))
                os.system('ssh {} echo "host_key_checking = false" >> /etc/ansible/ansible.cfg'.format(ip_add))
            
            

        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) :
            IP = input("Enter IP of target :- ")
            username = input("Enter user Name of target :- ")
            passwd = getpass.getpass("Enter password of target :- ")
            print("Select target system :- ")
            while(1) :
                print("""
                    1. Windows
                    2. Linux

                    """)
                sys = input("Enter Your Choice :- ")
                if (("Win" in sys) or ("win" in sys) or ("WIN" in sys)) :
                    protocol = "winrm"
                    break
                elif (("LINUX" in sys) or ("linux" in sys) or ("Linux" in sys)) :
                    protocol = "ssh"
                    break
                else :
                    print("\t !Please Select A Valied Option! ")

            os.system('ssh {} echo "{} ansible_user={} ansible_ssh_pass={} ansible_connection={}" >> /root/ip.txt'.format(ip_add,IP,username,passwd,protocol))

        elif ((("show" in ch2) or ("Show" in ch2) or ("SHOW" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) : 
            cmd = "ansible all --list-hosts"
            os.system("ssh {} {}".format(ip_add,cmd))
            
        elif ((("check" in ch2) or ("Check" in ch2) or ("Check" in ch2)) and (("conn" in ch2) or ("Conn" in ch2) or ("CONN" in ch2))) :     
            cmd = "ansible all -m ping"
            os.system("ssh {} {}".format(ip_add,cmd))
            
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")
            
