                            # Operation For Remote user
import os 
os.system("clear")

                                    # Basic Operation
def r_basicOperation(ip_add):
    i = 1
    while (1) :
        os.system("tput setaf 1")
        print("You Select Basic Operation" , end = "\n\n")
        print("""

                \t 1: check system date
                \t 2: System Calender
                \t 3: Check Currently User Name
                \t 4: Currently Working Ditectory
                \t 5: Listing Of File
                \t 6. Open Editor
                \t 7: Count Number Of Words In A File
                \t 8: exit

        """)
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if (("date" in ch2) or ("Date" in ch2) or ("DATE" in ch2)) :
            os.system("ssh {} date".format(ip_add))

        elif (("cal" in ch2) or ("Cal" in ch2) or ("CAL" in ch2)) :
            os.system("ssh {} cal".format(ip_add))
            
        elif ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) or ("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)))) :
            os.system("ssh {} whoami".format(ip_add))

        elif ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) ) and ((("dir" in ch2) or ("Dir" in ch2) or ("DIR" in ch2) or ("fol" in ch2) or ("Fol" in ch2) or ("FOL" in ch2)))) :
            os.system("ssh {} path".format(ip_add))
        
        elif ((("list" in ch2) or ("List" in ch2) or ("LIST" in ch2)) and ((("file" in ch2) or ("File" in ch2) or ("FILE" in ch2)))) :
            os.system("ssh {} ls".format(ip_add))

        elif ((("open" in ch2) or ("Open" in ch2) or ("OPEN" in ch2)) and (("editor" in ch2) or ("Editor" in ch2) or ("EDITOR" in ch2)))  :
            os.system("ssh {} vi".format(ip_add))

        elif ((("cou" in ch2) or ("Cou" in ch2) or ("COU" in ch2)) and (("word" in ch2) or ("Word" in ch2) or "WORD" in ch2)) :

            fileName = input("Enter Name Of File Which You Want To Count : ")
            os.system("ssh {} cat {} | wc".format(ip_add,fileName))

        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
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
        print("""

                \t 1: Check Package Install Or Not
                \t 2: Install Package
                \t 3: Remove Package
                \t 4: exit

        """)
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ((("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Check : ")
            os.system("ssh {} rpm -q {}".format(ip_add,pack))
        
        elif ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
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
        
        elif (((("uni" in ch2) or ("Uni" in ch2) or ("Uni" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2))) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Uninstall : ")
            x = os.system("ssh {} rpm -q {}".format(ip_add,pack))
            if x == 0 :
                print("""
                    In your System {} installed .
                    So we remove it for you and it will take some time
                """.format(pack))
                os.system("ssh {} dnf remove {} -y".format(ip_add,pack))
        
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
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
        print("""

                    \t 1:  Check Current Login User
                    \t 2:  Show All User Name
                    \t 3:  Add User
                    \t 4:  Remove User
                    \t 5:  Change Password Of A User
                    \t 6:  Add Group
                    \t 7:  Remove Group
                    \t 8:  lock User
                    \t 9:  Unlock User
                    \t 10:  exit

        """)
        os.system("tput setaf 7")
        
        ch2 = input("Enter Your Choise : ")

        if ((("log" in ch2) or ("Log" in ch2) or ("LOG" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            os.system("ssh {} whoami".format(ip_add))
        
        elif ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)) and (("name" in ch2) or ("Name" in ch2) or ("NAME" in ch2))) :
            os.system("ssh {} ls /home/".format(ip_add))
        
        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name : ")
            os.system("ssh {} useradd {}".format(ip_add,userName))
            os.system("ssh {} passwd {}".format(ip_add,userName))
            print("User added Successfuly")
        
        elif (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) )and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which You want to Delete : ")
            os.system("ssh {} userdel {}".format(ip_add,userName))
            os.system("ssh {} rm -rf /home/{}".format(ip_add,userName))
            print("User Successfuly Remove")
        
        elif (((("cha" in ch2) or ("Cha" in ch2) or ("CHA" in ch2)) or (("upd" in ch2) or ("Upd" in ch2) or ("UPD" in ch2)) )and (("pass" in ch2) or ("Pass" in ch2) or ("PASS" in ch2))) :
            userName = input("Enter User Name which user Password you want to change : ")
            os.system("ssh {} passwd {}".format(ip_add,userName))
            print("User Password Successfuly")
        
        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name : ")
            os.system("ssh {} groupadd {}".format(ip_add,grpName))
            print("User added Successfuly")
        
        elif (((("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) )and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name which You Want To Delete : ")
            os.system("ssh {} groupdel {}".format(ip_add,grpName))
            print("User Deleted Successfuly".format(ip_add))
        
        elif ((("loc" in ch2) or ("Loc" in ch2) or ("LOC" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Lock : ")
            os.system("ssh {} usermod -l".format(ip_add))
        
        elif ((("unl" in ch2) or ("Unl" in ch2) or ("UNL" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Unlock : ")
            os.system("ssh {} usermod -u".format(ip_add))
        
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
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
        print("""

                    \t 1:  Check IP Address
                    \t 2:  Istall HTTPD
                    \t 3:  Start Services Of Web Server
                    \t 4:  Stop Services Of Web Server
                    \t 5:  Check Status Of Web Server
                    \t 6:  exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("check" in ch2) or ("Check" in ch2) or ("CHECK" in ch2)) and (("ip" in ch2) or ("Ip" in ch2) or ("IP" in ch2))) :
            os.system("ssh {} ifconfig".format(ip_add))
        
        elif ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("httpd" in ch2) or ("Httpd" in ch2) or ("HTTPD" in ch2))) :
            i = os.system("ssh {} rpm -q httpd".format(ip_add))
            if i != 0 :
                print("""
                    In your System httpd not installed yet.
                    So we download it first and it will take some time
                """)
                os.system("ssh {} dnf install httpd -y".format(ip_add))
            else : 
                print("httpd already install in our system")
        
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl start httpd".format(ip_add))
        
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl stop httpd".format(ip_add))
        
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl status httpd".format(ip_add))
        
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
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
        print("""

                    \t 1:  Start Services Of Web Server
                    \t 2:  Stop Services Of Web Server
                    \t 3:  Check Status Of Web Server
                    \t 4:  Start Services Of Firewall
                    \t 5:  Stop Services Of Firewall
                    \t 6:  Check Status Of Firewall
                    \t 7:  Start Services Of Docker
                    \t 8:  Stop Services Of Docker
                    \t 9:  Check Status Of Docker
                    \t 10:  exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl start httpd".format(ip_add))
            os.system("ssh {} systemctl stop firewalld".format(ip_add))
        
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl stop httpd".format(ip_add))
        
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("ssh {} systemctl status httpd".format(ip_add))
        
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl start firewalld".format(ip_add))
        
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl stop firewalld".format(ip_add))
        
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("ssh {} systemctl status firewalld".format(ip_add))
        
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl start docker".format(ip_add))
        
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl stop docker".format(ip_add))
        
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl status docker".format(ip_add))
        
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
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
        print("""

                    \t 1:    Download Docker In Your System
                    \t 2:    Start Services Of Docker
                    \t 3:    Check Status Of Docker
                    \t 4:    Pull Docker Image
                    \t 5:    See All Docker Images In your System
                    \t 6:    Run A Simple Docker Container
                    \t 7:    See All Currently Running Docker Container
                    \t 8:    See All Container Either Runnig Or Stop
                    \t 9:    Remove One Docker Container 
                    \t 10:   Remove All Running Docker Container 
                    \t 11:   Stop Services Of Docker
                    \t 12:   exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("download" in ch2) or ("Download" in ch2) or ("DOWNLOAD" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            x = os.system("ssh {} rpm -q docker-ce".format(ip_add))
            if x != 0 :

                net = os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                if net != 0 :
                    Print("Please Check Your Internet Connection And Try Again")
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


        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl start docker".format(ip_add))
        
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl status docker".format(ip_add))
        
        elif ((("pull" in ch2) or ("Pull" in ch2) or ("PULL" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            image = input("Enter Image Name :-  ")
            version = input("Enter Version :- ")
            cmd = "docker pull {}:{}".format(image,version)
            os.system("ssh {} cmd".format(ip_add))
        
        elif ((("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) and (("imag" in ch2) or ("Imag" in ch2) or ("IMAG" in ch2))) :
            os.system("ssh {} docker images".format(ip_add))
        
        elif ((("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            name = input("Enter name which you want to give :- ")
            image = input("Enter image name :- ")
            tag = input("Enter Image tag :- ")
            os.system("ssh {} docker run -dit --name {} {}:{}".format(ip_add,name,image,tag))
        
        elif ((("curr" in ch2) or ("Curr" in ch2) or ("CURR" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker ps".format(ip_add))

        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("run" in ch2) or ("Run" in ch2) or ("RUN" in ch2)) and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker ps -a".format(ip_add))
        
        elif (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("one" in ch2) or ("One" in ch2) or ("ONE" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            name = input("Enter Name of Id of container which you want to remove :- ")
            os.system("ssh {} docker rm -f {}".format(ip_add,name))

        elif (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) and (("all" in ch2) or ("All" in ch2) or ("ALL" in ch2)) )and (("cont" in ch2) or ("Cont" in ch2) or ("CONT" in ch2))) :
            os.system("ssh {} docker rm -f $(docker ps -aq)".format(ip_add))

        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("ssh {} systemctl stop docker".format(ip_add))

        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        
        else :
            print("No Match Found Please Try Again")

                            # Permissions
def r_permission(ip_add) :
    while (1) :

        print("""
                1. give rwx permission to a file
                2. revoke rwx permission to a file
                3. Giev rwx permission to a folder/directory
                4. revoke rwx permission to a folder/directory
                5. exit

            """)
        opr = input("Enter Yor Requirment from the given operation :- ")
        if (("give" in opr) or ("Give" in opr) or ("GIVE" in opr) and  ("file" in opr) or ("File" in opr) or ("FILE" in opr)) :
            user = input("Enter User type (user, group, other) :- ")

            if (("user" in user) or ("User" in user) or ("USER" in user)) :                                                               
                u = "u"
                per_opt()
                permission = input("Enter Which permission you want give to User : - ") 
                file_name = input("Enter File Name Which permission you want to change :- ")
                path = input("Enter file path :- ")
                cmd = "chmod {}+{} {}/{}".format(u,permission,path,file_name)
                print(cmd)
                os.system("ssh {} ",format(ip_add) + cmd)

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
            
        elif (("re" in opr) or ("Re" in opr) or ("RE" in opr) and  ("file" in opr) or ("File" in opr) or ("FILE" in opr)) :
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
                

            
        elif (("give" in opr) or ("Give" in opr) or ("GIVE" in opr) and  ("dir" in opr) or ("Dir" in opr) or ("DIR" in opr) or ("fol" in opr) or ("Fol" in opr) or ("FOL" in opr)) :
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

        elif (("re" in opr) or ("Re" in opr) or ("RE" in opr) and  ("dir" in opr) or ("Dir" in opr) or ("DIR" in opr) or ("fol" in opr) or ("Fol" in opr) or ("FOL" in opr)) :
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

            elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
                print("""

                    You exit For Current Menu

                """)
                break
            
            else :
                print("No match found please try again")
            
        else :
            print("No Match Found Please Try Again")