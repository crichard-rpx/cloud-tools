#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import subprocess

ec = boto3.resource('ec2')

#instances = ec.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instances = ec.instances.filter(Filters=[{'Name': 'tag-key', 'Values': ['Name']}])

aws_nodes = []

for instance in instances:
    hostname = [tag for tag in instance.tags if tag['Key'] == 'Name']
    aws_nodes.append(hostname[0]['Value'].split()[0])

print(len(aws_nodes))
#print(aws_nodes)

chef_nodes = subprocess.check_output(["knife", "node", "list"]).split()
print(len(chef_nodes))

for node in chef_nodes:
    if node not in aws_nodes:
        print(node)



