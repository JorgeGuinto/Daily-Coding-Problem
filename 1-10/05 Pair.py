def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#print(type(cons(1,2)))
def car(a):
    def first(i,j):
        return i
    return a(first)

def cdr(b):
    def last(i,j):
        return j
    return b(last)

print(f"a = {car(cons(1,2))}")
print(f"b = {cdr(cons(1,2))}")
