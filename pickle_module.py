import pickle

# lst = ['BMW', 'Audi', 'Ferrari', 'Harryti Tuzuki']
# file = 'mypkl.pkl'
# fileobj = open(file, 'wb')
# pickle.dump(lst, fileobj)
# fileobj.close()


file = 'mypkl.pkl'
fileobj = open(file, 'rb')
crs = pickle.load(fileobj)
print(crs)  # output: ['BMW', 'Audi', 'Ferrari', 'Harryti Tuzuki']


# Ckeck for pickle.loads ?
