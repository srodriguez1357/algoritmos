def segundos(seg):
    segu=seg%60
    min=(seg%3600)//60
    hora=seg//3600
    return hora,min,segu
casa=int(input("dato"))
x,y,z=segundos(casa)
print(x,y,z)