#function implementing BFS algorithm
def bfs_algorithm( visited, graph, node ):
visited.append( node )
q.append( node )
# using loop to visit each node of the tree
while q:
v = q.pop( 0 )
print ( v, end = " " )
# visit neighbour
for u in graph[v]:
if u not in visited:
visited.append( u )
q.append( u )
# Driver Code
print( "Following is the result of the Breadth-First Search, starting from vertex 1:" )
# createing a grapgh
g = {
'1' : ( '2', '3' ),
'2' : ( '4', '5' ),
'3' : ( '6' ),
'4' : ( ),
'5' : ( '6' ),
'6' : ( )
}
# creating list to store visited nodes
visited = [ ]
# createing a queue
q = [ ]
# calling function
bfs_algorithm( visited, g, '1' )
