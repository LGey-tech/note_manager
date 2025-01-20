username = input('Введите ваше Имя и Фамилию:')
title = (input('Введите заголовок заметки:'))
content = (input('Введите описание заметки:'))
status = (input('Введите статус:'))
temp_created_date = input('Введите дату создания заметки (Формат:dd.mm.yyyy):')
temp_issue_date = input('Введите дату истечения срока заметки (дедлайн):')
task1 = input('Заголовок №1:')
task2 = input('Заголовок №2:')
note = [
    username,
    title,
    content,
    status,
    temp_created_date[0:5],
    temp_issue_date[0:5],
    [task1, task2]
]


username1 = ('Имя пользователя:')
title1 = ('Заголовок заметки:')
content1 = ('Описание заметки:')
status1 = ('Статус заметки:')
created_date1 = ('Дата создания заметки:')
issue_date1 = ('Дата истечения заметки (дедлайн):')
tasks = ('Заголовки:')

print(username1, note[0])
print(title1, note[1])
print(content1, note[2])
print(status1, note[3])
print(created_date1, note[4])
print(issue_date1, note[5])
print(tasks, note[6])
