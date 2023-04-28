data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2

for i in range(len(data)):
    print(i,data[i])
pos=head

#删除头结点
#head=data[head][1] 
#删除尾节点
pre=head
while pos!=-1:
    if data[pos][0]=="d8":
        break
    pre=pos
    pos=data[pre][1]
data[pre][1]=data[pos][1]   
#删除中间节点

pos=head
while pos!=-1:
    print(data[pos][0],end="-->")
    pos=data[pos][1]
    
