import os 
import pandas as pd
from networkx import from_pandas_adjacency

# returns output of the command as list of lines
def lcom(command):
	return os.popen(command).read().split("\n")


# getting list of all the modules
module_list = lcom("pacman -Q")

#removing versions from the name of modules
module_list = [each.split(" ")[0] for each in module_list if each!=""]


dependency_df = pd.DataFrame(index=module_list,columns=module_list)

dependency_df= dependency_df.fillna(0)

for each_module in module_list:
	
	temp_list = lcom("""pacman -Qi """+str(each_module)+"""|grep "Depends On"|cut -d: -f2""")

	for each_dependecy in temp_list:
		dependency_df.loc[each_module,each_dependecy] = 1

print(dependency_df)
dependency_df.to_csv("dependency.csv")

print(from_pandas_adjacency(dependency_df))




