def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_horizon_1():
    print '+ - - - - ',

def print_post_1():
    print '|         ',


def whole_horizon():
    do_twice(print_horizon_1)
    print '+'

def whole_horizon_2():
    do_four(print_horizon_1)
    print '+'
    
def whole_post():
    do_twice(print_post_1)
    print '|'

def whole_post_2():
    do_four(print_post_1)
    print '|'

def print_grid():
    whole_horizon()
    do_four(whole_post)
    whole_horizon()
    do_four(whole_post)
    whole_horizon()


def print_large_grid():
    whole_horizon_2()
    do_four(whole_post_2)
    whole_horizon_2()
    do_four(whole_post_2)
    whole_horizon_2()
    do_four(whole_post_2)
    whole_horizon_2()
    do_four(whole_post_2)
    whole_horizon_2()

    
print_grid()
print_large_grid()
