from classes import *
def expand(node):
    return[el.end for el in node.out_link]


def greedy(graph):
    start=graph[0]
    node:Node=start
    visited=[]
    while True:
        visited.append(node)
        if node.is_goal:
            break
        children=expand(node)
        #print(children)
        children=sorted(children,key=lambda y: y.h)
        #print(node,children)
        node=children[0]
        
    print(visited)
    cost=0
    for i in range(len(visited)-1):
        for link in visited[i].out_link:
            if link.end==visited[i+1]:
                cost+=link.cost
                break
    print(cost)
   
   

def a_star_fringe(to_visit,a_node):
    for el in to_visit:
        if el.node==a_node.node:
            if el.f>a_node.f:
                el.f=a_node.f
                el.parent=a_node.parent
            return
    to_visit.append(a_node)
    
def a_star(graph):
    start:Node=graph[0]
    node:AStarNode=AStarNode(start,start.h)
    visited:list[AStarNode]=[]
    to_visit:list[AStarNode]=[]
    while True:
        visited.append(node)
        if node.node.is_goal:
            break
        children:list[Node]=expand(node.node)
        for el in children:
            a_node=AStarNode(el,el.h+node.f-node.node.h+node.node.link_costs[el],node)
            a_star_fringe(to_visit,a_node)
        to_visit.sort(key=lambda n: n.f)
        #children=sorted(children,key=lambda y: y.h)
        #print(node,to_visit)
        node=to_visit.pop(0)
        
    #print(visited)
    cost=0
    node=visited[-1]
    while True:
        if node.parent==None:
            break
        parent:Node=node.parent.node
        #print(node,"to",node.parent,"is",parent.link_costs[node.node])
        cost+=parent.link_costs[node.node]
        node=node.parent
        
        pass
        
    
    print(cost)