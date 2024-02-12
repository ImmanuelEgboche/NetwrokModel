import csv
import unittest
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict




# info = {[('A', [('B', '5'), ('I', '5')]), ('B', [('C', '5'), ('I', '1')]), ('C', [('D', '5'), ('G', '5')]), 
# ('D', [('E', '5'), ('F', '1')]), ('E', [('F', '5')]), 
# ('G', [('H', '5')]), ('H', [('A', '5')]), ('I', [('G', '5')]), ('F', [('G', '3')])]}




# give this another 2 arguement s
def dijkstra(graph, source, target, demand):
    # Create a graph from the input data
    G = nx.Graph()
    
    edge_counter = 0 
    total_capacity = 0 
    
    
    # need to look at capacity, demand and weight  
    
    for node, edges in graph.items():
    # adds the weight to each edge
        for edge_target, weight, capacity in edges:
            G.add_edge(node, edge_target, weight=int(weight), capacity=int(capacity))
            edge_counter += 1
            total_capacity += int(capacity)
    total_capacity *= edge_counter
    
    total_demand = edge_counter * demand
    
    load = total_demand / total_capacity
    
    # Use networkx's built-in Dijkstra's algorithm
    path = nx.shortest_path(G, source=source, target=target, weight='weight')
    distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    
    edge_ratios = {edge: ((G.edges[edge]['capacity'] / G.edges[edge]['weight']) * 100) for edge in G.edges}
    
    
    
    return path, distance, load, edge_ratios

def highlight_shortest_path(graph, source, target, shortest_path):
    # Drawing the graph with highlighted shortest path
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8, node_size=700, edge_color='gray', width=2)
    
    # Draw all edges in light gray
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), edge_color='lightgray', width=2)
    
    # Draw the shortest path edges in red
    nx.draw_networkx_edges(graph, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='red', width=2)
    
    # Draw the nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    
    # Add labels
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    
    plt.show()

def read_demands_csv(csv_filepath):
    data = defaultdict(list)    
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data[row[0]].append((row[1], row[2]))
    return data

def read_network_csv(csv_filepath, demand_filepath):
    data = defaultdict(list)
    G = nx.Graph()
    
    data_demands = read_demands_csv(demand_filepath) 
    
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        # for row in reader:
        #     data[row[1]].append((row[2], row[3], row[4]))
            
        for row in reader:
            start_node, end_node, weight, capacity = row[1], row[2], row[3], row[4]
            data[start_node].append((end_node, weight, capacity))
            G.add_edge(start_node, end_node, weight=int(weight), capacity=int(capacity))
        
        # G.add_edge(data[0][1], data[0][2], weight=[0][4])
        
    
    
    # source_node = 'A'
    # source_target = 'D'
    
    for source, targets in data_demands.items():
        for target, demand in targets:
            # path, distance, load, edge_ratios
            shortest_path, shortest_distance, total_load, edge_ratios = dijkstra(data, source, target, int(demand))

            print(f"Shortest Path from {source} to {target}: {shortest_path}")
            print(f"Shortest Distance: {shortest_distance}")
            print(f"Total load: {total_load}")
            print(f"Edge ratio: {edge_ratios}")

            # G.add_edges_from((source, target, {'weight': int(weight)}) for target, weight, _ in data[source])
    
    # drawing graph 
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8)
            edge = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge)
            plt.show()
            # print(source)
            # print(target)
            # print(shortest_path)
            
            highlight_shortest_path(G, source, target, shortest_path)

    

if __name__ == '__main__':
    read_network_csv("network.csv", "demands.csv")


"""
USING DIJKSTRAS PLOT THE SHORTEST PATH FROM THE DEMANDS LIST ON THE NETWORK CSV, ADD THE DEMAND FOR EACH EDGE TRAVELED
THEN WITH CAPACITY AT EACH EDGE DIVIDE BY EACH OTHER THEN GIVE AS A PERCENTAGE 
"""


# class TestReadCsvFile(unittest.TestCase):
    
#     def test_read_Csv(self):
#         csv_file = "network.csv" # path to csv file
#         data = read_network_csv(csv_file)
#         expected_ans =      {
#             'A': [('B', '5'), ('I', '5')], 
#             'B': [('C', '5'), ('I', '1')], 
#             'C': [('D', '5'), ('G', '5')], 
#             'D': [('E', '5'), ('F', '1')], 
#             'E': [('F', '5')], 
#             'G': [('H', '5')], 
#             'H': [('A', '5')], 
#             'I': [('G', '5')], 
#             'F': [('G', '3')]
#             }
#         self.assertEqual(data, expected_ans)
        
#     def test_shortest_path_and_distance(self):
#         graph_data = {
#             'A': [('B', '5'), ('I', '5')],
#             'B': [('C', '5'), ('I', '1')],
#             'C': [('D', '5'), ('G', '5')],
#             'D': [('E', '5'), ('F', '1')],
#             'E': [('F', '5')],
#             'G': [('H', '5')],
#             'H': [('A', '5')],
#             'I': [('G', '5')],
#             'F': [('G', '3')]
#         }

#         source_node = 'A'
#         target_node = 'D'

#         expected_path = ['A', 'I', 'G', 'F', 'D']
#         expected_distance = 14

#         path, distance, load, edge_ratios = dijkstra(graph_data, source_node, target_node, demand)

#         self.assertEqual(path, expected_path)
#         self.assertEqual(distance, expected_distance)
        
# if __name__ == '__main__':
#     unittest.main()

