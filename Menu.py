import os
import subprocess as sp
import getpass
os.system("tput setaf 1")
print("\t\t\tWELCOME TO MY TUI THAT MAKES LFE SIMPLE")
os.system("tput setaf 7")
print("\t\t\t---------------------------------------")
os.system("tput setaf 2")
passwd = getpass.getpass("Enter the password: ")
os.system("tput setaf 2")
mypass = "tui"
if passwd != mypass:
    os.system("tput setaf 1")
    print("Authentication Failed")
    os.system("tput setaf 7")

    exit()
while 1:
    def RwebConfigure():
        os.system("tput setaf 2")
        os.system('clear')
        while 1:
            os.system('tput setaf 1')
            print('Yum Must Be Configured Before Working on Webserver')
            os.system('tput setaf 2')
            os.system(f'ssh {user}@{remoteip} yum install httpd -y')
            
            os.system("clear;tput setaf 7")
            page = input('Do you have your web page(y/n): ')
            if page == 'y':
                os.system("tput setaf 7")
                path = input('Enter path followed by file name(eg. /root/my.html ,etc): ')
                os.system("tput setaf 2")
                os.system(f'ssh {user}@{remoteip} cp {path} /var/www/html')
                os.system(f'ssh {user}@{remoteip} systemctl start httpd')
                os.system(f'ssh {user}@{remoteip} systemctl stop firewalld;clear')
                
                break
            elif page == 'n':
                os.system("clear;tput setaf 6")

                print("\n\tLet's create a webpage: ")
                os.system("tput setaf 7")
                print("\t=======================\n")
                fname = input('Enter File name: ')
                print('Enter Data inside your web page')
                data = input()
                os.system("tput setaf 2")
                os.system(f"echo '{data}' | ssh {user}@{remoteip} -T 'cat > /var/www/html/{fname}.html'")
                os.system(f'ssh {user}@{remoteip} systemctl start httpd;clear')
                os.system("tput setaf 1")
                os.system(f'ssh {user}@{remoteip} systemctl stop firewalld;clear')
                print('''
\t\t-------------------------------------------------------------------------------------   
\t\t\t\t  Congratulations!!! Your webpage is Ready To Uset
\t\t-------------------------------------------------------------------------------------
''')
                os.system("tput setaf 70")
                print(f'''Copy the URL and paste it on your browser: http://{remoteip}/{fname}.html''')
                os.system('tput setaf 7')
                break

    def webConfigure():
        while 1:
            os.system("tput setaf 1")
            print("\nYum Must Be Configured Before Working on Webserver")
            os.system("tput setaf 7")
            webpage = input('Do you have your web page(y/n): ')
            if webpage == "y":
                os.system("tput setaf 2")
                os.system("dnf install httpd -y")
                os.system("clear;tput setaf 7")
                webpath=input("\nEnter the path followed by the filename (e.g. /root/sheersh.html ) :")
                os.system(f"cp {webpath}  /var/www/html/")
                os.system("systemctl start httpd")
                os.system("systemctl stop firewalld")
                os.system("tput setaf 1")
                print("\nWeb server configured succesfully")
                break
            elif webpage == "n":
                os.system("clear;tput setaf 6")

                print("\n\tLet's create a webpage: ")
                os.system("tput setaf 7")
                print("\t=======================\n")
                
                fname = input("Enter File name(eg. index,mywebpage,etc) : ")
                print("\n")
                webdata=input("Enter the data to be inserted in webpage:")
                
                os.system("tput setaf 2")
                print("\n")
                os.system(f"echo '{webdata}' > /var/www/html/{fname}.html")
                os.system("systemctl start httpd")
                os.system("tput setaf 1")
                print("\n\nCongratulations!!! Your webpage is Ready To Use")
                os.system("systemctl stop firewalld")
                print("\nWeb server configured succesfully.\n")
                os.system("tput setaf 70")
                ipa=sp.getoutput("hostname -I | awk '{print $1}'")
                print(f'''Copy the below URL and paste it on your browser: http://{ipa}/{fname}.html''')
                print("\n")
                break
    
    def yumConfigure():
        os.system("tput setaf 2")
        os.system("mkdir /dvdproject")
        os.system("mount /dev/cdrom /dvdproject")
        os.system('''cat <<EOF | sudo tee /etc/yum.repos.d/dvd.repo
[dvd1]
baseurl=file:///dvdproject/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///dvdproject/BaseOS
gpgcheck=0
EOF
''')
        os.system("tput setaf 1")
        print("\n\nYum configured successfully")
        os.system("tput setaf 7")
        input("\nPress enter to continue.")
    


    def RyumConfigure():
        os.system("tput setaf 2")
        os.system(f"ssh {remoteip} mkdir /dvdproject")
        os.system(f"ssh {remoteip} mount /dev/cdrom /dvdproject")
        os.system(f''' ssh {remoteip} cat <<EOF | sudo tee /etc/yum.repos.d/dvd.repo
[dvd1]
baseurl=file:///dvdproject/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///dvdproject/BaseOS
gpgcheck=0
EOF
''')
        os.system("tput setaf 1")
        print("\n\nYum configured successfully")
        os.system("tput setaf 7")
        input("\nPress enter to continue.")

    def ip():
        os.system("tput setaf 7")
        print(remoteip)
        print("\t\t\t\tGenerate one time key\n\t\t\t\t=====================\n\nPlease follow the below steps for one time authentication:\nP.S. Just hit enter at the place of file..\n\n ")
        os.system("tput setaf 2")
        os.system("ssh-keygen")

    
        os.system("tput setaf 7")

    def remote():
        os.system("tput setaf 2 ")

        os.system(f'ssh-copy-id {user}@{remoteip}')
        os.system("clear;tput setaf 7")
        while 1:
            print('''
            Press 1: Run general commands
            Press 2: configure yum
            Press 3: User section
            Press 4: Web server
            Press 5: Software section
            Press 6: Go to main menu
            press 0: Exit
                        \n''')
            print("Enter your choice: ",end="")
            x=input()
            print(x)
            if int(x) == 1:
                general=input("\nEnter the command: ")
                os.system("tput setaf 2")
                os.system(f"ssh {remoteip} {general}")
            elif int(x) == 2:
                RyumConfigure()
            elif int(x) == 3:
                os.system("tput setaf 7")
                while 1:
                    os.system("clear")
                    print('''
            Press 1: add user
            Press 2: delete user
            Press 3: query about user
            Press 4: change password for a user
            Press 5: go to previous menu
            Press 0: exit
                        \n''')
                    print("Enter your choice: ",end="")
                    usr=input()
                    if int(usr) == 1:
                        print("\nEnter the username to add: ",end="")
                        addUser=input()
                        os.system(f"ssh {remoteip} useradd {addUser}")
                        os.system("tput setaf 1")
                        print("\nUser added succesfully")
                    elif int(usr) == 2:

                        print("\nEnter the username to delete: ",end="")
                        deleteUser=input()
                        
                        os.system(f"ssh {remoteip} userdel {deleteUser}")
                        os.system("tput setaf 1")
                        print("\nUser deleted succesfully")

                    elif int(usr) == 3:
                        print("\nEnter the username to query: ",end="")
                        queryUser=input()
                        os.system("tput setaf 2")
                        os.system(f"ssh {remoteip} id {queryUser}")
                    elif int(usr) == 4:
                        print("\nEnter the username to change password : ",end="")
                        passUser=input()
                        os.system(f"ssh {remoteip} passwd {passUser}")
                        os.system("tput setaf 1")
                        print("\nPassword changed succesfully")

                    elif int(usr) == 5:
                        break
                    elif int(usr) == 0:
                        os.system("tput setaf 7")
                        exit()
                    else:
                        os.system("tput setaf 1")
                        print("\n\t\tWrong Input Try Again !!!")
                    os.system("tput setaf 7")
                    print("\n")
                    input('Press Enter To continue')
                    os.system("clear")
            elif int(x) == 5:
                while 1:
                    os.system("clear")
                    os.system("tput setaf 7")
                    print('''
            Press 1: install software
            Press 2: download software
            Press 3: query about software
            Press 4: delete software
            Press 5: go to previous menu
            Press 0: exit
                        \n''')
                    print("Enter your choice: ",end="")
                    sft=input()
                    if int(sft) == 1:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system(f"ssh {remoteip} dnf install {softwareName} -y")
                        os.system("tput setaf 1")
                        print("\nSoftware installed succesfully")
                    elif int(sft) == 2:
                        os.system("tput setaf 7")
                        while 1:
                            print("\nPress 'e' to exit.\nEnter the appropriate link for the software: ",end="")
                            softwareName=input()
                            if softwareName == "e":
                                break
                            os.system("tput setaf 2")
                            os.system(f"ssh {remoteip} wget {softwareName}")
                            ec=sp.getoutput(f"ssh {remoteip} echo $?")
                            if ec == 0:
                                os.system("tput setaf 1")
                                print("\nSoftware downloaded succesfully")
                                break
                    elif int(sft) == 3:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system(f"ssh {remoteip} rpm -q {softwareName}")
                    elif int(sft) == 4:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system(f"ssh {remoteip} dnf remove {softwareName} -y ")
                        os.system("tput setaf 1")
                        print("\nSoftware deleted succesfully")
                    elif int(sft) == 5:
                        break
                    elif int(sft) == 0:
                        os.system("tput setaf 7")
                        exit()
                    else:
                        os.system("tput setaf 1")
                        print("\n\t\tWrong Input Try Again !!!")
                    os.system("tput setaf 7")
                    print("\n")
                    input('Press Enter To continue')
                    os.system("clear")

            elif int(x) == 4:
                while 1:
                    yumweb=input("Is yum configured.? (y/n)")
                    if yumweb == "y" :
                        print("\n")
                        RwebConfigure()
                        break
                    elif yumweb == "n" :
                        RyumConfigure()
                        os.system("clear")
                        RwebConfigure()
                        break

                    os.system("tput setaf 7")
                    os.system("clear")
            elif int(x) == 6:
                break
            elif int(x) == 0:
                os.system("tput setaf 7")
                exit()
            else:
                os.system("tput setaf 1")
                print("\nInvalid choice")
            os.system("tput setaf 7")
            print("\n")
            input('Press Enter To continue')
            os.system("clear")

    def local():

        os.system("clear")
        os.system("tput setaf 7")
        while 1:
            print('''
            Press 1: Run general commands
            Press 2: configure yum 
            Press 3: User section
            Press 4: Web server
            Press 5: Software
            Press 6: go to main menu
            press 0: Exit
			\n''')
            print("Enter your choice: ",end="")
            x=input()
            print(x)
            if int(x) == 1:
                general=input("\nEnter the command: ")
                os.system("tput setaf 2")
                os.system(f"{general}")
            elif int(x) == 2:
                yumConfigure()
            elif int(x) == 3:
                while 1:
                    os.system("clear")
                    os.system("tput setaf 7")
                    print('''
            Press 1: add user
            Press 2: delete user 
            Press 3: query about user
            Press 4: change password for a user
            Press 5: go to previous menu
            Press 0: exit
			\n''')
                    print("Enter your choice: ",end="")
                    usr=input()
                    if int(usr) == 1:
                        print("\nEnter the username to add: ",end="")
                        addUser=input()
                        os.system("useradd {}".format(addUser))
                        os.system("tput setaf 1")
                        print("\nUser added succesfully")
                    elif int(usr) == 2:
                        print("\nEnter the username to delete: ",end="")
                        deleteUser=input()

                        os.system("userdel {}".format(deleteUser))
                        os.system("tput setaf 1")
                        
                        print("\nUser deleted succesfully")

                    elif int(usr) == 3:
                        print("\nEnter the username to query: ",end="")
                        queryUser=input()
                        os.system("tput setaf 2")
                        os.system("id {}".format(queryUser))
                    elif int(usr) == 4:
                        print("\nEnter the username to change password : ",end="")
                        passUser=input()
                        os.system("passwd {}".format(passUser))
                        os.system("tput setaf 1")
                        print("\nPassword changed succesfully")

                    elif int(usr) == 5:
                        break
                    elif int(usr) == 0:
                        os.system("tput setaf 7")
                        exit()
                    else:
                        os.system("tput setaf 1")
                        print("\n\t\tWrong Input Try Again !!!")
                    os.system("tput setaf 7")
                    print("\n")
                    input('Press Enter To continue')
                    os.system("clear")
            elif int(x) == 5:
                os.system("tput setaf 7")
                while 1:
                    os.system("clear")
                    print('''
            Press 1: install software
            Press 2: download software
            Press 3: query about software
            Press 4: delete software
            Press 5: go to previous menu
            Press 0: exit
                        \n''')
                    print("Enter your choice: ",end="")
                    sft=input()
                    if int(sft) == 1:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system("dnf install {} -y".format(softwareName))
                        os.system("tput setaf 1")
                        print("\nSoftware installed succesfully")
                    elif int(sft) == 2:
                        while 1:
                            print("\nPress 'e' to exit.\nEnter the appropriate link for the software: ",end="")
                            softwareName=input() 
                            if softwareName == "e":
                                break
                            os.system("tput setaf 2")
                            os.system(f"wget {softwareName}")
                            ec=sp.getoutput("echo $?")
                            if ec == 0:
                                os.system("tput setaf 1")
                                print("\nSoftware downloaded succesfully")
                                break
                    elif int(sft) == 3:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system(f"rpm -q {softwareName}")   
                    elif int(sft) == 4:
                        print("Enter the software name: ",end="")
                        softwareName=input()
                        os.system("tput setaf 2")
                        os.system("dnf remove {} -y".format(softwareName))
                        os.system("tput setaf 1")
                        print("\nSoftware deleted succesfully")
                    elif int(sft) == 5:
                        break
                    elif int(sft) == 0:
                        os.system("tput setaf 7")
                        exit()
                    else:
                        os.system("tput setaf 1")
                        print("\n\t\tWrong Input Try Again !!!")
                    os.system("tput setaf 7")
                    print("\n")
                    input('Press Enter To continue')
                    os.system("clear")    

            elif int(x) == 4:
                os.system("tput setaf 7")
                while 1:
                    yumweb=input("Is yum configured.? (y/n)")
                    if yumweb == "y" :
                        webConfigure()
                        break
                    elif yumweb == "n" :
                        yumConfigure()
                        webConfigure()
                        break
                    os.system("tput setaf 7")
                    os.system("clear")
            elif int(x) == 6:
                break
            elif int(x) == 0:
                os.system("tput setaf 7")
                exit()
            else:
                os.system("tput setaf 1")
                print("\nInvalid choice")
            os.system("tput setaf 7")
            print("\n")
            input('Press Enter To continue')	
            os.system("clear")         
    
    os.system("tput setaf 70")

    print("\nMain Menu")
    os.system("tput setaf 7")
    print("""\n
    1. local
    2. remote
    0. exit
    """)
    choice=input("Please enter your choice: ")
    if (choice) == "1":
        local()
    elif (choice) == "2":
        remoteip=input("Enter the ip.: ")

        ip()
        user=input("\n\nEnter the username to login : ")
        os.system("clear")
        remote()
    elif choice == "0":
        os.system("tput setaf 7")
        exit()

    else:
        os.system("tput setaf 1")
        print("\t\t!!! Wrong input Please Try Again !!!")
    os.system("clear")
