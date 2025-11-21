def tags(param):
    def decorator(function):
        def wrapper(*args):
            return f"<{param}>{function(*args)}</{param}>"
        
        return wrapper
    
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
