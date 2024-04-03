# import re
# data = """
# park 800905-1049118
# kim 700905-1059119
# """
# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))

# #MULTILINE, M
# #--검색할문자열에서 ^python이면 문자열이 반드시 python으로 시작, python$이면 문자열이 반드시 python으로 끝

import re
p = re.compile('^python\s\w+', re.MULTILINE)
data = '''python one
life is too short
python two
you need python
python three
'''
print(p.findall(data))