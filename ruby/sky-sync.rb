#!/usr/bin/env ruby


require 'aws-sdk'
require 'chef-api'


ec2 = Aws::EC2::Resource.new(region: 'us-east-1')


# Set empty list for active AWS Hosts
#activeHosts = Array.new

# Get a list of all current AWS Hosts
#f = [ { name: 'instance-state-name', values: ['running'] } ]
#ec2.instances().each do |i|
#	name = i.tags.select{|tag| tag.key == 'Name'}
#	activeHosts.push("#{name[0].value.split[0]}")
#	
#end

#puts activeHosts.display


# Set empty list for active Chef Nodes
#chefNodes = Array.new

