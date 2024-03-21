## 리스트 자료형

odd = [1, 3, 5, 7, 9]
odd

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1,2, ['Life','is']]
f = list()

#리스트인덱싱
a = [1,2,3]
a[0] + a[2]
a[-1]

#다중리스트
a = [1,2,3,['a','b','c']]
a[0]
a[-1]
a[-1][0]

#리스트슬라이싱
a = [1,2,3,4,5]
a[0:2]
b = a[:2]
c = a[2:]
b
c

a = [1,2,3,['a','b','c',],4]
a[2:5]
a[3][:2]

#리스트 연산

a = [1,2,3]
b = [4,5,6]

a+b

a*3

len(a)

c = [44,55,66]
len(c)

a=[1,2,3]
a[2] + "hi" #오류
str(a[2])+"hi"

#리스트값 modify
a = [1,2,3]
a[2] = 4
a

del a[1]
a

a = [1,2,3,4,5]
del a[2:]

a

#리스트 관련 함수

a = [1,2,3]
a.append(4)
a
a.append(['a', 'b'])
a


a = [1,4,3,2]
a.sort()
a
a = ['a', 'b','d', 'c']
a.sort()

a = ['a','b','d','c']
a.reverse()
a

a = [1,2,3]
a.index(3)

a.insert(0,4)
a

a = [1,2,3]
a*=2
a

a.remove(3)#첫번째로 나오는 () 삭제
a

#리스트 요소 끄집어내기

a = [1,2,3]
a.pop()#설정 없으면 맨 마지막값, 끄집어내면 삭제됨
a = [1,2,3]
a.pop(1)
a

#요소세기

a = [1,2,3,1]
a.count(1)

#리스트 확장

a = [1,2,3]
a.extend([4,5])#리스트 + 리스트
a



##튜플 자료형

#리스트는 요솟값의 생성, 삭제, 수정이 가능하지만 튜플은 바꿀 수 없음

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab', 'cd'))

t1 = (1,2,'a','b')
t1[0]

t1 = (1,2,'a','b')
t1[1:]

t2 = (3,4)
t3 = t1+t2
t3

t2 = 3,4
t3 = t2*3
t3

t1 = (1,2,'a','b')
len(t1)


##딕셔너리 자료형

dic = {'name':'pey', 'phone':'010-9999-1234','birth':'1118'}

a = {1:'hi'}
a = {'a':[1,2,3]}

#딕셔너리 추가하기

a={1:'a'}
a[2] = 'b'
a

a['name'] = 'pey'
a

a[3] = [1,2,3]

a[3] = 1
a

del a[1]
a

#키를 사용해 value얻기

grade = {'pey':10, 'julliet':99}
grade['pey']
grade['julliet']

a = {1:'a',2:'b'}
a[1]
a[2]

a = {'a':1, 'b':2}
a['a']

#키 리스트 만들기

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
list(a.keys())
a.values()


for k in a.keys():
    print(k)

a.items()

#클리어

a.clear
a

#키로 밸류얻기

a.get('name')
a.get('phone')

a['unknown'] #에러
a.get('unknown') #none

#키가 존재하는지 조사

'name' in a
'unknon' in a

##집합 자료형

s1 = set([1,2,3])
s1
s=set()
s

s2 = set("Hello")
s2

"""
set의 특징
중복을 허용하지 않음
순서가 없음 = 인덱싱이 안됨 => 튜플이나 리스트로 변환한다음 확인
"""

#교집합 합집합 차집합

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2 #교집합
s1.intersection(s2)

s1 | s2 #합집합
s1.union(s2)

s1 - s2 #차집합
s2 - s1
s1.difference(s2)
s2.difference(s1)

#값 추가
s1 = set([1,2,3])
s1.add(4)
s1

#값 여러개추가
s1 = set([1,2,3])
s1.update([4,5,6])
s1

#특정 값 제거
s1 = set([1,2,3])
s1.remove(2)
s1

##불 자료형

a = True
b = False

type(a)
type(b)

1==1
2>1
2<1

#프로그램 예시

a = [1,2,3,4]
while a: #a가 참일 경우
    print(a.pop()) #pop(뒤에서부터 끄집어냄)을 계속실행

if []:
    print("참")
else:
    print("거짓")

if [1,2,3]:
    print("참")
else:
    print("거짓")

#bool
    
bool(None)

##변수

#변수의 주소
a = [1,2,3]
id(a)

#리스트를 복사할 때

a = [1,2,3]
b=a

id(a)
id(b)#동일

a is b

a[1] = 4
a
b


# 다르게 복사하기 :이용
a = [1,2,3]
b=a[:] #전체선택

a[1] = 4

a
b

#copy 모듈 이용

from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
a
b

b is a

#변수를 만드는 방법

(a, b) = 'python', 'life'#<-튜플
[a,b] = ['python', 'life'] #<-리스트
a = b = 'python'

(a,b) = (3,5)

a,b = b,a
a
b




