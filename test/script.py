import os

f1 = open('codes.txt', 'w+')

r = 2
for i in os.listdir('test_3'):
    f1.write(i[:len(i)-4]+'\n')
    f2 = os.path.join('test_3', i)
    f3 = os.path.join('test_3', 'image'+str(r)+'.png')
    r += 1
    os.rename(f2, f3)
    
f1.close()
