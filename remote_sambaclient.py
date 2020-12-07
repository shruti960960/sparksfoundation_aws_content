import os
def clientsmb():
    client_ip=input("Enter IP address of the client side : ")
    server_ip=input("Enter IP address of the server side : ")
    header=input("Enter name of header")
    os.system("ssh {} yum install samba-client cifs-utils".format(client_ip))
    os.system("ssh {} smbclient -L {}".format(client_ip,server_ip))
    mountPoint=input("Enter ur directory name where u want to mount : ")
    os.system("ssh {} mkdir {}".format(client_ip,mountPoint))
    os.system("ssh {} mount -o guest //{}/{} {}".format(client_ip,server_ip,header,mountPoint))
    os.system("ssh {} vim /etc/fstab".format(client_ip))
    os.system("ssh {} mount -a".format(client_ip))
