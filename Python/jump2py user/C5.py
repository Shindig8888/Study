###클래스

result1 = 0
result2 = 0


def add1(num):
    global result1
    result1+=num
    return result1

def add2(num):
    global result2
    result2+=num
    return result2
print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

##계산기는 이렇게 늘려야됨

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    
    def substract(self,num):
        self.result -=num
        return self.result
    
    def multi(self, num):
        self.multi *= num
        return self.result
    


cal1 = Calculator()
cal2 = Calculator()#객체들

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(8))
print(cal2.add(999))

## class: 과자 틀; 객체: 과자; 객체끼리는 독립적임

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)

##여기서 self에 해당하는건 변수 a

print(a.first)
print(a.second)

b = FourCal()

b.setdata(3,7)
b.first
a.first

class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result
    
a = FourCal()
a.setdata(4,2)
a.add()


class Fourcal3():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
    

a = Fourcal3()
b = Fourcal3()
a.setdata(4,2)
b.setdata(3,8)
a.add()
a.mul()
a.div()
a.sub()
b.add()
b.mul()
b.div()
b.sub()

##생성자
a = Fourcal3()
a.add()#오류발생

#__init__

class FourCal:
    def __init__(self, first, second):#생성자로 객체생성 자동호출
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result
    def sub(self):
        result = self.first-self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first/self.second
        return result    
    
a = FourCal() #값을 입력해야됨
a = FourCal(4,2)

a.first
a.second
a.add()
a.div()

#클래스의 상속

class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
a.add()
a.mul()
a.sub()
a.div() #기존 클래스를 변경하지 않고 기능을 추가, 변경할 때 상속

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
    def add(self):
        result = self.first+self.second*2
        return result
    
a = MoreFourCal(4,2)
a.pow()
a.add()


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result
        

a = SafeFourCal(4,0)
a.div()

##클래스변수

class Family:
    lastname = "김"

Family.lastname

a = Family()
b = Family()

a.lastname
b.lastname

Family.lastname = "박"

a.lastname
b.lastname #둘 다 변경

'''
Class.클래스변수 = "다른변수" ==>클래스변수를 변경
a.클래스변수 = "다른변수" ==>그냥 객체변수를 생성하는 신텍스, 클래스변수는 변하지 않는다
'''

###모듈###

#함수, 변수, 클래스를 모아 놓은 파이썬 "파일"

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
#->mod1.py에 저장

#import 모듈_이름
#   모듈_이름.함수()
#함수만 불러오기 ==> form 모듈_이름 import 함수_이름

#from mod1 import add, sub

##if__name__=="main":의 의미


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


if __name__ == "main": #직접 파일을 실행했을 때 __name__변수 == "main"이기때문에True, 대화형 인터프리터나 다른 파일에서 모듈로 불러올때는 False(변수이름은 파일명)
    print(add(1,4))
    print(sub(4,2))


#->md1.py에 저장
    
import mod2

result = mod2.add(3,4)
print(result)

result = mod2.Math()

b = result.solv(4)

print(b)

###다른 디렉토리###

##시스템 디렉토리 추가
import sys

sys.path
sys.path.append("C:\\Users\\claix\\OneDrive\\Desktop\\Coddimg\\Study\\Python\\jump2py user")


import mod2
print(mod2.add(3,4))

###pythonpath

#프롬프트에서 입력
#set PYTHONPATH=C:\Users\claix\OneDrive\Desktop\Coddimg\Study\Python\jump2py user


###패키지
#디렌터리와 파이썬 모듈로 이루어짐 모듈==.py파일

'''C:\Users\claix>set PYTHONPATH=C:\Users\claix\OneDrive\Desktop\Coddimg\Study\Python\jump2py user

C:\Users\claix>python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import game.sound.echo #디렉토리
>>> game.sound.echo.echo_test() #함수실행, PYTHONPATH안의 import한 디렉토리 주소를 모두 연결해야됨
echo

#아니면, 

C:\Users\claix>python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from game.sound import echo #디렉토리에서 echo를 import하면
>>> echo.echo_test()#명령을 줄일 수 있음
echo
>>> from game.sound.echo import echo_test #디렉토리를 늘릴수록 
>>> echo_test() #명령을 줄임
echo
>>> quit()

C:\Users\claix>python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import game #import안에 __init__에서 정의됐을 때 참조가능
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'game' has no attribute 'sound'

C:\Users\claix>python
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import game.sound.echo.echo_test #한번에 함수까지 불러오는것도 불가능 마지막은 모듈 또는 패키지여야함
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package
>>>
'''

