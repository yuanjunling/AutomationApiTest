a = [1,2,3,4,5,6,7,8]
b  = [i**2 for i in a if i>=5] #列表推导式
print(b)

students = {
    '喜小乐':18,
    '石敢当':20,
    '横小无':22
}
b = {key:value for key,value in students.items()}
print(b)