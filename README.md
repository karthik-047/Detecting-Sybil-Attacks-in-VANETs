				
				
				
				
				### Securing VANETs against Sybil Attacks
				







	Files:
		
		set_depart.py - sets the departure time of nodes to 0.
		sumo_test.py  - main code.
		Test_1 - 5    - Test scenarios having different config files and route files.
	
	
	Usage:
	
		python .\randomTrips.py -n .\2022-03-17-09-19-01\Test_4\bryan_test.net.xml -r .\2022-03-17-09-19-01\Test_4\routes.rou.xml -o .\2022-03-17-09-19-01\Test_4\trips.xml -e 1000 -p 20 --random -s 8 --min-distance 1500.0
		
		Run this script in the sumo/tools folder to genrate the route file.
		-e 1000: end time for simulation - 1000s
		-p 20:   a vehicle is genrated every 20s.
		-s 8: random seed generator.
		--min-distance 1500: minimum distance between every source destination: 1500m
	
	Then run the set_depart.py inside the test folder to change the departure time for all vehicles to 0.
	
	Copy the route of any two vehicles, and add copies while changing the node ids. Hence, the last 5 nodes will be sybil nodes.
	
	Run the sumo_test.py inside the test folder, once the sim opens run the simulation and close the window once it ends. The possible sybil nodes are stored in final_overlap.csv
	
	Filter the file based on Distance column and generate different files like, greater_200,..350.
	
	Run the file filter_veh_id.py to generate the frequency of occurence of each pair. Filter the ones that occur 5 or more times.
		