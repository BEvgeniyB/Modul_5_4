class Building:
    total = 0

    def __init__(self):
        self.number= self.change_total(1)
    def __str__(self):
        return str(f'Здание № {self.number}')

    def __del__(self):
        #print(f'Снесли  {str(self)}')
        Building.total -= 1
    def change_total(self,num):
        Building.total += num
        return Building.total
building = []
for i in range(1,41):

    building.append(Building())
print(f'Сносим  {building[3]}')
del building[3]
print(Building.total)
print(*building)

