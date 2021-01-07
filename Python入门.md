# Python基础知识
# 1.下载python
#### [官网地址](www.python.org)(勾选path)
#### 使用vscode,pycham略

# 2.语法总结
## 1.标识符
1. 在 Python 里，标识符由字母、数字、下划线组成,但不能以数字开头。

2. 在 Python 里，的标识符是区分大小写的。

3. 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import 而导入

4. 以双下划线开头的 foo 代表类的私有成员

5. 以双下划线开头和结尾的 foo 代表 Python 里特殊方法专用的标识，如 init__() 代表类的构造函数。

## 2.数据类型
1. 五种数据类型  
Numbers（数字）  
String（字符串）  
List（列表）  
Tuple（元组）  
Dictionary（字典）  

2. Python支持四种不同的数字类型：

    int（有符号整型）  
    long（长整型[也可以代表八进制和十六进制]）  
    float（浮点型）  
    complex（复数）  
    python的字串列表有2种取值顺序:  

    从左到右索引默认0开始的，最大范围是字符串长度少1  
    从右到左索引默认-1开始的，最大范围是字符串开头  
    List（列表） 是 Python 中使用最频繁的数据类型。  

    列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。  
    列表用 [ ] 标识，是 python 最通用的复合数据类型。  
    列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列  表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可  以为空表示取到头或尾。  
    加号 + 是列表连接运算符，星号 * 是重复操作。  
    
    元组是另一个数据类型，类似于List（列表）。  
    元组用”()”标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于  只读列表。  
    字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。  

    列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字  典当中的元素是通过键来存取的，而不是通过偏移存取。  
    字典用”{ }”标识。字典由索引(key)和它对应的值value组成。

## 3. 数据类型转换  

    int(x [,base]):将x 转换为一个整数  
    long(x [,base] ):将x转换为一个长整数  
    float(x):将x转换到一个浮点数  
    complex(real [,imag]):创建一个复数  
    str(x):将对象 x 转换为字符串  
    repr(x)将对象 x 转换为表达式字符串  
    eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象  
    tuple(s)将序列 s 转换为一个元组  
    list(s)将序列 s 转换为一个列表  
    set(s)转换为可变集合  
    dict(d)创建一个字典。d 必须是一个序列 (key,value)元组
    frozenset(s)转换为不可变集合  
    chr(x)将一个整数转换为一个字符  
    unichr(x)将一个整数转换为Unicode字符  
    ord(x)将一个字符转换为它的整数值  
    hex(x)将一个整数转换为一个十六进制字符串  
    oct(x)将一个整数转换为一个八进制字符串    

## 4.运算符
1. 算术运算符  
加 - 两个对象相加 a + b 输出结果 30  
减 - 得到负数或是一个数减去另一个数 a - b 输出结果 -10  
乘 - 两个数相乘或是返回一个被重复若干次的字符a * b 输出 结果 200  
/ 除 - x除以y b / a 输出结果 2  
% 取模 - 返回除法的余数 b % a 输出结果 0  
幂 - 返回x的y次幂 ab 为10的20次方， 输出结果 100000000000000000000  
// 取整除 - 返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0  

2. 赋值运算符   
没什么特别的  

3. 位运算符  
没什么特别的,依然是
按位与& 按位或| 按位异或^ 按位取反~ 左移右移<<>>

4. 逻辑运算符  
没什么特别的

5. 成员运算符 in  
in 如果在指定的序列中找到值返回 True，否则返回 False。 x 在 y 序列中 , 如果 x 在 y 序列中返回 True。   
not in 如果在指定的序列中没有找到值返回 True，否则返回 False。 x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

6. 身份运算符 is is  
is is 是判断两个标识符是不是引用自一个对象 x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False  
is not is not 是判断两个标识符是不是引用自不同对象 x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False  

## 5.字符串

1. 字符串一般使用''或者"",''' '''则用来长文字
2. 字符串可以通过string[x] 的方式进行索引、分片,代码示例:
    ```
    name = 'My name is Mike'
    print(name[0])
    'M'
    print(name[-5])
    's'
    print(name[11:14]) # from 11th to 14th, 14th one is excluded
    'Mik'
    print(name[11:15]) # from 11th to 15th, 15th one is excluded
    'Mike'
    print(name[5:]) # from 5 to end
    'me is Mike'
    print(name[:5])
    'My na'
    ```
3. 字符串的方法
* replace 方法：第一个参数表示被替代部分，第二个参数表示替代成怎样的字符串。
  
* 字符串填空，如：
    ```
    city = input("write the name of city:"")
    url = "http://apistore.baidu.com/mri.../weather?citypiny={}.format(city)
    ```
4. python中str和int不能直接计算

