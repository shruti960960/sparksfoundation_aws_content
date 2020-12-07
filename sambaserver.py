import os
def samba_server():
    os.system("yum install samba*")
    os.system("vim /etc/samba/smb.conf")
    print("enter ur directory name which you wants to share: ",end="")
    directoryName=input()
    os.system("mkdir {0}".format(directoryName))
    os.system("chmod 777 {0}".format(directoryName))
    os.system("semanage fcontext -a -t samba_share_t '/{0}(/.*)?'".format(directoryName)) 
    os.system("restorecon -vvRF {0}".format(directoryName))
    os.system("systemctl restart smb nmb")
    os.system("systemctl enable smb nmb")
    print("smb nmb successfully restart and enable")
    os.system("firewall-cmd --add-service=samba --permanent")
