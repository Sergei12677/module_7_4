print()

team1_num = 5
print("В команде Мастера кода участников: %s !" % team1_num)

team1_num = 5
team2_num = 6

print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print()

score_2 = 42

print("Команда Волшебники данных решила задач: {} !".format(score_2))


team1_time = 1552.512
team2_time = 2153.31451

print("Волшебники данных решили задачи за {} с !".format(team1_time))
print("Мастера кода решили задачи за {} с !".format(team2_time))

print()


score_1 = 40

print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
    print(f"{challenge_result}")

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f"{challenge_result}")

else:
    challenge_result = 'Ничья!'
    print(f"{challenge_result}")

tasks_total = score_2 + score_1
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')