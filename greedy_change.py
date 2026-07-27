#거스름돈 문제
#거스름돈이 500원,100원,50원,10원
#손님에게 거슬러 주어야 할 돈이 N원(N은 항상 10의 배수)
#거슬러 주어야할 동전의 최소 개수

n=int(input("거슬러 줄 돈을 입력하세요 : "))
count=0
array=[500,100,50,10]

for coin in array:
    count+=n//coin
    n%=coin #현재 동전을 사용하고 남은 금액

print(str(count)+"개")