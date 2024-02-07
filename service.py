import csv
import unittest
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def dijkstra(graph, source, target):
    # Create a graph from the input data
    G = nx.Graph()
    
    for node, edges in graph.items():
        G.add_edges_from((node, target, {'weight': int(weight)})for target, weight in edges)
    
    # Use networkx's built-in Dijkstra's algorithm
    path = nx.shortest_path(G, source=source, target=target, weight='weight')
    distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    
    return path, distance

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
    G = nx.DiGraph()  # Use a directed graph to represent flow
    
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            source = row[0]
            target = row[1]
            demand = int(row[2])
            
            data[source].append((target, demand))
    
    for node, edges in data.items():
        G.add_edges_from((node, target, {'demand': demand}) for target, demand in edges)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8, connectionstyle='arc3,rad=0.1')
    
    # Draw edge labels with demand
    edge_demand = nx.get_edge_attributes(G, 'demand')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_demand)
    
    plt.show()

def read_network_csv(csv_filepath):
    data = defaultdict(list)
    G = nx.Graph()
    
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        
        # ignoring header 
        next(reader)
        
        for row in reader:
            data[row[1]].append((row[2], row[4]))
        
        # G.add_edge(data[0][1], data[0][2], weight=[0][4])
    
    source_node = 'A'
    source_target = 'D'
    
    shortest_path, shortest_distance = dijkstra(data, source_node, source_target)
    
    print(f"Shortest Path from {source_node} to {source_target}: {shortest_path}")
    print(f"Shortest Distance: {shortest_distance}")
    
    
    for node, edges in data.items():
        G.add_edges_from((node, target, {'weight': int(weight)})for target, weight in edges)
    
    
    # drawing graph 
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8)
    edge = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge)
    plt.show()
    
    highlight_shortest_path(G, source_node, source_target, shortest_path)

    
    return data

read_demands_csv("demands.csv")

class TestReadCsvFile(unittest.TestCase):
    
    def test_read_Csv(self):
        csv_file = "network.csv" # path to csv file
        data = read_network_csv(csv_file)
        expected_ans =      {
            'A': [('B', '5'), ('I', '5')], 
            'B': [('C', '5'), ('I', '1')], 
            'C': [('D', '5'), ('G', '5')], 
            'D': [('E', '5'), ('F', '1')], 
            'E': [('F', '5')], 
            'G': [('H', '5')], 
            'H': [('A', '5')], 
            'I': [('G', '5')], 
            'F': [('G', '3')]
            }
        self.assertEqual(data, expected_ans)
        
    def test_shortest_path_and_distance(self):
        graph_data = {
            'A': [('B', '5'), ('I', '5')],
            'B': [('C', '5'), ('I', '1')],
            'C': [('D', '5'), ('G', '5')],
            'D': [('E', '5'), ('F', '1')],
            'E': [('F', '5')],
            'G': [('H', '5')],
            'H': [('A', '5')],
            'I': [('G', '5')],
            'F': [('G', '3')]
        }

        source_node = 'A'
        target_node = 'D'

        expected_path = ['A', 'I', 'G', 'F', 'D']
        expected_distance = 14

        path, distance = dijkstra(graph_data, source_node, target_node)

        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)
        
if __name__ == '__main__':
    unittest.main()

