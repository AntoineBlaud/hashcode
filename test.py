import tqdm

b=  []
for i in tqdm.tqdm(range(10000)):
    for x in range(10000):
        for y in range(100):
            b.append(x)
    
    
