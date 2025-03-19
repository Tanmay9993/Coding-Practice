

# 1. Say Hello, World!
if __name__ == '__main__':
    print("Hello, World!")


# 2. If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird') 
    elif n % 2 == 0 and n >=2 and n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and n >=6 and n <= 20:
        print('Weird')
    else:
        print('Not Weird') 


# 3. Arithmetic Ops
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# 4. Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# 5. Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i ** 2)


# 6. Print Function
if __name__ == '__main__':
    n = int(input())
    output = ''
    for i in range(1,n+1):
        output += str(i)
    print(output)


