moves=2
row=int(input('Number of Rows: '))
col=int(input('Number of Cols: '))

print('Finding combination of total moves required...')

cells=row*col

def factors(x):
    f=1
    for i in range(1,int(x)+1):
        f*=i
    return f
comb=factors(cells)/(2*factors(cells-moves))
print(round(comb))
