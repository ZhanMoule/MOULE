# -*- coding: cp936 -*-
#��ʼ�������ԭ����
data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2
def lprint(hd):
    p=hd
    while p!=-1:
        print(data[p][0], end=' -> ')
        p=data[p][1]
lprint(head)

#����ڵ�

pos=input("������������Ǹ�Ԫ��ǰ��")
num=input("�������²���Ԫ�ص�����")

p=head
while p!=-1:
   if data[p][0]==pos:
       break  
   pre=p
   p=data[p][1]
data.append([num,data[pre][1]])
data[pre][1]=len(data)-1

#�������ִ�н��
print(data)
lprint(head)
