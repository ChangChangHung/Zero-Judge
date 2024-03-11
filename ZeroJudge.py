def get(file):
    with open (file,'r',encoding='utf-8') as r:
        data=r.read().strip().split('\n')
        r.close()
    return data
def write(data):
    with open('span.txt','a',encoding='utf-8') as f:
        minute=f'{data[0][1:]}'
        if 'min' in minute:
            value=minute[:-4]
        f.write(f'{file} ')
        f.write(minute)
        f.write('\n')
    return int(value)

import os
minutes=[]
FileList = os.listdir('./')
for file in FileList:
    if file!='ZeroJudge.py':
        try:
            minutes.append(write(get(file)))
        except:
            pass

import matplotlib.pyplot as plt

print(minutes)
plt.plot(minutes)
plt.savefig('Zero Judge.png')
plt.show()