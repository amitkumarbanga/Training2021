def employee_details(**kwargs):
    print(type(kwargs))
    print(kwargs)

employee_details(name = "Amit", salary = 0000, gmail = "amitbanga17@gmail.com")

def employee_details(*args, **kwargs):
    print(*args)
    print(kwargs)

employee_details(10, 20, 30, 40, 50, name = "Amit", salary = 0000, gmail = "amitbanga17@gmail.com")