###__init__.py의 용도
#python 3.3 이전까지는 __init__.py가 없으면 패키지로 인식하지 않음

#공통함수의 정의 (__init__.py 내 저장)

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}")

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import game
# >>> print(game.VERSION)
# 3.5
# >>> game.print_version_info()
# The version of this game is 3.5
# >>> quit()


###패키지 내 모듈을 미리 import
    
from .graphic.render import render_test

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import game
# >>> game.render_test()
# render

###패키지 초기화

print("Initializing game . . .")

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import game
# Initializing game . . .

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from game.graphic.render import render_test
# Initializing game . . .

##초기화코드는 한 번 실행된 후 다시 import를 수행해도 실행되지 않음
# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import game
# Initializing game . . .
# >>> from game.graphic.render import render_test
# >>> quit()

### __all__

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from game.sound import * #디렉터리의 __all__편수를 설정하고 import
# Initializing game . . .
# >>> echo.echo_test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined 

__all__ = ['echo'] #를 game\\sound\\__init__.py에 저장, import 할 수 있는 모듈을 지정
#다만 a.b.c,...,last 일 경우 last가 모듈이면 __all__과 상관없이 import가능

# C:\Users\claix>python
# Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from game.sound import *
# Initializing game . . .
# >>> echo.echo_test()
# echo

###relative 패키지(한 모듈에서 다른 패키지경로의 모듈을 사용할 때)

#render.py를
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()

# >>> from game. graphic.render import render_test
# Initializing game . . .
# >>> render_test()
# render
# echo
    
from .. sound.echo import echo_test #.은 현재 디렉터리, ..은 부모 디렉터리
def render_test():
    print("render")
    echo_test()



####예외처리
    
f = open("나 없는 파일", 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나 없는 파일'

4 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

a = [1,2,3]
a[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range #4번째 인덱스가 없음

##Try - exept문

#try-except만 쓰는 방법; 이 경우에는 오류의 종류와 상관없이 오류가 발생하면 except블록 수행
try:
    ...
except:
    ...

#발생 오류만 포함한 except 문; 정해놓은 오류와 동일한 경우에만 except 블록 수행
try:
    ...
except '발생오류':
    ...

#발생 오류와 오류 변수까지 포함한 except문: 특정 오류가 발생하면 그 오류메시지를 변수에 저장하여 출력
try:
    4/0
except ZeroDivisionError as e:
    print(e)

#try-finally 문; 오류와 상관없이 finally의 명령을 수행
try:
    f = open('foo.txt', 'w')
finally:
    f.close()

#여러 개의 오류 처리
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(f"{e}, 0으로 나눌 수 없습니다.")
except IndexError as e:
    print(f"{e}, 인덱싱 할 수 없습니다.")

    #list index out of range, 인덱싱 할 수 없습니다.


try:
    a = [1,2]
    print(a[3])
    4/0
except(ZeroDivisionError, IndexError) as e:
    print(e)
    #표현만 다르고 먼저발생한 오류에만 대응하는건 같음
    

#try-else문
    
try: 
    age = int(input("나이를 입력하세요 : "))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age<=18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

        #오류가 일어날경우 except문 수행

##오류 회피하기
        
try:
    f = open("없는 파일", 'w')
except FileNotFoundError:
    pass

# >>> try:
# ...     f = open("없는 파일", 'w')
# ... except FileNotFoundError:
# ...     pass
# ...
# >>>

##오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError("fly 함수를 사용해주세요")
    
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

#Eagle()은 Bird()를 상속했으나 fly()를 오버라이딩하여 구현하지 않아 에러발생

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

###예외만들기

class MyError(Exception):
    pass


def say_nick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

##오류메시지 사용
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)


###내장 함수
    
#abs 절댓값
abs(3)
abs(-3)
abs(-1.2)

#all 다 참이어야 참
all([1,2,3])
all([1,2,None])
all([]) #빈 값은 True

#any 하나라도 참이면 참
any([1,2,3])
any([1,2,None])
any([None,None])
any([]) #빈 값은 False


#chr 유니코드 값을 받아 문자를 리턴
chr(97)
chr(44032)

#dir 객체가 지닌 변수나 함수를 보여줌
dir([1,2,3])

#divmod(a,b) a를 b로 나눈후 몫과 나머지를 튜블로 반환
divmod(7,3)

#enumerate
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)
#i에 대한 인덱스를 생성(emu, listvalue) => for 로 i<=emu, listvalue<=name

