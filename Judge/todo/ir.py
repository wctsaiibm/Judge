import sys
from tasks import eval

total = sys.argv[1]

fin = []
fout = []
for i in range(1, int(total)+1):
    fin.append(str(i)+'.in')
    fout.append(str(i)+'.out')

results = [eval.delay(i, o) for i, o in zip(fin, fout)]
correct = 0
for r in results:
    try:
        k = r.get()
    except:
        continue
    if int(k) == 1:
        correct += 1
print str(correct) + ' / ' + str(total)
