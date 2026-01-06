def outer_function():   
    x = 10

    def inner_function():
        nonlocal x
        x += 5
        return x

    result = inner_function()
    return result, x    

print(outer_function())