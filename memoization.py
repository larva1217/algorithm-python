#메모제이션
#다이나믹 프로그래밍 기법 중 하나
#한 번 계산한 결과를 메모리 공간에 메모하는 기법


d=[0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x]=fibo(x-1)*fibo(x-2)

    return d[x]

