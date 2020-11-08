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
                \t 10 : Hadoop Management
                \t 11 : exit
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
        
                    \t 1.  Setup Ansible in You system
                    \t 2.  Add Target
                    \t 3.  Show all target nodes
                    \t 4.  Check Connectivity with target nodes
                    \t 5.  Exit

    """) 

def aws_menu():
    print("""
                    \t 1.    Login Your Account
                    \t 2.    Create a key Pair
                    \t 3.    List key Pairs
                    \t 4.    Create a Security group
                    \t 5.    Add InBound Rules To existing security group
                    \t 6.    Describe all the Instances
                    \t 7.    Start a Stopped instances
                    \t 8.    Stop an Instance
                    \t 9.    Terminate an Instance
                    \t 10.   Launch an Instance 
                    \t 11.   Create a Volume(EBS)
                    \t 12.   Delete a volume(EBS)
                    \t 13.   Deattach a volume(EBS)
                    \t 14.   Attach volume(EBS) to any Instance
                    \t 15.   Create a S3 Bucket
                    \t 16.   Copy Data to Any s3 Bucket
                    \t 17.   Create a CloudFront Distribution
                    \t 18.   exit

    """)

def hadoop_menu():
    print("""
                    \t 1:    Download Softwares reqiured for installing hadoop
                    \t 2:    Installation of Hadoop Cluster
                    \t 3:    Configure system as Name Node (Master)
                    \t 4:    Configure system as Data Node (Slave)
                    \t 5:    Configure system as Client
                    \t 6:    Start Name Node Service
                    \t 7:    Start Data Node Service
                    \t 8:    Stop Name Node Service
                    \t 9:    Stop Data Node Service
                    \t 10:   Perform Operations (report,list,upload,change block size and upload,remove,read)  
                    \t 11:   Exit

    """)

def l_core_site(name,ip):
    os.system('echo "<?xml version="1.0"?>" > /etc/hadoop/core-site.xml')
    os.system('echo -e "<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n" >> /etc/hadoop/core-site.xml')
    os.system('echo -e "<!-- Put site-specific property overrides in this file. -->\n" >> /etc/hadoop/core-site.xml')
    os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
    os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
    os.system('echo "<name>{}</name>" >> /etc/hadoop/core-site.xml'.format(name))
    os.system('echo "<value>hdfs://{}:9001</value>" >> /etc/hadoop/core-site.xml'.format(ip))
    os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
    os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')

def l_hdfs_site(hdfs_type,dir):
    os.system('echo "<?xml version="1.0"?>" > hdfs-site.xml')
    os.system('echo -e "<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n" >> hdfd-site.xml')
    os.system('echo -e "<!-- Put site-specific property overrides in this file. -->\n" >> hdfs-site.xml')
    os.system('echo "<configuration>" >> hdfs-site.xml')
    os.system('echo "<property>" >> hdfs-site.xml')
    os.system('echo "<name>{}</name>" >> hdfs-site.xml'.format(hdfs_type))
    os.system('echo "<value>/{}</value>" >> hdfs-site.xml'.format(dir))
    os.system('echo "</property>" >> hdfs-site.xml')
    os.system('echo "</configuration>" >> hdfs-site.xml')

def r_core_site(ip_add,name,ip):
    os.system('ssh {} echo "<?xml version="1.0"?>" > /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo -e "<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n" >> /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo -e "<!-- Put site-specific property overrides in this file. -->\n" >> /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo "<configuration>" >> /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo "<property>" >> /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo "<name>{}</name>" >> /etc/hadoop/core-site.xml'.format(ip_add,name))
    os.system('ssh {} echo "<value>hdfs://{}:9001</value>" >> /etc/hadoop/core-site.xml'.format(ip_add,ip))
    os.system('ssh {} echo "</property>" >> /etc/hadoop/core-site.xml'.format(ip_add))
    os.system('ssh {} echo "</configuration>" >> /etc/hadoop/core-site.xml'.format(ip_add))

def r_hdfs_site(ip_add,hdfs_type,dir):
    os.system('ssh {} echo "<?xml version="1.0"?>" > hdfs-site.xml'.format(ip_add))
    os.system('ssh {} echo -e "<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n" >> hdfd-site.xml'.format(ip_add))
    os.system('ssh {} echo -e "<!-- Put site-specific property overrides in this file. -->\n" >> hdfs-site.xml'.format(ip_add))
    os.system('ssh {} echo "<configuration>" >> hdfs-site.xml'.format(ip_add))
    os.system('ssh {} echo "<property>" >> hdfs-site.xml'.format(ip_add))
    os.system('ssh {} echo "<name>{}</name>" >> hdfs-site.xml'.format(ip_add,hdfs_type))
    os.system('ssh {} echo "<value>/{}</value>" >> hdfs-site.xml'.format(ip_add,dir))
    os.system('ssh {} echo "</property>" >> hdfs-site.xml'.format(ip_add))
    os.system('ssh {} echo "</configuration>" >> hdfs-site.xml'.format(ip_add))