#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import re
with open('terraform.tfstate') as json_data:
    d = json.load(json_data)

attributes_list={
    "^default_ip_address$":"IP:",
    "^disk.*size.*$":"HDD (GB):",
    "^memory$":"RAM (MB):",
    "^num_cpus$":"Num of CPU:"
    }

allResources = d['modules'][0]['resources']
for resource in (allResources):  
    if "vsphere_virtual_machine" in resource:
        print ("VM:",resource.rsplit('.', 1)[-1])
        vmatribs=d['modules'][0]['resources'][resource]["primary"]["attributes"]
        for parameter in vmatribs:
            for atribute in attributes_list:
                match = re.match(atribute, str(parameter))
                if match:
                    print(" ", attributes_list.get(atribute), vmatribs[parameter])
				
