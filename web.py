import os
def web():
    os.system("yum install httpd")
    os.system("systemctl start httpd")
    filename=input("Enter filename want to host on web")
    os.system("cp {} /var/www/html/".format(filename))
    os.system("systemctl restart httpd")
