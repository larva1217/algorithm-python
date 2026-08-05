import heapq

def heapsort(iterable):
    h=[]
    result=[]

    for value in iterable:
        heapq.heappush(h,value) #리스트 h에 value 삽입

    for i in range(len(h)):
        result.append(heapq.heappop(h)) #힙에서 가장 작은 값을 반환

    return result

print(heapsort([6, 5, 9, 3, 4, 1, 2]))
