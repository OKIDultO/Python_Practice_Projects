'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：(a>b)?a:b这是条件运算符的基本例子。
'''

x = int(input("请输入成绩:"))

print("A" if x>=90 else ("B" if x>=60 else "C"))
