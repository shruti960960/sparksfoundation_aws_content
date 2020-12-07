import os
def serversmb():
    os.system("ssh {} yum install samba*".format(remoteIp))
    os.system("ssh {} vim -X /etc/samba/smb.conf".format(remoteIp))
    directoryName=input("Enter directory name which you wants to share : ")
    os.system("ssh {} mkdir {}".format(remoteIp,directoryName))
    os.system("ssh {} chmod 777 {}".format(remoteIp,directoryName))
    os.system("ssh {} semanage fcontext -a -t samba_share_t '/{}(/.*)?'".format(remoteIp,directoryName)) 
    os.system("ssh {} restorecon -vvRF {}".format(remoteIp,directoryName))
    os.system("ssh {} systemctl restart smb nmb".format(remoteIp))
    os.system("ssh {} systemctl enable smb nmb".format(remoteIp))
    print("smb nmb successfully restart and enable")
    os.system("ssh {} firewall-cmd --add-service=samba --permanent".format(remoteIp))
