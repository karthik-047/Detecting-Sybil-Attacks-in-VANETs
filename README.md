				
				
				
				
					###CSCE665_Project Securing VANETs against Sybil Attacks###
				




	Files:
		
		vanet_sybil.py  - python script to do all the functions
		Test_1 - 5      - Test scenarios having different config files and route files.
	
	
	Usage:
		
		- Download the sumo simulator for Win from https://www.eclipse.org/sumo/ and set the environment path variables
		
		- Run the file sumo/tools/osmWebWizard.py and select any desired location to generate the osm file
		
		- Run the command in the command prompt: netconvert --osm my_osm_net.xml -o my_net.net.xml
		  to generate the netfile.
		  
		- Run the below command to generate the route file.
		python .\randomTrips.py -n <path to netfile> -r <path to route file> -o <path to trips file> -e 1000 -p 20 --random -s 8 --min-distance 1000.0
		
		-e 1000: end time for simulation - 1000s
		-p 20:   a vehicle is genrated every 20s.
		-s 8: random seed generator - Change the value 
		--min-distance 1000: minimum distance between every source destination: 1000m
	
		- Generate the sumocfg file by adding the netfile and routefile and save as .cfg
			<configuration>
				<input>
					<net-file value="generated net-file"/>
					<route-files value="generated route-file"/>
				</input>
			</configuration>
		
		- Run the python script vanet_sybil.py inside the test folder to start the simulation.
		
		- Hit play button on the popped up SUMO window and close the window once simulation ends.
		
		- The code will continue to execute and the files will be generated and the overlap_xxx_freq.xlsx contains the final values. 
		
		- The nodes havin the frequency >=5 are considered sybil nodes.
		
		
		
