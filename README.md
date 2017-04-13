# batch-iterator
Usefull python implementation of batch iterator. 

# limitations
can only iterate on numpy arrays(or on the objects, convertable to them)

# requirements
numpy

# usage
```python
x = np.arange(10)
y = np.arange(10,20)
z = np.arange(10*10).reshape((10,-1))

for x_b,y_b,z_b in iterate_minibatches(x,y,z, batchsize=2):
    print("batch :")
    print(x_b, y_b, z_b)
```

returns:
batch :
[0 1] [10 11] [[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]]
batch :
[2 3] [12 13] [[20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]]
batch :
[4 5] [14 15] [[40 41 42 43 44 45 46 47 48 49]
 [50 51 52 53 54 55 56 57 58 59]]
batch :
[6 7] [16 17] [[60 61 62 63 64 65 66 67 68 69]
 [70 71 72 73 74 75 76 77 78 79]]
batch :
[8 9] [18 19] [[80 81 82 83 84 85 86 87 88 89]
 [90 91 92 93 94 95 96 97 98 99]]
