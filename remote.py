                            # Operation For Remote user
import os 
os.system("clear")


                                    # Basic Operation
def basicOperation(ip_add):
    i = 1
    while (1) :
        os.system("tput setaf 1")
        print("You Select Basic Operation" , end = "\n\n")
        print("""

                1: check system date
                2: System Calender
                3: Check Currently User Name
                4: Currently Working Ditectory
                5: Listing Of File
                6. Open Editor
                7: Count Number Of Words In A File
                8: exit

        """)
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if (("date" in ch2) or ("Date" in ch2) or ("DATE" in ch2)) :
            os.system("date")

        elif (("cal" in ch2) or ("Cal" in ch2) or ("CAL" in ch2)) :
            os.system("cal")
            
        elif ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) or ("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)))) :
            os.system("whoami")

        elif ((("curr" in ch2) or ("Curr" in ch2) or ("Curr" in ch2) or ("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)))) :
            os.system("path")
        
        elif ((("list" in ch2) or ("List" in ch2) or ("LIST" in ch2)) and ((("file" in ch2) or ("File" in ch2) or ("FILE" in ch2)))) :
            os.system("ls")

        elif ((("open" in ch2) or ("Open" in ch2) or ("OPEN" in ch2)) and (("editor" in ch2) or ("Editor" in ch2) or ("EDITOR" in ch2)))  :
            os.system("vim")

        elif ((("cou" in ch2) or ("Cou" in ch2) or ("COU" in ch2)) and (("word" in ch2) or ("Word" in ch2) or "WORD" in ch2)) :

            fileName = input("Enter Name Of File Which You Want To Count : ")
            os.system("cat {} | wc".format(fileName))

        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")
    


                                    #Package Management

def packManagement(ip_add):
    while (1):
        os.system("tput setaf 1")
        print("You Select Package Management" , end = "\n\n")
        print("""

                1: Check Package Install Or Not
                2: Install Package
                3: Remove Package
                4: exit

        """)
        os.system("tput setaf 7")
        ch2 = input("Enter Your Choise : ")

        if ((("che" in ch2) or ("Che" in ch2) or ("CHE" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Check : ")
            os.system("rpm -q {}".format(pack))
        elif ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Install : ")
            x = os.system("rpm -q {}".format(pack))
            if x != 0 :
                print("""
                    In your System {} not installed yet.
                    So we download it first and it will take some time
                """.format(pack))
                os.system("dnf install {} -y".format(pack))
        elif (((("uni" in ch2) or ("Uni" in ch2) or ("Uni" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2))) and (("pac" in ch2) or ("Pac" in ch2) or ("PAC" in ch2))) :
            pack = input("Enter Package Name Which You Want To Uninstall : ")
            x = os.system("rpm -q {}".format(pack))
            if x == 0 :
                print("""
                    In your System {} installed .
                    So we remove it for you and it will take some time
                """.format(pack))
                os.system("dnf remove {} -y".format(pack))
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                                        #Main Menu

def mainMenu(ip_add):
    os.system("tput setaf 1")
    print("""
                1 : Basic Operation
                2 : Package Management
                3 : User Management
                4 : Networking
                5 : Services Management
                6 : Use Docker Management
                7 : exit
    """)
    os.system("tput setaf 7")




                                    #UserManagement

def userManagement(ip_add):
    while (1):
        print("You Select User Management" , end = "\n\n")
        os.system("tput setaf 1")
        print("""

                    1:  Check Current Login User
                    2:  Show All User Name
                    3:  Add User
                    4:  Remove User
                    5:  Change Password Of A User
                    6:  Add Group
                    7:  Remove Group
                    8:  lock User
                    9:  Unlock User
                    10:  exit

        """)
        os.system("tput setaf 7")
        
        ch2 = input("Enter Your Choise : ")

        if ((("log" in ch2) or ("Log" in ch2) or ("LOG" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            os.system("whoami")
        elif ((("user" in ch2) or ("User" in ch2) or ("USER" in ch2)) and (("name" in ch2) or ("Name" in ch2) or ("NAME" in ch2))) :
            os.system("ls /home/")
        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name : ")
            os.system("useradd {}".format(userName))
            os.system("passwd {}".format(userName))
            print("User added Successfuly")
        elif (((("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) or (("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) )and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which You want to Delete : ")
            os.system("userdel {}".format(userName))
            os.system("rm -rf /home/{}".format(userName))
            print("User Successfuly Remove")
        elif (((("cha" in ch2) or ("Cha" in ch2) or ("CHA" in ch2)) or (("upd" in ch2) or ("Upd" in ch2) or ("UPD" in ch2)) )and (("pass" in ch2) or ("Pass" in ch2) or ("PASS" in ch2))) :
            userName = input("Enter User Name which user Password you want to change : ")
            os.system("passwd {}".format(userName))
            print("User Password Successfuly")
        elif ((("add" in ch2) or ("Add" in ch2) or ("ADD" in ch2)) and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name : ")
            os.system("groupadd {}".format(grpName))
            print("User added Successfuly")
        elif (((("del" in ch2) or ("Del" in ch2) or ("DEL" in ch2)) or (("rem" in ch2) or ("Rem" in ch2) or ("REM" in ch2)) )and (("gro" in ch2) or ("Gro" in ch2) or ("GRO" in ch2))) :
            grpName = input("Enter Group Name which You Want To Delete : ")
            os.system("groupdel {}".format(grpName))
            print("User Deleted Successfuly")
        elif ((("loc" in ch2) or ("Loc" in ch2) or ("LOC" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Lock : ")
            os.system("usermod -l")
        elif ((("unl" in ch2) or ("Unl" in ch2) or ("UNL" in ch2)) and (("user" in ch2) or ("User" in ch2) or ("USER" in ch2))) :
            userName = input("Enter User Name Which User You Want To Unlock : ")
            os.system("usermod -u")
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                                 #Networking

def Networking(ip_add):
    while (1) :    
        print("You Select Networking " , end = "\n\n")
        os.system("tput setaf 1")
        print("""

                    1:  Check IP Address
                    2:  Istall HTTPD
                    3:  Start Services Of Web Server
                    4:  Stop Services Of Web Server
                    5:  Check Status Of Web Server
                    6:  exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("check" in ch2) or ("Check" in ch2) or ("CHECK" in ch2)) and (("ip" in ch2) or ("Ip" in ch2) or ("IP" in ch2))) :
            os.system("ifconfig")
        elif ((("ins" in ch2) or ("Ins" in ch2) or ("INS" in ch2)) and (("httpd" in ch2) or ("Httpd" in ch2) or ("HTTPD" in ch2))) :
            i = os.system("rpm -q httpd")
            if i != 0 :
                print("""
                    In your System httpd not installed yet.
                    So we download it first and it will take some time
                """)
                os.system("dnf install httpd -y")
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl start httpd")
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl stop httpd")
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl status httpd")
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")


                                #Service Management
def serviceManagement(ip_add):
    while (1) :
        print("You Select Services Management " , end = "\n\n")
        oa.system("tput setaf 1")
        print("""

                    1:  Start Services Of Web Server
                    2:  Stop Services Of Web Server
                    3:  Check Status Of Web Server
                    4:  Start Services Of Firewall
                    5:  Stop Services Of Firewall
                    6:  Check Status Of Firewall
                    7:  Start Services Of Docker
                    8:  Stop Services Of Docker
                    9:  Check Status Of Docker
                    10:  exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl start httpd")
            os.system("systemctl stop firewalld")
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl stop httpd")
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("web" in ch2) or ("Web" in ch2) or ("WEB" in ch2))) :
            os.system("systemctl status httpd")
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl start firewalld")
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl stop firewalld")
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("firewall" in ch2) or ("Firewall" in ch2) or ("FIREWALL" in ch2))) :
            os.system("systemctl status firewalld")
        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl start docker")
        elif ((("stop" in ch2) or ("Stop" in ch2) or ("STOP" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl stop docker")
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl status docker")
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")



                                        # Docker Management
def dockerManagement(ip_add):
    while (1) :
        print("You Select Docker Management " , end = "\n\n")
        os.system("tput setaf 1")
        print("""

                    1:   Download Docker In Your System
                    2:   Start Services Of Docker
                    3:   Check Status Of Docker
                    4:   Pull Docker Image
                    5:   See All Docker Images In your System
                    6:   Run A Docker Container
                    7:   See All Currently Running Docker Container
                    8:   Stop Services Of Docker
                    9:   Remove Docker Container
                    10:  Remove All Running Docker Container
                    11:   exit

        """)
        os.system("tput setaf 7")

        
        ch2 = input("Enter Your Choise : ")

        if ((("download" in ch2) or ("Download" in ch2) or ("DOWNLOAD" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            x = os.system("rpm -q docker-ce")
            if x != 0 :

                net = os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
                if net != 0 :
                    Print("Please Check Your Internet Connection And Try Again")
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


        elif ((("start" in ch2) or ("Start" in ch2) or ("START" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl start docker")
        elif ((("status" in ch2) or ("Status" in ch2) or ("STATUS" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            os.system("systemctl status docker")
        elif ((("pull" in ch2) or ("Pull" in ch2) or ("PULL" in ch2)) and (("docker" in ch2) or ("Docker" in ch2) or ("DOCKER" in ch2))) :
            image = input("Enter Image Name :-  ")
            version = input("Enter Version :- ")
            cmd = "docker pull {}:{}".format(image,version)
            os.system("cmd")
        elif (("exit" in ch2) or ("quit" in ch2) or ("Exit" in ch2) or ("Quit" in ch2)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")