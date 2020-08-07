# a = [1,2,3,4,5,6,7,8]
# b  = [i**2 for i in a if i>=5] #列表推导式
# print(b)
#
# students = {
#     '喜小乐':18,
#     '石敢当':20,
#     '横小无':22
# }
# b = {key:value for key,value in students.items()}
# print(b)
#
# f =lambda x,n: x+n
# print(f(1,2))
# dict1 = { 'a': 1, 'b': 2 }
# dict2 = { 'b': 3, 'c': 4 }
# merged ={**dict1,**dict2}
# print(merged)
# mystring = "10 awesome python tricks"
# print(mystring.title())
# mys = "yuan-jun-ling"
# myss = mys.split('-')
# print(myss)
import random


# print(
    # random.choice(['139', '188', '185', '136', '158', '151']) + "".join(random.choice("0123456789") for i in range(8)))
print(random.choice(['135','136','138','158','151'])+"".join(random.choice("123456789") for i in range(8)))

mylist = ['The', 'quick', 'brown', 'fox']
mystring ="+".join(mylist)
print(mystring)

bbbc=map(lambda s:s.upper(),["aaaa","ccc"])#匿名函数
print(list(bbbc))
y=2
x = "Success!" if (y == 2) else "Failed!"#三元表达式
print(x)

if(n:=11)>10:
    print(f"List is too long ({n} elements, expected <= 10)")