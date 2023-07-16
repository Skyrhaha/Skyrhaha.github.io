# 参考资料
- Source https://github.com/networkx/networkx
- Website https://networkx.org/
- https://networkx.org/nx-guides/

<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install networkx
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
import networkx as nx

nx.__version__
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'3.1'</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
import networkx as nx
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("B", "D", weight=2)
G.add_edge("A", "C", weight=1)
G.add_edge("C", "D", weight=4)
nx.shortest_path(G, "A", "D", weight="weight")
nx.draw(G, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image1.png)
# Tutorial

## Creating a graph

<p style="color: #303f9f;"><b>In:</b></p>

```python
# Create an empty graph with no nodes and no edges
import networkx as nx
G = nx.Graph()
```
## Nodes and Edges

<p style="color: #303f9f;"><b>In:</b></p>

```python
# Nodes
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

# Edges
G.add_edge(1,2)
e = (2,3)
G.add_edge(*e) # unpack edge tuple*
G.add_edges_from([(1,2), (1,3)])
G.add_edges_from(H.edges)

G.clear()

G.add_edges_from([(1,2), (1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam") # adds node 'spam'
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(f"{G.number_of_nodes()=}")
print(f"{G.number_of_edges()=}")

nx.draw(G, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
G.number_of_nodes()=8&#xA;G.number_of_edges()=3&#xA;</pre>
![](./images_networkx/image2.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
DG = nx.DiGraph()
DG.add_edge(2,1) # adds the nodes in order 2,1
DG.add_edge(1,3)
DG.add_edge(2,4)
DG.add_edge(1,2)

assert list(DG.successors(2)) == [1,4]
assert list(DG.edges) == [(2,1),(2,4),(1,3),(1,2)]
nx.draw(DG, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image3.png)
## Examing elements of a graph

<p style="color: #303f9f;"><b>In:</b></p>

```python
print(f"{list(G.nodes)=}")
print(f"{list(G.edges)=}")
print(f"{list(G.adj['m'])=}, {list(G.neighbors('m'))=}") # adj or neighbors
print(f"{G.degree['spam']=}") # the number of edeges incident to 'spam'
print(f"{list(G.degree)=}")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
list(G.nodes)=[1, 2, 3, 'spam', 's', 'p', 'a', 'm']&#xA;list(G.edges)=[(1, 2), (1, 3), (3, 'm')]&#xA;list(G.adj['m'])=[3], list(G.neighbors('m'))=[3]&#xA;G.degree['spam']=0&#xA;list(G.degree)=[(1, 2), (2, 1), (3, 2), ('spam', 0), ('s', 0), ('p', 0), ('a', 0), ('m', 1)]&#xA;</pre>
## Removing elements from a graph

<p style="color: #303f9f;"><b>In:</b></p>

```python
G.remove_node(2)
G.remove_nodes_from("spam")
list(G.nodes)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[1, 3, 'spam']</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G.remove_edge(1, 3)
nx.draw(G, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image4.png)
## Using the graph constructors

<p style="color: #303f9f;"><b>In:</b></p>

```python
G.add_edge(1,2)
H = nx.DiGraph(G) # create a DiGraph using the connections from G
list(H.edges)
# nx.draw(H, with_labels=True, font_weight='bold')

edgelist = [(0,1), (1,2), (2,3)]
H = nx.Graph(edgelist) # create a graph from an edge list
list(H.edges)

adjacency_dict = {0:(1,2), 1:(0,2), 2:(0,1)}
H = nx.Graph(adjacency_dict) # create a Graph dict mapping nodes to nbrs
list(H.edges())

nx.draw(H, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image5.png)
## What to use as nodes and edges

<p style="color: #303f9f;"><b>In:</b></p>

```python
G = nx.Graph()

n1='n1'
n2=2

x = {
    'src': n1,
    'dst': n2,
    'remark': 'src->dst'
}
G.add_edge(n1, n2, object=x)
nx.draw(G, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image6.png)
## Accessing edges and neighbors

<p style="color: #303f9f;"><b>In:</b></p>

```python
G = nx.Graph([(1,2,{"color": "yellow"})])
G[1] # same as G.adj[1]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
AtlasView({2: {'color': 'yellow'}})</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G[1][2]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'color': 'yellow'}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G.edges[1,2]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'color': 'yellow'}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G.add_edge(1,3)
G[1][3]['color'] = 'blue'
G.edges[1,2]['color'] = 'red'
G.edges[1,2]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'color': 'red'}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
FG = nx.Graph()
FG.add_weighted_edges_from([
    (1,2,0.125),
    (1,3,0.75),
    (2,4,1.2),
    (3,4,0.375)
])

for n,nbrs in FG.adj.items():
    for nbr, eattr in nbrs.items():
        wt = eattr['weight']
        if wt<0.5: print(f"({n},{nbr},{wt:.3})")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
