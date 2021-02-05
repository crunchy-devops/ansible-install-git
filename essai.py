import os

items = []
dev = []
with open('fdisk_example.txt') as file:
    line = file.readlines()  # premiere ligne
    for l in line:
        element = l.split(',')
        #print(element[0])
        if "Disk /" in element[0]:
            items.append(element)
    print(items)
    for disk in items:
        device_info=disk[0].split()
        dev.append(device_info[1][:-1])
    print(dev[-1])