# 리스트를 딕셔너리로 변환하는 예제
my_list = ['a', 'b', 'c']
my_dict = dict(enumerate(my_list))
print(my_dict)

#eval; 문자열로 구성된 표현식을 입력으로 받아 문자열을 실행한 결괏값을 리턴

eval('1+2')
eval('"hi"+"a"')
eval('divmod(4,3)')

#filter; 함수를 통해 참인것만 수집 filter(함수, 리스트튜플) => 함수의 결과가 bullian 타입인경우 효율적

def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x>0

print(list(filter(positive, [1,-3,2,0,-5,6])))

list(filter(lambda x : x>0,[1,-3,2,0,-5,6])) #x>0 == True 인경우 'original list'에서 해당하는 값을 반환

list(filter(lambda x : x+2,[1,-3,2,0,-2,6])) #x+2 == True 이기 때문에 전체리스트를 반환


#hex 16진수

hex(234)

#id 객체를 입력받아 객체의 고유 주솟값을 리턴
a = 3
id(a)

b = 3
id(b)

#input([prompt]) []는 괄호안의 내용을 생략가능

#int 정수

#isinstance 클래스의 인스턴스인지 확인

class Person: 
    pass

a = Person()
isinstance(a, Person)

b = 3
isinstance(b, Person)

#len 길이
#list list변환

#map(함수, iterable); map()은 연산결과를 반환, filter는 연산결과로 참이나오면 그에 해당하는 원본 리스트 요소를 반환

def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number+2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2
list(map(two_times, [1,2,3,4,5]))

list(map(lambda x:x*2, [1,2,3,4,5]))

#max 최댓값을 리턴
#min 최솟값을 리턴

#Oct 정수를 8진수로
oct(34)

#open(filename, [mode]) mod에서 b는 wb,rb,ab 와 같이 사용가능, 바이러니 +다른 모드

#ord(c) 문자의 유니코드 숫자 값을 리턴

#pow(x,y) x의 y승

#range
list(range(5)) #0부터 4까지
list(range(5,10)) #5부터 9까지
list(range(0,-10,-2)) #0부터 -9까지 표현하는데 간격이 -2가되도록 표현
list(range(0,101,4)) #4의 배수 중 양수를 100까지 표현

#round(number, [,ndigitis]) 반올림(숫자, 부동소수점자리수)

#sorted([3,2,1]) 정렬
#리스트자료형의 sort는 리스트 자체를 정렬
#sorted는 정렬된 값을 반환

#str 문자화

#sum 입력 데이터의 합을 반환

#tuple 튜플화

#type 입력값의 자료현이 무엇인지 알려줌

#zip(*iterable) 동일한 개수로 이루어진 데이터들을 묶어서 리턴: 튜플로 묶어줌

list(zip([1,2,3],[4,5,6]))
print(dict(zip([1,2,3],[4,5,6])))

####표준 라이브러리

##datetime.date

#날짜 간 일수 계산
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
diff.days
print(type(diff))

#요일
day = datetime.date(2021, 12, 14)
day.weekday()#요일 0==월
day.isoweekday()#요일 1==월

##time
#time.time 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴
import time
time.time()

#time.localtime; time.time()에 의해 받은 값을 현재 현지시간으로 변환
time.localtime(time.time())

#time.asctime time.localtime에서 받은 튜플을 보기좋게 변환(뭔지랄인지)
time.asctime(time.localtime(time.time()))

#time.ctime 위에 다합친거(휴)
time.ctime()

#time.strftime  시간에 관계된 것을 세밀하게 표현하는 포맷코드 입력
import time
time.strftime("%x", time.localtime(time.time()))
time.strftime("%c", time.localtime(time.time()))
time.strftime("%Z", time.localtime(time.time()))

#time.sleep
import time 
for i in range(10):
    print(i)
    time.sleep(1)


