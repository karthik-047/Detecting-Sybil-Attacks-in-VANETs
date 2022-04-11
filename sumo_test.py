#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
import os
import sys
import random
import bisect
import subprocess
from collections import defaultdict
import math
import traci

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import sumolib  # noqa
from sumolib.miscutils import euclidean  # noqa
from sumolib.geomhelper import naviDegree, minAngleDegreeDiff  # noqa

sumoCmd = ["sumo-gui.exe", "-c", "bryan_test.sumocfg"]
traci.start(sumoCmd)
step = 0
traci.poi.add("POI1",2781.86,1766.33, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI2",2858.79,1451.28, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI3",3015.09,1634.45, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI4",3183.61,1507.45, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI5",3367.97,1691.96, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI6",3563.35,1484.36, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI7",3415.59,1264.55, color=(255, 255, 255), width=500, height=500, layer="1")
traci.poi.add("POI8",2986.96,1353.70, color=(255, 255, 255), width=500, height=500, layer="1")
print(traci.poi.getPosition("POI1"))
while step < 2000:
   traci.simulationStep()
   #print(traci.vehicle.getPosition("0"))
   step = step+1
traci.close()