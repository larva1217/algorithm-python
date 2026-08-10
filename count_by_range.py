#값이 특정 범위에 속하는 데이터 개수를 구하기

from bisect import bisect_left,bisect_right

#bisect_left(a, x) → x가 들어갈 수 있는 가장 왼쪽 위치
#bisect_right(a, x) → x가 들어갈 수 있는 가장 오른쪽 위치
def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_value-left_value

a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))