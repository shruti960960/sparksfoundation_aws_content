import os
def web():
    os.system("ssh {} yum install httpd".format(remoteIp))
    os.system("ssh {} systemctl start httpd".format(remoteIp))
    filename=input("Enter filename wants to web host")
    os.system("ssh {} ")
