a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b        # 12 = 0000 1100
print ("1 - c 的值为：", c)
 
c = a | b        # 61 = 0011 1101 
print ("2 - c 的值为：", c)
 
c = a ^ b        # 49 = 0011 0001
print ("3 - c 的值为：", c)
 
c = ~a           # -61 = 1100 0011
print ("4 - c 的值为：", c)
 
c = a << 2       # 240 = 1111 0000
print ("5 - c 的值为：", c)
 
c = a >> 2       # 15 = 0000 1111
print ("6 - c 的值为：", c)
var1='Hello World'
print(var1[1:8:2])
var2='Hello World'
print("已更新字符串:",var2[:6]+"yang")
print("yang \
AAA杨少爷\
wine")
print("\\")
print('\'')
print("Hello \b World")
print("Hello \v World")
print("Hello \t World")
print("Hello \n World")
print("Hello \f world")
print('Hello\rworld')
print('yang peijin\r杨佩锦')
print("\110\145\154\154\157\40\127\157\162\154\144\41")
import time

for i in range(101):
    print("\r{:3}%".format(i),end=' ')
a="yang"
b="qian"
print(a[1:4])
if ("H" in a ):
    print ("H 在变量 a 中")
else:print("H 不在变量 a 中")
print(r'\n')
print ("我叫 %s 今年 %d 岁!" % ('杨佩锦', 18))
AAA="""一周都是满课谁懂
终于周五了发现忘了python
学习学习！！！！(\t)
[aaa\n   bbb]"""
print(AAA)
print(f'{AAA}')
list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)
A=['yang','pei','jin']
print(A[2])
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
[['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
['a', 'b', 'c']
print(x[0][1])
a=dict()
print(a)
print(type(a))
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 1209            
tinydict['School'] = "CDUT"  
 
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 
True
'crabgrass' in basket
False
a = set('abracadabra')
b = set('alacazam')
print(a)                                  
{'a', 'r', 'b', 'c', 'd'}
print(a - b)                             
{'r', 'd', 'b'}
print(a | b)                              
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              
{'a', 'c'}
print(a ^ b)                              
{'r', 'd', 'b', 'm', 'z', 'l'}
num=int(input("5："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
    
number = -1
guess = 10
if guess == number:
    print("恭喜，你猜对了！")
elif guess < number:
    print("猜的数字小了...")
elif guess > number:
    print("猜的数字大了...")
# !/usr/bin/python3
 
num=int(input("输入一个数字：10"))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
{'d', 'r'}
print (type(a))
list=[1,2,3,4]
it = iter(list)    
print (next(it))   
print (next(it))
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        
        result = original_function(*args, **kwargs)
    
        
        return result
    return wrapper

# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现
#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support # type: ignore
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

