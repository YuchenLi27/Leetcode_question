a = 2
b = 2
c = 3

print(id(a))
print(id(b))
print(id(c))
print("helo")
a = 4
a = b
a = 5
print(a)
print(id(a))
print(b)
print(id(b))

print("word")
x = "xuan"
print(id(x))
x = "xaan"
print(id(x))
print(x[1])
# x[1] = "t"

print('mutable')
x = [1,2,3]
print(id(x))
print(id(x[1]))
x[1] = 3
print(x)
print(id(x))
print(id(x[1]))
x=[7,8,9]
print(x)
print(id(x))

def fun(b):
    print(id(b))
    # b = 3
    # b[0] = 3
    b.append(4)
    # b = [7, 8 ,9]
    print(id(b))

print("function:")
# a =2
a = [1, 2, 3]
print(id(a))
fun(a)
print(id(a))
print(a)

print("new copy")
a = [1,2,3]
b = a
print(id(a))
print(id(b))
b[0] = 4
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))

print("new copy 2")
a = [1, 2, 3]
b = []
for i in a:
    b.append(i)
print(a)
print(b)
print(id(a))
print(id(b))
b[0] = 4
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))


