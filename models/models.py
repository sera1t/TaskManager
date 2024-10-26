from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

engine = create_engine(os.getenv('APP_URL_DB'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)

class TaskUser(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    relations = Column(Integer, ForeignKey('users.id'), nullable=False)
    name_task = Column(String(255), nullable=True)
    description_task = Column(Text)
    execution_date = Column(DateTime, default=datetime.now(), nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)



