def main() -> None:
    values = [
        int(part)
        for part in input("Введите 10 целых чисел: ").split()
    ]
    if len(values) != 10:
        print("Ошибка: требуется ровно 10 элементов")
        raise SystemExit(1)

    total = 0
    for item in values:
        if abs(item) < 5:
            total += item

    compact_total = sum(item for item in values if abs(item) < 5)
    print(f"Сумма: {total}")
    print(f"Проверка: {compact_total}")


if __name__ == "__main__":
    main()