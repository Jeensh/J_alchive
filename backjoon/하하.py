from bisect import bisect_left, bisect_right



a = [1,2 ,4,4,8]
a.sort()
print(a)
print(bisect_left(a, 4))
print(bisect_right(a, 4))