
def get_function(function):
    def include_fuction(*args):
        func_resalt = function(*args)
        revers = func_resalt[::-1]
        k = int(len(func_resalt) / 2)
        return func_resalt[0:k] == revers[0:k]
    return include_fuction

@get_function
def dec_to_base(n, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = []
    while n:
        n, y = divmod(n, base)
        r.append(dec_to_base.table[y])
    return ''.join(reversed(r))

def is_polyndrom(n: int) -> int:
    for r in range(2,37,1):
        print(r)
        if dec_to_base(n, r):
            return r
    return 0

print(is_polyndrom(2054170329))
# text = "121212"
# revers = text[::-1]
# k = int(len(text)/2)
# print(text ,"yes" if text[0:k] == revers[0:k] else "no")
