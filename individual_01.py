def main() -> None:
    values = [
        int(part)
        for part in input("Введите 10 целых чисел: ").split()
    ]
    if len(values) != 10:
        print("Ошибка: требуется ровно 10 элементов")
        raise SystemExit(1)

    total_negatives = 0
    for item in values:
        if item < 0:
            total_negatives += item

    # Равнозначное списковое включение для сравнения по заданию
    comprehension_total = sum([item for item in values if item < 0])

    print(f"Сумма отрицательных элементов (цикл): {total_negatives}")
    print(f"Сумма через включение: {comprehension_total}")


if __name__ == "__main__":
    main()