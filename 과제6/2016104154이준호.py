#2016104154 이준호 과제 6

def printMatrix(d):
    m = len(d)
    n=len(d[0])
    
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

# 교재 예시 input 
# a=['A','A','C','A','G','T','T','A','C','C']
# b=['T','A','A','G','G','T','C','A']

# 과제6 조건(2)
a=['T','G','A','C','A','A','G','T']
b=['T','A','C','A','A','T','T']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        # case1: 시작점을 맞출경우
        penalty=0
        if a[i] != b[j]:
            penalty=1
        opt = table[i+1][j+1]+penalty
        minindex[i][j] = (i+1,j+1)
        # case2: b의 시작점에 틈을 줄 경우
        if opt > table[i+1][j]+2:
            opt = table[i+1][j]+2
            minindex[i][j] = (i+1,j)
        # case3: a의 시작점에 틈을 줄 경우
        if opt > table[i][j+1]+2:
            opt = table[i][j+1]+2
            minindex[i][j] = (i,j+1)
        table[i][j] = opt

printMatrix(table)
x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")