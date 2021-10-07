# coding: utf-8
import numpy; # for matrix and coordinates.
import random; # for random algorithm path.



# FUNCTIONS

# Function that finds the neighbors of the given block.

def Find_Neighbors(row, column, path):

	global Distance;
	global Visited;
	neighbors = [];

	# horizontal and vertical neighbors.
	neighbors.append(Labyrinth[row+1][column]);
	neighbors.append(Labyrinth[row][column+1]);
	neighbors.append(Labyrinth[row][column-1]);
	neighbors.append(Labyrinth[row-1][column]);


	# Remove any 0 or walls we find.
	neighbors = [i for i in neighbors if i != '0']
	
	for block in Visited:
		Visited.update({block: 0}); # Reset visited.
	for block in path:
		Visited.update({block: 1}); # Set as visited the blocks we have so far that implement our current path.

	
	Paths = [];
	temp = "";
	
	# we set to dictionary our new path, the distance cost is the length minus -1 (I) as we don't count the start.
	# also we add each neighbor/path to Paths list.
	for Neighbor_block in neighbors:
		Distance.update({path+Neighbor_block : len(path+Neighbor_block) - 1});
		Paths.append(path+Neighbor_block);

	
	Sorted_paths = [];
	# The paths here will always have the same path distance, so we sort based on the in-Depth search.
	
	for block in Paths:
		if Visited[block[-1]] == 1: # if it is visited.
			Sorted_paths.append(block); # Set as later block to visit in B&B algorithm.
		else: # if not visited 
			Sorted_paths.insert(0,block); # Set as next block to visit in B&B algorithm.


	# If the first 2 blocks are both unvisited then choose algorithm path randomly.
	if len(Sorted_paths) > 1 and Visited[Sorted_paths[0][-1]] == 0 and Visited[Sorted_paths[1][-1]] == 0:
		# If random value is 1 the path is unchanged, if it is 2 we swap the first and second element,thus changing the path.
		if random.choice([1, 2]) == 2: # Change algorithm path.
			Sorted_paths[0], Sorted_paths[1] = Sorted_paths[1], Sorted_paths[0];


	return Sorted_paths;


# MAIN 


# We create a matrix where the path of the labyrinth is symbolized with a letter and the walls with 0. 
Labyrinth =      [[0,    0,      0,    0,    0], 
    		 [0,    "D",    "E",  "F",   0], 
    		 [0,    "C",     0,   "H",   0], 
    		 [0,    "B",    "L",  "J",   0], 
    		 [0,    "A",     0,   "K",   0], 
    		 [0,    "I",     0,   "G",   0]]

# We make A into a numpy array so we can work with coordinates.
Labyrinth = numpy.array(Labyrinth)
print(Labyrinth);

# We flip the matrix upside-down cause we want the coordinates to start form the bottom left.
Labyrinth = numpy.flipud(Labyrinth);


# Dictionary that keeps paths to explore and their distances.
global Distance;
Distance = {
};


# Dictionary to set vitited blocks so we can utilise the in-Depth search method.
global Visited; # At the start no blocks are visited so they are equal to 0.
Visited = {
	"I" : 0,
	"A" : 0,
	"B" : 0,
	"C" : 0,
	"D" : 0,
	"E" : 0,
	"F" : 0,
	"H" : 0,
	"J" : 0,
	"K" : 0,
	"L" : 0,
	"G" : 0,	
};

# Keep path we take so we can find the distance, and also save the final path.
path = "";
Final_path = "";


# We initialise the coordinates of starting block I.
I = [1,0];


# and everything we need for the Branch and Bound algorithm.
Metwpo_Anazhthshs = [];
Kleisto_Synolo = [];
Mikroskopio = [];
Orio = float('inf'); # + infinity.
Paidia = [];

# Used to determine if the procedure starts it's first iteration.
first_time = True;

