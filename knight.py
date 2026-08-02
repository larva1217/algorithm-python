#왕실의 나이트
#8*8 좌표(행:1~8, 열:a~h)
#나이트는 2가지 경우로 이동
#수평으로 두 칸 이동한 뒤 수직으로 한 칸
#수직으로 두 칸 이동한 뒤 수평으로 한 칸
#8*8 좌표 평면에 나잍트의 위치가 주어졌을 때
#나이트가 이동할 수 있는 경우의 수는?

input_data=input("열과 행을 입력하시오 : ")
row=int(input_data[1]) #행
col=int(input_data[0]) #열

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result=0

for step in steps:
    next_row=row+step[0]
    next_col=col+step[1]

    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        result+=1

print(result)