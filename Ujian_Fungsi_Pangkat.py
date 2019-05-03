
def pangkat(x,y):
    hasil = x
    for i in range(1,y):
        hasil = hasil * x
    return hasil

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))