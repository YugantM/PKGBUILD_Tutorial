# import list
import os 
import numpy as np
from numpy import genfromtxt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
import networkx as nx
# --------------------------------------------------------------------------------------------------------------------

file_name = "dependency.csv"

# returns output of the command as list of lines
def lcom(command):
	return os.popen(command).read().split("\n")
# --------------------------------------------------------------------------------------------------------------------


# checks substring in main string
def sub_check(substring,string):

	if substring in string:
		return substring

	else:
		pass
# --------------------------------------------------------------------------------------------------------------------


# this function checks for updates in the module list
def sync():

	# Flags
	update_found = None
	file_found = os.path.isfile("./"+file_name)

	# Checks if file is present in the current directory or not
	if file_found:

		# generates list of package which occurs change in the system's package-list [added or removed]
		changes_in_package_list = list(set(pd.read_csv(file_name).index) & set([each.split(" ")[0] for each in lcom("pacman -Q") if each!=""]) )


		# checks if there is change in the package list
		if len(changes_in_package_list)==0:

			update_found = False
			print("Updates not found")

		else:

			update_found = True
			print("updates found:",changes_in_package_list)

	else:

		# getting list of all the modules
		module_list = lcom("pacman -Q")

		# removing versions from the name of modules
		module_list = [each.split(" ")[0] for each in module_list if each!=""]

		# generating list of packages
		cols = [each.split("\n")[0] for each in module_list if each.split("\n")[0] != None]

		# creates a blank dataframe where index and columns represents all the packages
		# shape of the frame is NxN, N = number of packages available in the system
		dependency_df = pd.DataFrame(index=cols,columns=cols)

		# fills the dataframe with 0
		dependency_df = dependency_df.fillna(0)

		# this loop interates through all the columns
		for each_module in list(dependency_df.columns):

			# this will print name of each module
			print("#")
			print(each_module)
			
			# this is a temporary list which gets dependencies for the given package
			temp_list = lcom("""pacman -Qi """+str(each_module)+"""|grep "Depends On"|cut -d: -f2""")

			# cleaning the list
			temp_list = temp_list[0].split(" ")[1:]
			
			# this is the list which will hold names of the packages as dependecies for the given package[each_module]
			dependency_list = []

			# this loop iterates through the temporary list 
			for each in temp_list:
				
				# this loop iterates through list of all the packages
				for each_temp_module in module_list:
					
					# checks and appends the names of the dependecies
					temp = sub_check(each_temp_module,each)
					if temp!=None:
						dependency_list.append(temp)

			# prints the list of dependecies
			print(dependency_list)

			# this loop will fill the row with 1 if a package has the dependency
			for each_dependecy in dependency_list:

				dependency_df.loc[each_module,each_dependecy] = 1

		# writes the csv file from dataframe
		dependency_df.to_csv(file_name)

		# if update has found in the system prints and returns dataframe
		if update_found:
			print("Adjancency matrix")
			return dependency_df
	
	# if no updates in the system, reads the csv file and returns the dataframe
	print("Adjancency matrix")	
	return pd.read_csv(file_name).set_index('Unnamed: 0')
# --------------------------------------------------------------------------------------------------------------------



# below code is for generating graph
# will write proper comments after finalizing the code
print('printing G2')

G2 = nx.from_pandas_adjacency(sync())

cols = list(sync().index)
nx.draw(G2,with_labels=True,node_size=500)
plt.axis('equal')
plt.savefig("graph.svg",format='svg',bbox_extra_artists=Artist.pick)

