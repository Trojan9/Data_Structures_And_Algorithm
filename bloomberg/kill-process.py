class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
#         just like a hashMap jare...but we named it graph
#create a graph of list
#first we map every parent val to its respective children list
        graph=defaultdict(list)
        res=[]
        for child,parent in zip(pid,ppid):
            graph[parent].append(child)
        
        #then we use queue
        qu=deque()
        #add this kill integer to our queue
        qu.append(kill)
        while qu:
            #now get our first value
            kill_int=qu.popleft()
            #add to res
            res.append(kill_int)
            #now if this kill int is a parent..we just add all the children values into our queue
            #we do this so we will check those children values one by one cuz this children values might also have a child or children..and we need to kill everything related to this our kill node or int
            if kill_int in graph:
                #this extend adds all the children list into the queue
                #now we repeat this process for all the children to check if they also have children
                qu.extend(graph[kill_int])
        return res





from collections import defaultdict, deque
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        queue = deque()
        kill_process = [kill]
        queue.append(kill)

        #first create like a tree, it will be like a map..parent to list of children
        graph = defaultdict(list)
        # 5 -> [1,2]
        for i in range(len(ppid)):
            graph[ppid[i]].append(pid[i])
        while queue:
            search = queue.popleft()
            if search in graph:
                #concatinate the list
                queue.extend(graph[search])
                kill_process = kill_process + graph[search]
        return kill_process
            
            
