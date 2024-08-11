import re
def fun1(s,f):
    if f in s:
        return "yes"
    else:
        return "No"

def fun2(s,f):
    if re.search(f,s):
        return "yes"
    return "no"

s='abcabc'
f='abc'
print(fun2(s,f))