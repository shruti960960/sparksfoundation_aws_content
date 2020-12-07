import os
def samba_client():
    client_ip=input("Enter IP address of the client side : ")
    server_ip=input("Enter IP address of the server side : ")
    header=input("Enter name of header")
    os.system("ssh {0} yum install samba-client cifs-utils".format(client_ip))
    os.system("ssh {0} smbclient -L {1}".format(client_ip,server_ip))
    mountPoint=input("Enter ur directory name where u want to mount : ")
    os.system("ssh {0} mkdir {1}".format(client_ip,mountPoint))
    os.system("ssh {0} mount -o guest //{1}/{2} {3}".format(client_ip,server_ip,header,mountPoint))
    os.system("ssh {0} vim /etc/fstab".format(client_ip))
    os.system("ssh {0} mount -a".format(client_ip))
