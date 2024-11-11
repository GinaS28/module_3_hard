
def calculate_structure_sum (structure):
    sum = 0
    if isinstance(structure, (int, float)):
        sum += structure

    elif isinstance(structure, str):
        sum += len(structure)

    elif isinstance(structure, dict):
        for key, value in structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)

    elif isinstance(structure, (list, tuple, set)):
        for i in  structure:
            sum += calculate_structure_sum(i)

    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
