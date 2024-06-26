def decorator(func):
    def wrapper():
        print('hello')
        func()
        print('hello')
    return wrapper

def say_hello():
    print('hello')

say_hello=decorator(say_hello)
say_hello()