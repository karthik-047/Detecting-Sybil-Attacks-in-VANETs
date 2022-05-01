#!/usr/bin/env python
#

import xml.etree.ElementTree as ET
tree = ET.parse('routes.rou.xml')
root = tree.getroot()
for vehicle in root.findall('vehicle'):
  vehicle.attrib['depart'] = str(0.00)


tree.write('output.xml')