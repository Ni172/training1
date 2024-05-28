# def fibinachi(n):
#     a = 0
#     b = 1
#     list_fib = []
#     if n < 0:
#         return "Incorrect input"
#     if n == 0:
#         list_fib.append(a)
#         return list_fib
#     if n == 1:
#         list_fib.append(b)
#         return list_fib
#     for i in range(n):
#         list_fib.append(a)
#         c = a + b
#         a = b
#         b = c
#     return list_fib
#
#
# print(fibinachi(5))

# def fib(n):
#     a, b = 0, 1
#     if n < 0:
#         yield "Incorrect input"
#     if n == 0:
#         yield 0
#     if n == 1:
#         yield b
#     else:
#         for _ in range(n):
#             yield a
#             a, b = b, a + b
#
#
# print(list(fib()))

############################################


# def isprime(a):
#     msg = 'isprime'
#     for i in range(2,a):
#         if a%i == 0:
#             print(f"{a} devide to {i}")
#             msg= 'not isprime'
#     return msg
#
# print(isprime(1))

# def isprime(a):
#     if a >= 0:
#         return all([False if a % i == 0 else True for i in range(2, (int(a / 2) + 1))])
#     else:
#         return False
#
#
# print(isprime(1))

####################################################

# def is_polindrom(*n):
#     if n == n[::-1]:
#         return True
#     else:
#         return False
#
# print(is_polindrom('1113'))

# def is_polindrom(n):
#     for i in range(int(len(n) / 2)):
#         if n[i] != n[len(n) - i - 1]:
#             return False
#     return True
#
#
# print(is_polindrom('127721'))

# def is_polindrom(n):
#     i = 0
#     k = len(n) - 1
#     while i < k:
#         if n[i] != n[k]:
#             return False
#         i += 1
#         k -= 1
#     return True
# print(is_polindrom('1231'))
#########################################
# from itertools import groupby
#
# def remove_duplicate_char(n):
#     # return ''.join([ch for ch, group in groupby(n)])
#     list_with_single_char = []
#     for ch, group in groupby(n):
#         if ch not in list_with_single_char:
#             list_with_single_char.append(ch)
#     return list_with_single_char
#
#
# print(remove_duplicate_char('hhjj2    hh kjk'))

#####################################

# n = [1, 2, 0,3, 6,0]
# count = 0
# list_of_count = []
# prev_digith = n[0]
# start_scope = None
# stop_scope = None
# for i in range(1, len(n)):
#     if prev_digith==0 and n[i]!=0:
#         start_scope = True
#     if n[i] != 0 and start_scope:
#         count+=1
#         scope = True
#     if n[i] == 0 and start_scope:
#         stop_scope = True
#     if stop_scope:
#         list_of_count.append(count)
#         count=0
#         start_scope = False
#         stop_scope = False
#     prev_digith = n[i]
# try:
#     print(max(list_of_count))
# except:
#     print(0)

#
# n=[1,2,0,1,2,3,6,0]
# sum_val = 0
# result = []
# for i in n:
#     if i != 0:
#         sum_val+=i
#     else:
#         result.append(sum_val)
#         sum_val=0
# print(result)

###################################################
# l = [[1,3,2],[7,0,8]]
# print(list(map(sorted,l)))


# s = '{[]}'
# l =[]
# open = '{[('
# close = '}])'
# a='{}'
# b='[]'
# c='()'
# for i in s:
#     if i in open:
#         l.append(i)
#     if i in close:
#         if ''.join(l[-1:])+i ==a or ''.join(l[-1:])+i ==b or ''.join(l[-1:])+i ==c :
#             try:
#                 l.pop()
#             except:
#                 l=['']
#         else:
#             l = ['']
#             break
# if l == []:
#     print('ok')
# else:
#     print('not ok')

#################################

# n = 4
# s = str(bin(n))
# print(s)
# max_len = 0
# for i in s.split('1')[1:]:
#     if max_len < len(i):
#         max_len = len(i)
# print(max_len)

# n = [5, 4, 6, 8, 9, 1]
# print([max(n[i:i+3]) for i in range(len(n)-3+1)])


###########################################

# def index_greater_then_value(l,val):
#     return [index for index,i in enumerate (l) if i>val]
#
# l = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
# val = 3000
# print(index_greater_then_value(l,val))

###################################################

# def remove_string_from_tuple(l):
#     new_list = []
#     for i in l:
#         list_temp = []
#         for y in i:
#             if not isinstance(y, str):
#                 list_temp.append(y)
#         new_list.append(tuple(list_temp))
#     return new_list
# #     return [tuple(y for y in i if not isinstance(y, str)) for i in l]
# l= [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# print(remove_string_from_tuple(l))

#############################################

# def sort_list_of_tuple_per_index(l,index):
#     return sorted(l,key = lambda x:x[index])
#
# l = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# print(sort_list_of_tuple_per_index(l,0))

