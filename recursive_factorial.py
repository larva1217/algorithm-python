#팩토리얼-재귀함수

def factorial_recursive(n):
    if n<=1:
        return 1
    else:
        return n*factorial_recursive(n-1)

result=factorial_recursive(10)
print(result)