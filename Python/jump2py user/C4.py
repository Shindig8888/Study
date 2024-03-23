## v파이썬의 입출력

#파이썬 함수 구조

def add(a,b):
    return(a+b)


a = 3
b = 4
c = add(a,b)
print(c)

#일반적인 함수

def add(a,b):
    result = a+b
    return result

a = add(3,4)
print(a)

#입력값이 없는 함수

def say():
    return 'hi'

a = say()
print(a)

#리턴값이 없는 함수

def add(a,b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")#리턴값은 리턴 명령어로 받은 값만을 뜻함

add(3,4) #함수자체가 리턴값을 가지지않고 출력기능
print(a) #리턴값이 없기 때문에 none

# 입력값도, 리턴값도 없는 함수

def say():
    print('hi')

say()


#매개변수를 지정하여 호출하기

def sub(a,b):
    return a-b

result = sub(a=7, b=3)#def에서 지정한 a,b

print(result)

result = sub(b=8, a=5)

# 입력값이 몇개가 될 지 모를 때

def add_many(*a):
    result = 0
    for i in a:
        result += i
    return result

resultf = add_many(1,2,3)
print(resultf)

def add_mul(choice, *a):
    if choice =='add':
        result = 0
        for i in a:
            result += i
    elif choice == 'mul':
        result = 1
        for i in a:
            result *= i
    return result
    
b = add_mul('add', 1,2,3,4,5,6)
print(b)

b = add_mul('mul', 1,2,3,4,5,6)
print(b)

#키워드 매개변수 => 딕셔너리

def print_kwargs(**a):
    print(a)

print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3)

#함수의 리턴값은 언제나 하나

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)


def add_and_mul(a,b):
    return a+b
    return a*b

am = add_and_mul(3,4)
print(am) #첫번째 리턴에서 끝

#특정상황에서 리턴으로 빠져나가기

def say_nick(nick):
    if nick =='바보':
        return
    print(f"나의 별명은 {nick} 입니다.")

print(say_nick ("야호"))
print(say_nick ("바보"))

#매개변수 초기값 설정

def say_myself(name, age, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살 입니다.")
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박박박", 108)
say_myself("박박김", 16, None)


# def say_myself(name, man=True, age): #parameter without a default follows parameter with a default: 초깃값이 있는 매개변수 뒤에 없는 매개변수가 위치할수없음
#     print(f"나의 이름은 {name}입니다.")
#     print(f"나이는 {age}살 입니다.")
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다")

#함수 안에서 선언한 변수의 효력 범위
        
a = 1
def vartest(a):
    a += 1

vartest(a)
print(a) #==> 1; 함수 안에서 선언한 함수는 함수만의 것, 함수밖의 변수와는 상관없음

def vartest(a):
    a = a+1

vartest(3)
print(a)

vartest(a)

#함수 안에서 함수 밖의 변수를 변경하는 법

def vartest(a):
    a +=1
    return a #리턴값저장

a = vartest(a) #변수a를 리턴값으로 만듦
print(a)


a = 1
def vartest():
    global a #a를 파라미터가 아니라 글로벌변수로 취급
    a += 1

vartest()
print(a)
#외부변수를 사용하는 함수는 권장하지 않으므로 리턴값을 사용하는걸 권장


#lambda 예약어

add = lambda a,b:a+b
result = add(1,2)
print(result)

###사용자 입출력

a = input()
input("안내문구 : ")

number = input("숫자를 입력하세요: " )
print(number)

##print

a = 123
print(a)

a = "python"
a = [1,2,3]

#큰따옴표로 둘러싸인 문자열은 +와 동일

print("life " "is " "short")

#문자열 띄어쓰기는 쉼표로

print("life", "is", "short")

#한줄에서 결과물 출력

for i in range(10):
    print (i, end=' ')


##파일 읽고 쓰기
    
#파일 생성하기
    
f = open("새 파일.txt", "w")
f.close

'''
r = 읽기모드: 파일을 읽기만 할 때 사용
w = 쓰기모드: 파일에 내용을 쓸 때 사용
a = 추가모드: 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

#정보기입(w)
f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt" , 'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다. \n"
    f.write(data)
f.close


##파일을 읽기
#readline

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close

while True:
    data = input()
    if not data: break
    print(data)

#readlines()
    
f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close

#기존 줄바꿈+print()의 내장 줄바꿈=>줄바꿈2개


# line.strip

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'r')
lines = f.readlines()
for line in lines:
    line = line.strip()# 문자열에 앞뒤로 붙어있는 공백과 줄바꿈제거
    print(line)
f.close

#read 함수

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'r')
data = f.read()
print(data)
f.close #전체내용 리턴

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'r')
for line in f:
    print(line)
f.close

#파일에 새로운 내용 추가
f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close

f = open("C:/Users/claix/OneDrive/Desktop/Coddimg/Study/새 파일.txt",'r')
for line in f:
    print(line, end="")
f.close

#with문과 사용

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close

with open("foo.txt", 'w') as f:
    f.write("If life gives you lemon, just make lemonade")

with open("foo.txt", 'r') as f:
    for line in f:
        print(line)


###프로그램의 입출력
import sys
args = sys.argv[1:]
for i in args:
    print(i)
