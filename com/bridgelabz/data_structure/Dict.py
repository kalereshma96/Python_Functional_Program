d = {'abc':12,'xyz':23,'pqr':542}
d['ghj']=57
print(d['abc'])
del d['ghj']
print(d)
print(list(d))
print(sorted(d))
print('abc' in d)