import random
import time
n = (int)(input("정수 n 입력: "))
m=[]
# a = list(map(int,input("리스트 A 입력 : ").split()))
# a 원소 입력 후 각각의 원소 모두 정수로 변환
start = time.time() # 시작 시간 저장 - 입력하는데 걸리는 시간 빼기 위해 input 아래에 작성
a = [random.randrange(1,100) for i in range(n)]
# print("리스트 A의 원소 출력 :",a)

m.append(a[0])

for i in range(1,len(a)):
    m.append(max(m[i-1],a[i]))

# print("리스트 M의 원소 출력 :",m)
print("time :",time.time() - start) # 현재시각 - 시작시간 = 실행시간
# O(n)