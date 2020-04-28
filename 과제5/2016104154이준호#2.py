#binary tree
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p

#utility.py
def printMatrix(d):
    m = len(d)
    n=len(d[0])
    
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

#print float matrix
def printMatrixF(d):
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print("%5.2f" % d[i][j],end=" ")
        print()

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)
    
def print_postOrder(root):
    if not root:
        return

    print_postOrder(root.l_child)
    print_postOrder(root.r_child)
    print(root.data)

# algorithm code starts here

key=[" ","A","B","C","D"]
p=[0,0.375, 0.375, 0.125,0.125]
n=len(p)-1

a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

inf = 1000
def optsearchtree(n,a,r):
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j=i+diagonal
            small = inf # when next diagnoal, have to init small = inf
            for k in range(i,j+1):
                psum = 0
                if(small > a[i][k-1]+a[k+1][j]):
                    for s in range(i,j+1):
                        psum += p[s] # p[s] == a[s][s]
                    a[i][j] = a[i][k-1]+a[k+1][j]+psum
                    small = a[i][k-1]+a[k+1][j]
                    idx = k
                r[i][j] = idx
    return a[1][n]

optsearchtree(n,a,r)

printMatrixF(a)
print()
printMatrix(r)

root=tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)
# 교훈 : import pdb 모듈 불러오고, 원하는 breakpoint에다가 breakpoint라고 코드 입력 후 f5로 컴파일 하면 한줄씩 디버깅 가능
# print할 때 개행 방지를 위해선 print("원하는 것 print",end="") 처럼 end=""를 입력해주면 됨
