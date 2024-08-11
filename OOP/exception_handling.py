'''
1.Errors are problems in a program due to which the program will stop the execution.
2.On the other hand, exceptions are raised when some internal events occur which change the normal
  flow of the program.

3.Try and except statements are used to catch and handle exceptions in Python. Statements that can raise
  exceptions are kept inside the try clause and the statements that handle the exception are written
  inside except clause.

4.In Python, you can also use the else clause on the try-except block which must be present after
  all the except clauses. The code enters the else block only if the try clause does not raise an exception.

5.If finally block is provided, it will always execute after try and except blocks.

'''
def without_try(x,y):
    z=x/y
    print(z)

def with_try(x,y):
    try:
        z = x / y
    except TypeError:
        print("Sorry! string and int cannot be divided")

def list_fun(a):
    try:
        print('first element %d' % (a[0]))
        print('fourth element %d' % (a[3]))
    except:
        print('list out of bounce')

def specific_exception():
    def fun(a):
        if a<5:
            b=a/(a-4)
        print('value of b:',b)

    try:
        # fun(4)
        fun(6)
    except ZeroDivisionError:
        print('give bigger value')
    except NameError:
        print('give smaller value')

def try_else(a,b):
    try:
        b=((a+b)/(a-b))
    except ZeroDivisionError:
        print('zero division error')
    else:
        print('b:',b)

x='vedant'
y=2

# without_try(x,y) will throw TypeError
# with_try(x,y) this will print except statement

a=[1,2,4]
# list_fun(a)

# specific_exception()

# try_else(4,3)

