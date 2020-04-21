import random
import time
def maxsearch(s):
    maxValue = s[0]
    if len(s) == 1:
        return s[0]
    for i in range(1,len(s)):
        if maxValue < s[i]:
            maxValue = s[i]
    return maxValue
# max 값 찾는 함수, 순차탐색을 이용하여 구현
a=[]
m=[]
n=(int)(input("정수 n 입력 :"))
start = time.time() 
# 시작 시간 저장 - 입력하는데 걸리는 시간 빼기 위해 input 아래에 작성
for i in range(0,n):
    tmp = random.randrange(1,100)
    a.append(tmp)
    m.append(maxsearch(a))

print("리스트 A의 원소 출력 :",a)
print("리스트 M의 원소 출력 :",m)
print("time :",time.time() - start) # 현재시각 - 시작시간 = 실행시간
