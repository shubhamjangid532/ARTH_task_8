import getpass
import os
def ansible_setup():
    while(1):
        os.system("tput setaf 1")
        print("""
        
            1. \t Setup Ansible in You system
            2. \t Add Target
            3. \t Show all target nodes
            4. \t Check Connectivity with target nodes
            5. \t Exit

        """) 
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ((("setup" in ch2) or ("Setup" in ch2) or ("SETUP" in ch2)) and (("ansible" in ch2) or ("ANSIBLE" in ch2) or ("Ansible" in ch2))) :
            os.system("pip3 install ansible")
            os.system("mkdir /etc/ansible")
            os.system("touch /root/ip.txt")
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
            
