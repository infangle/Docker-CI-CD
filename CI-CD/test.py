from helloWorld import hello

def test():
    assert(hello() == "Hello World")
    assert(hello() != "Hello")
    assert(hello() != "World")