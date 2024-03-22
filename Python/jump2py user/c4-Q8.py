import sys

args = sys.argv[1:]

result = 0
for i in list(map(int, args)):
    result += i

print(result)

###map 함수를 이용해도되고 int(i)와 같은 방식으로 계산해도 됨