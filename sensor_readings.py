from operator import itemgetter


def main() -> None:
    count = int(input("Количество измерений: "))
    if count <= 0:
        print("Ошибка: количество должно быть положительным")
        raise SystemExit(1)

    readings = []
    for index in range(count):
        name = input(f"Название датчика {index + 1}: ").strip()
        temperature = float(input("Температура: "))
        readings.append((name, temperature))

    total = 0.0
    for name, temperature in readings:
        total += temperature
    average = total / len(readings)

    selected = [
        (name, temperature)
        for name, temperature in readings
        if temperature > average
    ]
    selected.sort(key=itemgetter(1), reverse=True)

    print(f"Средняя температура: {average:.2f}")
    if selected:
        for name, temperature in selected:
            print(f"{name}: {temperature:.2f} °C")
    else:
        print("Измерений выше среднего нет")


if __name__ == "__main__":
    main()