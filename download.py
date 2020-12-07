import os
def download():
    src=input("Enter source from where to download : ")
    dest=input("Enter destination : ")
    os.system("wget {} {}".format(src,dest))
    print("Successfully downloaded at destination {}".format(dest))