##math.gcd: 최대 공약수
import math
math.gcd(60,100,80)

##math.lcm: 최소 공배수
import math
math.lcm(15,25)

#random
import random
random.random()

random.randint(1,10)

import random
def random_pop(data):
    number = random.randint(0,len(data-1))
    return data.pop(number)
if __name__ == "__main":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

data = [1,2,3,4,5]
random.sample(data, len(data))

#itertools.zip_longest
students = ['한민서', '황지민', '이영철', '이광수']
snacks = ['사탕', '초콜릿', '젤리']

result = zip(students, snacks)
print(list(result))

import itertools
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue = "새우깡")
print(list(result))

#itertools.permutation
import itertools
list(itertools.permutations(['1','2', '3'], 2))#순서상관있음
for a, b in itertools.permutations(['1','2', '3'], 2):
    print(a+b)

#itertools.combinations
list(itertools.combinations(['1','2', '3'], 2))#순서상관없음
for a, b in itertools.combinations(['1','2','3'], 2):
    print(a+b)

import itertools
it = itertools.combinations(range(1,46),6)
print(len(list(it)))

#itertools.combiations_with_replacement()
import itertools
it = itertools.combinations_with_replacement(range(1,46),6)
print(len(list(it)))


##functools
#functools.reduce
import functools
data = [1,2,3,4,5]
result = functools.reduce(lambda x,y: x+y, data)
print(result)

num_list = [3,2,8,1,6,7]
max_num = functools.reduce(lambda x, y: x if x>y else y, num_list)
print(max_num)


##operator
#operator.itemgetter
from operator import itemgetter

students = [
    ("Jane", 22, 'A'),
    ("Dave", 32, 'B'),
    ('Sally', 17, 'B')]


result = sorted(students, key=itemgetter(1))
print(result)

students = [
    {'name':'jane', 'age':22, 'grade':'A'},
    {'name':'dave', 'age':32, 'grade':'B'},
    {'name':'sally', 'age':17, 'grade':'B'},
]

result = sorted(students, key = itemgetter('age'))
print(result)


#operator.attrgetter

from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B')
]

result = sorted(students, key = attrgetter('age'))

#shutil: 파일을 복사, 이동

#glob: 특정 디렉터리의 파일 이름 모두

import glob
glob.glob('C:\\Users\\claix\\OneDrive\\Desktop\\Coddimg\\Study\\Python\\jump2py user\\C*')

#pickle
import pickle
f = open('test.txt', 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open('test.txt', 'rb')
data = pickle.load(f)
f.close()
print(data)

#os

import os
os.environ
os.environ['PATH']
os.chdir("C: \WINDOWS")
os.getcwd()

os.system("dir")#시스템명령어

f = os.popen("dir") #명령어 결과물을 읽기모드형태의 파일객체로 리턴
print(f.read())

#zipfile 파일 압축
import zipfile
with zipfile.ZipFile('mytext', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

with zipfile.Zipfile('mytext.zip') as myzip:
    myzip.extractall()

#threading

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)
print("Start")
threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

print("End")

#tempfile
import tempfile
filename = tempfile.mkstemp()
filename
f = tempfile.TemporaryFile()
f
f.close()


#traceback 오류추적
import traceback
def a():
    return 1/0
def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다")
        print(traceback.format_exc())
main()


#json
import json
with open('myinfo.json') as f:
    data = json.load(f)

import json
d = {"name": "홍길동", "birth": "0525", "age": 30}
json_data = json.dump(d)

#urllib SSL은 import ssl
import urllib.request

def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'. format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' %page, 'wb') as f:
            f.write(s.read())

get_wikidocs(12)

#webbrowser
import webbrowser

webbrowser.open('http://naver.com')

###외부 라이브러리
##Faker
from faker import Faker
fake = Faker()

fake.name()

fake = Faker('ko-KR')
fake.name()

fake.address()

test_data = [(fake.name(), fake.address()) for i in range(30)]
test_data

##sympy

from fractions import Fraction
import sympy

x = sympy.symbols("x") #미지수 생성

f = sympy.Eq(x*Fraction('2/5'), 1760)
sympy.solve(f)


import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
sympy.solve(f)

import sympy
x, y = sympy.symbols("x, y")
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
sympy.solve([f1, f2])
