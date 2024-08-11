# basically we use json in python to convert the dictionary which is limited to
# python language to json format which is compatible with lang like c++,js

book={}
book['oomd']={
    'name':'object oriented modelling',
    'released':2010,
    'author':'J Charles'
}
book['se']={
    'name':'Software Engineering',
    'released':2008,
    'author':'Pankaj jalote'
}

import json
a=json.dumps(book)
with open("D:\\Python\\Trials\\book.txt","w") as f:
    f.write(a)
print(type(a))
b=json.loads(a)
print(b)
print(type(b))