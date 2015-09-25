# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:06:17 2015

@author: Maria
"""
import json
import sys
import urllib2
import csv

if __name__=='__main__':
    #for key, busline in sys.argv[1:], sys.argv[2:]:
        bus_key = sys.argv[1]
        bus_no = sys.argv[2]
        bus_status = sys.argv[3]
        url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehcileMonitoringDetailLevel=calls&LineRef=%s'
        request = urllib2.urlopen(url)
        metadata = json.loads(request.read())

stations = len(metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
busloc = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'StopName', 'StopStatus']
        writer.writerow(headers)
        
buscount = 0
for i in range(stations):
    buscount +=1
    location = busloc[i]["MonitoredVehicleJourney"]["VehicleLocation"]
    lat = location[u"Latitude"]
    lon = location[u"Longitude"]
    now = busloc[i]["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["StopPointName"]
    next_stop = busloc[i]["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"]
    print "Bus", buscount, "is at latitude", lat, "and longtitude", lon, "and stop status is", next_stop

        
        