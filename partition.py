import os
def partition():
    hd=input("Enter path of harddisk : ")
    os.system("fdisk {}".format(hd))
    os.system("udevadm settle")
