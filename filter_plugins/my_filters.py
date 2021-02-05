#!/usr/bin/python
from natsort import natsorted
import re


class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
            'latest_version': self.latest_version,
            'list_devices': self.list_devices
        }

    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable

    def latest_version(self, list_of_version):
        array = list_of_version.split("\n")
        sorted = natsorted(array)
        res = sorted[::-1]
        for val in res:
            list_of_version = val
            if len(list_of_version) == 4:
                m = re.search(r'^(v\d{1}.\d{1})', list_of_version)
                if m.group(0):
                    break
        return list_of_version

    def list_devices(self, from_fdisk):
        items = []
        dev = []
        element = from_fdisk.split(',')
        # print(element[0])
        if "Disk /" in element[0]:
            items.append(element)
        for disk in items:
            device_info = disk[0].split()
            dev.append(device_info[1][:-1])
        return dev[-1]
