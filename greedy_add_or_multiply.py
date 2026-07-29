#곱하기 혹은 더하기 - 그리디 알고리즘
#숫자(0~9)를 문자열로 입력받음
#왼쪽에서 오른쪽으로 하나씩 몯든 숫자를 확인하며
#숫자 사이에 "+" or "*"
#만들어질 수 있는 가장 큰 수는?

data=input("숫자를 입력하세요 : ")
result=int(data[0])

for i in range(1,len(data)):
    num=int(data[i])

    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)