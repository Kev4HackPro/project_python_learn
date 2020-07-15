# defining the decorator functions


def make_bold(fn):
    # noinspection SpellCheckingInspection
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"

    return makebold_wrapped


def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"

    return makeitalic_wrapped


# Applying decorators to function hello
@make_bold
@make_italic
def hello():
    return 'hello world'


# call function hello
print(hello())