from helloWorld import hello

def test_hello():
    assert(hello() == "Hello World")
    assert(hello() != "Hello")
    assert(hello() != "World")
