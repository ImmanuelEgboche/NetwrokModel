import csv
import unittest
import networkx as nx
import matplotlib.pyplot as plt

def read_csv(csv_filepath):
    data = []
    with open(csv_filepath, 'r') as file:
        reader = csv.reader(file)
        
        # ignoring header 
        header = next(reader)
        print(f"Header: {header}")
        
        G = nx.Graph()
        for row in reader:
            data.append(row)
        
        print(data)
        # G.add_edge(data[0][1], data[0][2], weight=[0][4])
        
        for i in data:
            G.add_edge(i[1], i[2], weight=i[4])
    
    """
    
    [['1', 'A', 'B', '10', '5'], ['2', 'B', 'C', '10', '5'], ['3', 'C', 'D', '10', '5'], ['4', 'D', 'E', '10', '5'], ['5', 'E', 'F', '10', '5'], ['6', 'G', 'H', '10', '5'], ['7', 'H', 'A', '10', '5'], ['8', 'A', 'I', '10', '5'], ['9', 'B', 'I', '10', '1'], ['10', 'C', 'G', '10', '5'], ['11', 'D', 'F', '10', '1'], ['12', 'I', 'G', '10', '5'], ['13', 'F', 'G', '10', '3']]
    
    """
    
    
    
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
        expected_ans =  [
    ['1', 'A', 'B', '10', '5'],
    ['2', 'B', 'C', '10', '5'],
    ['3', 'C', 'D', '10', '5'],
    ['4', 'D', 'E', '10', '5'],
    ['5', 'E', 'F', '10', '5'],
    ['6', 'G', 'H', '10', '5'],
    ['7', 'H', 'A', '10', '5'],
    ['8', 'A', 'I', '10', '5'],
    ['9', 'B', 'I', '10', '1'],
    ['10', 'C', 'G', '10', '5'],
    ['11', 'D', 'F', '10', '1'],
    ['12', 'I', 'G', '10', '5'],
    ['13', 'F', 'G', '10', '3']
]
        self.assertEqual(data, expected_ans)
        
if __name__ == '__main__':
    unittest.main()

