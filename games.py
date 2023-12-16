# Модуль games
# Демонструє створення модуля

def ask_yes_no(question):
    """Задає питання з відповіддю (y/n)."""
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)? ').lower()
    return response

def ask_number(question, low, high):
    """Просить ввести число із заданого діапазону."""
    response = None
    while response not in range(low, high + 1):
        response = int(input(question))
    return response

  
if __name__ == "__main__":
    print("Ви запустили модуль games, "
          "а не імпортували його (import games).")
    print("Тестування модуля.")
    answer = ask_yes_no("Продовжуємо тестування")
    print("Функція ask_yes_no повернула", answer)
    answer = ask_number("Введіть ціле число від 1 до 10:", 1, 10)
    print("Функція ask_number повернула", answer)
