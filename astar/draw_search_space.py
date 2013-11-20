import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

idx = 0
order = {}

f = open("guesses", 'r')
for i, line in enumerate(f):

    parent, child = line.strip().split('\t')

    if parent not in order:
        order[parent] = idx
        idx += 1
    if child not in order:
        order[child] = idx
        idx += 1

    parent_order = order[parent]
    child_order = order[child]

    val1 = "(" + str(parent_order) + ") " + parent
    val2 = "(" + str(child_order) + ") " + child
    g.add_edge(val1, val2)


nx.draw(g)
plt.show()