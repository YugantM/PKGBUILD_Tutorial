# import list
import os 
import numpy as np
from numpy import genfromtxt
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
import networkx as nx
import regex as re
from graphviz import Source
# --------------------------------------------------------------------------------------------------------------------


# constants
file_name = "dependency.csv"
nodes_file = "graph_nodes.csv"
# --------------------------------------------------------------------------------------------------------------------


# returns output of the command as list of lines
def lcom(command,split=True):
    if split:
        return os.popen(command).read().split("\n")
    else:
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

        # creates blank dataframe to contain the nodes
        graph_nodes = pd.DataFrame(columns=['node1','node2'])

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
                temp = pd.DataFrame([[each_module,each_dependecy]],columns=['node1','node2'])
                graph_nodes = graph_nodes.append(temp,ignore_index=True)
                dependency_df.loc[each_module,each_dependecy] = 1

        # writes the csv files from dataframes
        dependency_df.to_csv(file_name)
        graph_nodes.to_csv(nodes_file)


        # if update has found in the system prints and returns dataframe
        if update_found:
            print("Adjancency matrix")
            return dependency_df, graph_nodes
    
    # if no updates in the system, reads the csv file and returns the dataframe
    return pd.read_csv(file_name).set_index('Unnamed: 0'), pd.read_csv(nodes_file).set_index('Unnamed: 0')
# --------------------------------------------------------------------------------------------------------------------



# below code is for generating graph
# will write proper comments after finalizing the code
# just palced here for reference if needed
def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1000, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='black', edge_alpha=0.2, edge_tickness=1,
               edge_text_pos=0.5,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = ['' for each in range(len(graph))]

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.axis('equal')
    plt.savefig("graph.svg",format='svg',dpi =95)


# draw example


packages = list(sync()[0].index)

# generates tree for each package in the system
for each_package in packages:
    
    tree = lcom("""pactree {0} -g""".format(each_package),split=False)

    with open('./Graphs/{0}.gv'.format(each_package),'w') as out:
        out.writelines("\n".join(tree))

    src = Source(str("\n".join(tree)))

    src.render('./Graphs/{0}.gv'.format(each_package), format='svg') 

#dot.render('test-output/round-table.gv', view=True) 
#print([re.sub(r'[^\w\s]','',each).strip(" ").split(" ") for each in tree[3:]])

'''for each in tree:
    print(each.split("->"))
'''#for each in 
'''
x,y = sync()
#graph = [("calc", "add"),("calc", "mul"),(22, 23), (23, 24),(24, 25), (25, 20)]
y = y.head(8)
print(y)
y = zip(list(y['node1']),list(y['node2']))
#print(y)
draw_graph(list(y))

print('printing G2')

G2 = nx.from_pandas_adjacency(sync())

cols = list(sync().index)
nx.draw(G2,with_labels=True,node_size=500)

plt.axis('equal')
plt.savefig("graph.svg",format='svg',bbox_extra_artists=Artist.pick)
'''
