import math


def main() -> None:
    raw_input = input("Введите вещественные числа: ").split()
    if not raw_input:
        print("Ошибка: список пуст")
        raise SystemExit(1)

    original = [float(part) for part in raw_input]

    # 1. Сумма отрицательных элементов
    negatives = [x for x in original if x < 0]
    sum_negatives = sum(negatives)

    # 2. Поиск первых вхождений минимума и максимума
    min_index = 0
    max_index = 0
    for index, item in enumerate(original):
        if item < original[min_index]:
            min_index = index
        if item > original[max_index]:
            max_index = index

    left, right = min_index, max_index
    if left > right:
        left, right = right, left

    between_elements = original[left + 1:right]
    if between_elements:
        prod_between = math.prod(between_elements)
        prod_result_str = f"{prod_between:.6f}"
    else:
        # По общим правилам: произведение пустой выборки равно 1
        prod_result_str = "1.000000 (пустая выборка между экстремумами)"

    # 3. Преобразование независимой копии
    transformed = original.copy()
    transformed.sort()

    print(f"Сумма отрицательных элементов: {sum_negatives:.6f}")
    print(f"Индекс первого минимума: {min_index}")
    print(f"Индекс первого максимума: {max_index}")
    print(f"Произведение элементов между ними: {prod_result_str}")
    print(f"Исходный список: {original}")
    print(f"Отсортированный список: {transformed}")


if __name__ == "__main__":
    main()