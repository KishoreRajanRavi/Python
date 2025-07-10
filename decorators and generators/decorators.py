def decorator_function(funct):
    def wrapper():
        print("tea in fancy glass")
        funct()
        print("Thank You")
    return wrapper
@decorator_function
def serve_tea():
    print("Here is your tea")
serve_tea()
