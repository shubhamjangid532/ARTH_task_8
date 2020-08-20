import os                                                                #Main Menu

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
                \t 8 : exit
    """)
    os.system("tput setaf 7")


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