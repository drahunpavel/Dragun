from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



'''
Создать питоновский файл models.py . Создать таблицу Users определив 
поля( id: первичный ключ, first_name,last_name:строки длинной в 50 символов, age: целое число). 
Создать “движок” для подключения SQLite и создать таблицу через Base.metadata.create_all(engine)
'''

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)


class UsersHandler():
    def __init__(self) -> None:
        self.engine = create_engine(
            'sqlite:///homework15(SQLite3,SqlAlchemy)/db/SQLite/example.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self) -> None:
        # create_all - создание всех таблиц, которые есть в моделях
        Base.metadata.create_all(self.engine)

    def add_users(self, users: List[Users]) -> None:
        # добавление по одной сущности
        # for data in users_data:
        #     user = Users(**data)
        #     session.add(user)
        self.session.add_all(users)
        self.session.commit()
        self.session.close()

    'Создать сессию и вывести первых 3 пользователей отсортированных по убыванию возроста'

    def get_users_1(self) -> None:
        users = self.session.query(Users).order_by(
            Users.age.desc()).limit(3).all()
        print_data(users)
        self.session.close()

    'Создать сессию и вывести  пользователей по имени “Jhon”'

    def get_users_2(self) -> None:
        search_name = 'Jhon'
        users = self.session.query(Users).filter_by(
            first_name=search_name).all()
        print_data(users)
        self.session.close()

    'Создать сессию и вывести  пользователей  старше 20 лет, а также в фамилии которых есть буква “a”. '

    def get_users_3(self) -> None:
        users = self.session.query(Users).filter(Users.age > 20, Users.last_name.like(
            '%a%')).order_by(Users.last_name.desc()).all()
        print_data(users)
        self.session.close()

    'Создать сессию и вывести  пользователей от 10 до 20 лет, а также всех тех кому 30 лет.'

    def get_users_4(self) -> None:
        users = self.session.query(Users).filter(
            ((Users.age >= 10) & (Users.age <= 20)) | (Users.age == 30)
        ).all()
        print_data(users)
        self.session.close()

    def __del__(self):
        self.session.close()


def print_data(users: List[Users]) -> None:
    print('--------------------')
    if len(users) == 0:
        print('users no found')
    else:
        for user in users:
            print(
                f"id: {user.id}, full name: {user.first_name} {user.last_name}, age: {user.age}")


'Создать сессию и добавить в базу 5 разных пользователей.'
users_data = [
    Users(first_name="Jhon", last_name="Doe", age=30),
    Users(first_name="Alice", last_name="Smith", age=25),
    Users(first_name="Bob", last_name="Johnson", age=35),
    Users(first_name="Emily", last_name="Brown", age=40),
    Users(first_name="David", last_name="Wilson", age=45)
]

users_data_2 = [
    Users(first_name="Jhon", last_name="Smith", age=14),
    Users(first_name="Bob", last_name="Doe", age=15),
    Users(first_name="Emily", last_name="Johnson", age=15),
    Users(first_name="Emily", last_name="Brown", age=20),
    Users(first_name="Alice", last_name="Wilson", age=15)
]

users_handler = UsersHandler()
# users_handler.create_table()
# users_handler.add_users(users=users_data)
# users_handler.add_users(users=users_data_2)
users_handler.get_users_1()
users_handler.get_users_2()
users_handler.get_users_3()
users_handler.get_users_4()
