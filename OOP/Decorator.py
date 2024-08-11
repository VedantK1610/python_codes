def greet(fx):   #here fx is hello fun
    def mfx(*args,**kwargs):
        print("Good morning sir")
        fx(*args,**kwargs)
        print("Good night")
    return mfx


@greet
def hello():
    print("Thanks for accessing this function")

@greet
def add(a,b):
    print(a+b)

hello()
print("\n")
add(1,2)