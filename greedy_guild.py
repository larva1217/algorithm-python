#모험가 길드 문제
#모험가는 N명
#공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가와 여행
#만들 수 있는 그룹 수의 최대값은?
#몇 명의 모험가는 남아있어도 됨

n=int(input("모험가 수를 입력하시오 : "))
data=list(map(int,input("공포도를 입력하시오 : ").split()))
data.sort()

result=0 #총 그룹수
count=0 #현재 그룹에 포함된 모험가 수

for i in data:
    count+=1

    if count>=i: #현재 그룹에 포함된 모험가 수>공포도
        result+=1
        count=0

print("그룹 수 : ", result)