# Start Branch and Bound procedure.
while True:
	# if it is the first iteration, the starting block ( I ) becomes the first element of Metwpo_Anazhthshs.
	if first_time == True:

		first_time = False;
		Metwpo_Anazhthshs.append("I");
		Mikroskopio.append("I"); # we add it to Mikroskopio

		path = path + "I"; # Initialise the path.

		# We find the neighboring blocks for I then, we store each neighbor to Paidia.
		Paidia = Find_Neighbors(I[0], I[1], path);

		print("--------------------------------------------------------");
		print("1)Metwpo Anazhthshs |2)Kleisto Synolo| 3)Mikroskopio|4)Orio |5)Paidia ");
		print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)"+str(Paidia)+" ");

		# We add the block that was checked to Kleisto Synolo.
		Kleisto_Synolo.append(Metwpo_Anazhthshs[0]);

		continue;

	# After first iteration and until G has been reached.
	elif Orio == float('inf'):

		# Helper variable bool for the sake of the algorithm iteration.
		found = False;

		# We remove the block that we checked.
		Metwpo_Anazhthshs.pop(0);

		# The new Metwpo Anazhthshs is the previous plus the Paidia on front (in depth search).
		Metwpo_Anazhthshs = Paidia + Metwpo_Anazhthshs;

		path = str(Metwpo_Anazhthshs[0]); # Update the path.	
	
		# If the block that is next for examination, has already been examined (in Kleisto_Synolo) then we just remove it and check the next one
		# in Metwpo_Anazhthshs. So Kleisto_Synolo stays the same, Mikroskopio changes and Paidia is empty.
		
		same_block = path[-1]; #we check if last character of the path has already been examined.
		
	
		for block in Kleisto_Synolo: 
    			if(block == Metwpo_Anazhthshs[0] or path.count(same_block) >= 2):
				
				# Set bool found to true so we move on with the algorithm.
				found = True;

				Distance.pop(path); # we remove this path as it won't be taken.

				# we clear the Mikroskopio so we can append the new block we want to examine.
				Mikroskopio = [];
				Mikroskopio.append(Metwpo_Anazhthshs[0]);
				
				# We clear the Paidia list so we can find the new neighboring blocks.
				Paidia = [];	
				
				print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)KLADEMA: EPANALHPSH KATASTASHS "+str(Mikroskopio[0][-1]));				

				break;
		if found == True:
			continue;


		# We clear the Paidia list so we can find the new neighboring blocks.
		Paidia = [];

		# we clear the Mikroskopio so we can append the new block we want to examine.
		Mikroskopio = [];
		Mikroskopio.append(Metwpo_Anazhthshs[0]);

		
		# If we reach the ending block G , we find the distance and also the Paidia list is empty.
		if Mikroskopio[0][-1] == "G":
			Orio = Distance[path];
			print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)TELIKH KATASTASH");

			# We add the block that was checked to Kleisto Synolo.
			Kleisto_Synolo.append(Metwpo_Anazhthshs[0]);

			Final_path = Metwpo_Anazhthshs[0]; # Update the final path.
	
			continue;
		
		# We get the coordinates of the block in examination so we can find it's neighbors.
		block_row, block_col = numpy.where(Labyrinth == Mikroskopio[0][-1]); # example IA , we want the A so we can find it's neighbors.

		# We find the neighboring blocks for the block in examination, and we store each neighbor in Paidia.
		Paidia = Find_Neighbors(block_row[0],block_col[0], path);

		print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)"+str(Paidia)+" ");
		
		# We add the block that was checked to Kleisto Synolo.
		Kleisto_Synolo.append(Metwpo_Anazhthshs[0]);
		
		continue;
		
	# If ending block G has been reached, we try to find the best possible path to it distance.
	else:
		# Helper variable bool for the sake of the algorithm iteration.
		found = False;
			
		# We remove the block that we checked.
		Metwpo_Anazhthshs.pop(0);
		
		# The new Metwpo Anazhthshs is the previous plus the Paidia on front (in depth search).
		Metwpo_Anazhthshs = Paidia + Metwpo_Anazhthshs;


		# B&B algorithm ends.
		if Metwpo_Anazhthshs == []:

			print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)TELOS 4)ELAXISTO KOSTOS/APOSTASH: "+str(Orio)+" 5)"+str(Paidia)+" ");
			print("TELIKO MONOPATI: "+Final_path);
			break;

		path = str(Metwpo_Anazhthshs[0]); # Update the path.	


		# If we reach the ending block G , we find the distance and also the Paidia list is empty.
		if Metwpo_Anazhthshs[0][-1] == "G" and Orio >= Distance[path]:
			
			# We clear the Paidia list because it is empty when we reach the end block.
			Paidia = [];
			Orio = Distance[path];
			print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)TELIKH KATASTASH");
			
			Kleisto_Synolo.append(Metwpo_Anazhthshs[0]);
			
			Final_path = Metwpo_Anazhthshs[0]; # Update the final path.

			continue;
		
		# If the block that is next for examination, has already been examined (in Kleisto_Synolo) then we just remove it and check the next one
		# in Metwpo_Anazhthshs. So Kleisto_Synolo stays the same, Mikroskopio changes and Paidia is empty.
		
		same_block = path[-1]; #we check if last character of the path or block has already been examined.
		
	
		for block in Kleisto_Synolo: 
    			if(block == Metwpo_Anazhthshs[0] or path.count(same_block) >= 2):
				
				# Set bool found to true so we move on with the algorithm.
				found = True;

				Distance.pop(path); # we remove this path as it won't be taken.

				# we clear the Mikroskopio so we can append the new block we want to examine.
				Mikroskopio = [];
				Mikroskopio.append(Metwpo_Anazhthshs[0]);
				
				# We clear the Paidia list so we can find the new neighboring blocks.
				Paidia = [];	
				
				print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)KLADEMA: EPANALHPSH KATASTASHS "+str(Mikroskopio[0][-1]));				
				break;
		if found == True:
			continue;


		# We clear the Paidia list so we can find the new neighboring blocks.
		Paidia = [];

		# we clear the Mikroskopio so we can append the new block we want to examine.
		Mikroskopio = [];
		Mikroskopio.append(Metwpo_Anazhthshs[0]);

		# We get the coordinates of the block in examination so we can find it's neighbors.
		block_row, block_col = numpy.where(Labyrinth == Mikroskopio[0][-1]); # example IA , we want the A so we can find it's neighbors.

		# We find the neighboring blocks for the block in examination, and we store each neighbor in Paidia.
		Paidia = Find_Neighbors(block_row[0],block_col[0], path);


		test2 = False;
		# Check distances of neightbors, we keep the neighbors only if their distance is less than Orio.
		while(True):
			for block in Paidia:
				if Distance[block] >= Orio:
					Paidia.pop(0);
					if Paidia == []:
						test2 = True;
					continue;
				else:
					test2 = True;
					break;
			if test2 == True:

				break;
			else:
				continue;


		if Paidia == []:
			print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)KLADEMA: KOSTOS PAIDIWN >= ORIO.");
	
		else:

			print("1)"+str(Metwpo_Anazhthshs)+" 2)"+str(Kleisto_Synolo)+" 3)"+str(Mikroskopio)+" 4)"+str(Orio)+" 5)"+str(Paidia)+" ");

		# We add the block that was checked to Kleisto Synolo.
		Kleisto_Synolo.append(Metwpo_Anazhthshs[0]);

		continue;
