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
        