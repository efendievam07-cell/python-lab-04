def main() -> None:
    original = [
        int(part)
        for part in input("Введите целые числа: ").split()
    ]
    nonnegative = [item for item in original if item >= 0]
    ordered = sorted(nonnegative, reverse=True)

    print(f"Исходный список: {original}")
    print(f"После фильтрации: {nonnegative}")
    print(f"После сортировки: {ordered}")


if __name__ == "__main__":
    main()