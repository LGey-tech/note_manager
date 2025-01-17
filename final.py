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

print(note)