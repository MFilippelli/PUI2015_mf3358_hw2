# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:53:27 2015

@author: Maria
"""

import datetime
import json
import sys
import urllib2

if __name__=='__main__':
        bus_key = sys.argv[1]
        bus_no = sys.argv[2]
        url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehcileMonitoringDetailLevel=calls&LineRef=%s
        request = urllib2.urlopen(url)
        metadata = json.loads(request.read())
        
stations = len(metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
busloc = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

buscount = 0
for i in range(stations):
    buscount +=1
    location = busloc[i]["MonitoredVehicleJourney"]["VehicleLocation"]
    lat = location[u"Latitude"]
    lon = location[u"stations = len(metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
busloc = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']Longitude"]
    print "Bus", buscount, "is at latitude", lat, "and longtitude", lon
    
print location