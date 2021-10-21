def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(num):
            #print("Result:",result,"iteration:",i+1)
            result *=i+1
    return result
