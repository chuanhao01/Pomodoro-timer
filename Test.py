import time
from datetime import datetime, date, time, timedelta



class Pomodoro():
    ''' Mimics a Pomodoro timer, a time management tool that breaks work into intervals separated by
        breaks.
    '''

    # define timer types
    TIMER_NONE = 0
    TIMER_TASK = 1
    TIMER_SHORT_BREAK = 2
    TIMER_LONG_BREAK = 3

    def __init__(self):
        '''
            Initialize a pomodoro timer
        '''

        # define goals
        self.task_goal = 8
        self.task_count = 0
        self.long_break_goal = 4

        # define task length
        self.task_length = timedelta(minutes=25)

        # define break periods
        self.short_break = timedelta(minutes=3)
        self.long_break = timedelta(minutes=15)

        # initialize timer
        self.timer_type = self.TIMER_NONE

    def start_task(self):
        '''
            Stars a task timer.
        '''

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.task_length
        self.timer_type = self.TIMER_TASK

        print('\n---- begin task {} ----\n'.format(self.task_count + 1))

    def start_short_break(self):
        '''
            Starts a short break timer.
        '''

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.short_break
        self.timer_type = self.TIMER_SHORT_BREAK

        print('\n---- begin short break ----\n')

    def start_long_break(self):
        '''
            Starts a long break timer.
        '''

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.long_break
        self.timer_type = self.TIMER_LONG_BREAK

        print('\n---- begin long break ----\n')

    def complete_task(self):
        '''
            Increases task count by 1.
        '''

        # increase task counter
        self.task_count += 1

    def done(self):
        '''
            Denotes whether the Pomodoro task goal has been met.

            Returns True if task goal has been met.  False otherwise.
        '''
        return self.task_count == self.task_goal

    def get_time_remaining(self):
        '''
            returns the amount of time remaining in the current timer in the form of a timedelta object.
        '''
        return self.timer_end - datetime.now()

    def format_timedelta(self, td):
        '''
            Formats a timedelta object to a string displaying minutes & seconds.
        '''

        # find seconds
        total_seconds = int(td.total_seconds())

        # 3600 seconds in an hour
        hours, remainder = divmod(total_seconds, 3600)

        # 60 seconds in a minute
        minutes, seconds = divmod(remainder, 60)

        return ('{} mins {} secs'.format(minutes, seconds))

    def print_summary(self):
        '''
            Prints a summary of the current timer type & time remaining.
        '''

        task_name = 'none'

        # format timer output
        if self.timer_type == self.TIMER_TASK:
            task_name = 'task'
        elif self.timer_type == self.TIMER_SHORT_BREAK:
            task_name = 'short break'
        elif self.timer_type == self.TIMER_LONG_BREAK:
            task_name = 'long break'

        # format time remaining output
        time_remaining = self.format_timedelta(self.get_time_remaining())


def main():

    # create pomodoro & begin first task
    pomodoro = Pomodoro()
    pomodoro.start_task()

    while True:

        # Initialize last_summary variable to 15 seconds in the past
        last_summary = pomodoro.timer_start - timedelta(seconds=15)

        # while the timer is running
        while pomodoro.get_time_remaining() > timedelta(seconds=0):

            current_time = datetime.now()

            # print a summary of the current timer every 15 seconds
            if (current_time - last_summary) > timedelta(seconds=15):
                pomodoro.print_summary()

                # update timer to track when the last summary was printed
                last_summary = current_time

        # if we are on a task, complete the task.  Otherwise, we start the task timer
        if pomodoro.timer_type == Pomodoro.TIMER_TASK:

            # complete the task
            pomodoro.complete_task()

            # check to see if need to continue to a break or stop the pomodoro
            if pomodoro.done():
                break
            elif pomodoro.task_count % pomodoro.long_break_goal == 0:
                pomodoro.start_long_break()
            else:
                pomodoro.start_short_break()
        else:
            pomodoro.start_task()

    # we have met our pomodoro goal
    print('\nPomodoro Complete!')

if __name__ == '__main__':
    main()
