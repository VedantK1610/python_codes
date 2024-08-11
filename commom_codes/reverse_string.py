def fun(s):
    if len(s)==0:
        return s
    return fun(s[1:]) + s[0]

s='vedant'
print(fun(s))