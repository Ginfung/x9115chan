def do_twice(f,arg):
    f(arg)
    f(arg)

def do_four(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)

def print_out(s):
    print s

do_four(print_out,'spam')
