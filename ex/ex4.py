def search(f):
    x= 0
    while not f(x):
        x +=1
    return x
   

def is_three(x):
    return x==3

def square(x):
    return x*x

def positive(x):
    return max(0, square(x)-100)

def inverse(f):
    """ Returns g(y) such that g(f(x))  --> x.""" 
    def inverse_of_f(y):
        def is_inverse_of_y(x):
            return f(y) == y
        return search(is_inverse_of_y)
    return inverse_of_f
    #return lambda y: search(lambda x: f(x)==y)

def is_4_squared(x):
    return square(4) == x


print(search(is_4_squared))

def is_sqart_16(x):
    return square(x) == 16

print(search(is_sqart_16))

# High function 
# ex1
def compose1(f,g):
    return lambda x: f(g(x))

h = compose1(lambda x:x*x,lambda y: y+1)
print(h(12))

# ex2
def compose2(f,g):
    return lambda x: f(g(x))

def add_one(y):
    return y+1

h = compose2(square,add_one)
print(h(12))

# ex3
def compose3(f,g):
    def composed(x):
        return f(g(x))
    return composed

h = compose3(square,add_one)

# 以上 三个列子相同作用