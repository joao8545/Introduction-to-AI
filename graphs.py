from  classes import *
from algorithms import *
s=Node("s",12)
a=Node("a",8)
b=Node("b",11)
c=Node("c",5)
d=Node("d",8)
e=Node("e",4)
f=Node("f",4)
g=Node("g",0,True)
h=Node("h",6)
p=Node("p",11)
q=Node("q",9)
r=Node("r",6)

graph1=[s,a,b,c,d,e,f,g,h,p,q,r]

Link.create_link(s,d,3)
Link.create_link(s,e,9)
Link.create_link(s,p,1)
Link.create_link(b,a,2)
Link.create_link(c,a,2)
Link.create_link(d,c,8)
Link.create_link(d,b,1)
Link.create_link(d,e,2)
Link.create_link(e,h,1)
Link.create_link(e,r,9)
Link.create_link(f,g,5)
Link.create_link(f,c,2)
Link.create_link(h,p,4)
Link.create_link(h,q,4)
Link.create_link(p,q,15)
Link.create_link(q,r,3)
Link.create_link(r,f,5)
        
greedy(graph1)

a_star(graph1)