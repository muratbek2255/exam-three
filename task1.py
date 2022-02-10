"""У вас имеется следующий список: /
[1, 4.7, ‘hi’, False, None]
Необходимо создать из него словарь с ключами “int”, “float”, “str”, “bool”, “none” и соответствующим значением из списка.
Вместо этих значений в списке и их порядок могут быть и другие, напишите код, который будет работать с любыми значениями, то есть он должен быть универсальным
Например из списка
[True, 2.3, None, “brook”, 5]
Надо получить:
{
“float”: 2.3,
“bool”: True,
“none”: None,
“int”: 5,
“str”: “brook”
}
"""


dict = {
    "float":[],
    "bool":[],
    "none":[],
    "int":[],
    "str":[]
}


class FilterDict:

    def __init__(self, our_list: list):
        self.our_list = our_list

    # Здесь мы сопоставляем с ключами
    def filter_dict(self):
        for output in self.our_list:
            if float == type(output):
                dict["float"].append(output)
            elif bool == type(output):
                dict["bool"].append(output)
            elif None == type(output):
                dict["none"].append(output)
            elif int == type(output):
                dict["int"].append(output)
            elif str == type(output):
                dict["str"].append(output)

Result = FilterDict([1, 4.7, "hi", False, None])
Result.filter_dict() #Выдаст нам ключ и слово
print(dict)
