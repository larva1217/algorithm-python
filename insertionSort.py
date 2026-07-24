#삽입정렬-처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 것
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): #첫 번째 원소는 정렬되어 있다고 생각
    for j in range(i,0,-1):
        if array[j]<array[j-1]: #앞쪽 원소가 더 크면
            array[j],array[j-1]=array[j-1],array[j]

print(array)