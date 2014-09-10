# -*- coding:utf-8 -*-
# Python Cook Book
# 章节一 文本
# 所有经典代码示例
# 部分代码将经过优化后在这里放出
# pycookbook所有示例代码均经过调试
# 项目地址:https://github.com/qddegtya/pycookbook

ONESTRING="abcdefghijklmn"
MULTILINE="one line\n" \
          "two line"
print ONESTRING[:-2:2]
print ONESTRING.isdigit()
print ONESTRING.count("a")
print MULTILINE.splitlines()
print "\n".join(MULTILINE.splitlines())
print list(ONESTRING)
print ONESTRING*3

# 1.1 每次处理一个字符
for everystr in list(ONESTRING):
    print everystr

for everystr in ONESTRING:
    print everystr

results=[str.upper(everystr) for everystr in ONESTRING]
mapresults=map(str.upper,ONESTRING)
print results
print mapresults

# 1.2 字符和字符值之间的转换
print ord('a')
print chr(97)
print ord(u'\u2020')
print repr(unichr(8224))
print map(ord,'ciao')
print ''.join(map(chr,range(97,100)))

#测试一个对象是否是类字符串
def is_string(anobj):
    """str和unicode类型的共同基类为basestring"""
    return isinstance(anobj,basestring)

def is_string_like(anobj):
    """鸭子判断法,通过各种行为组合判断"""
    try:
        anobj+''
    except:
        return False
    else:
        return True

print repr(is_string('fdafda'))
print repr(is_string_like('fdaaffdasfdas'))

# 1.4 字符串对齐
print 'a'.center(20,'*')

# 1.5 去除字符串两端的空格
x='xy y z '
print x.strip('xy')
print x.lstrip()
print x.rstrip()

# 1.6 合并字符串
# 通常使用%来完成这个拼接，有很多潜在的好处
# join采用的是将碎片字符一口吞下
# 很多性能低下的python程序都是使用了+或者+=来拼接字符
# 推荐采用中间数据结构容纳临时结果，最后直接join
# 这里还特意提到了提高python程序性能的psyco(JIT编译器)
import operator
largeString=reduce(operator.add,['a','b','c'],u'我是最开始的值')
print largeString

# 1.7 将字符串逐字符或逐词反转
revchars='abc'[::-1] #直接使用步长为-1的特别切片方式
print revchars
