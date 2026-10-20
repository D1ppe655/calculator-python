import logic

def get_number(prompt):
    """Безопасный ввод числа с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Ошибка: Введите корректное число.")

def main():
    print("=== КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР ===")
    
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Проценты (%)")
        print("0. Выход")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "0":
            print("До свидания!")
            break
            
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Неверный пункт меню. Попробуйте снова.")
            continue
            
        if choice == "5":
            print("\nФормат: 'Сколько процентов' от 'Числа'.")
            num1 = get_number("Введите число: ")
            num2 = get_number("Введите процент (%): ")
        else:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")
            
        try:
            if choice == "1":
                res = logic.add(num1, num2)
            elif choice == "2":
                res = logic.subtract(num1, num2)
            elif choice == "3":
                res = logic.multiply(num1, num2)
            elif choice == "4":
                res = logic.divide(num1, num2)
            elif choice == "5":
                res = logic.percent(num2, num1) # num1 - число, num2 - процент
                
            print(f"Результат: {res}")
            
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()