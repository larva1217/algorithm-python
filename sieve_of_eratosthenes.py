#에라토스테네스의 알고리즘
#특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 때 사용
#O(NloglogN)

import math

n=1000 #2부터 1000까지의 모든 수에 대하여 소수 판별

array=[True for i in range(n+1)] #처음엔 모든 수가 소수(True)인 것으로 초기화  [True, True, True, True, True, True]

for i in range(2,int(math.sqrt(n)+1)):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1

for i in range(2,n+1):
    if array[i]:
        print(i, end=" ")