# Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


from cgitb import reset
import itertools


games = int(input('Введите кол-во завершенных игр -> ')) # ввод кол-ва игр

res_game = [input('введите в формате: команда;голы;команда;голы-> ').split(';') for i in range(games)] # вводим данные в определенном формате, получаем список списков
print(res_game)

team = [(i[0], i[2]) for i in res_game] # выборка только названий команд
print(team)

teams = set(itertools.chain.from_iterable(team)) # получаем сет из всех команд-участников
print(teams)

itog = {i:[0]*5 for i in teams} # создаем словарь для выведения результата каждой команды
print(itog)

# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
for team1, goly1, team2, goly2 in res_game: # в цикле формируем итоговый результат Команда:Всегоигр Побед Ничьих Поражений Всегоочков
    itog[team1][0] += 1
    itog[team2][0] += 1

    if goly1 > goly2:
          
        itog[team1][1] += 1
        itog[team1][4] += 3
        itog[team2][3] += 1
        
    elif  goly1 < goly2:
      
        itog[team2][1] += 1
        itog[team2][4] += 3
        itog[team1][3] += 1

    else:

        itog[team2][2] += 1
        itog[team2][4] += 1
        itog[team1][2] += 1
        itog[team1][4] += 1
      
        
print(itog)  


