# 2016104154 이준호

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

# 문제1 : 7쪽 실습과제
import math
def bin(n,k):
    if(k==0 or n==k):
        return 1
    else:
        return bin(n-1,k-1) + bin(n-1,k)
        
def bin2(n,k):
    b=[[0 for col in range(k+1)] for row in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,min(i,k)+1):
            if(j==0 or j==i):
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j-1] + b[i-1][j]
    return b[n][k]

print(bin(10,5),bin2(10,5))

# 문제2 : 24-26쪽 실습과제
def allShortestPath(g,n):
    p = [[0]*n for t in range(n)]
    d = g
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if(d[i][k]+d[k][j] < d[i][j]):
                    p[i][j] = k+1
                    d[i][j] = d[i][k] +d[k][j]
    return(d,p)
# k가 아닌 k+1을 해준 이유: 배열의 index는 0부터 시작이므롤 0~n으로 for문을 돌렸으나 문제조건이 노드의 num은 1부터 시작이므로 p에 노드값을 넣어줄땐 k+1을 넣는다.

def _path(p,q,r):
    if(p[q][r]!=0):
        _path(p,q,p[q][r]-1)
        print("v",p[q][r])
        _path(p,p[q][r]-1,r)
# 경로탐색시에 p는 노드의 값(index+1)이 들어간 것이므로, index의 값으로 바꿔줘야해서 -1 해줘야 한다.

def path(p,q,r):
    print("v",q)
    _path(p,q-1,r-1)
    print("v",r)
# (5,3)은 곧 p에선 배열의 index 때문에 4행 2열과 같으므로 -1을 해줘야 한다.

inf = 1000
g=[[0,1,inf,1,5],[9,0,3,2,inf],[inf,inf,0,4,inf],[inf,inf,2,0,3],[3,inf,inf,inf,0]]
printMatrix(g)
d,p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)

path(p,5,3)