(1,2,0.125)&#xA;(2,1,0.125)&#xA;(3,4,0.375)&#xA;(4,3,0.375)&#xA;</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
for (u,v,wt) in FG.edges.data('weight'):
    if wt<0.5: print(f"({u},{v},{wt:.3})")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
(1,2,0.125)&#xA;(3,4,0.375)&#xA;</pre>
## Adding attributes to graphs, nodes, and edges

### Graph attributes

<p style="color: #303f9f;"><b>In:</b></p>

```python
G = nx.Graph(day="Friday")
G.graph
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'day': 'Friday'}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G.graph['day']='Monday'
G.graph
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'day': 'Monday'}</pre>
### Node attributes

<p style="color: #303f9f;"><b>In:</b></p>

```python
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.nodes[1]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{'time': '5pm'}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
G.nodes[1]['room']=714
G.nodes.data()
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
NodeDataView({1: {'time': '5pm', 'room': 714}, 3: {'time': '2pm'}})</pre>
### Edge attributes

<p style="color: #303f9f;"><b>In:</b></p>

```python
G.add_edge(1,2,weight=4.7)
G.add_edges_from([(3,4),(4,5)], color='red')
G.add_edges_from([(1,2,{'color': 'blue'}), (2,3, {'weight': 8})])
G[1][2]['weight']=4.7
G.edges[3,4]['weight']=4.2
```
## Directed graphs

<p style="color: #303f9f;"><b>In:</b></p>

```python
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
DG.out_degree(1, weight='weight')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
0.5</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
DG.degree(1, weight='weight')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
1.25</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
list(DG.successors(1))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[2]</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
list(DG.neighbors(1))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[2]</pre>
## Multigraphs

<p style="color: #303f9f;"><b>In:</b></p>

```python
MG = nx.MultiGraph()
MG.add_weighted_edges_from([
    (1,2,0.5),
    (1,2,0.75),
    (2,3,0.5)
])
dict(MG.degree(weight='weight'))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{1: 1.25, 2: 1.75, 3: 0.5}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
GG = nx.Graph()
for n,nbrs in MG.adjacency():
    for nbr,edict in nbrs.items():
        minvalue = min([d['weight'] for d in edict.values()])
        GG.add_edge(n, nbr, weight=minvalue)

nx.draw(G, with_labels=True, font_weight='bold')
nx.shortest_path(GG,1,3)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[1, 2, 3]</pre>
![](./images_networkx/image7.png)
## Graph generators and graph operations

### Using a (constructive) generator for a classic graph

<p style="color: #303f9f;"><b>In:</b></p>

```python
K_5 = nx.complete_graph(5)
nx.draw(K_5, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image8.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
K_3_5 = nx.complete_bipartite_graph(3,5)
nx.draw(K_3_5, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image9.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
barbell = nx.barbell_graph(10, 10)
nx.draw(barbell, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image10.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
lollipop = nx.lollipop_graph(10, 20)
nx.draw(lollipop, with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image11.png)
## Analyzing graphs

<p style="color: #303f9f;"><b>In:</b></p>

```python
G = nx.Graph()
G.add_edges_from([(1,2), (1,3)])
G.add_node("spam")

nx.draw(G, with_labels=True, font_weight='bold')
list(nx.connected_components(G))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[{1, 2, 3}, {'spam'}]</pre>
![](./images_networkx/image12.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
sorted(d for n,d in G.degree())
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[0, 1, 1, 2]</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
nx.clustering(G)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{1: 0, 2: 0, 3: 0, 'spam': 0}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
sp = dict(nx.all_pairs_shortest_path(G))
sp
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{1: {1: [1], 2: [1, 2], 3: [1, 3]},&#xA; 2: {2: [2], 1: [2, 1], 3: [2, 1, 3]},&#xA; 3: {3: [3], 1: [3, 1], 2: [3, 1, 2]},&#xA; 'spam': {'spam': ['spam']}}</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
sp[3]
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
{3: [3], 1: [3, 1], 2: [3, 1, 2]}</pre>
## Drawing graphs

<p style="color: #303f9f;"><b>In:</b></p>

```python
import matplotlib.pyplot as plt

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image13.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3
}

subax1=plt.subplot(221)
nx.draw_random(G, **options)

subax2=plt.subplot(222)
nx.draw_circular(G, **options)

subax3=plt.subplot(223)
nx.draw_spectral(G, **options)

subax4=plt.subplot(224)
nx.draw_shell(G, nlist=[range(5,10),range(5)], **options)
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image14.png)
<p style="color: #303f9f;"><b>In:</b></p>

```python
G = nx.dodecahedral_graph()
shells = [[2,3,4,5,6], [8,1,0,19,18, 17,16,15,14,7],[9,10,11,12,13]]
nx.draw_shell(G, nlist=shells, **options)
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image15.png)
### save drawings to a file

<p style="color: #303f9f;"><b>In:</b></p>

```python
nx.draw(G)
plt.savefig("data/networkx_savefig.png")
```
<p style="color: #d84315;"><b>Out:</b></p>

![](./images_networkx/image16.png)