############################################

# def insert_val_per_index(l, index, val):
#     n = index
#     while n < len(l):
#         l.insert(n, val)
#         n += index
#     return l
#
#
# l = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# index = 1
# val = 20
# print(insert_val_per_index(l, index, val))

#########################
# def solution(n:list[int]):
#     n1 = []
#     for i in range(len(n)):
#         for j in range(i, len(n)):
#             if n[i] + n[j] == 7:
#                 n1.append((n[i], n[j]))
#     return n1
#
# l=[6, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(solution(l))


##########################

# l = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# d = {}
# for i in l:
#     d[i[0]]=i[1:]
# print(d)

#############################
from collections import defaultdict


# def test(*dicts):
#     result = defaultdict(list)
#     for el in dicts:
#         for key in el:
#             result[key].append(el[key])
#     return dict(result)
#
# def test(d1, d2):
#     d = {}
#     for k ,v in d1.items():
#         d[k] = [v]
#     for k ,v in d2.items():
#         d[k].append(v)
#     return d
# d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# d2 = {'x': 300, 'y': 'Red', 'z': 600}
# print(test(d1, d2))

################################
# from  collections import defaultdict
# l=[7, 23, 3.2, 3.3, 8.4]
# d=defaultdict(list)
# for el in l:
#     d[str(el)[0]].append(el)
# print(dict(d))

########################
# rows = 5
# for i in range(1,rows+1):
#     for j in range(rows+1,0,-1):
#         if i<j:
#             print('*',end=' ')
#         else:
#             print('',end=' ')
#     print('\n')
#
#
# for i in range(rows+1,1,-1):
#     for j in range(1,i):
#         print('*',end=' ')
#     print('\n')

##################################

# def decorator1(h):
#     def inner():
#         print('aa')
#     return inner
#
# @decorator1
# def my_function(a,b):
#     pass
#
# my_function()


# def smart_list(func):
#     def inner(l,a):
#
#         if not isinstance(kwargs,list):
#             print("this not list")
#             return
#         return kwargs
#     return inner
#
# @smart_list
# def function1(l):
#     print(l)
#
#
#
# function1({'1':''})

# x=1
# class Nikolai:
#     @property
#     def niko(self):
#         return x
#
#     @niko.setter
#     def niko(self,b):
#         global x
#         x=b
#
# a=Nikolai()
# # a.niko='hello'
# print(a.niko)

# n=4
# l=[]
# count = 0
# for i in range(n):
#     l.append([])
#     for j in range(n):
#             l[i].append(count)
#             count+=1
# print(l)
# # print(sum([l[len(l)-i-1][len(l)-i-1] for i in range(len(l))]))
# l=[l[i][::-1] if i%2!=0 else l[i] for i in range(n)]
# print(l)
# for i in l:
#     print(''.join(str(j) + ' ' for j in i))


# def solution(A):
#     l = []
#     for i in A:
#         l.append(i)
#         if i+1 in l or i-1 in l:
#             return True
#     return False
#
# A=[20,6,7,8,10,25]
# print(solution(A))


# from collections import Counter
# s = ['a','a','b','c','c','c','c']
# d = Counter(s)
# if len(s)<2:
#     print(''.join(s))
#
# d = sorted(d.items(),key=lambda x:x[1],reverse=True)
# for i in range(len(d)-1):
#     if d[i][1] > d[i+1][1]:
#         print(d[i+1][0])
#         break


# def miss_two_digits(arr: list):
#     if len(arr) == 0:
#         return 1, 2
#     arr_sort = sorted(arr)
#     if arr_sort[0] == 1:
#         return 2, 3
#     if arr_sort[0] == 2:
#         return 1, 3
#     if arr_sort[0] == 3:
#         return 1, 2
#     prev_element = arr_sort[0]
#     dig1 = None
#     dig2 = None
#
#     for i in range(1, len(arr_sort)):
#         if arr_sort[i] != prev_element + 1:
#             dig1 = prev_element + 1
#             sum_all = int(((len(arr_sort) + 2) * (len(arr_sort) + 3)) / 2)
#             dig2 = sum_all - sum(arr_sort) - dig1
#             return dig1, dig2
#         prev_element = arr_sort[i]
#
# print(miss_two_digits([2, 4]))

# def x(s1,s2):
#     return sorted(s1) == sorted(s2)
#
# print(x('aab','baaa'))



# def maxArea(height: list[int]) -> int:
#     max_area = 0
#     l = []
#     for index, value in enumerate(height, start=1):
#         l.append([index, value])
#
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             area = min(l[i][1], l[j][1]) * (l[j][0] - l[i][0])
#             max_area = max(max_area, area)
#     return max_area
#
#
# height = [1,8,6,2,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(maxArea(height))


