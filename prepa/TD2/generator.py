
import random

done = set()
array = [str(random.randint(0,1000)) for _ in range(200)]
couple = []
#m = random.randint(0,len(array)/2)
m = 50
for i in range(m):

    s= False
    while(not s):
        a = random.randint(0,len(array)-1)
        b = random.randint(0,len(array)-1)
        if(a not in done and b not in done):
            done.add(a);done.add(b);couple.append((a,b))
            s = True


with open("C:/Users/antoi/Documents/GitHub/hashcode/prepa/TD2/Balance/3.in",'w') as f:
    f.write(str(len(array))+ " "+str(m)+"\n")
    couple = list(map(lambda x:str(x[0])+" "+str(x[1]),couple))
    f.write(' '.join(couple)+"\n")
    f.write(' '.join(array)+"\n")
