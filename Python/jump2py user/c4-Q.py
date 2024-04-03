
##Q1
def is_odd(number):
    if number%2==0:
        print("짝수입니다")
    else:
        print("홀수입니다")

is_odd(3)
is_odd(999999999999999998)

is_odd = lambda x: print("홀수입니다") if x%2==1 else print("짝수입니다")

###정답, 람다함수 학습할 것


##Q2
def is_even(*number):
    result = 0
    for i in number:
        result+=i
    return result/len(number)
        
is_even(2,4)

is_even(2,4,6,8)

is_even(3,6,9)

###정답이지만 def문에는 print보다는 return을 사용

##Q3
imput1 = input("첫번째 숫자를 입력하세요 : ")
imput2 = input("두번째 숫자를 입력하세요 : ")

total = int(imput1)+int(imput2)
print(total)
###정답

##Q4
#3번, 나머지는 띄어쓰기가 없음
###정답

##Q5
f1 = open("test.txt", 'w')
f1.write("life is too short")
f1.close

f2 = open("test.txt", 'r')
readline = f2.readlines()
print(readline)
f2.close

f2 = open("test.txt", 'r')
readline = f2.readlines()
print(f2.read())
f2.close

###close를 까먹지말기

with open("test.txt", 'w') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r') as f2:
    print(f2.read())

###read 뒤에는()

##Q6
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close

###정답

f2 = open("test.txt", 'r')
readline = f2.readlines()
for i in readline:
    print(i)
f2.close

with open("test.txt", 'r') as f2:
    readline = f2.readlines()
    for i in readline:
        print(i)

##Q7

###readlines()를 통해 list로 불러온 후 항목을 수정
# 파일을 읽기 모드로 열고 모든 줄을 읽어옴
f = open("test.txt", 'r')
body = f.readlines()
f.close()
print(body)
# 두 번째 줄을 변경함
body[1] = "you need python\n"
# 파일을 쓰기 모드로 다시 열고 변경된 내용을 기록함
f = open("test.txt", 'w')
f.writelines(body)
f.close()

###read를 통해 str 문자열로 불러온 후 수정하기 replace사용
# 파일을 읽기 모드로 열고 모든 내용을 읽어옴
with open("test.txt", 'r') as f:
    content = f.read()
# 변경할 문자열을 포함하는 문자열 생성
new_content = content.replace("a", "you need python")
print(new_content)
# 파일을 쓰기 모드로 열고 변경된 내용을 기록함
with open("test.txt", 'w') as f:
    f.write(new_content)



