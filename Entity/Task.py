from models.models import TaskUser, engine
from sqlalchemy.orm import Session

class TaskEntity:
    def __init__(self, task: dict):
        self.task = TaskUser(
            relations = task['user'],
            name_task = task['name_task'],
            description_task = task['description_task'],
            execution_date =  task['execution_date']
        )

    def create_task_user(self) -> int:
        try:
            with Session(engine) as session:
                print(self.task)
                session.add(self.task)
                session.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

class TaskDisplay:
    def __init__(self, user):
        self.user = user

    def display_task_user(self):
        try:
            with Session(engine) as session:
                tasks = session.query(TaskUser).filter(self.user.id == TaskUser.relations).all()

            return tasks
        except Exception as e:
            print(e)
            return 0

