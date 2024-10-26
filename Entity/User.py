from models.models import User, engine
from sqlalchemy.orm import Session


class UserEntity:
    def __init__(self, user: dict):
        self.user: User = User(
            username=user['username'],
            password=user['password']
        )

    def create_user(self) -> int:
        try:
            with Session(engine) as session:
                session.add(self.user)
                session.commit()
            return 1
        except:
            return 0

    def check_user_db(self) -> dict:
        with Session(engine) as session:
            check_user = session.query(User).filter(self.user.username == User.username).first()
            if not check_user:
                return {'status': 0, 'msg': 'No user'}
        return {'status': 1, 'msg': 'Yes user', 'user': check_user}
