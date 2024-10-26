from Entity import User, Task
from datetime import datetime


def main():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    data_user = {
        'username': login,
        'password': password
    }
    new_user = User.UserEntity(data_user)
    check_user = new_user.check_user_db()

    if check_user['status']:
        print(f'Добро пожаловать {check_user['user'].username}')
        user = check_user['user']
        isTask = _task_display(user)

        if not isTask:
            print('Создайте задачу')
            name_task: str = str(input('Введите название задачи: '))
            description_task: str = str(input('Введите описание задачи: '))
            execution_date = datetime.strptime(input('Введите дату выполнения задачи через тире (год-месяц-день): '), '%Y-%m-%d')
            task_create = {
                'user': user.id,
                'name_task': name_task,
                'description_task': description_task,
                'execution_date': execution_date
            }

            task = Task.TaskEntity(task_create)
            task.create_task_user()
            _task_display(check_user)


    else:
        print('Пользователь не найден.')

def _task_display(user: User.UserEntity):
    user_task = Task.TaskDisplay(user)
    task_display = user_task.display_task_user()

    if task_display:
        print(f'Список ваших задач {task_display[0].name_task}')
        return 1
    else:
        print('У вас нету задач')
        return 0

