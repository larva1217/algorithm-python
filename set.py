#집합 자료형
#set() - 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
#중복 허용 X
#순서가 없다

s1=set([1,2,3])
print(s1) #{1, 2, 3}

s2=set("Hello")
print(s2) #{'H', 'o', 'e', 'l'}

s3={1,2,3}
print(s3)

s4={'a','b','c'}
print(s4)

#집합 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트, 튜플로 변환해야한다.
s5=set([1,2,3])

li=list(s5)
print(li)    #[1, 2, 3]
print(li[0])

t1=tuple(s5)
print(t1)    #(1, 2, 3)
print(t1[0])


s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2))

#차집합
print(s1-s2)
print(s1.difference(s2))

#값 1개 추가하기-add
s1.add(4)
print(s1)

#값 여러개 추가하기-update
s1.update([10,11,12])
print(s1)

#특정 값 제거하기-remove
s1.remove(4)
print(s1)

#특정 값 제거하기-discare 존재하지 않은 값 제거해도 오류X
s1.discard(5)
print(s1)

#모든 값 제거하기-clear
s1.clear()
print(s1)