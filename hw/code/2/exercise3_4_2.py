def do_twice(f,arg):
    f(arg)
    f(arg)

def print_twice(s):
    print s
    print s

do_twice(print_twice,'spam')

