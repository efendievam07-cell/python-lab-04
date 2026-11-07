def main() -> None:
    values = [
        int(part)
        for part in input("Введите целые числа: ").split()
    ]
    if not values:
        print("Ошибка: список пуст")
        raise SystemExit(1)

    min_index = 0
    max_index = 0
    for index, item in enumerate(values):
        if item < values[min_index]:
            min_index = index
        if item > values[max_index]:
            max_index = index

    left, right = min_index, max_index
    if left > right:
        left, right = right, left

    count = 0
    for item in values[left + 1:right]:
        if item > 0:
            count += 1

    print(f"Индекс первого минимума: {min_index}")
    print(f"Индекс первого максимума: {max_index}")
    print(f"Положительных между ними: {count}")


if __name__ == "__main__":
    main()