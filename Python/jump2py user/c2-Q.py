
##Q1
(80+75+55)/3
###정답!!!

##Q2
if 13%2:
    print("홀수")
else:
    print("짝수")
###정답!!!

##Q3
a = "881120-1068234"
yyyymmdd = "19"+a[:6]
print(yyyymmdd)
print(a[7:])
###정답!!!

##Q4
pin = "881120-1068234"
print(pin[7])
###정답!!!

##Q5
a = "a:b:c:d"
a.replace(":","#")
###정답!!!

##Q6
a = [1,3,5,4,2]
a.sort()
a
a.reverse()
a
###정답!!!

##Q7
a = ["Life", "is", 'too', 'short']
result = a[0]+a[1]+a[2]+a[3]
result = " ".join(a)
print(result)
###정답!!!


##Q8
a = (1,2,3)
b = (4,)
a = a+b
print(a)
###정답!!!

##Q9

a=dict()
a
#a[[1]] = 'python', 리스트는 키로 지정할 수 없음
###정답!!!

##Q10

a = {'A':90, 'B':80, 'c':70}
result = a.pop('B')

print(a)
print(result)
###정답!!!

##Q11

a = [1,1,1,2,2,3,3,3,4,4,5]

aSet = set(a)

b = list(aSet)

print(b)
###정답!!!

##Q12

a=b=[1,2,3]
a[1] = 4
#a와 b모두 변할거같음, a와 b를 동일하게 설정했기때문에, 혹시 모르니 아이디를 확인:
id(a)
id(b)
#id가 동일하므로 a가 변하면 b도 같이 변함

print(b)
###정답!!!

