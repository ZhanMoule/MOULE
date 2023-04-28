from random import randint

def rnddata(n):				#产生随机数值的降序链表
    data=[]
    head=-1
    tmp=randint(95,99)
    data.append([tmp,head])
    head=0
    for i in range(1,n):
        tmp=data[i-1][0]-randint(1,5)
        data.append([tmp,data[i-1][1]])
        data[i-1][1]=_________
    return data
a=rnddata(10)
b=rnddata(15)
print('序列一：',a,'\n序列二：',b)

ka=qa=heada=kb=headb=0		        #初始化所有指针位置
while ka!=-1 and kb!=-1:
    if __________:
        qa=ka
        ka=a[ka][1]
    else:
        if ka==heada:			#插入在头节点前



        else:				#插入在其他节点前



while kb!=-1:				#插入在尾节点后（a链表结束，b链表还有数据）
    
    
    
#输出结果
print('合并后的存储结构:',a)
print('链表逻辑结构: head =',heada)
p=heada
while p!=-1:
    print(a[p][0],end= ' ')
    p=a[p][1]
    
