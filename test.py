#max(set(), key)

a=[1,2,3,1,1,1,2,4,]
count=max(set(a), key=a.count)

print(count)

#list그대로 사용해도 답은 나오지만 8개 element에 대해 전부 검색을 실시하기 때문에 리소스낭비