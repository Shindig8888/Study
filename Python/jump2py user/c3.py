###제어문

money = True
if money:
    print("택시를 타고간다")
else:
    print("걸어간다")



#비교
money = 2000

if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#==:같음 !=:같지않음


#or
money = 2000
card = True

if money>3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


#in (리스트,튜플,문자열)
    
1 in [1,2,3]
1 not in [1,2,3]

a = ['a','b','c']
'a' in ['a','b','c']
'j' not in a

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#elif
    
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고가라')
else:
    if card:
        print('택시를 타고가라')
    else:
        print('걸어가라')
    

if 'money' in pocket:
    print('택시를 타고가라')
elif card:
    print('택시를 타고가라')
else:
    print('걸어가라')    

#조건부 표현식
    
if score >=60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"


##While 문

treehit = 0
while treehit < 10:
    treehit=treehit+1
    print("나무를 %d번 찍었습니다" %treehit)
    if treehit == 10:
        print('나무 넘어집니다')

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number: """

number = 0

while number !=4:
    print(prompt)
    number = int(input())


#break
    
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee-1
    print("남은 커피의 양은 %d입니다" %coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break


coffee = 10

while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee-1
    elif money>300:
        print("거스름돈 %d원을 주고 커피를 줍니다" % (money-300))
        coffee = coffee-1
    else : 
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d잔입니다." % coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break


#while continue

a = 0
while a<10:
    a = a+1
    if a % 2 ==0: continue
    print(a)


#무한루프
    
while True:
    print("Ctrl+C를 눌러야 While문을 빠져나갈 수 있습니다")





## for 문
    
test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

marks = [90,25,67,45,80]
number = 0
for i in marks:
    number = number+1
    if i >= 60:
        print("%d번 학생은 합격입니다 축하드립니다" % number)
    else:
        print("%d번 학생은 불합격입니다 화이팅" % number)


marks = {"김철수":90, "김영희":25, "단형우":67, "최인용":45, "김치환":80}

for {name, mark} in marks.items():
    if mark >= 60:
        print("%s 학생은 합격입니다 축하드립니다" %name)
    else:
        print("%s 학생은 불합격입니다 다시도전하세요" %name)


marks = {"김철수":90, "김영희":25, "단형우":67, "최인용":45, "김치환":80}

for name, mark in marks.items():
    if mark >= 60:
        print("%s 학생은 합격입니다 축하드립니다" %name)
    else:
        print("%s 학생은 불합격입니다 다시도전하세요" %name)


# 딕셔너리를 사용할 때는 for 변수1, 변수2 in 딕셔너리.items(): 로 조건을 설정
        

# for continue
marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number = number+1
    if mark < 60: continue
    else:
        print("%d번 학생은 합격입니다 축하드립니다" %number)

#range
        
a = range(10)
a

add = 0
for i in range(1,11):
    add = add+i

add

marks = [90,25,67,45,80]
for number in range(len(marks)): #아까는 순서대로 짚으면서 넘버를 매겨야했는데
    if marks[number] <60:#지금은 number 로 key를 만들면서 marks리스트 안의 번호로 점수를 확인
        continue
    print("%d번 학생 합격입니다 축하드립니다" %(number+1))


for i in range(2,10):
    for j in range(1,10):
        print("%d  %d은 %d" %(i,j,i*j))
    print('')
    

#리스트 컴프리헨션
    
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

a = [1,2,3,4]
result = [num*3 for num in a if num %2==0]
print(result)


result = []

for num in a:
    if num % 2:
        result.append(num)
    else:
        result.append(num*3)

print(result)

result = [x*y for x in range(2,10)
        for y in range(1,10)]
print(result)