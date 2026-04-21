def who_is_higher(name1, name2, registry):
    floors = {}
    for entry in registry:
        parts = entry.split()
        name = parts[0]
        floor = int(parts[-1])
        floors[name] = floor

    f1 = floors.get(name1)
    f2 = floors.get(name2)

    if f1 is None or f2 is None:
        return "Один из жильцов не найден"

    diff = abs(f1 - f2)
    if f1 > f2:
        return f"{name1} выше на {diff} этажа"
    elif f2 > f1:
        return f"{name2} выше на {diff} этажа"
    else:
        return "Живут на одном этаже"

# Пример использования
riestr = ["Саша этаж 11", "Кирилл этаж 3", "Маша этаж 13", "Денис этаж 6"]
print(who_is_higher("Маша", "Саша", riestr))
