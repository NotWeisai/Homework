n = int(input("Введите число: "))
def find_simple_numbers(n):
    simple = [1]
    for k in range(2, n+1):
        for i in range(2, int(k/2)+1):
            if (k % i) == 0:
                break
        else:
            simple.append(k)
    return simple

print(f"Все простые числа от 1 до {n}: {find_simple_numbers(n)}")