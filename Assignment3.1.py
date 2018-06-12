'''
2.​ Problem Statement
Problem Statement 1:
Write a function to compute 5/0 and use try/except to catch the exceptions.

'''

def div(n,d):
    try:
        return n/d
    except Exception as ZeroDivisionError:
        return ("Denominator can't be zero")
    except Exception as e:
        return (e)
print(div(5,0))
