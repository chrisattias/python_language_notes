global_variable_text = "Hello world"
def a():
    print("This is a")
    local_variable_text = "Hello moon"
    b()
    print("This is a again")
    return "This string is the function a return value"
def b():
    print("This is b")
    return "This string is the function b return value"
a()