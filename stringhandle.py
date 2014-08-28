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