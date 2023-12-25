import networkx as nx
import plotly.graph_objects as go

print('2023 - Day 25')

with open('./2023/Day25/input.txt') as file:
    lines = [line.rstrip() for line in file]

G=nx.Graph()

for line in lines:
    node0,rest = line.split(':')
    G.add_node(node0.strip())
    nodes=rest.split()
    for node in nodes:
        if node not in G.nodes():
            G.add_node(node)
        G.add_edge(node0,node,capacity=1)

cut_value,partition = nx.minimum_cut(G,'hnp','vlt')
assert cut_value==3, f"wrong cut value ({cut_value}), select different pair"
reachable,unreachable=partition

print('------------------------')
print('Part 1:',len(reachable)*len(unreachable))
print('------------------------')