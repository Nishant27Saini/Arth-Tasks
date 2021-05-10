import os
while True:
    os.system("tput setaf 3")
    print("\t\t\t welcome to python script ")
    print(
    """
    \n
    Press 1 to see all the hard-Disks available in the system
    Press 2 to create persistent volume(pv)
    Press 3 to create volume group(vg)
    Press 4 to create logical volume (lv)
    Press 5 to see the information of vg
    Press 6 to extend the size of lv
    Press 7 to reduce the size of lv
    Press 0 to exit
    """
    )
    ch = input("Enter your choice: ")
    print(ch)
    if int(ch) == 0:
        break
    if  int(ch) == 1:
        os.system("fdisk -l")
    if int(ch) == 2:
        pv = input("enter the name of hard-disk of which you want to create the pv: ")
        os.system("pvcreate {}".format(pv))
    if int(ch) == 3:
        print("press 2 if you want to add two persistent volumes in the volume group: ")
        print("press 3 if you want to add three persistent volumes in the volume group: ")
        co = input("Enter your choice: ")
        if int(co) == 2:
            pv_name = input("enter the name by which you want to create volume group: ")
            pv1 = input("enter the name of 1st pv: ")
            pv2 = input("enter the name of 2nd pv: " )
            os.system("vgcreate {} {} {}".format(pv_name,pv1,pv2))
        if int(co) == 3:
            pv_name = input("enter the name by which you want to create volume group: ")
            pv1 = input("enter the name of 1st pv: ")
            pv2 = input("enter the name of 2nd pv: ")
            pv3 = input("enter the name of 3rd pv: ")
            os.system("vgcreate {} {} {} {}".format(pv_name,pv1,pv2,pv3))
    if int(ch) == 4:
        size = input("enter the size of logical volume that you want to create: ")
        name = input("enter the name by which you want to create logical volume: ")
        vggroup = input("enter the volume group from which you want to create logical volume: ")
        os.system("lvcreate --size {}G  --name {}  {}".format(size,name,vggroup))
        os.system("mkfs.ext4 /dev/{}/{}".format(vggroup,name))
    if int(ch) == 5:
        name = input("enter the name of volume group , whose infromation you want to see: ")
        os.system("vgdisplay {}".format(name))
    if int(ch) == 6:
        name = input("enter the logical volume whose size you want to increase: ")
        size = input("enter the size in GiB by which you want to increase the size of lovical volume: ")
        name1 = input("enter the name of volume group in which that logical volume exist: ")
        os.system("lvextend --size +{}G  /dev/{}/{}".format(size,name1,name))
        os.system("resize2fs /dev/{}/{}".format(name1,name))
    if int(ch) == 7:
        name = input("enter the name of logical volume whose size you want to decrease: ")
        name1 = input("enter the volume group name in which that lv is created: ")
        size = input("enter the size by which you want to decrease the size of lv: ")
        os.system("lvreduce --size -{}G /dev/{}/{}".format(size,name1,name))
    else:
        print("not supported")
