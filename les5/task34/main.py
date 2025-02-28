from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_session.global_init("db/mars_explorer.db")
    add_users()
    add_job()


def add_users():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org1"
    user.set_password("1")
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Queen"
    user.name = "Margo"
    user.age = 21
    user.position = "part of team"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "margo_queen@mars.org1"
    user.set_password("2")
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Daemon"
    user.name = "Met"
    user.age = 23
    user.position = "hulk"
    user.speciality = "engineer"
    user.address = "module_3"
    user.email = "daemon@mars.org1"
    user.set_password("3")
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
        print(user.name)


def add_job():
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2,3"
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
