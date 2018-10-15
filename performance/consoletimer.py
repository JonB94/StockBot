from __future__ import with_statement
import time


class consoletimer(object):


    def __init__(self, taskname):
        self.taskname = taskname
        self.starttime = time.time()


    def __enter__(self):
        print('>> Starting task "%s"...' % self.taskname)
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        timetake = time.time() - self.starttime
        print('<< Finished task "%s" in %s seconds...' % (self.taskname, str(timetake)))


    def get_timetake(self):
        return time.time() - self.starttime
