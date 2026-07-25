#퀵 정렬

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start #피벗-맨 앞의 원소
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]: #피벗보다 큰 값을 찾을 때 까지 이동(왼쪽)
            left += 1

        while right > start and array[right] >= array[pivot]: #피벗보다 작은 값을 찾을 때 까지 이동(오른쪽)
            right -= 1

        if left > right: #왼쪽 포인터, 오른쪽 포인터가 엇갈리면, 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #작은 데이터와 큰 데이터 교체 
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1) #왼쪽 부분만 다시 정렬
    quick_sort(array, right + 1, end) #오른쪽 부분만 다시 정렬

quick_sort(array,0,len(array)-1)

print(array)

