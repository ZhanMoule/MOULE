data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2

for i in range(len(data)):
    print(i,data[i])

pos=head
while pos!=-1:
    print(data[pos][0], end=' -> ')
    pos=data[pos][1]

#删除头节点
num=input("请输入你要删除的数字num=input")
if data[head][0]==num:
    head=data[head][1]

#删除中间某一个
"""else:
    pos=head
    while pos!=-1:
        if data[pos][0]==num:
            break
        pre=pos
        pos=data[pos][1]
    data[pre][1]=data[pos][1]
"""
pre=pos
while pos!=-1:
    if data[pos][0]=="d5":
        break
    pre=pos
    pos=data[pos][1]
data[pos][1]=pre
print(data[pos][0],end="->")
        
    
    

#删除尾节点


print()
pos=head
while pos!=-1:
    print(data[pos][0], end=' -> ')
    pos=data[pos][1]
