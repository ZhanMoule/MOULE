data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
print()
#删除头节点
def delhead(head):
    return data[head][1]

#删除尾节点
def deltail():
    p=head
    while data[p][1]!=-1:
        pre=p
        p=data[p][1]
    data[pre][1]=-1

#删除中间节点
#根据索引查找前继节点
def delindex(p):
        pre=head
        while data[pre][1]!=p:
            pre=data[pre][1]
        data[pre][1]=data[p][1]
        
#根据值查找前继节点,删除某节点
def delvalue(head,numv):
    p=head
    while data[p][0]!=numv and p!=-1:
        pre=p
        p=data[p][1]
    if p==head:				#删头节点
        head=data[head][1]
    elif p==-1:				#没找到
        print('not find')
    else:
        data[pre][1]=data[p][1]	#删除其他节点
        
    return head

            
#自定义函数应用
#head=delhead(head)
#deltail()
#delindex(3)
x=input('请输入要删除的数据：')
head=delvalue(head,x)

#访问输出
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
