import random
while(1):
    n = int(input("input n: "))
    if(n<3):
        print("n must be over 3, put another int number")
    else:
        break
s = [random.randrange(1,10) for i in range(n)]
print(s)
temp = 0
while True:
    while(1):
        m = int(input("input m: "))
        if(m > n):
            print("out of range, put another int number")
        else:
            break
    mlist=[]
    # 여기서 mlist를 초기화 해야함
    if(m==0):
        print("program end")
        break
    for i in range(0,n):
        end = False
        for j in range(i,i+m):
            if(n-i <m):
                end = True
                break
            # 새로운 배열을 다 채우면 end=true
            temp += s[j]
        if(end):
            break
        # end = true일때 배열 채우기를 멈추고 for문을 탈출  
        mlist.append(temp)
        temp = 0    
    print(mlist)
    mlist.sort()
    # tmax와 tmin을 쉽게 구하기 위해 정렬
    tmax = mlist[len(mlist)-1]
    tmin = mlist[0]
    print("tmax: ",tmax)
    print("tmin: ",tmin)
