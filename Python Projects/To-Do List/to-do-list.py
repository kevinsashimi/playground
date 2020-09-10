from sqlalchemy import create_engine
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date, timedelta

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    print()

    today = date.today()
    rows = session.query(Table).order_by(Table.deadline).all()
    choice = int(input())

    if choice == 1:
        if not rows:
            print(f"Today {today.day} {today.strftime('%b')}:")
            print("Nothing to do!\n")
        else:
            task_id = 1
            today_rows = session.query(Table).filter(Table.deadline == today).all()
            print(f"Today {today.day} {today.strftime('%b')}:")

            for row in today_rows:
                print(f"{task_id}. {row.task}")
                task_id += 1

            print()

    elif choice == 2:
        next_date = today
        last_date = today + timedelta(days=7)
        while next_date != last_date:
            task_id = 1
            today_rows = session.query(Table).filter(Table.deadline == next_date).all()
            print(f"{next_date.strftime('%A')} {next_date.day} {today.strftime('%b')}:")

            if not today_rows:
                print("Nothing to do!")
            else:
                for row in today_rows:
                    print(f"{task_id}. {row.task}")
                    task_id += 1

            print()
            next_date += timedelta(days=1)
        print()

    elif choice == 3:
        print("All tasks:")
        task_id = 1

        for row in rows:
            print(f"{task_id}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
            task_id += 1

        print()

    elif choice == 4:
        missed_rows = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline).all()
        task_id = 1

        if not missed_rows:
            print("Nothing is missed!")
        else:
            print("Missed tasks:")

            for row in missed_rows:
                print(f"{task_id}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
                task_id += 1

        print()

    elif choice == 5:
        print("Enter task")
        newTask = input()
        print("Enter deadline")
        deadline = input()
        new_row = Table(task=newTask,
        deadline=datetime.strptime(deadline, '%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")

    elif choice == 6:
        print("Choose the number of the task you want to delete:")
        task_id = 1

        for row in rows:
            print(f"{task_id}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
            task_id += 1

        del_index = int(input())
        del_id = 1

        for row in rows:
            if del_id == del_index:
                del_task_num = row.id
            del_id += 1

        session.query(Table).filter(Table.id == del_task_num).delete()
        session.commit()

        print("The task has been deleted!\n")

    elif choice == 0:
        break
