#문자열 재정렬
#알파벳 대문자, 숫자(0~9)로 구성된 문자열
#모든 알파벳을 오름차순으로 정렬
#모든 숫자를 더한 값을 이어서 붙인다.

data=input()
result=[]
value=0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)

result.sort()

if value!=0:
    result.append(str(value))

print("".join(result))