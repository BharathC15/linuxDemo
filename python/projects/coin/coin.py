import numpy as np
trials=1000000
found=0
for i in np.arange(trials):
    n=np.sum(np.random.randint(2,size=6))
    if(n==2):
        found+=1
print(found/trials)
