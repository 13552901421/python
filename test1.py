#coding=utf-8
import os
from os import path

'''
多行注释/字符串
'''

#数据类型5种
string_path = 'D:\\test1'
num = 3.1415926
list = [1,'test',3.14,3 + 2j]
tuple = (1,'tuple_test',list,3.14)
dict = {1:'test','er':'erer'}
print(type(dict))

#逻辑控制、运算符
if list is not None:
    for index,item in enumerate(list):
        print(item)
    while index >= 0:
        # if index == 2:
            # break
        print(index)
        index -= 1
    print(index)
elif len(list) > 2:
    pass
else:
    pass
# print(index)#index有效范围？？

if path.exists(string_path) == False:
    os.mkdir(string_path)

#函数
def sum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

# print(type(num))
print(sum(1,2,3.14,5,6))

lsum = lambda x,y: x * y

# print(lsum(3,2))

#类
class myUtil:
    PI = 3.14
    # def __init__(self,r):
    #     self.r = r
    def ceril(self,r):
        c = self.PI * r**2
        # return c
        print(c)
    if __name__ == '__main__':
        print('i am myUtil~')
    # print('i am myUtil~')
util = myUtil()
print(util.PI)
# util.ceril(2)

#异常处理
assert 3.14 in list

# open('a.txt','w+')
try:
    open('D:\a.txt','w+')
except Exception as e:
    print("Error:can't open a.txt")
    print(e.args)
    # raise
# else:
#     print('---else---')
finally:
    print('---finally---')

print('try_except_test@@@')

# with open('a.txt','r') as file:
#     file.readline()


