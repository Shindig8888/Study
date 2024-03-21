##Q1

#shirt need
###오답. 가장 먼저 참인것만 출력됨!!!!

##Q2

result = 0
i = 0


while i <=1000:
    i=i+1
    if i % 3 == 0:
        result=result+i
    else:
        continue
    if i==1001:
        break

print(result)
###정답!!!


##Q3

i = 0
while i<=4:
    i+=1
    print("%s" %("*"*i))
    if i == 5:
        break
###정답!!!
    
##Q4
    
for i in range(1,101):
    print(i)
###정답!!!
    

##Q5
a = [70,60,55,75,95,90,80, 80, 85,100]
total = 0

for score in a:
    total += score

average = total/len(a)
print(average)

###정답!!!


##Q6

numbers = [1,2,3,4,5]
result = []

result = [n*2 for n in numbers if n % 2 == 1]

print(result)

###기억이 안나서 보면서 풀었음. [목표식(변수나중에정의) for 변수 in 리스트 if~]