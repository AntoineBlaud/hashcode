years = [x for x in range(2014,2020)]
levels = ["q","f"]

import random

year = random.choice(years)
level = random.choice(levels)

print("Subject: %s-%s"%(year,level))