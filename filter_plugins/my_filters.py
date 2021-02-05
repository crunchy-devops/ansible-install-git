#!/usr/bin/python
from natsort import natsorted
import re


class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
            'latest_version': self.latest_version,
            'get_device': self.get_device
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

    def get_device(self, from_fdisk):
        items = []
        dev = []
        f = []
        element = from_fdisk.split('\n')
        for disk in element:
            if "Disk /" in disk:
                items.append(disk)
        for el in items:
            device_info = el.split(':')
            dev.append(device_info)
        #return dev
        for a in dev:
            f.append(a[0])
        for d in f:
            c = d.split()
        return c[1]