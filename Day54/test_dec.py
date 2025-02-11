def delay_decorator(function):
    def wrapper_funtion():
        time.sleep(2)
        function()
    
    return wrapper_function