## 6.函数
1.使用函数  
举些你可能已经使用过的函数例子:
```
    判断数据类型：type(str) 
    字符串类型数据转为整数型：int(str)
```
Python 中所谓的使用函数就是把你要处理的对象放到一个名字后面的括号就可以了,上述函数是python的`内建函数`

2.函数参数

3.匿名函数  
Python 使用 lambda 来创建匿名函数  
基本语法：lambda [arg1 [,arg2,.....argn]]:expression  
示例：
```
sum = lambda num1 , num2 : num1 + num2;
print( sum( 1 , 2 ) )
```
匿名函数中，有一个特别需要`注意的问题`，比如，把上面的例子改一下：
```
num2 = 100
sum1 = lambda num1 : num1 + num2 ;

num2 = 10000
sum2 = lambda num1 : num1 + num2 ;

print( sum1( 1 ) )
print( sum2( 1 ) )

你会认为输出什么呢？第一个输出是 101，第二个是 10001，结果不是的，输出的结果是这样：

10001
10001

这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的

```

## 7.循环与判断
1. 布尔  
没什么特别的

2. for循环
打印九九乘法表：
```
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()
```
3. while循环
在 Python 的 while 循环中，可以使用 else 语句：
```
    count = 0
    while count < 3:
    print (count)
    count = count + 1
    else:
    print (count)

```
另外for循环也可以使用else,执行完for后执行

## 8.数据结构
Python 有四种数据结构，分别是：列表、字典、元组、集合。我们先从整体上认识一下这四种数据结构：
```
list = [val1,val2,val3,val4] #列表
dict = {key1:val1,key2:val2} #字典
tuple = (val1,val2,val3,val4) #元组
set = {val1,val2,val3,val4} #集合
```

1. 列表  
   
列表中的每个元素都是可变的；

列表中的元素是有序的，也就是说每个元素都有一个位置；

列表中可以容纳 Python 中的任何对象。如下：
```
all_in_list = [
   1, #整数
   1.0, #浮点数
   'a word', #字符串
   print(1), #函数
   True, #布尔值
   [1,2], #列表中套列表
   (1,2), #元祖
   {'key':'value'} #字典
]
增删改查:以后写
```
2. 字典  
   
字典中数据必须是以键值对的形式出现的；

逻辑上讲，键是不能重复的；

字典中的键（key）是不可变的，也就是无法修改的，而值（value）是可变的，可修改的，可以是任何对象。

下面是个例子：

NASDAQ_code = {
   'BIDU':'Baidu',
   'SINA':'Sina',
   'YOKU':'Youku'
}

3. 元组

元组可以理解为一个稳固版的列表，因为元组是不可以修改的，因此在列表中的存在的方法均不可以使用在元组上，但是元组是可以被查看索引的，方式和列表一样。

letters = ('a, 'b', 'c', 'd')
letters[0]

4. 集合  

则更接近数学上集合的概念。每一个集合中是的元素是无序的、不重复的任意对象，我们可以通过集合去判断数据的从属关系，有时还可以通过集合把数据结构中重复的元素减掉。

集合不能被切片也不能被索引，除了做集合运算之外，集合元素可以被添加还有删除：

a_set = {1,2,3,4}
a_set.add(5)
a_set.discard(5)

5. 技巧
多重循环

代码演示：

for a, b in zip(num, str):
    print(b, 'is', a)

4.5.2 推导式
代码演示：

a = []
for i in range(1, 11):
    a.append(i)

可以换成列表解析的方式来写：

b = [i for in i range(1, 11)]
列表解析式不仅方便，并且在执行效率上要远远胜过前者。

## 9.类
1. 类方法：
```
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print('Energy!')

coke = CocaCola()
coke.drink()
```
2. self 
self仅仅代表被实例化的对象,可以改名字

3. 魔术方法:构造函数_init
```
   def __init__(self,logo_name):
        self.local_logo = logo_name
```

4. 类的继承  

如下代码：
```
class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]
coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()
```
表示 CaffeineFree 继承了 CocaCola 类。

类中的变量和方法可以被子类继承，但如需有特殊的改动也可以进行`覆盖`
(修改类的值将会影响对象的值,反之则没有影响)

## 10.使用第三方库
1. 安装自己的库
* 找到你的 Python 安装目录，找到下面的 site-packages 文件夹
* 将你写的 py 文件放进去

2. 安装第三方库
* 使用pip安装库
* 在cmd里查看pip:pip --version
* 下载对应的几个wheel文件(https://blog.csdn.net/qq_44880255/article/details/106305419)
* 只需要在命令行里面输入：pip3 install PackageName






















参考:https://blog.csdn.net/u012195214/article/details/79243055