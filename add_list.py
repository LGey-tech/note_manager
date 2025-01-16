username = input('Введите ваше Имя и Фамилию:')
title = (input('Введите заголовок заметки:'))
content = (input('Введите описание заметки:'))
status = (input('Введите статус:'))
temp_created_date = input('Введите дату создания заметки (Формат:dd.mm.yyyy):')
temp_issue_date = input('Введите дату истечения срока заметки (дедлайн):')

print(f"Вас зовут:", username)
print(f"Ваша заметка:", title)
print(f"Описание заметки:", content)
print(f'Статус заметки:', status)
print(f'Дата создания:', temp_created_date[0:5])
print(f'Дата истечения срока:', temp_issue_date[0:5])

task1 = input('Заголовок №1:')
task2 = input('Заголовок №2:')
task3 = input('Заголовок №3:')

print(f'1.',task1,'\n2.',task2,'\n3.',task3)
