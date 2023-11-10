def fibonacci_sequence_calc(n):
    """
    This is to calculate the fibonacci sequence of a given number
    """
    if(n==1):
        return 0
    if(n==2):
        return 1
    else:
        return fibonacci_sequence_calc(n-1)+fibonacci_sequence_calc(n-2)
num=int(input("Enter a number to check fibonacci\n"))
print(fibonacci_sequence_calc(num))
