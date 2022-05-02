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
from tkinter.messagebox import NO
from turtle import shape
import numpy
import pandas as pd
import subprocess
from collections import defaultdict
import math
import traci

MAX_STEP = 500
NO_VEHICLES = 55
RSU_COUNT = 20

config_file =  "bryan_test.sumocfg"

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


def make_list(st,rs):
    tlist = list()
    for i in range (NO_VEHICLES):
        if(dis_range[st][rs][i]==1):
            tlist.append(i)
    return tlist

#list of RSU coordinates
rsu_loc = [[2676.39,1667.14],[2866.53,1551.57],[3073.44,1622.41],[3261.72,1512.42],[3470.50,1586.99],[3540.96,1374.41],[3095.81,1385.66],[2844.16,1339.06],[2989.56,1857.28],[3379.16,1810.68],
           [2616.71,1449.19],[2834.06,1331.29],[2973.72,1137.42],[2680.53,1886.02],[3244.56,1237.90],[3673.22,1471.03],[3595.83,1783.72],[2912.82,1960.32],[2477.07,1606.26],[3411.30,1070.37]]


#checking the distance between the RSUs to determine the range
dis_array = numpy.zeros(shape=(RSU_COUNT,RSU_COUNT))
for i in range (RSU_COUNT):
    for j in range (RSU_COUNT):
        if(j!=i):
            dis_array[i,j] = find_distance(rsu_loc[i],rsu_loc[j])/2

# print("In range")
# for i in range (RSU_COUNT):
#     for j in range (RSU_COUNT):
#         if(dis_array[i][j]>200):
#             print(i,j,dis_array[i][j])


#starting the sumo simulation
sumoCmd = ["sumo-gui.exe", "-c",config_file]
traci.start(sumoCmd)
step = 0


#adding Roadside units as Point of Interests (PoI)
traci.poi.add("RSU1",2676.39,1667.14, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU2",2866.53,1551.57, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU3",3073.44,1622.41, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU4",3267.34,1531.77, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU5",3470.50,1586.99, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU6",3430.44,1384.51, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU7",3095.81,1385.66, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU8",3124.05,1842.35, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU9",2887.62,1761.37, color=(255, 255, 255), width=500, height=500)
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


traci.poi.add("RSU11",2616.71,1449.19, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU12",2834.06,1331.29, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU13",2973.72,1137.42, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU14",2680.53,1886.02, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU15",3244.56,1237.90, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU16",3673.22,1471.03, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU17",3595.83,1783.72, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU18",2912.82,1960.32, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU19",2477.07,1606.26, color=(255, 255, 255), width=500, height=500)
traci.poi.add("RSU20",3411.30,1070.37, color=(255, 255, 255), width=500, height=500)

traci.poi.highlight("RSU11",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU12",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU13",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU14",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU15",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU16",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU17",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU18",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU19",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)
traci.poi.highlight("RSU20",color=(255,0,0),size = 100, alphaMax=255, duration=MAX_STEP)

#veh_loc indexing: [step_value] [vehicle_id] [x and y coordinate]
#storing x and y coordinates of 50 vehicles for MAX_STEP times
veh_loc = numpy.zeros(shape=(MAX_STEP,NO_VEHICLES,2))

#to store distance between all rsus and all vehicles
dis_db = numpy.zeros(shape=(MAX_STEP,RSU_COUNT,NO_VEHICLES))
dis_range = numpy.zeros(shape=(MAX_STEP,RSU_COUNT,NO_VEHICLES))
#using step in simulation
while step < MAX_STEP:
   traci.simulationStep()
   id_count  = traci.vehicle.getIDCount()
   id_names = traci.vehicle.getIDList()
   for i in id_names:
       veh_loc[step,int(i)]= traci.vehicle.getPosition(i)   
   step = step+1
traci.close()

#calculating the distance between RSU and vehicles for 10RSU, 50vehicles, MAX_STEP times
for k in range (MAX_STEP):
    for i in range (RSU_COUNT):
        for j in range (NO_VEHICLES):
            if(any(veh_loc[k][j])!=0):
                dis_db[k][i][j] = find_distance(rsu_loc[i],veh_loc[k][j])
                if(0<dis_db[k][i][j]<=100):
                    dis_range[k][i][j] = 1
li1 = list()
li2 = list()
li4 = list()
flag1 = False
filename = "overlap.csv"
with open(filename,'w',newline = '') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter = ',')
    csvwriter.writerow(['RSU_ID1','TIME1','RSU_ID2','Time2','Veh IDs','Distance'])
    for i in range (RSU_COUNT):
        for k in range (MAX_STEP):
            li1 = make_list(k,i)
            for i1 in range (RSU_COUNT):
                if(i1!=i):
                    for k1 in range (MAX_STEP):
                        if(k1!=k):
                            li2 = make_list(k1,i1)
                            if((len(li1)>=2)and(len(li2)>=2)):
                                li3 = list(set(li1)&set(li2))
                                if(len(li3)>=2):
                                    li3.sort()
                                    if(dis_array[i][i1]>150):
                                        print(li3,li4)
                                        if(li3==li4):
                                            flag1 = True
                                            break
                                        else:
                                            li4 = li3
                                            print(i,k,i1,k1,li3,dis_array[i][i1])
                                            csvwriter.writerow([i,k,i1,k1,li3,dis_array[i][i1]])
                                            break
                                        
df = pd.read_csv('overlap.csv')
df.drop_duplicates(subset=['Veh IDs', 'Distance'],inplace=True)
df.to_csv('final_overlap.csv',index = False)
                                   