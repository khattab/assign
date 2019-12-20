from netaddr import *
import random
from datetime import *
import time


def random_date(data):
    random.seed(data)
    d = random.randint(1, int(time.time()))
    return datetime.fromtimestamp(d).strftime('%Y-%m-%d')

# print((random_date("2019-30-09 12:05:50")))

count = 0
kavicF = open("kav.txt", "w+")
for ip in IPNetwork('192.0.0.0/12'):
    count += 1
    print("No. %s is %s" % (count, ip))
    kavicF.write("No. %s is %s %s \n" % (count, ip))
