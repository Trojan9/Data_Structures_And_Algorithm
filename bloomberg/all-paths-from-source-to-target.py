class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #so here a binary tree is also a graph..so we will approach this with methods we use in binary trees
        #for this question we will solve it with depth first search /.....recursion method
        #difference is that in binary tree we know we have just 2 nodes coected but here we don't actually know
        #so we have to loop through
        #so now we will have path and output..which are both list...paths holds all val we have passed when transversing...so we check if present node is equals to our target which is always n-1..then add this paths to our output
        
        #first we get our target..which we always know its n-1..where n is len of graph
        end=len(graph)-1
        def dfs(node,path,output):
            if  node==end:
                output.append(path)
            #the we transverse through each child nodes connected to our node..its just like our dfs(node.left), dfs(node.right)...but here we don't know how many nodes are connected
            for nx in graph[node]:
                #we add new node to our path..i.e list of nodes we have seen
                dfs(nx,path+[nx],output)
        output=[]
        #we know our target always starts from 0 to n-1
        #so first node is 0, path is [0]
        dfs(0,[0],output)
        return output


####### more explanation ##################


#graph = [[1,2], [3], [3], []]
#This means:

#Node 0 → [1, 2]

#Node 1 → [3]

#Node 2 → [3]

#Node 3 → []

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        #define a list to hold the result of all the paths available
        result = []
        #node is present node, path is a list that will hold concurrent nodes that leads to target
        def dfs (node, path):
            if node == target:
                #adds the paths with present node as target
                result.append(path[:]) # same as result.add([...path]) but in python
                #breaks the recursion
                return
            for child in graph[node]:
                #now add the child into the path
                path.append(child)
                #this will continually call dfs till the last node without a child
                dfs(child,path)
                # when the recursion breaks, this removes all with path not ending with target node
                path.pop()

        dfs(0,[0])

        return result 
        
        
