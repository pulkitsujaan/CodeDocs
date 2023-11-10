def func1(a):
    try:
        return int(a)-1
    except:
        raise ValueError("Enter a valid number")
num=func1('akk')
print(num)