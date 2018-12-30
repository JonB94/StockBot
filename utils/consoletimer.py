from __future__ import with_statement
import time


class ConsoleTimer(object):
    """
    Adds timer output to console.
    """

    def __init__(self, taskname: str):
        """Init function
        
        Arguments:
            taskname {str} -- The name or description of the task being performed.
        """
        self.taskname = taskname
        self.starttime = time.time()

    def __enter__(self):
        """
        Outputs at the start of the task.
        """
        print('>> Starting task "%s"...' % self.taskname)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Outputs at the end of the task.
        """
        timetake = time.time() - self.starttime
        print('<< Finished task "%s" in %s seconds...' % (self.taskname, str(timetake)))

    def get_timetake(self):
        """Gets the time that a task took.
        
        Returns:
            float -- the total time that the task took to complete
        """

        return time.time() - self.starttime
