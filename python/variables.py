statement = 'hello world!'
r, g, b = 'red', 'green', 'blue'
numbers = [1, 2, 3]
n1, n2, n3 = numbers
a = b = c = 'same'
print('statement: ' + statement)
print(r, g, b)
print(n1, n2, n3)

def myFunc():
    global statement
    statement = 'new hello world!'
    global x
    x = 2
myFunc()
print('new statement:', statement)
print(x)
print(a, b, c)