import functools

def decor(func):
    @functools.wraps(func)
    def inner(arg, x='End!'):
        new_arg=x        
        x=arg*10
        return func(new_arg, x)
    return inner

def Fun(arg, x='Begin!'):
    print(x)
    return(arg)

print(Fun(10))
print('//////')
print(decor(Fun)(10))
