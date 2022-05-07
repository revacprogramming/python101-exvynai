def add(a, b):
    return a + b

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    c = add(a, b)
    print(a, '+', b, '=', c)


main()
