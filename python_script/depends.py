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

		# generates list of package which are changed [added or removed]
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


		dependency_df = pd.DataFrame(index=cols,columns=cols)

		dependency_df = dependency_df.fillna(0)


		for each_module in list(dependency_df.columns):

			print("#")
			print(each_module)
			
			temp_list = lcom("""pacman -Qi """+str(each_module)+"""|grep "Depends On"|cut -d: -f2""")

			temp_list = temp_list[0].split(" ")[1:]
			
			dependency_list = []

			for each in temp_list:

				
				for each_temp_module in module_list:
					
					temp = sub_check(each_temp_module,each)
					if temp!=None:
						dependency_list.append(temp)

			print(dependency_list)

			for each_dependecy in dependency_list:

				dependency_df.loc[each_module,each_dependecy] = 1

		dependency_df.to_csv(file_name)

		if update_found:
			print("Adjancency matrix")
			return dependency_df
	
	print("Adjancency matrix")	
	return pd.read_csv(file_name).set_index('Unnamed: 0')
		# --------------------------------------------------------------------------------------------------------------------



print('printing G2')

G2 = nx.from_pandas_adjacency(sync())

cols = list(sync().index)
nx.draw(G2,with_labels=True,node_size=500)
plt.axis('equal')
plt.savefig("graph.svg",format='svg',bbox_extra_artists=Artist.pick)

