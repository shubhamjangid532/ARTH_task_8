                            # Operation For local user

import os
from com_fun import *
import getpass
os.system("clear")


                                    # Basic Operation
def l_basicOperation():
    i = 1
    while (1) :
        os.system("tput setaf 1")
        print("You Select Basic Operation" , end = "\n\n")
        basic_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or (("date" in ch2) or ("Date" in ch2) or ("DATE" in ch2)) :
            os.system("date")

        elif ch2 == "2" or (("cal" in ch2) or ("Cal" in ch2) or ("CAL" in ch2)) :
            os.system("cal")
            
        elif ch2 == "3" or ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) or ("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)))) :
            os.system("whoami")

        elif ch2 == "4" or ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) ) and ((("dir" in ch2) or ("Dir" in ch2) or ("DIR" in ch2) or ("fol" in ch2) or ("Fol" in ch2) or ("FOL" in ch2)))) :
            os.system("pwd")
        
        elif ch2 == "5" or ((("list" in ch2) or ("List" in ch2) or ("LIST" in ch2)) and ((("file" in ch2) or ("File" in ch2) or ("FILE" in ch2)))) :
            os.system("ls")

        elif ch2 == "6" or ((("open" in ch2) or ("Open" in ch2) or ("OPEN" in ch2)) and (("editor" in ch2) or ("Editor" in ch2) or ("EDITOR" in ch2)))  :
            os.system("vim")

        elif ch2 == "7" or ((("cou" in ch2) or ("Cou" in ch2) or ("COU" in ch2)) and (("word" in ch2) or ("Word" in ch2) or "WORD" in ch2)) :

            fileName = input("Enter Name Of File Which You Want To Count : ")
            os.system("cat {} | wc".format(fileName))

        elif ch2 == "8" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")
    


                                    #Package Management

