import os
import getpass
import subprocess as sp
from com_fun import *
from local import *
from myinfo import *
from remote import *


while (1) :
        os.system("tput setaf 1")
        print("\t\t\t Hello MR. Thanks For Using My Program")
        os.system("tput setaf 7")
        print("\t\t--------------------------------------------------")
        MyDetails()

        print()
        selection()
        inp = input("Enter Where You Want To Perform Operation :- ")
        if (("own" in inp) or ("Own" in inp) or ("OWN" in inp) or ("local" in inp) or ("Local" in inp) or ("LOCAL" in inp)) :
            
            os.system("tput setaf 2")
            print("""
                    We first setup yum in you system 
            """)
            os.system("tput setaf 7")
            
            net = os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
            if net != 0 :
                print("Please make sure Your Internet in connected")
                exit()
            while (1):
                os.system("tput setaf 1")
                mainMenu()
                os.system("tput setaf 7")

                ch1 = input("Enter Your Choice : ")
                
                if ch1 == "1" or ((("bas" in ch1) or ("Bas" in ch1)) and (("oper" in ch1) or ("Oper" in ch1) or ("OPER" in ch1))) :
                    l_basicOperation()
                    os.system("tput setaf 7")


                elif ch1 == "2" or ((("pack" in ch1) or ("Pack" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    l_packManagement()
                    os.system("tput setaf 7")

                elif ch1 == "3" or ((("per" in ch1) or ("Per" in ch1) or ("PER" in ch1))) :
                    l_permission()
                    os.system("tput setaf 7")


                elif ch1 == "4" or ((("user" in ch1) or ("User" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    l_userManagement()
                    os.system("tput setaf 7")


                elif ch1 == "5" or ((("net" in ch1) or ("Net" in ch1))) :
                    l_Networking()
                    os.system("tput setaf 7")


                elif ch1 == "6" or ((("serv" in ch1) or ("Serv" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    l_serviceManagement()
                    os.system("tput setaf 7")


                elif ch1 == "7" or ((("Docker" in ch1) or ("docker" in ch1) or ("DOCKER" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    l_dockerManagement()
                    os.system("tput setaf 7")
                
                elif ch1 == "8" or (("Ansible" in ch1) or ("ansible" in ch1) or ("ANSIBLE" in ch1)) :
                    l_ansible_setup()
                    os.system("tput setaf 7")
                
                elif ch1 == "9" or (("aws" in ch1) or ("AWS" in ch1) or ("Aws" in ch1)) :
                    l_aws()
                    os.system("tput setaf 7")

                elif ch1 == "10" or (("hadoop" in ch1) or ("Hadoop" in ch1) or ("HADOOP" in ch1)) :
                    l_hadoop()
                    os.system("tput setaf 7")
                
                elif ch1 == "11" or (("exit" in ch1) or ("quit" in ch1) or ("Exit" in ch1) or ("Quit" in ch1)) :
                    print("""

                        You exit For Current Menu

                    """)
                    break
                
                else :
                    print("No Match Found Please Try Again")

            os.system("tput setaf 7")
            a = input("For Return to main menu Press 1 and For exit Press any other number to exit: "  )
            if (("exit" in a) or ("quit" in a) or ("Exit" in a) or ("Quit" in a)) :
                print("""

                    You exit For Current Menu

                """)
                break
            os.system("clear")
        elif (("rem" in inp) or ("Rem" in inp) or ("REM" in inp) or ("other" in inp) or ("Other" in inp) or ("OTHER" in inp)) :
            print("You Select Remote System")
            print("Enter Only working IP")
            ip_add = input("Enter the ip Address of Remote System: - ")
            print("""
                    Through ssh key-gen you don't need to enter remote password
                    again and again
                """)
            key = input("Have you Generate ssh-keygen in our system (yes/no) :- ")
            if (("no" in key) or ("No" in key) or ("NO" in key) or ("not" in key) or ("Not" in key) or ("NOT" in key)) :
                os.system("ssh-keygen")
                os.system("ssh-copy-id root@{}".format(ip_add))

            elif ((("yes" in key) or ("Yes" in key) or ("YES" in key))) :
                os.system("ssh-copy-id root@{}".format(ip_add))
            else :
                print("No Match Found Please Try Again")
                exit()

            os.system("tput setaf 2")
            print("""
                    We first setup yum in you system 
            """)
            os.system("tput setaf 7")
            net = os.system("ssh {} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(ip_add))
            if net != 0 :
                print("Please make sure Your Internet in connected")
                exit()
            while (1):
                os.system("tput setaf 1")
                mainMenu()
                os.system("tput setaf 7")

                

                ch1 = input("Enter Your Choice : ")
                

                if ch1 == "1" or ((("bas" in ch1) or ("Bas" in ch1)) and (("oper" in ch1) or ("Oper" in ch1) or ("OPER" in ch1))) :
                    r_basicOperation(ip_add)
                    os.system("tput setaf 7")


                elif ch1 == "2" or ((("pack" in ch1) or ("Pack" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    r_packManagement(ip_add)
                    os.system("tput setaf 7")

                elif ch1 == "3" or ((("per" in ch1) or ("Per" in ch1) or ("PER" in ch1))) :
                    r_permission(ip_add)
                    os.system("tput setaf 7")

                elif ch1 == "4" or ((("user" in ch1) or ("User" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    r_userManagement(ip_add)
                    os.system("tput setaf 7")


                elif ch1 == "5" or ((("net" in ch1) or ("Net" in ch1))) :
                    r_Networking(ip_add)
                    os.system("tput setaf 7")


                elif ch1 == "6" or ((("serv" in ch1) or ("Serv" in ch1) and (("mana" in ch1) or ("Mana" in ch1)))) :
                    r_serviceManagement(ip_add)
                    os.system("tput setaf 7")


                elif ch1 == "7" or ((("Docker" in ch1) or ("docker" in ch1) or ("DOCKER" in ch1)) and (("mana" in ch1) or ("Mana" in ch1)  or ("MANA" in ch1))) :
                    r_dockerManagement(ip_add)
                    os.system("tput setaf 7")

                elif ch1 == "8" or (("Ansible" in ch1) or ("ansible" in ch1) or ("ANSIBLE" in ch1)) :
                    r_ansible_setup(ip_add)
                    os.system("tput setaf 7")
                
                elif ch1 == "9" or (("aws" in ch1) or ("AWS" in ch1) or ("Aws" in ch1)) :
                    r_aws()
                    os.system("tput setaf 7")

                elif ch1 == "10" or (("hadoop" in ch1) or ("Hadoop" in ch1) or ("HADOOP" in ch1)) :
                    r_hadoop(ip_add)
                    os.system("tput setaf 7")
                

                if ch1 == "11" or (("exit" in ch1) or ("quit" in ch1) or ("Exit" in ch1) or ("Quit" in ch1)) :
                    print("""

                        You exit For Current Menu

                    """)
                    break
                
                else :
                    print("No Match Found Please Try Again")

            os.system("tput setaf 7")
            a = input("For Return to main menu Press 1 and For exit Press any other number to exit: "  )
            if (("exit" in a) or ("quit" in a) or ("Exit" in a) or ("Quit" in a)) :
                print("""

                    You exit For Current Menu

                """)
                break
            os.system("clear")

        
        elif (("exit" in inp) or ("quit" in inp) or ("Exit" in inp) or ("Quit" in inp)) :
            print("""

                You exit For Current Menu

            """)
            break
        else :
            print("No Match Found Please Try Again")