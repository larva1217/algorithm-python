#선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): 
    min_index=i #가장 작은 원소 인덱스

    for j in range(i+1,len(array)):
        if array[min_index]>array[j]: #더 작은 값을 발견
            min_index=j

    array[min_index],array[j]=array[j],array[min_index]

print(array)
        