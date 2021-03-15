import time

mylist = [int(i) for i in range(100)]


def get_function_time(function):
    def include_fuction(*args):
        start_time = time.clock()
        func_resalt = function(*args)
        print(time.clock() - start_time)
        return func_resalt
    return include_fuction


@get_function_time
def for_mylist(mylist):
    summ = 0
    for f in mylist:
        summ += f
    return summ


@get_function_time
def while_mylist(mylist):
    summ = 0
    i = 0
    while i < len(mylist):
        summ += mylist[i]
        i += 1
    return summ


@get_function_time
def recurse_mylist(mylist, i, summ):
    if i > len(mylist) - 1:
        return summ
    else:
        summ += mylist[i]
        i += 1
        return recurse_mylist(mylist, i, summ)


print(for_mylist(mylist))
print(while_mylist(mylist))
print(recurse_mylist(mylist))
