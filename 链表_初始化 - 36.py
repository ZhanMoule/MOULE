#初始化并输出原数据
data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2
def lprint(hd):
    p=hd
    while p!=-1:
        print(data[p][0], end=' -> ')
        p=data[p][1]
lprint(head)


#插入节点







#访问输出执行结果
print()
lprint(head)
