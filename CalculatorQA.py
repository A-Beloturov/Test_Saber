symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "/", "*", "(", ")", "."}
def calculate(s):
    try:
        for c in s:
           if c not in symbols:
               return "Только цифры и операторы"
        return eval(s)
    except ZeroDivisionError:
        return "Деление на ноль"
    except SyntaxError:
        return "Неправильный синтаксис выражения"

calc = input()
print(calculate(calc))