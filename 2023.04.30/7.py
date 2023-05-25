# import ref_7
from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec

script_dir = Path(path[0])
module_path = script_dir / '# ref 7.py'

spec = spec_from_file_location(module_path.stem, module_path)
ref_7 = module_from_spec(spec)
modules[module_path.stem] = ref_7
spec.loader.exec_module(ref_7)

general_dictionary = {}

for cities in ref_7.list_of_dicts:
    for city, value in cities.items():
        # ИСПРАВИТЬ: используйте словарные методы вместо явной проверки наличия ключа в словаре
        if city not in general_dictionary:
            general_dictionary[city] = {value}
        else:
            general_dictionary[city] = general_dictionary[city] | {value}

# КОММЕНТАРИЙ: вот это прям хороший пример использования print()
# ИСПОЛЬЗОВАТЬ: создание множества избыточно — дублей не будет, потому что на каждый уникальный ключ создаётся одна строка — а значит можно распаковать сразу генераторное выражение, взятое в круглые скобки
print(*(f'{city!r}: {value}' for city, value in general_dictionary.items()), sep=',\n')


# 'Тула': {2, 3},
# 'Пермь': {9, 3},
# 'Ростов-на-Дону': {5, 6},
# 'Ульяновск': {4, 7},
# 'Махачкала': {5},
# 'Барнаул': {5},
# 'Хабаровск': {7},
# 'Краснодар': {9, 4},
# 'Самара': {2},
# 'Санкт-Петербург': {4, 6},
# 'Ярославль': {9},
# 'Тольятти': {9},
# 'Новосибирск': {7},
# 'Липецк': {1},
# 'Красноярск': {9, 1},
# 'Тюмень': {5},
# 'Москва': {1}


# ИТОГ: хорошо, но можно лучше — 3/4
