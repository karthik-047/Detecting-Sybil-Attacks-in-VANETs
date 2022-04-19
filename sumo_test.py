#!/usr/bin/env python
#
from __future__ import print_function
from __future__ import absolute_import
from dis import dis
from gettext import find
import os
from re import M
import sys
import random
import bisect
import math
import csv
from turtle import shape
import numpy
import pandas as pd
import subprocess
from collections import defaultdict
import math
import traci

MAX_STEP = 1000
NO_VEHICLES = 50
RSU_COUNT = 10

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import sumolib  # noqa
from sumolib.miscutils import euclidean  # noqa
from sumolib.geomhelper import naviDegree, minAngleDegreeDiff  # noqa


#function to find the distance between two points
def find_distance(p1,p2):
    sq1 = (p2[0]-p1[0])** 2
    sq2 = (p2[1]-p1[1])** 2
    dis = math.sqrt(sq1+sq2)
    return dis

#list of RSU coordinates
rsu_loc = [[2676.39,1667.14],[2866.53,1551.57],[3073.44,1622.41],[3261.72,1512.42],[3470.50,1586.99],[3540.96,1374.41],[3095.81,1385.66],[2844.16,1339.06],[2989.56,1857.28],[3379.16,1810.68]]


#checking the distance between the RSUs
dis_array = numpy.zeros(shape=(10,10))
for i in range (0,len(rsu_loc)):
    for j in range (0,len(rsu_loc)):
        if(j!=i):
            dis_array[i,j] = find_distance(rsu_loc[i],rsu_loc[j])/2


#print(dis_array)  

#starting the sumo simulation
sumoCmd = ["sumo-gui.exe", "-c", "bryan_test.sumocfg"]
traci.start(sumoCmd)
step = 0


#adding Roadside units as Point of Interests (PoI)
traci.poi.add("RSU1",2676.39,1667.14, color=(255, 255, 255), width=5000, height=5000)
traci.poi.add("RSU2",2866.53,1551.57, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU3",3073.44,1622.41, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU4",3261.72,1512.42, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU5",3470.50,1586.99, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU6",3430.44,1384.51, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU7",3095.81,1385.66, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU8",3124.05,1842.35, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU9",2887.62,1761.37, color=(255, 255, 255), width=500, height=500,)
traci.poi.add("RSU10",3338.95,1778.16, color=(255, 255, 255), width=500, height=500)

traci.poi.highlight("RSU1",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU2",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU3",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU4",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU5",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU6",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU7",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU8",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU9",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU10",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
#veh_loc indexing: [step_value] [vehicle_id] [x and y coordinate]
#storing x and y coordinates of 50 vehicles for MAX_STEP times
veh_loc = numpy.zeros(shape=(MAX_STEP,NO_VEHICLES,2))

#to store distance between all rsus and all vehicles
dis_db = numpy.zeros(shape=(MAX_STEP,RSU_COUNT,NO_VEHICLES))
#using step in simulation
while step < MAX_STEP:
   traci.simulationStep()
   id_count  = traci.vehicle.getIDCount()
   id_names = traci.vehicle.getIDList()
   
   #print(traci.vehicle.getPosition('0'),traci.vehicle.getPosition('1'))
   for i in id_names:
       #print(traci.vehicle.getNeighbors(i,7))
       veh_loc[step,int(i)]= traci.vehicle.getPosition(i)
       #print(i,traci.vehicle.getPosition(i))
   #print(veh_loc[step])
   #print("\n")
   step = step+1
traci.close()

#calculating the distance between RSU and vehicles for 10RSU, 50vehicles, MAX_STEP times
for k in range (MAX_STEP):
    for i in range (RSU_COUNT):
        for j in range (NO_VEHICLES):
            if(any(veh_loc[k][j])!=0):
                dis_db[k][i][j] = find_distance(rsu_loc[i],veh_loc[k][j])
    
#storing the vehicle ids and distances when < 100m at each step:
filename = "veh_range0.csv"
id_list = []
dis_list = []
for i in range (RSU_COUNT):
    new_name = filename.replace('0',str(i))
    with open(new_name,'w',newline = '') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter = ',')
        csvwriter.writerow(['Vehicle ID','Distance from RSU','Time step'])
        for k in range (MAX_STEP):
            for j in range (NO_VEHICLES):
                if(0<dis_db[k][i][j]<=100):
                    id_list.append(j)
                    dis_list.append(dis_db[k][i][j])
            csvwriter.writerow([id_list,dis_list,k])
            id_list.clear()
            dis_list.clear()