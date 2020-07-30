import re
# \d    匹配一个数字
# \w   匹配一个字母或数字
# \s    匹配一个空格
# .      匹配任意字符
# *  任意个字符
# +  至少一个字符
# ？ 0个或一个字符
# {n} n个字符
# {n-m}  n-m个字符
#
#
# [] 表示范围
# [0-9a-zA-Z\-]   匹配一个数字，字母或者下划线
# ^ 表示开头
# $ 表示结束
# if re.match(r'^\d{4}$','055211'):
#     print("yes")
# else:
#     print("no")
#
# a = re.split(r'[\s\.]+','a..a')
# print(a)

# group
res = re.match(r'^(\d{3,4})-(\d{3,8})$','0574-1122345')

# group(0)  整个原始字符串
# group(n)  第n个子字符串

print(res.group(1))

