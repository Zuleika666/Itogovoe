# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

note = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "},
{" V ":" S009 "}, {" VIII":" S007 "}]

mnozhestvo = set()
print(note)
for dict_i in note:
    print(dict_i)
    # for key in dict_i:
    #     print(dict_i[key])
#         mnozhestvo.add(dict_i[key])
# print(mnozhestvo)        