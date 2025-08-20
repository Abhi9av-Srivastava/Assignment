>>> def fun(n):
...     print(n)
...     if n>4:
...         return
...     fun(n+1)
...
>>> fun(1)
1
2
3
4
5