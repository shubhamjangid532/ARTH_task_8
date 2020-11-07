import os                                                        
                                        #Main Menu

def mainMenu():
    os.system("tput setaf 1")
    print("""
                \t 1 : Basic Operation
                \t 2 : Package Management
                \t 3 : User Management
                \t 4 : Networking
                \t 5 : Permissions 
                \t 6 : Services Management
                \t 7 : Use Docker Management
                \t 8 : Ansible Management
                \t 9 : AWS Management
                \t 10 : exit
    """)
    os.system("tput setaf 7")

def basic_menu():
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

def pack_menu():
    print("""

                \t 1: Check Package Install Or Not
                \t 2: Install Package
                \t 3: Remove Package
                \t 4: exit

    """)

def user_menu():
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

def net_menu():
    print("""

                    \t 1:  Check IP Address
                    \t 2:  Istall HTTPD
                    \t 3:  Start Services Of Web Server
                    \t 4:  Stop Services Of Web Server
                    \t 5:  Check Status Of Web Server
                    \t 6:  exit

    """)


def services_menu():
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

def docker_menu():
    print("""

                    \t 1:    Download Docker In Your System
                    \t 2:    Start Services Of Docker
                    \t 3:    Check Status Of Docker
                    \t 4:    See All Docker Images In your System
                    \t 5:    Launch A Simple Docker Container
                    \t 6:    See All Currently Running Docker Container
                    \t 7:    See All Container Either Runnig Or Stop
                    \t 8:    Remove One Docker Container 
                    \t 9:    Remove All Running Docker Container 
                    \t 10:   Stop Services Of Docker
                    \t 11:   exit

    """)

def permission_menu():
    print("""
                \t 1. give rwx permission to a file
                \t 2. revoke rwx permission to a file
                \t 3. Giev rwx permission to a folder/directory
                \t 4. revoke rwx permission to a folder/directory
                \t 5. exit

    """)


def selection():
    os.system("tput setaf 1")
    print("""
        
            1. Own System
            2. Remote System
            3. Exit

    """)
    os.system("tput setaf 7")




def per_opt() :
    print("""
                
                    for read permission press r
                    for write permission press w
                    for exicute/run permission press x
                    for both read and write press rw 
                    and so on

    """)
def ansible_menu():
    print("""
        
            1. \t Setup Ansible in You system
            2. \t Add Target
            3. \t Show all target nodes
            4. \t Check Connectivity with target nodes
            5. \t Exit

    """) 

def aws_menu():
    print("""
                    \t 1:    Login Your Account
                    \t 2:    Create a key Pair
                    \t 3:    List key Pairs
                    \t 4:    Create a Security group
                    \t 5:    Add InBound Rules To existing security group
                    \t 6:    Describe all the Instances
                    \t 7:    Start a Stopped instances
                    \t 8:    Stop an Instance
                    \t 9:    Terminate an Instance
                    \t 10:   Launch an Instance 
                    \t 11:   Create a Volume(EBS)
                    \t 12:   Delete a volume(EBS)
                    \t 13:   Deattach a volume(EBS)
                    \t 14:   Attach volume(EBS) to any Instance
                    \t 15:   Create a S3 Bucket
                    \t 16:   Copy Data to Any s3 Bucket
                    \t 17:   Create a CloudFront Distribution
                    \t 18:   exit

""")