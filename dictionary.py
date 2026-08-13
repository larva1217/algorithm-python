#딕셔너리
#Key, Value를 한 쌍으로 가지는 자료형
#{Key1: Value1, Key2: Value2, Key3: Value3, ...}

dic = {'name':'lee', 'phone':'010-1111-2222', 'birth':'1217'}

a = {'a': [1, 2, 3]}


#딕셔너리 추가하기
a={'1':'a'}

a[2]='b'
print(a)  #{1: 'a', 2: 'b'}

a['name']='pey'
print(a)  #{1: 'a', 2: 'b', 'name': 'pey'}


#딕셔너리 삭제하기
del a['1']
print(a)

#딕셔너리에서 Key를 사용해 Value 얻기
grade={'pey':10,'julliet':90}
grade['pey'] #Key를 사용해서 Value를 얻을 수 있다
grade['julliet']


#딕셔너리에서 Key는 고유한 값
#중복되는 Key 값을 사용하면 하나를 제외한 나머지 것들이 모두 무시
a={'1':'a','1':'b'}
a['1']


#Key 리스트 만들기 - keys
#리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다
a = {'name':'lee', 'phone':'010-1111-2222', 'birth':'1217'}
a.keys()

#딕셔너리 키 객체를 리스트로 반환
list(a.keys())


#valuse 리스트 만들기 - values
a.values()

#Key,value 쌍 얻기 - items
a.items()

#key, value 쌍 모두 지우기 - clear
a.clear()

#key로 value 얻기
#존재하지 않는 키로 값을 가져올 경우 -> None 반환 
#a['nokey'] -> 오류 발생 
a = {'name':'lee', 'phone':'010-1111-2222', 'birth':'1217'}
a.get('name')  #'lee'


#찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게
a.get('nokey', '정보없음')


#해당 key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name':'lee', 'phone':'010-1111-2222', 'birth':'1217'}
'name' in a #True

#key로 value 꺼내기 - pop
a = {'name':'lee', 'phone':'010-1111-2222', 'birth':'1217'}
phone=a.pop('phone')
print(phone)