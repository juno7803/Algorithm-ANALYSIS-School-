# 2016104154 이준호
# 1번 2번 두문제 다 최솟값을 구하기 위해 비교하기 위한 값을 1000이라고 가정하여 풀었습니다(small = 1000 이라고 초기화 하여 비교함)
import math
import pdb

# utility.py code - printMatrix
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

#[11쪽 실습과제1] 연쇄행렬 곱셈 알고리즘
def order(p,i,j):
    if(i == j):
        print("A",i,end='')
    else:
        k = p[i][j]
        print("(",end='')
        order(p,i,k)
        order(p,k+1,j)
        print(")",end='')

d=[5,2,3,4,6,7,8]
n = len(d)-1 # 인덱스 값이므로 n-1

m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

inf = 1000 # 최솟값 비교 위해 원소의 최댓값을 1000이라고 가정하여 풀이
def minmult(n,m,p):
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j=i+diagonal
            small = inf # small의 초기값 설정 => 최대한 큰 값으로 + 대각선에서 최솟값을 다 찾으면 다음 대각선 에선 다시 small을 inf로 초기화
            for k in range(i,j):
                if(small > m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]):
                    m[i][j] = m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                    small = m[i][j]
                    idx = k
                p[i][j] = idx
    return m[1][n]

minmult(n,m,p)
print("실습과제1: 연쇄행렬 곱셈 알고리즘")
printMatrix(m)
print()
printMatrix(p)
print()
order(p,1,n)
print()

#[23쪽 실습과제2] 최적 이진검색 트리
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

print("\n실습과제2: 최적 이진검색 트리")
optsearchtree(n,a,r)
printMatrixF(a)
print()
printMatrix(r)

root=tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)