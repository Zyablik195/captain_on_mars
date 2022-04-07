from flask import Flask
from data import db_session
from data.users import User
from data.departments import Department
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    name = input()
    db_session.global_init("db/blogs.db")
    # db_session.global_init(name)
    # app.run()
    db_sess = db_session.create_session()
    dick = {
        'user.surname': ['Scott', 'Шварцнигер', 'Гослинг', 'Путин'],
        'user.name': ['Ridley', 'Арнольд', 'Райан', 'Владимир'],
        'user.age': [21, 55, 37, 64],
        'user.position': ['captain', 'terminator', 'legenda', 'boss_of_this_gym'],
        'user.speciality': ['research engineer', 'zloy dyadya', 'v rolyah', 'yadernaya bomba'],
        'user.address': ['module_1', 'kachalka', 'film drive', 'v nashih serdcah'],
        'user.email': ['scott_chief@mars.org', 'bigcock@yandex.ru', 'lalala228@noob.com', 'obamaloh@russia.win']
    }
    for i in range(4):
        user = User()
        user.surname = dick['user.surname'][i]
        user.name = dick['user.name'][i]
        user.age = dick['user.age'][i]
        user.position = dick['user.position'][i]
        user.speciality = dick['user.speciality'][i]
        user.address = dick['user.address'][i]
        user.email = dick['user.email'][i]
        db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()