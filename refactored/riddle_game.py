from game_logic import get_random_riddle, check_answer

MAX_ATTEMPS = 4

def main_game_loop():
    """
    Функция задает пользователю загадку на которую он должен ответить.
    Если он ответил правильно то программа успешно завершается.
    Если же ответил неправильно то задает новую случайную загадку.
    У пользователя есть фиксированное число попыток.
    Если число попыток закончится то программа автоматически завершится.
    """
    
    k = 0 #счетчик попыток
    while k < MAX_ATTEMPS :
        k += 1
        print("\nПопытка № {}".format(k))
        
        riddle, correct_answer = get_random_riddle()
        print(riddle)
        
        answer = input("Введите ответ на загадку: ")
        
        answer = check_answer(answer)      
    
        if answer != correct_answer:
            print(f"\nНеправильный ответ, правильным ответом будет '{correct_answer }'. Старайтесь лучше!")
        else:
            print(f"\nВы верно угадали что правильным ответом будет '{correct_answer }'. Молодец!")
            break
    else:
        print('\nВы использовали все доступные попытки')

if __name__ == '__main__':
    main_game_loop()