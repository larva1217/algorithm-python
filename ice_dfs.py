#NxM 얼음틀
#구멍이 뚫려 있는 부분 0
#칸막이가 존재하는 부분 1
#구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어있는 경우
#서로 연결된 것으로 간주
#얼음이 주어졌을 때 생성되는 연결되는 것의 개수

def dfs(x,y):
    if x<-1 or x>=n or y<=-1 or y>=m:
        return False
        
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

n,m=map(int, input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int, input())))

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result += 1
print(result)

