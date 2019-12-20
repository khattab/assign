import random
import time
from datetime import datetime


class GenerateDateTime(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        # print(self.GenRandomDate(start="20-01-2018 13:30:00", end="23-01-2018 04:50:34"))

    def GenRandomDate(self, start, end):
        frmt = '%d-%m-%Y %H:%M:%S'

        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))

        ptime = stime + random.random() * (etime - stime)
        dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
        return dt


g = GenerateDateTime(start='', end='')
r = g.GenRandomDate(start="30-10-2019 13:30:00", end="20-10-2019 04:50:34")
print(r)