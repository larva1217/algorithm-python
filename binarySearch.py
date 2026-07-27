#이진 탐색 - 정렬된 배열에서 가운데 값을 기준으로 탐색 범위를 절반씩 줄여가며, 
# 찾고 싶은 값(target)의 인덱스를 반환하는 알고리즘
#target-찾고 싶은 값
def  binary_search(array,target,start,end):
    if start>end:
        return
    
    mid=(start+end)//2

    if array[mid]==target:
        return mid

    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)

    else:
        return binary_search(array,target,mid+1,end)

array=[1,3,5,7,9]
print(binary_search(array,7,0,len(array)-1))