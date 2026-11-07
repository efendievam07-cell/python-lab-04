def main() -> None:
    raw_parts = input("Введите целые числа для кортежа: ").split()
    original_tuple = tuple(int(part) for part in raw_parts)

    # Формируем новый кортеж по правилу: четные удваиваем, нечетные сохраняем
    result_list = []
    for item in original_tuple:
        if item % 2 == 0:
            result_list.append(item * 2)
        else:
            result_list.append(item)

    transformed_tuple = tuple(result_list)

    print(f"Исходный кортеж: {original_tuple}")
    print(f"Результирующий кортеж: {transformed_tuple}")


if __name__ == "__main__":
    main()