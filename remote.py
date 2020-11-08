                            # Operation For Remote user
import os 
import getpass
from com_fun import *
os.system("clear")

                                    # Basic Operation

def r_basicOperation(ip_add):
    i = 1
    while (1) :
        os.system("tput setaf 1")
        print("You Select Basic Operation" , end = "\n\n")
        basic_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or (("date" in ch2) or ("Date" in ch2) or ("DATE" in ch2)) :
            os.system("ssh {} date".format(ip_add))

        elif ch2 == "2" or (("cal" in ch2) or ("Cal" in ch2) or ("CAL" in ch2)) :
            os.system("ssh {} cal".format(ip_add))
            
        elif ch2 == "3" or ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) or ("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)))) :
            os.system("ssh {} whoami".format(ip_add))

        elif ch2 == "4" or ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) ) and ((("dir" in ch2) or ("Dir" in ch2) or ("DIR" in ch2) or ("fol" in ch2) or ("Fol" in ch2) or ("FOL" in ch2)))) :
            os.system("ssh {} pwd".format(ip_add))
        
        elif ch2 == "5" or ((("list" in ch2) or ("List" in ch2) or ("LIST" in ch2)) and ((("file" in ch2) or ("File" in ch2) or ("FILE" in ch2)))) :
            os.system("ssh {} ls".format(ip_add))

        elif ch2 == "6" or ((("open" in ch2) or ("Open" in ch2) or ("OPEN" in ch2)) and (("editor" in ch2) or ("Editor" in ch2) or ("EDITOR" in ch2)))  :
            os.system("ssh {} vi".format(ip_add))

        elif ch2 == "7" or ((("cou" in ch2) or ("Cou" in ch2) or ("COU" in ch2)) and (("word" in ch2) or ("Word" in ch2) or "WORD" in ch2)) :

            fileName = input("Enter Name Of File Which You Want To Count : ")
            os.system("ssh {} cat {} | wc".format(ip_add,fileName))

        elif ch2 == "8" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")
    


                                    #Package Management

