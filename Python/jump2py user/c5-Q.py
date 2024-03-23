##Q1##
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCaculator(Calculator):
    def minus(self, mval):
        self.value -= mval

cal = UpgradeCaculator()
cal.value
cal.add(10)
cal.minus(7)

print(cal.value)
##정답##

##Q2##

class Calulator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >=100:
            self.value = 100
      


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
##정답##  


##Q4##
a = list(filter(lambda x : x>0, [1,-2,3,-5,8,-3]))
print(a)

##Q4##
int('0xea', 16)

##Q5##
a = list(map(lambda x : x*3, [1,2,3,4]))
print(a)

##Q7##
max_value = max([-8,2,7,5,-3,5,0,-1])
min_value = min([-8,2,7,5,-3,5,0,-1])
max_value+min_value


##Q8##
round_value = round(17/3, 4)
print(round_value)

##Q9##

import os
os.chdir("C:\\Users\\claix\\OneDrive\\Desktop\\Coddimg\\Study")
result = os.popen("dir")

##Q10##
import glob
glob.glob('*.py')

##11##
import time
time.strftime("%Y/%m/%d  %H:%M:%S")

##Q12##
import random
result = []
while len(result)<6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)

###오답###


##Q13##
import datetime

a = datetime.date(1995,11,20)
b = datetime.date(1998, 10, 6)
diff = a-b
abs(diff)

data = [('윤 서 현', 15.25),
            ('김 예 지', 13.31),
            ('송 순 자', 15.57),
            ('박 예 원', 15.34),
            ('김 시 우', 15.48),
            ('배 숙 자', 17.9),
            ('전 정 웅', 13.39),
            ('김 혜 진', 16.63),
            ('최 보 람', 17.14),
            ('한 지 영', 14.83),
            ('이 성 호', 17.7),
            ('김 옥 순', 16.71),
            ('황 민 지', 17.65),
            ('김 영 철', 16.7),
            ('주 병 철', 15.67),
            ('박 상 현', 14.16),
            ('김 영 순', 14.81),
            ('오 지 아', 15.13),
            ('윤 지 은', 16.93),
            ('문 재 호', 16.39)]

import operator
a = sorted(data, key=operator.itemgetter(1))
for d in a: 
    print(d)


##Q15##
import itertools
cleaner = ['나지혜', '성성민', '윤지현', '김정숙']
a = list(itertools.combinations(cleaner, 2))
print(a)

##Q16##
inport itertools
alpha = ['a','b','c','d']
a = itertools.permutations(alpha, 4)
print(list(a))

##Q17##
people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
chore = ['청소', '빨래', '설거지']
import random
a = random.sample(people, len(people))
b = random.sample(chore, len(chore))

import itertools
result = list(itertools.zip_longest(a, b, fillvalue="휴식"))
print(result)

##Q18##
import math


length = math.gcd(200,80)
tiles_need = int(200/length*80/length)
print(length)
print(tiles_need)