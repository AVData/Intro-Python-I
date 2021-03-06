# pass-by-reference vs passing-by-value
# define a function that multiplies its input by 2
# this function passess its input by-value
def mult_by_2(x):
    return x * 2

y = mult_by_2(12)
# print(id(y))
z = mult_by_2(y)
# print(id(y))

# passing by reference
# typically, data structure passed to a function are passed in by reference, in
# large part because data structures take up a lot of memory, which would mean
# the copying would be expensive
def mult2_list(l):
    # multiply every int in the list by 2
    # mutate the contents of the list
    for i in range(len(l)):
        l[i] *= 2

l = [1, 2, 3]
print(id(l))
mult2_list(l)
print(id(l))
print(l)
