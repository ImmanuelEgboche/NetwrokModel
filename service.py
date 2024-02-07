import csv
import unittest
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def dijkstra(graph , source, target):
    distances = {node: float('infinty') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0 

    visted = set()
    
    while visted != set(graph):
        # Choosing the node with the smallest distance
        current_node = min([node for node in graph if node not in visted], key=lambda node: distances[node])
        
        visted.add(current_node)
        
        for neighbour, weight, in graph[current_node]:
            if distances[current_node] + weight < distances[neighbour]:
                distances[neighbour] = distances[current_node] + weight
                predecessors[neighbour] = current_node
    # Buliding path to the target 
        

def read_csv(csv_filepath):
    data = defaultdict(list)
    G = nx.Graph()
    
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        
        # ignoring header 
        next(reader)
        
        for row in reader:
            data[row[1]].append((row[2], row[4]))
        
        # G.add_edge(data[0][1], data[0][2], weight=[0][4])
        
    for node, edges in data.items():
        G.add_edges_from((node, target, {'weight': int(weight)})for target, weight in edges)
    
    """
    
    {'A': [('B', '5'), ('I', '5')], 'B': [('C', '5'), ('I', '1')], 'C': [('D', '5'), ('G', '5')], 'D': [('E', '5'), ('F', '1')], 'E': [('F', '5')], 'G': [('H', '5')], 'H': [('A', '5')], 'I': [('G', '5')], 'F': [('G', '3')]}
    
    """
    
    print(data)
    
    
    
    # drawing graph 
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8)
    edge = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge)
    plt.show()
    
    
    return data

class TestReadCsvFile(unittest.TestCase):
    def test_read_Csv(self):
        csv_file = "network.csv" # path to csv file
        data = read_csv(csv_file)
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
        
if __name__ == '__main__':
    unittest.main()

