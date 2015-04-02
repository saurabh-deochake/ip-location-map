#!/usr/bin/env python
import urllib
import json

coord_list = [] # List of tuples containing coordinates as (Longitude, Latitude)
cache = {} # Dict containing data from IPs that have already been requested
           # from the API
with open('ips.txt','r') as ip_file:
    for ip in ip_file:
        print('Getting location for {}'.format(ip))
        if ip not in cache:
            url = 'https://freegeoip.net/json/{}'.format(ip)
            ip_data = json.loads(urllib.urlopen(url).read())
            cache[ip] = ip_data
        else:
            ip_data = cache[ip]
        coord_list.append((ip_data['longitude'], ip_data['latitude']))

with open('geo.txt', 'w') as geo_file:
    for coordinates in coord_list:
        ip_longitude, ip_latitude = coordinates
        geo_file.write('{},{}\n'.format(ip_longitude, ip_latitude))