def r_packManagement(ip_add):
    while (1):
        os.system("tput setaf 1")
        print("You Select Package Management" , end = "\n\n")
        pack_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Check : ")
            os.system("ssh {} rpm -q {}".format(ip_add,pack))
        
        elif ch2 == "2" or ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Install : ")
            x = os.system("ssh {} rpm -q {}".format(ip_add,pack))
            if x != 0 :
                print("""
                    In your System {} not installed yet.
                    So we download it first and it will take some time
                """.format(pack))
                os.system("ssh {} dnf install {} -y".format(ip_add,pack))
            else : 
                print("{} already in our system".format(pack))
        
        elif ch2 == "3" or (((("uni" in ch2) or ("Uni" in ch2) or ("Uni" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2))) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Uninstall : ")
            x = os.system("ssh {} rpm -q {}".format(ip_add,pack))
            if x == 0 :
                print("""
                    In your System {} installed .
                    So we remove it for you and it will take some time
                """.format(pack))
                os.system("ssh {} dnf remove {} -y".format(ip_add,pack))
        
        elif ch2 == "4" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")




                                    #UserManagement

def r_userManagement(ip_add):
    while (1):
        print("You Select User Management" , end = "\n\n")
        os.system("tput setaf 1")
        user_menu()
        os.system("tput setaf 7")
        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("log" in ch2) or ("Log" in ch2) or ("LOG" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            os.system("ssh {} whoami".format(ip_add))
        
        elif ch2 == "2" or ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)) and (("name" in ch2) or ("Name" in ch2) or ("NAME" in ch2))) :
            os.system("ssh {} ls /home/".format(ip_add))
        
        elif ch2 == "3" or ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name : ")
            os.system("ssh {} useradd {}".format(ip_add,userName))
            os.system("ssh {} passwd {}".format(ip_add,userName))
            print("User added Successfuly")
        
        elif ch2 == "4" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) )and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which You want to Delete : ")
            os.system("ssh {} userdel {}".format(ip_add,userName))
            os.system("ssh {} rm -rf /home/{}".format(ip_add,userName))
            print("User Successfuly Remove")
        
        elif ch2 == "5" or (((("cha" in ch2) or ("Cha" in ch2) or ("CHA" in ch2)) or (("upd" in ch2) or ("Upd" in ch2) or ("UPD" in ch2)) )and (("pass" in ch2) or ("Pass" in ch2) or ("PASS" in ch2))) :
            userName = input("Enter User Name which user Password you want to change : ")
            os.system("ssh {} passwd {}".format(ip_add,userName))
            print("User Password Successfuly")
        
        elif ch2 == "6" or ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name : ")
            os.system("ssh {} groupadd {}".format(ip_add,grpName))
            print("User added Successfuly")
        
        elif ch2 == "7" or (((("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) )and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name which You Want To Delete : ")
            os.system("ssh {} groupdel {}".format(ip_add,grpName))
            print("User Deleted Successfuly".format(ip_add))
        
        elif ch2 == "8" or ((("loc" in ch2) or ("Loc" in ch2) or ("LOC" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Lock : ")
            os.system("ssh {} usermod -l".format(ip_add))
        
        elif ch2 == "9" or ((("unl" in ch2) or ("Unl" in ch2) or ("UNL" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Unlock : ")
            os.system("ssh {} usermod -u".format(ip_add))
        
        elif ch2 == "10" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")


                                 #Networking

def r_Networking(ip_add):
    while (1) :    
        print("You Select Networking " , end = "\n\n")
        os.system("tput setaf 1")
        net_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("check" in ch2) or ("Check" in ch2) or ("CHECK" in ch2)) and (("ip" in ch2) or ("Ip" in ch2) or ("IP" in ch2))) :
            os.system("ssh {} ifconfig".format(ip_add))
        
        elif ch2 == "2" or ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("httpd" in ch2) or ("Httpd" in ch2) or ("HTTPD" in ch2))) :
            i = os.system("ssh {} rpm -q httpd".format(ip_add))
            if i != 0 :
                print("""
                    In your System httpd not installed yet.
                    So we download it first and it will take some time
                """)
                os.system("ssh {} dnf install httpd -y".format(ip_add))
            else : 
                print("httpd already install in our system")
        
        elif ch2 == "3" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl start httpd".format(ip_add))
        
        elif ch2 == "4" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl stop httpd".format(ip_add))
        
        elif ch2 == "5" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl status httpd".format(ip_add))
        
        elif ch2 == "6" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")


                                #Service Management
def r_serviceManagement(ip_add):
    while (1) :
        print("You Select Services Management " , end = "\n\n")
        os.system("tput setaf 1")
        services_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl start httpd".format(ip_add))
            os.system("ssh {} systemctl stop firewalld".format(ip_add))
        
        elif ch2 == "2" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl stop httpd".format(ip_add))
        
        elif ch2 == "3" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl status httpd".format(ip_add))
        
        elif ch2 == "4" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl start firewalld".format(ip_add))
        
        elif ch2 == "5" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl stop firewalld".format(ip_add))
        
        elif ch2 == "6" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl status firewalld".format(ip_add))
        
        elif ch2 == "7" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl start docker".format(ip_add))
        
        elif ch2 == "8" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl stop docker".format(ip_add))
        
        elif ch2 == "9" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl status docker".format(ip_add))
        
        elif ch2 == "10" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")



                                        # Docker Management
def r_dockerManagement(ip_add):
    while (1) :
        print("You Select Docker Management " , end = "\n\n")
        os.system("tput setaf 1")
        docker_menu()
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("download" in ch2) or ("Download" in ch2) or ("DOWNLOAD" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            x = os.system("ssh {} rpm -q docker-ce".format(ip_add))
            if x != 0 :

                net = os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                if net != 0 :
                    print("Please Check Your Internet Connection And Try Again")
                else :
                    print("It Will Take Time According To Your Internet Speed" , end = "\n\n")
                    inst = os.system("ssh {} dnf install docker-ce --nobest -y".format(ip_add))
                    if inst != 0 :
                        print("Some Problem Occur Please Try Agian")
                    else :
                        os.system("ssh {} firewall-cmd  --permanent --zone=public --add-masquerade".format(ip_add))
                        os.system("ssh {} firewall-cmd --reload".format(ip_add))
                        os.system("ssh {} systemctl restart docker".format(ip_add))
                        print("Docker Successfully Install In Your System")


        elif ch2 == "2" or ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl start docker".format(ip_add))
        
        elif ch2 == "3" or ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl status docker".format(ip_add))
        
        
        elif ch2 == "4" or ((("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) and (("imag" in ch2) or ("Imag" in ch2) or ("IMAG" in ch2))) :
            os.system("ssh {} docker images".format(ip_add))
        
        elif ch2 == "5" or ((("launch" in ch2) or ("Launch" in ch2) or ("LAUN"  in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            name = input("Enter name which you want to give :- ")
            image = input("Enter image name :- ")
            tag = input("Enter Image tag :- ")
            os.system("ssh {} docker run -dit --name {} {}:{}".format(ip_add,name,image,tag))
        
        elif ch2 == "6" or ((("curr" in ch2) or ("Curr" in ch2) or ("CURR" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker ps".format(ip_add))

        elif ch2 == "7" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker ps -a".format(ip_add))
        
        elif ch2 == "8" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("one" in ch2) or ("One" in ch2) or ("ONE" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            name = input("Enter Name of Id of container which you want to remove :- ")
            os.system("ssh {} docker rm -f {}".format(ip_add,name))

        elif ch2 == "9" or (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker rm -f $(docker ps -aq)".format(ip_add))

        elif ch2 == "10" or ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl stop docker".format(ip_add))

        elif ch2 == "11" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")

                            # Permissions
def r_permission(ip_add) :
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
                os.system("ssh {} {}",format(ip_add,cmd))

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

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
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt() 
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)                                                                                                              
            
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
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                fold_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter Folder path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,fold_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                fold_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter Folder path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,fold_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)                                                                                                               
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
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("group" in user) or ("Group" in user) or ("GROUP" in user)) :
                u = "g"
                per_opt()
                permission = input("Enter Which permission you want give to Group : - ")
                file_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

            elif (("other" in user) or ("Other" in user) or ("OTHER" in user)) :
                u = "o"
                per_opt()
                permission = input("Enter Which permission you want give to Other : - ")
                file_name = input("Enter Folder Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}-{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

            
            
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
def r_ansible_setup(ip_add):
    while(1):
        os.system("tput setaf 1")
        ansible_menu()
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ch2 == "1" or ((("setup" in ch2) or ("Setup" in ch2) or ("SETUP" in ch2)) and (("ansible" in ch2) or ("ANSIBLE" in ch2) or ("Ansible" in ch2))) :
            print("Installation may take 10 to 15 minutes and also depends upon your internet connection ")
            net = os.system("ssh {} pip3 install ansible".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
            a = os.system("ssh {} ls /etc/ | grep ip.txt > garbage".format(ip_add))
            if a != 0:
                os.system("ssh {} touch /root/ip.txt".format(ip_add))
            a = os.system("ssh {} ls /etc/ | grep ansible > garbage".format(ip_add))
            if a != 0:
                os.system("ssh {} mkdir /etc/ansible".format(ip_add))
                os.system('ssh {} echo "[defaults]" > /etc/ansible/ansible.cfg'.format(ip_add))
                os.system('ssh {} echo "inventory = /root/ip.txt" >> /etc/ansible/ansible.cfg'.format(ip_add))
                os.system('ssh {} echo "host_key_checking = false" >> /etc/ansible/ansible.cfg'.format(ip_add))
            
            

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
                if (("Win" in sys) or ("win" in sys) or ("WIN" in sys)) :
                    protocol = "winrm"
                    break
                elif (("LINUX" in sys) or ("linux" in sys) or ("Linux" in sys)) :
                    protocol = "ssh"
                    break
                else :
                    print("\t !Please Select A Valied Option! ")

            os.system('ssh {} echo "{} ansible_user={} ansible_ssh_pass={} ansible_connection={}" >> /root/ip.txt'.format(ip_add,IP,username,passwd,protocol))

        elif ch2 == "3" or ((("show" in ch2) or ("Show" in ch2) or ("SHOW" in ch2)) and (("target" in ch2) or ("Target" in ch2) or ("Target" in ch2))) : 
            cmd = "ansible all --list-hosts"
            os.system("ssh {} {}".format(ip_add,cmd))
            
        elif ch2 == "4" or ((("check" in ch2) or ("Check" in ch2) or ("Check" in ch2)) and (("conn" in ch2) or ("Conn" in ch2) or ("CONN" in ch2))) :     
            cmd = "ansible all -m ping"
            os.system("ssh {} {}".format(ip_add,cmd))
            
        elif ch2 == "5" or (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                            # AWS Management

def r_aws(ip_add):
    while (1) :
        print("You Selected Amazon Web Services " , end = "\n\n")
        os.system("tput setaf 1")
        aws_menu()
        os.system("tput setaf 7")

        choice = input("Enter Your Choice : ")

        if choice == "1" or ((("login" in choice) or ("Login" in choice) or ("LOGIN" in choice)) and (("acc" in choice) or ("Acc" in choice) or ("ACC" in choice))) :
            net = os.system("ssh {} aws configure".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
            print("logined")

        elif choice == "2" or ((("Create" in choice) or ("create" in choice)) and (("CREATE" in choice) or ("key" in choice) or ("Key" in choice) or ("KEY" in choice))):
            keyname = input("Enter the new key name : ")
            net = os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(ip_add,keyname))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
            print("Key pair created")
        
        elif choice == "3" or ((("list" in choice) or ("List" in choice)) and (("LIST" in choice)) and (("key" in choice) or ("Key" in choice) or ("KEY" in choice))):
            net = os.system("ssh {} aws ec2 describe-key-pairs".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        
        elif choice == "4" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("sec" in choice) or ("Sec" in choice) or ("SEC" in choice))):
            sgname = input("Enter the sg name : ")
            description = input("Give the Description : ")
            vpc = input("Enter the vpc ID : ")
            net = os.system("ssh {0} aws ec2 create-security-group --group-name {1} --description {2} --vpc-id {3}".format(ip_add,sgname,description,vpc))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "5" or ((("add" in choice) or ("Add" in choice) or ("ADD" in choice)) and (("Inbound" in choice) or ("inbound" in choice) or ("INBOUND" in choice))):
            sgname = input("Enter the sg name : ")
            protocol = input("Enter the protocol : ")
            port = input("Enter the port number : ")
            cidr = input("Enter the cidr block : ")
            net = os.system("ssh {0} aws ec2 authorize-security-group-ingress --group-name {1} --protocol {2} --port {3} --cidr {4} ".format(ip_add,sgname,protocol,port,cidr))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        elif choice == "6" or ((("des" in choice) or ("Des" in choice) or ("DES" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            net = os.system("ssh {} aws ec2 describe-instances".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        
        elif choice == "7" or ((("start" in choice) or ("Start" in choice) or ("START" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to start : ")
            net = os.system("ssh {} aws ec2 start-instances --instance-ids {}".format(ip_add,instID))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        
        elif choice == "8" or ((("stop" in choice) or ("Stop" in choice) or ("STOP" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to stop : ")
            net = os.system("ssh {} aws ec2 stop-instances --instance-ids {}".format(ip_add,instID))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        
        elif choice == "9" or ((("ter" in choice) or ("Ter" in choice) or ("TER" in choice)) and (("Insta" in choice) or ("insta" in choice) or ("INSTA" in choice))):
            instID = input("Enter the instances ID to Terminate : ")
            net = os.system("ssh {} aws ec2 terminate-instances --instance-ids {}".format(ip_add,instID))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
        
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
                    net = os.system("ssh {0} aws ec2 run-instances --image-id {1} --instance-type {2} --security-group-ids {3} --subnet-id {45} --count {5} --key-name {6} --user-data=file://{7}".format(ip_add,amiID,itype,sgID,subnetID,count,keypair,userData))
                    if net != 0 :
                        print("Please Check Your Internet Connection And Try Again")
                    break
                elif ch1 == "2" or (("no" in ch1) or ("NO" in ch1) or ("No" in ch1)):
                    net = os.system("ssh {0} aws ec2 run-instances --image-id {1} --instance-type {2} --security-group-ids {3} --subnet-id {4} --count {5} --key-name {6} ".format(ip_add,amiID,itype,sgID,subnetID,count,keypair))
                    if net != 0 :
                        print("Please Check Your Internet Connection And Try Again")
                    break
                else:
                    print("Invalid choice")

        elif choice == "11" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            size = input("Enter the size of volume in gb : ")
            vtype = input("Enter the volume type : ")
            az = input("Enter the Availibilty zone : ")
            net = os.system("ssh {0} aws ec2 create-volume --size {1} --volume-type {2} --availability-zone {3} ".format(ip_add,size,vtype,az))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "12" or ((("Delete" in choice) or ("Delete" in choice) or ("DELETE" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            os.system("ssh {} aws ec2 delete-volume --volume-id {}".format(ip_add,volID))
        
        elif choice == "13" or ((("detach" in choice) or ("Detach" in choice) or ("DETACH" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            net = os.system("ssh {} aws ec2 detach-volume --volume-id {}".format(ip_add,volID))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "14" or ((("attach" in choice) or ("Attach" in choice) or ("ATTACH" in choice)) and (("Vol" in choice) or ("vol" in choice) or ("VOL" in choice))):
            volID = input("Enter the volume ID : ")
            instID = input("Enter the instance ID : ")
            net = os.system("ssh {0} aws ec2 attach-volume --volume-id {1} --instance-id {2} --device /dev/sdf".format(ip_add,volID,instID))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "15" or ((("Create" in choice) or ("create" in choice) or ("CREATE" in choice)) and (("s3" in choice) or ("S3" in choice) or ("bucket" in choice) or ("Bucket" in choice) or ("BUCKET" in choice))):
            bucketName = input("Enter the bucket name : ")
            region = input("Enter the region : ")
            access = input("Enter the permission : ")
            lc = input("Enter the location constraint : ")
            net = os.system("ssh {0} aws s3api create-bucket --bucket {1} --region {2} --ac {3} --create-bucket-configuration LocationConstraint={4}".format(ip_add,bucketName,region,access,lc))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "16" or ((("copy" in choice) or ("COPY" in choice) or ("Copy" in choice)) and (("s3" in choice) or ("S3" in choice) or ("bucket" in choice) or ("Bucket" in choice) or ("BUCKET" in choice))):
            path = input("Enter the local path of file to upload : ")
            bucketName = input("Enter the bucket name to upload : ")
            fileName = input("Enter the File name to save as : ")
            access = input("Enter the permission : ")
            net = os.system("ssh {} aws s3 cp {0} s3://{1}/{2}.jpg --ac {3} ".format(ip_add,path,bucketName,fileName,access))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "17" or ((("Create" in choice) or ("create" in choice)) and (("CREATE" in choice) or ("cloud" in choice) or ("Cloud" in choice) or ("CLOUD" in choice))):
            origin = input("Enter the origin domain name : ")
            net = os.system("ssh {} aws cloudfront create-distribution --origin-domain-name {}".format(ip_add,origin))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

        elif choice == "18" or (("exit" in choice) or ("quit" in choice) or ("Exit" in choice) or ("Quit" in choice) or ("QUIT" in choice) or ("EXIT" in choice)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again") 

                            # Hadoop Management
def r_hadoop(ip_add):
    while (1) :
        print("You Selected Hadoop " , end = "\n\n")
        os.system("tput setaf 1")
        hadoop_menu()
        os.system("tput setaf 7")

        choice = input("Enter Your Choice : ")

        if choice == "1" or (("Download" in choice) or ("download" in choice) or ("DOWNLOAD" in choice)):
            print("It Will Take Time According To Your Internet Speed" , end = "\n\n")
            net = os.system("ssh {} wget https://github.com/shubhamjangid532/ARTH_task_8/raw/master/hadoop-1.2.1-1.x86_64.rpm".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")

            net = os.system("ssh {} wget https://github.com/shubhamjangid532/ARTH_task_8/raw/master/jdk-8u171-linux-x64.rpm".format(ip_add))
            if net != 0 :
                print("Please Check Your Internet Connection And Try Again")
            print("Downloaded")

        elif choice == "2" or ((("install" in choice) or ("Install" in choice) or ("INSTALL" in choice)) and (("hadoop" in choice) or ("Hadoop" in choice) or ("HADOOP" in choice))):
            x = os.system("ssh {} rpm -q jdk-8u171-linux-x86.rpm".format(ip_add))
            if x != 0 :
                os.system("ssh {} yum install jdk-8u171-linux-x86.rpm -y".format(ip_add))
            x = os.system("ssh {} rpm -q hadoop-1.2.1-1.x86_64.rpm")
            if x != 0 :
                os.system("ssh {} rpm -i hadoop-1.2.1-1.x86_64.rpm  --force".format(ip_add))
            print("Installed")
        elif choice == "3" or ((("conf" in choice) or ("Conf" in choice) or ("CONF" in choice)) and (("name" in choice) or ("Name" in choice) or ("NAME" in choice) or ("master" in choice) or ("Master" in choice) or ("MASTER" in choice))):
            ip = input("Enter Your IP : ")
            nn = input("Enter the name for NameNode Directory : ")
            os.system("ssh {} mkdir /{}".format(ip_add,nn))
            new_file = open("/etc/hadoop/core-site.xml","r")
            lines = new_file.readlines()
            lines[7] = "<property>\n"
            new_file = open("/etc/hadoop/core-site.xml", "w")
            new_file.writelines(lines)
            new_file.close()
            new_file = open("/etc/hadoop/core-site.xml","a")
            new_file.write("<name>fs.default.name</name>\n") 
            new_file.write("<value>hdfs://{}:9001</value>\n".format(ip))
            new_file.write("</property>\n")
            new_file.write("</configuration>\n")

            n_file = open("/etc/hadoop/hdfs-site.xml","r")
            line = n_file.readlines()
            line[7] = "<property>\n"
            n_file = open("/etc/hadoop/hdfs-site.xml", "w")
            n_file.writelines(line)
            n_file.close()
            n_file = open("/etc/hadoop/hdfs-site.xml","a")
            n_file.write("<name>dfs.name.dir</name>\n") 
            n_file.write("<value>/{}</value>\n".format(nn))
            n_file.write("</property>\n")
            n_file.write("</configuration>\n")
            print("NameNode setup Successfully")
            os.system("hadoop namenode -format")
            os.system("hadoop-daemon.sh start namenode")
            os.system("jps")
        elif choice == "4" or ((("conf" in choice) or ("Conf" in choice) or ("CONF" in choice)) and (("data" in choice) or ("Data" in choice) or ("DATA" in choice) or ("slave" in choice) or ("Slave" in choice) or ("SLAVE" in choice))):
            ip = input("Enter the NameNode's IP : ")
            dn = input("Enter the name for DataNode Directory : ")
            os.system("mkdir /{}".format(dn))
            new_file = open("/etc/hadoop/core-site.xml","r")
            lines = new_file.readlines()
            lines[7] = "<property>\n"
            new_file = open("/etc/hadoop/core-site.xml", "w")
            new_file.writelines(lines)
            new_file.close()
            new_file = open("/etc/hadoop/core-site.xml","a")
            new_file.write("<name>fs.default.name</name>\n") 
            new_file.write("<value>hdfs://{}:9001</value>\n".format(ip))
            new_file.write("</property>\n")
            new_file.write("</configuration>\n")

            n_file = open("/etc/hadoop/hdfs-site.xml","r")
            line = n_file.readlines()
            line[7] = "<property>\n"
            n_file = open("/etc/hadoop/hdfs-site.xml", "w")
            n_file.writelines(line)
            n_file.close()
            n_file = open("/etc/hadoop/hdfs-site.xml","a")
            n_file.write("<name>dfs.data.dir</name>\n") 
            n_file.write("<value>/{}</value>\n".format(dn))
            n_file.write("</property>\n")
            n_file.write("</configuration>\n")
            print("DataNode setup Successfully")
            os.system("hadoop-daemon.sh start datanode")
            os.system("jps")
        elif choice == "5" or ((("conf" in choice) or ("Conf" in choice) or ("CONF" in choice)) and (("client" in choice) or ("Client" in choice) or ("CLIENT" in choice))):
            ip = input("Enter the DataNode's IP : ")
            new_file = open("/etc/hadoop/core-site.xml","r")
            lines = new_file.readlines()
            lines[7] = "<property>\n"
            new_file = open("/etc/hadoop/core-site.xml", "w")
            new_file.writelines(lines)
            new_file.close()
            new_file = open("/etc/hadoop/core-site.xml","a")
            new_file.write("<name>fs.default.name</name>\n") 
            new_file.write("<value>hdfs://{}:9001</value>\n".format(ip))
            new_file.write("</property>\n")
            new_file.write("</configuration>\n")
            print("Client setup Successfully")
        elif choice == "6" or ((("START" in choice) or ("start" in choice) or ("Start" in choice)) and (("name" in choice) or ("Name" in choice) or ("NAME" in choice) or ("master" in choice) or ("Master" in choice) or ("MASTER" in choice))):
            os.system("ssh {} hadoop-daemon.sh start namenode".format(ip_add))
        elif choice == "7" or ((("STOP" in choice) or ("stop" in choice) or ("Stop" in choice)) and (("data" in choice) or ("Data" in choice) or ("DATA" in choice) or ("slave" in choice) or ("Slave" in choice) or ("SLAVE" in choice))):
            os.system("ssh {} hadoop-daemon.sh start datanode".format(ip_add))
        elif choice == "8" or ((("START" in choice) or ("start" in choice) or ("Start" in choice)) and (("name" in choice) or ("Name" in choice) or ("NAME" in choice) or ("master" in choice) or ("Master" in choice) or ("MASTER" in choice))) "8":
            os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip_add))
        elif choice == "9" or ((("STOP" in choice) or ("stop" in choice) or ("stop" in choice)) and (("data" in choice) or ("Data" in choice) or ("DATA" in choice) or ("slave" in choice) or ("Slave" in choice) or ("SLAVE" in choice))):
            os.system("ssh {} hadoop-daemon.sh stop datanode".format(ip_add))
        elif choice == "10" or ((("per" in choice) or ("Per" in choice) or ("PER" in choice)) and (("opr" in choice) or ("Opr" in choice) or ("OPR" in choice))):
            ch1 = input("""Who Are You? : 
            1. NamedNode
            2. DataNode
            3. Client
        
            Choice: """)
            if ch1 == "1" or ((("name" in choice) or ("Name" in choice) or ("NAME" in choice) or ("master" in choice) or ("Master" in choice) or ("MASTER" in choice))):
                print("""What Operation you want to perform?:
                1. Get Report
                2. Upload files
                3. Upload files with custom block size
                4. Read files
                5. Remove files
                6. List all files of a particular directory
            
                """)
                ch2 = input("please enter only numbers ")
                if ch2 == "1":
                    os.system("ssh {} hadoop dfsadmin -report".format(ip_add))
                elif ch2 == "2":
                    fileName = input("Enter the File Name to upload : ")
                    os.system("ssh {} hadoop fs -put {} /".format(ip_add,fileName))
                elif ch2 == "3":
                    fileName = input("Enter the File Name to upload : ")
                    blockSize = input("Enter the block size in bytes : ")
                    os.system("ssh {0} hadoop fs -Ddfs.block.size={1} -put {2} /".format(ip_add,blockSize,fileName))
                elif ch2 == "4":
                    fileName = input("Enter the File Name to read : ")
                    os.system("ssh {} hadoop fs -cat /{}".format(ip_add,fileName))
                elif ch2 == "5":
                    fileName = input("Enter the File Name to remove : ")
                    os.system("ssh {} hadoop fs -rm {} /".format(ip_add,fileName))
                elif ch2 == "6":
                    os.system("ssh {} hadoop fs  -ls /".format(ip_add))
            
                else:
                    print("No Match Found Please Try Again")

            elif ch1 == "2"  or ((("data" in choice) or ("Data" in choice) or ("DATA" in choice) or ("slave" in choice) or ("Slave" in choice) or ("SLAVE" in choice))):
                print("""What Operation you want to perform?:
                1. Upload files
                2. Upload files with custom block size
                3. Read files
                4. Remove files
                5. List all files of a particular directory
            
                """)
                ch2 = input("please enter only numbers ")
                if ch2 == "1":
                    fileName = input("Enter the File Name to upload : ")
                    os.system("ssh {} hadoop fs -put {} /".format(ip_add,fileName))
                elif ch2 == "2":
                    fileName = input("Enter the File Name to upload : ")
                    blockSize = input("Enter the block size in bytes : ")
                    os.system("ssh {0} hadoop fs -Ddfs.block.size={1} -put {2} /".format(ip_add,blockSize,fileName))
                elif ch2 == "3":
                    fileName = input("Enter the File Name to read : ")
                    os.system("ssh {} hadoop fs -cat /{}".format(ip_add,fileName))
                elif ch2 == "4":
                    fileName = input("Enter the File Name to remove : ")
                    os.system("ssh {} hadoop fs -rm {} /".format(ip_add,fileName))
                elif ch2 == "5":
                    os.system("ssh {} hadoop fs  -ls /".format(ip_add))
                
                else:
                    print("No Match Found Please Try Again")
            elif ch1 == "3" or (("client" in choice) or ("Client" in choice) or ("CLIENT" in choice)):
                print("""What Operation you want to perform?:
                1. Upload files
                2. Upload files with custom block size
                3. Read files
                4. Remove files
                5. List all files of a particular directory
    
                """)
                ch2 = input("please enter only numbers ")
                if ch2 == "1":
                    fileName = input("Enter the File Name to upload : ")
                    os.system("ssh {} hadoop fs -put {} /".format(ip_add,fileName))
                elif ch2 == "2":
                    fileName = input("Enter the File Name to upload : ")
                    blockSize = input("Enter the block size in bytes : ")
                    os.system("ssh {} hadoop fs -Ddfs.block.size={0} -put {1} /".format(ip_add,blockSize,fileName))
                elif ch2 == "3":
                    fileName = input("Enter the File Name to read : ")
                    os.system("ssh {} hadoop fs -cat /{}".format(ip_add,fileName))
                elif ch2 == "4":
                    fileName = input("Enter the File Name to remove : ")
                    os.system("ssh {} hadoop fs -rm {} /".format(ip_add,fileName))
                elif ch2 == "5":
                    os.system("ssh {} hadoop fs  -ls /".format(ip_add))
            
                else:
                    print("No Match Found Please Try Again")
    
            else:
                print("No Match Found Please Try Again")
            

        elif choice == "11" or (("exit" in choice) or ("quit" in choice) or ("Exit" in choice) or ("Quit" in choice) or ("QUIT" in choice) or ("EXIT" in choice)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")   