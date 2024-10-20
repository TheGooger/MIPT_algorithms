def foo(n):
    if n == 1:
        print("Матрешка")
    else:
        print("Верх матрешки для n=", n)
        foo(n-1)
        print("Низ матрешки для n=", n)

num = int(input("Сколько матрешек? "))
foo(num)
