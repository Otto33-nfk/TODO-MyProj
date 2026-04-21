import operator

def filter_and_sort(data, field, condition, value, sort_field, reverse=False):
    ops = {
        '>': operator.gt,
        '<': operator.lt,
        '==': operator.eq,
        '>=': operator.ge,
        '<=': operator.le
    }
    op = ops.get(condition)
    if op is None:
        raise ValueError("Неподдерживаемое условие")

    filtered = [item for item in data if op(item[field], value)]
    filtered.sort(key=lambda x: (x[sort_field], x['name']), reverse=reverse)
    return filtered

# Пример
students = [
    {"name": "Ivan", "age": 19, "score": 75},
    {"name": "Anna", "age": 20, "score": 90},
    {"name": "Petr", "age": 18, "score": 90},
    {"name": "Olga", "age": 21, "score": 60}
]

result = filter_and_sort(students, field="score", condition=">", value=70,
                         sort_field="age", reverse=False)
print(result)
