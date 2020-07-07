def outer():
    """This is fine if we want our function to do the task
    i.e print inner title and outer title"""
    title = 'original title'

    def inner():
        title = 'another title'
        print('inner: ', title)

    inner()
    print('outer:', title)


outer()


# but if we want the inner() to modify the outer(), we can't do as above
# we have to use a non-local variable
def outer():
    title = 'original title'

    def inner():
        nonlocal title
        title = 'another title'
        print('inner:', title)

    inner()
    print('outer:', title)


outer()
