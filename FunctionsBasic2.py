def countdown(n):
    x=[]
    for n in range(n,-1,-1):
        x.append(n)
    return x

print(countdown(5))

def print_and_return(a,b):
    print(a)
    return(b)

print(print_and_return(3,5))

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))


def greater_than(list):
    x=[]
    max = list[1]
    for n in range(0,len(list)):
        if n > max:
            x.append(n)
    if len(x) < 2:
        return "false"
    print(len(x))
    return x


print(greater_than([5,2,3,2,1,4]))
print(greater_than([0,3]))

def this_that(a,b):
    z=[]
    z.append(b)
    v = z*a
    return v

print(this_that(4,7))
print(this_that(10,8))
