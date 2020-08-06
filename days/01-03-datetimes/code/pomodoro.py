"""
Simplified Pomodoro Timer
"""

import time
from datetime import datetime, timedelta


DATEFMTSTR = '%d/%m/%Y %H:%M:%S'
NAP = 10
LONGBREAK = 15
SHORTBREAK = 3


class Task(dict):

    def __getattr__(self, key):
        try:
            return(self[key])
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __str__(self):
        return (f'Task: {task.name}\n'
                f'Started : {task.start_time.strftime(DATEFMTSTR)}\n'
                f'End Time: {task.end_time.strftime(DATEFMTSTR)}')


task = Task(duration=timedelta(minutes=25), complete=False, checks=0)


def task_complete():
    """
    Ask User if task is complete yet.
    """
    complete = input('Is the Task Complete Y/N: ')
    return complete.lower() == 'y'


def handle_break():
    task.checks += 1
    if task.checks < 4:
        task.break_time = SHORTBREAK
    else:
        task.checks = 0
        task.break_time = LONGBREAK

    print(f'Please take a break for {task.break_time} minutes')
    time.sleep(task.break_time * 60)
    print('OK Get back to it!\n')
    task.end_time = datetime.now() + task.duration


def main():
    task.name = input('Please Enter Task Name: ')
    task.start_time = datetime.now()
    task.end_time = task.start_time + task.duration
    print(task)

    while not task.complete:

        if datetime.now() < task.end_time:
            # print(f'Sleeping for {NAP} seconds...')
            time.sleep(NAP)
        elif task_complete():
            task.complete = True
        else:
            handle_break()
            print(task)

    print('Task Complete - have a beer!')


if __name__ == '__main__':
    main()
