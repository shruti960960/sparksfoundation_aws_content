#!/usr/bin/python3
print("content-type: text/html")
print()

import os 
import getpass
import partition 
import sambaserver
import sambaclient
import nfs
import lvm
import web
import download
import copy
import move
import remote_lvm
import remote_sambaserver
import remote_sambaclient
import remote_nfs


os.system("tput setaf 1")
print("\t\tHello this is TUI project which will makes ur life simple")

os.system("tput setaf 7")
print("\t\t---------------------------------------------------------")

passwd = getpass.getpass("Enter ur password : ")
apass = "shruti"
if passwd != apass:
    print("authentication failure")
    exit()


print("Where u like to run ur job local/remote : ", end="")
location=input()

if location=="remote":
    remoteIp = input("Enter ur IP : ")
    
while True:
    print("""
    Press 1  : To check which user account currently login
    Press 2  : To check present working directory 
    Press 3  : To navigate to some another directory
    Press 4  : To list all the files and directories of particular directory
    Press 5  : To see current IST date and time 
    Press 6  : To check cal
    Press 7  : To create file
    Press 8  : To remove file
    Press 9  : To create directory
    press 10 : To remove directory
    Press 11 : To copy files or directory
    Press 12 : To move files or directory
    Press 13 : To read the content of file 
    Press 14 : To search word from file
    Press 15 : To create user
    Press 16 : To delete user
    Press 17 : To check connectivity with google
    Press 18 : To download anything form google
    Press 19 : To configure web server
    Press 20 : To create partion
    Press 21 : To configure samba server
    Press 22 : To configure samba client
    Press 23 : To configure nfs
    Press 24 : To configure lvm
    Press 25 : To exit
    """)
    print("enter ur choice : ",end="")
    ch=input()
    print(ch)
    if location == "local":
        if int(ch) == 1:
            os.system("who")
        elif int(ch) == 2:
            os.system("pwd")
        elif int(ch) == 3:
            directory=input("Enter path of directory : ")
            os.system("cd {}".format(directory))
        elif int(ch) == 4:
            directory=input("Enter path of directory : ")
            os.system("ls {}".format(directory))
        elif int(ch) == 5:
            os.system("date")
        elif int(ch) == 6:
            os.system("cal")
        elif int(ch) == 7:
            fileName=input("Enter Filename: ")
            os.system("touch {0}".format(fileName))
            print("file successfully created")
        elif int(ch) == 8:
            fileName=input("Enter Filename: ")
            os.system("rm {0}".format(fileName))
            print("file successfullly removed")
        elif int(ch) == 9:
            directoryName=input("Enter directory name : ")
            os.system("mkdir {0}".format(directoryName))
            print("directory successfully created")
        elif int(ch) == 10:
            directoryName=input("Enter directory name : ")
            os.system("rmdir {0}".format(directoryName))
            print("directory successfully removed")
        elif int(ch) == 11:
            copy.copy()
        elif int(ch) == 12:
            move.move()
        elif int(ch) == 13:
            filename=input("Enter path of file : ")
            os.system("cat {}".format(filename))
        elif int(ch) == 14:
            filename=input("Enter path of file : ")
            word=input("Enter word to search : ")
            os.system("grep {} {}".format(word,filename))
        elif int(ch) == 15:
            userName=input("Enter username : ")
            os.system("useradd {0}".format(userName))
        elif int(ch) == 16:
            userName=input("Enter username : ")
            os.system("userdel {0}".format(userName))
        elif int(ch) == 17:
            os.system("ping 8.8.8.8")
        elif int(ch) == 18:
            download.download()
        elif int(ch) == 19:
            web.web()
        elif int(ch) == 20:
            partition.partition()
        elif int(ch) == 21:
            sambaserver.samba_server()
        elif int(ch) == 22:
            sambaclient.samba_client()
        elif int(ch) == 23:
            nfs.nfs()
        elif int(ch) == 24:
            lvm.lvm()
        elif int(ch) == 25:
            exit()
        else:
            print("do not supported")
        input("enter to continue...")        
        os.system("clear")
    
    elif location == "remote":
        if int(ch) == 1:
            os.system("ssh {} who".format(remoteIp))
        elif int(ch) == 2:
            os.system("ssh {} pwd".format(remoteIp))
        elif int(ch) == 3:
            directory=input("Enter path of directory : ")
            os.system("ssh {} cd {}".format(remoteIp,directory))
        elif int(ch) == 4:
            directory=input("Enter path of directory : ")
            os.system("ssh {} ls {}".format(remoteIp,directory))
        elif int(ch) == 5:
            os.system("ssh {0} date".format(remoteIp))
        elif int(ch) == 6:
            os.system("ssh {0} cal".format(remoteIp))
        elif int(ch) == 7:
            fileName=input("Enter Filename: ")
            os.system("ssh {} touch {}".format(remoteIp,fileName))
            print("file successfully created")
        elif int(ch) == 8:
            fileName=input("Enter Filename: ")
            os.system("ssh {} rm {}".format(remoteIp,fileName))
            print("file successfullly removed")
        elif int(ch) == 9:
            directoryName=input("Enter directory name : ")
            os.system("ssh {} mkdir {}".format(remoteIp,directoryName))
            print("directory successfully created")
        elif int(ch) == 10:
            directoryName=input("Enter directory name : ")
            os.system("ssh {} rmdir {}".format(remoteIp,directoryName))
            print("directory successfully removed")
        elif int(ch) == 11:
            source=input("Enter path of source : ")
            destination=input("Enter path of destination : ")
            os.system("ssh {} cp {} {}".format(remoteIp,source,destination))
            print("successfully copied ")
        elif int(ch) == 12:
            source=input("Enter path of source : ")
            destination=input("Enter path of destination : ")
            os.system("ssh {} mv {} {}".format(remoteIp,source,destination))
            print("successfully moved")
        elif int(ch) == 13:
            filename=input("Enter path of file : ")
            os.system("ssh {} cat {}".format(remoteIp,filename))
        elif int(ch) == 14:
            filename=input("Enter path of file : ")
            word=input("Enter word to search : ")
            os.system("ssh {} grep {} {}".format(remoteIp,word,filename))
        elif int(ch) == 15:
            userName=input("Enter username : ")
            os.system("ssh {} useradd {}".format(remoteIp,userName))
        elif int(ch) == 16:
            userName=input("Enter username : ")
            os.system("ssh {} userdel {}".format(remoteIp,userName))
        elif int(ch) == 17:
            os.system("ssh {} ping 8.8.8.8".format(remoteIp))
        elif int(ch) == 18:
            src=input("Enter source from where to download : ")
            dest=input("Enter destination : ")
            os.system("ssh {} wget {} {}".format(remoteIp,src,dest))
            print("Successfully downloaded at destination {}".format(dest))
        elif int(ch) == 19:
            os.system("ssh {} yum install httpd".format(remoteIp))
        elif int(ch) == 20:
            os.system("ssh {} lsblk".format(remoteIp))
            hd=input("Enter path of harddisk : ")
            os.system("ssh {} fdisk {}".format(remoteIp,hd))
            os.system("udevadm settle")
        elif int(ch) == 21:
            remote_sambaserver.serversmb()
        elif int(ch) == 22:
            remote_sambaclient.clientsmb()
        elif int(ch) == 23:
            remote_nfs.nfs()
        elif int(ch) == 24:
            remote_lvm.lvm()
        elif int(ch) == 25:
            exit()
        else:
            print("do not supported")
        input("enter to continue...")
        os.system("clear")		
    else:
        print("location doesnt support")

            
        

