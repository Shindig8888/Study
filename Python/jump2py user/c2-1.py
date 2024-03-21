## 숫자 형태
# 정수형(int)
a = 123
a = -178
a = 0

# 실수형(float)
a = 1.2
a = -3.45
a = 4.24e10
b = 4.4e-10

print(a)
print(b)

#8진수
a = 0o177
print(a)

# 16진수
a = 0x8ff
b = 0xabc

print(a)
print(b)

## 연산자

#사칙연산
a = 3
b = 4

a+b
a-b
a*b
a/b

# 제곱
a**b

# 나머지 리턴
7 % 3

#몫 리턴
9//4

# 복합 연산
a = 1
a = a + 1
print(a)

a+=1 #=a=a+1
a-=1 #=a=a-1

## 문자열 자료형(str)

food = "python's favorite food is perl" #문자열 안에 '가 들어가는 경우
food

say = '"python is very easy" he says.' #문자열 안에 "가 들어가는 경우
say

food = 'python\'s favorite food is perl' #문자열 안에 '가 들어가는 경우 역슬래쉬
food

#줄바꾸기

multiline = "life is too short\nyou need puthon"
print(multiline)

multiline = '''
life is too short \a
you need python
'''

#문자열 연산

head = "python "
tail = "is fun!"
head+tail #문자열 합

a = "python "
a * 2 #문자열 곱

print("=" * 50)
print("My Program")
print("=" * 50)

#문자열 길이

a = "life is too short"
len(a)

#문자열 인덱싱
a = "Life is too short, You need Python"
a[3] #파이썬은 0부터 셈

a[0]
a[12]
a[-1]#뒤에서부터 읽기, [-0]에서 0=-0이므로 뒤에서읽기는 해당안됨

#문자열 슬라이싱

a[0:4] #끝번호에 해당하는 번호는 출력하지 않음(미만으로 생각)
a[5:7]
a[12:17]

a[19:] #19번부터 끝까지 출력

a[:17] #처음부터 17번까지
a[:]
a[19:-7] #20번째부터 뒤에서 6번까지

# 슬라이싱으로 문자열 나누기

a = "20230331Rainy"
date = a[:8]
weather = a[-5:]
date
weather

a = "20230331Rainy"
year = a[:4]
day = a[4:8]

year
day
weather

a = "pithon"
a[1]="y"
a ##에러

a = a[:1]+'y'+a[2:]
a

#문자열 포매팅

"I eat %d apples" % 3

"I eat %s apples" % "five" # %d 는 숫자, %s 는 문자

number = 3
"I eat %d apples" %number #변수사용

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days" %(number, day)

"Error is %s%" % 98

"Error is %s%%" % 98

#정렬
"%10s" %"hi"
"%-10sjane" %"hi"

#소수점
"%0.4f" %3.421324231

"%10.4f" %3.421324231
 
##format 함수
"I eat {0} apples". format(3)

"I eat {0} applea". format("five")

number = 3
"I eate {0} apples". format(number)

number = 10
day = "three"
"I eat {0} apples, so I was sick for {1} days". format(number, day)

"I eat {number} apples, so I was sick for {day} days". format(number = 10, day = 3)

"I ate {0} apples, so I was sick for {day} days.".format(10, day=day)

#format 정렬

"{0:<10}". format("hi") #10칸 중 왼쪽정렬

"{0:>10}". format("hi") #10칸 중 오른쪽정렬
                  
"{0:^10}". format("hi") #10칸 중 가운데정렬

"{0:=^10}". format("hi") #10칸 중 가운데정렬, 공백을 =으로 채우기
"{0:!<10}". format("hi") #10칸 중 왼쪽정렬, 공백을 !으로 채우기

#소수점

y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)

#{또는} 문자표현

"{{ and }}".format()

# f문자열 포매팅(파이썬 3.6부터 지원)

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다'

'나의 이름은 {name}입니다. 나이는 {age}입니다'.format(name = name, age = age)

f'나는 내년이면 {age+1}살이 된다'

d = {'name':'홍길동' , 'age' : 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'

f'{"hi":>10}'

f'{"hi":^10}'


f'{"hi":=<10}'

y = 3.14151910
f'{y:0.4f}'
f'{y:10.4f}'

f'{{ and }}'

##문자열 관련 함수

#문자 갯수
a='hobby'
a.count('b')

#위치
a = 'Python is the best choice'
a.find('b')
a.find('e') #처음 나온 위치를 반환
a.find('k') #찾지 못하면 -1반환

a. index('b')
a. index('k') #찾지 못하면 에러

#문자열 삽입
", ".join('abcd') # abcd 사이사이에 , 
", ".join(['a','b', 'c', 'd'])

#대문자, 소문자
a = 'hi'
a = a.upper()
a
a.lower()

#공백지우기

a = " hi "
a.lstrip()
a.rstrip()
a.strip()

#문자열 바꾸기

a = "Life is too short"
a.replace("Life", "Your leg")

#문자열 나누기

a = "Life is too short"
a.split()