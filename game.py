# game.py

from gameparts import Board
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    current_player = 'X' 
    running = True
    while running:
        game.display()
        while True:
                # В этом блоке содержатся операции, которые могут вызвать исключение
                try:
                    # Пользователь вводит значение номера строки
                    row = int(input('Введите номер строки: '))
                    # Если введённое число меньше 0 или больше
                    # или равно game.field_size...
                    if row < 0 or row >= game.field_size:
                        # ...выбрасывается собственное исключение FieldIndexError
                        raise FieldIndexError
                    column = int(input('Введите номер столбца: '))
                    # Если введённое число меньше 0 или больше
                    # или равно game.field_size...
                    if column < 0 or column >= game.field_size:
                        # ...выбрасывается собственное исключение FieldIndexError
                        raise FieldIndexError
                except ValueError:
                    print(
                            'Буквы вводить нельзя. Только числа.')                        
                                
                    print('Пожалуйста, введите значения для строки и столбца заново.')
                                # ...и цикл начинает свою работу сначала,
                                # предоставляя пользователю ещё одну попытку ввести данные
                    continue   
                # Если возникает исключение FieldIndexError...
                except FieldIndexError:
                    # ...выводятся сообщения...
                    print(
                        'Значение должно быть неотрицательным и меньше '
                        f'{game.field_size}.'
                    )
                    print('Пожалуйста, введите значения для строки и столбца заново.')
                    # ...и цикл начинает свою работу сначала,
                    # предоставляя пользователю ещё одну попытку ввести данные
                    continue
                except Exception as e:
                    print(f'Возникла ошибка: {e}')
                    continue
                # Если в блоке try исключения не возникло...
                else:
                    # ...значит, введённые значения прошли все проверки
                    # и могут быть использованы в дальнейшем.
                    # Цикл прерывается
                    break
        
        game.make_move(row, column, current_player)
        
        print('Ход сделан!')
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'
        
    # Запускается бесконечный цикл
    
if __name__ == '__main__':
    main() 