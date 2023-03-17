class Node:

    def __init__(self,label,h=0,is_goal=False,):
        self.label=label
        self.h=h
        self.out_link:list[Link]=[]
        self.in_link:list[Link]=[]
        self.is_goal=is_goal
        
    def __str__(self):
        return f"{self.label.upper()}"
    
    def __repr__ (self):
        return f"{self.label.upper()}"
    
    def create_outgoing_link(self,target,cost):
        l=Link(self,target,cost)
        self.out_link.append(l)
        target.in_link.append(l)
        
        
class Link:
    def __init__(self,start,end,cost) -> None:
        self.start=start
        self.end=end
        self.cost=cost
        
    def __str__(self) -> str:
        return f"{self.start} --{self.cost}--> {self.end}"
    
    def __repr__(self) -> str:
        return f"{self.start} --{self.cost}--> {self.end}"
    
    @staticmethod
    def create_link(start:Node,end:Node,cost:int):
        l=Link(start,end,cost)
        start.out_link.append(l)
        end.in_link.append(l)
        return
 