def l_packManagement():
    while (1):
        os.system("tput setaf 1")
        print("You Select Package Management" , end = "\n\n")
        pack_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Check : ")
            os.system("rpm -q {}".format(pack))
        
        elif ch2 == "2" or ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Install : ")
            x = os.system("rpm -q {}".format(pack))
            if x != 0 :
                print("""
                    In your System {} not installed yet.
                    So we download it first and it will take some time
                """.format(pack))
                os.system("dnf install {} -y".format(pack))
            else : 
                print("{} already in our system".format(pack))
        
        elif ch2 == "3" or (((("uni" in ch2) or ("Uni" in ch2) or ("Uni" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2))) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Uninstall : ")
            x = os.system("rpm -q {}".format(pack))
            if x == 0 :
                print("""
                    In your System {} installed .
                    So we remove it for you and it will take some time
                """.format(pack))
                os.system("dnf remove {} -y".format(pack))
        
        elif ch2 == "4" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")




                                    #UserManagement

def l_userManagement():
    while (1):
        print("You Select User Management" , end = "\n\n")
        os.system("tput setaf 1")
        user_menu()
        os.system("tput setaf 7")
        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("log" in ch2) or ("Log" in ch2) or ("LOG" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            os.system("whoami")
        
        elif ch2 == "2" or ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)) and (("name" in ch2) or ("Name" in ch2) or ("NAME" in ch2))) :
            os.system("ls /home/")
        
        elif ch2 == "3" or ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name : ")
            os.system("useradd {}".format(userName))
            os.system("passwd {}".format(userName))
            print("User added Successfuly")
        
        elif ch2 == "4" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) )and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which You want to Delete : ")
            os.system("userdel {}".format(userName))
            os.system("rm -rf /home/{}".format(userName))
            print("User Successfuly Remove")
        
        elif ch2 == "5" or (((("cha" in ch2) or ("Cha" in ch2) or ("CHA" in ch2)) or (("upd" in ch2) or ("Upd" in ch2) or ("UPD" in ch2)) )and (("pass" in ch2) or ("Pass" in ch2) or ("PASS" in ch2))) :
            userName = input("Enter User Name which user Password you want to change : ")
            os.system("passwd {}".format(userName))
            print("User Password Successfuly")
        
        elif ch2 == "6" or ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name : ")
            os.system("groupadd {}".format(grpName))
            print("User added Successfuly")
        
        elif ch2 == "7" or (((("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) )and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name which You Want To Delete : ")
            os.system("groupdel {}".format(grpName))
            print("User Deleted Successfuly")
        
        elif ch2 == "8" or ((("loc" in ch2) or ("Loc" in ch2) or ("LOC" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Lock : ")
            os.system("usermod -l")
        
        elif ch2 == "9" or ((("unl" in ch2) or ("Unl" in ch2) or ("UNL" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Unlock : ")
            os.system("usermod -u")
        
        elif ch2 == "10" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")


                                 #Networking

def l_Networking():
    while (1) :    
        print("You Select Networking " , end = "\n\n")
        os.system("tput setaf 1")
        net_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("check" in ch2) or ("Check" in ch2) or ("CHECK" in ch2)) and (("ip" in ch2) or ("Ip" in ch2) or ("IP" in ch2))) :
            os.system("ifconfig")
        
        elif ch2 == "2" or ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("httpd" in ch2) or ("Httpd" in ch2) or ("HTTPD" in ch2))) :
            i = os.system("rpm -q httpd")
            if i != 0 :
                print("""
                    In your System httpd not installed yet.
                    So we download it first and it will take some time
                """)
                os.system("dnf install httpd -y")
            else : 
                print("httpd already install in our system")
        
        elif ch2 == "3" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl start httpd")
        
        elif ch2 == "4" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl stop httpd")
        
        elif ch2 == "5" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl status httpd")
        
        elif ch2 == "6" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")


                                #Service Management
def l_serviceManagement():
    while (1) :
        print("You Select Services Management " , end = "\n\n")
        os.system("tput setaf 1")
        services_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl start httpd")
            os.system("systemctl stop firewalld")
        
        elif ch2 == "2" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl stop httpd")
        
        elif ch2 == "3" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl status httpd")
        
        elif ch2 == "4" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl start firewalld")
        
        elif ch2 == "5" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl stop firewalld")
        
        elif ch2 == "6" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl status firewalld")
        
        elif ch2 == "7" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl start docker")
        
        elif ch2 == "8" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl stop docker")
        
        elif ch2 == "9" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl status docker")
        
        elif ch2 == "10" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")



                                        # Docker Management

def l_dockerManagement():
    while (1) :
        print("You Select Docker Management " , end = "\n\n")
        os.system("tput setaf 1")
        docker_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("download" in ch2) or ("Download" in ch2) or ("DOWNLOAD" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            x = os.system("rpm -q docker-ce")
            if x != 0 :

                net = os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                if net != 0 :
                    print("Please Check Your Internet Connection And Try Again")
                else :
                    print("It Will Take Time According To Your Internet Speed" , end = "\n\n")
                    inst = os.system("dnf install docker-ce --nobest -y")
                    if inst != 0 :
                        print("Some Problem Occur Please Try Agian")
                    else :
                        os.system("firewall-cmd  --permanent --zone=public --add-masquerade")
                        os.system("firewall-cmd --reload")
                        os.system("systemctl restart docker")
                        print("Docker Successfully Install In Your System")


        elif ch2 == "2" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl start docker")
        
        elif ch2 == "3" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl status docker")
        
        elif ch2 == "4" or ((("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) and (("imag" in ch2) or ("Imag" in ch2) or ("IMAG" in ch2))) :
            os.system("docker images")
        
        elif ch2 == "5" or ((("launch" in ch2) or ("Launch" in ch2) or ("LAUN" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            name = input("Enter name which you want to give :- ")
            image = input("Enter image name :- ")
            tag = input("Enter Image tag :- ")
            os.system("docker run -dit --name {} {}:{}".format(name,image,tag))
        
        elif ch2 == "6" or ((("curr" in ch2) or ("Curr" in ch2) or ("CURR" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("docker ps")

        elif ch2 == "7" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("docker ps -a")
        
        elif ch2 == "8" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("one" in ch2) or ("One" in ch2) or ("ONE" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            name = input("Enter Name of Id of container which you want to remove :- ")
            os.system("docker rm -f {}".format(name))

        elif ch2 == "9" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("docker rm -f $(docker ps -aq)")

        elif ch2 == "10" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl stop docker")
        
        elif ch2 == "11" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")


                            # Permissions
def l_permission() :
    while (1) :

        os.system("tput setaf 1")
        permission_menu()
        os.system("tput setaf 7")
        opr = input("Enter Yor Requirment from the given operation :- ")
        if opr == "1" or (("give" in opr) or ("Give" in opr) or ("GIVE" in opr) and  ("file" in opr) or ("File" in opr) or ("FILE" in opr)) :
            user = input("Enter User type (user, group, other) :- ")

            if (("user" in user) or ("User" in user) or ("USER" in user)) :                                                               
                u = "u"
                per_opt()
                permission = input("Enter Which permission you want give to User : - ") 
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            else :
                print("No match found please try again")
            
        elif opr == "2" or (("re" in opr) or ("Re" in opr) or ("RE" in opr) and  ("file" in opr) or ("File" in opr) or ("FILE" in opr)) :
            user = input("Enter User type (user, group, other) :- ")

            if (("user" in user) or ("User" in user) or ("USER" in user)) :
                u = "u"
                per_opt()
                permission = input("Enter Which permission you want give to User : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt() 
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)                                                                                                              
            
            else :
                print("No match found please try again")
        
                

            
        elif opr == "3" or (("give" in opr) or ("Give" in opr) or ("GIVE" in opr) and  ("dir" in opr) or ("Dir" in opr) or ("DIR" in opr) or ("fol" in opr) or ("Fol" in opr) or ("FOL" in opr)) :
            user = input("Enter User type (user, group, other) :- ")

            if (("user" in user) or ("User" in user) or ("USER" in user)) :                                                               
                u = "u"
                per_opt()
                permission = input("Enter Which permission you want give to User : - ")
                fold_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter Folder path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,fold_name)
                print(cmd)
                os.system(cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                fold_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter Folder path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,fold_name)
                print(cmd)
                os.system(cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                fold_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter Folder path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,fold_name)
                print(cmd)
                os.system(cmd)                                                                                                               
            else :
                print("No match found please try again")

        elif opr == "4" or (("re" in opr) or ("Re" in opr) or ("RE" in opr) and  ("dir" in opr) or ("Dir" in opr) or ("DIR" in opr) or ("fol" in opr) or ("Fol" in opr) or ("FOL" in opr)) :
            user = input("Enter User type (user, group, other) :- ")

            if (("user" in user) or ("User" in user) or ("USER" in user)) :                                                               
                u = "u"
                per_opt()
                permission = input("Enter Which permission you want give to User : - ")
                file_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system(cmd)

            
            
            else :
                print("No match found please try again")
            
        elif opr == "5" or (("exit" in opr) or ("quit" in opr) or ("Exit" in opr) or ("Quit" in opr)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                             # Ansible
def l_ansible_setup():
    while(1):
        os.system("tput setaf 1")
        ansible_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("setup" in ch2) or ("Setup" in ch2) or ("SETUP" in ch2)) and (("ansible" in ch2) or ("ANSIBLE" in ch2) or ("Ansible" in ch2))) :
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
            
            

        elif ch2 == "2" or ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) :
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
                if sys == "1" or (("Win" in sys) or ("win" in sys) or ("WIN" in sys)) :
                    protocol = "winrm"
                    break
                elif sys == "2" or (("LINUX" in sys) or ("linux" in sys) or ("Linux" in sys)) :
                    protocol = "ssh"
                    break
                else :
                    print("\t !Please Select A Valied Option! ")

            os.system('echo "{} ansible_user={} ansible_ssh_pass={} ansible_connection={}" >> /root/ip.txt'.format(IP,username,passwd,protocol))

        elif ch2 == "3" or ((("show" in ch2) or ("Show" in ch2) or ("SHOW" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) : 
            cmd = "ansible all --list-hosts"
            os.system(cmd)
            
        elif ch2 == "4" or ((("check" in ch2) or ("Check" in ch2) or ("Check" in ch2)) and (("conn" in ch2) or ("Conn" in ch2) or ("CONN" in ch2))) :     
            cmd = "ansible all -m ping"
            os.system(cmd)
            
        elif ch2 == "5" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                            # AWS Management

def l_aws():
    while (1) :
        print("You Selected Amazon Web Services " , end = "\n\n")
        os.system("tput setaf 1")
        aws_menu()
        os.system("tput setaf 7")

        choice = input("Enter Your Choice : ")

        if choice == "1" or ((("login" in choice) or ("Login" in choice) or ("LOGIN" in choice)) and (("acc" in choice) or ("Acc" in choice) or ("ACC" in choice))) :
            os.system("aws configure")
            print("logined")

        elif choice == "2" or ((("Create" in choice) or ("create" in choice)) and (("CREATE" in choice) or ("key" in choice) or ("Key" in choice) or ("KEY" in choice))):
            keyname = input("Enter the new key name : ")
            os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
            print("Key pair created")
        
        elif choice == "3" or ((("list" in choice) or ("List" in choice)) and (("LIST" in choice)) and (("key" in choice) or ("Key" in choice) or ("KEY" in choice))):
            os.system("aws ec2 describe-key-pairs")
        
        elif choice == "4" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("sec" in choice) or ("Sec" in choice) or ("SEC" in choice))):
            sgname = input("Enter the sg name : ")
            description = input("Give the Description : ")
            vpc = input("Enter the vpc ID : ")
            os.system("aws ec2 create-security-group --group-name {0} --description {1} --vpc-id {2}".format(sgname,description,vpc))
        
        elif choice == "5" or ((("add" in choice) or ("Add" in choice) or ("ADD" in choice)) and (("Inbound" in choice) or ("inbound" in choice) or ("INBOUND" in choice))):
            sgname = input("Enter the sg name : ")
            protocol = input("Enter the protocol : ")
            port = input("Enter the port number : ")
            cidr = input("Enter the cidr block : ")
            os.system("aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3} ".format(sgname,protocol,port,cidr))
        
        elif choice == "6" or ((("des" in choice) or ("Des" in choice) or ("DES" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            os.system("aws ec2 describe-instances")
        
        elif choice == "7" or ((("start" in choice) or ("Start" in choice) or ("START" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to start : ")
            os.system("aws ec2 start-instances --instance-ids {}".format(instID))
        
        elif choice == "8" or ((("stop" in choice) or ("Stop" in choice) or ("STOP" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to stop : ")
            os.system("aws ec2 stop-instances --instance-ids {}".format(instID))
        
        elif choice == "9" or ((("ter" in choice) or ("Ter" in choice) or ("TER" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to Terminate : ")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(instID))
        
        elif choice == "10" or ((("launch" in choice) or ("Launch" in choice) or ("LAUNCH" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            amiID = input("Enter the AMI ID : ")
            itype = input("Enter the instance type : ")
            sgID = input("Enter the security-group-ID to attach: ")
            subnetID = input("Enter the Subnet ID : ")
            count = input("Enter the number of instances to launch : ")
            keypair = input("Enter the key-pair to attach : ")
            while(1):    
                ch1 = input("""Do You Want To add User Data File 1to run scripts : 
                    1. Yes
                    2. No
                choice: """)
                if ch1 == "1" or (("yes" in ch1) or ("YES" in ch1) or ("Yes" in ch1)) :
                    userData = input("Enter the local path of user data file : ")
                    os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --security-group-ids {2} --subnet-id {3} --count {4} --key-name {5} --user-data=file://{6}".format(amiID,itype,sgID,subnetID,count,keypair,userData))
                    break
                elif ch1 == "2" or (("no" in ch1) or ("NO" in ch1) or ("No" in ch1)):
                    os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --security-group-ids {2} --subnet-id {3} --count {4} --key-name {5} ".format(amiID,itype,sgID,subnetID,count,keypair))
                    break
                else:
                    print("Invalid choice")

        elif choice == "11" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            size = input("Enter the size of volume in gb : ")
            vtype = input("Enter the volume type : ")
            az = input("Enter the Availibilty zone : ")
            os.system("aws ec2 create-volume --size {0} --volume-type {1} --availability-zone {2} ".format(size,vtype,az))
        
        elif choice == "12" or ((("Delete" in choice) or ("Delete" in choice) or ("DELETE" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            os.system("aws ec2 delete-volume --volume-id {}".format(volID))
        
        elif choice == "13" or ((("detach" in choice) or ("Detach" in choice) or ("DETACH" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            os.system("aws ec2 detach-volume --volume-id {}".format(volID))
        
        elif choice == "14" or ((("attach" in choice) or ("Attach" in choice) or ("ATTACH" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            instID = input("Enter the instance ID : ")
            os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(volID,instID))
        
        elif choice == "15" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("s3" in choice) or ("S3" in choice) or ("bucket" in choice) or ("Bucket" in choice) or ("BUCKET" in choice))):
            bucketName = input("Enter the bucket name : ")
            region = input("Enter the region : ")
            access = input("Enter the permission : ")
            lc = input("Enter the location constraint : ")
            os.system("aws s3api create-bucket --bucket {0} --region {1} --ac {2} --create-bucket-configuration LocationConstraint={3}".format(bucketName,region,access,lc))
        
        elif choice == "16" or ((("copy" in choice) or ("COPY" in choice) or ("Copy" in choice)) and (("s3" in choice) or ("S3" in choice) or ("bucket" in choice) or ("Bucket" in choice) or ("BUCKET" in choice))):
            path = input("Enter the local path of file to upload : ")
            bucketName = input("Enter the bucket name to upload : ")
            fileName = input("Enter the File name to save as : ")
            access = input("Enter the permission : ")
            os.system("aws s3 cp {0} s3://{1}/{2}.jpg --ac {3} ".format(path,bucketName,fileName,access))
        
        elif choice == "17" or ((("Create" in choice) or ("create" in choice)) and (("CREATE" in choice) or ("cloud" in choice) or ("Cloud" in choice) or ("CLOUD" in choice))):
            origin = input("Enter the origin domain name : ")
            os.system("aws cloudfront create-distribution --origin-domain-name {}".format(origin))
        
        elif choice == "18" or (("exit" in choice) or ("quit" in choice) or ("Exit" in choice) or ("Quit" in choice) or ("QUIT" in choice) or ("EXIT" in choice)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")    
