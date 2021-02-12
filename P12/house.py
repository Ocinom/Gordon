class house():

    house_type = 'dwelling'
    location = 'terrestrial'

    def __init__(self, name, material, size, storeys):
        self.name = name
        self.material = material
        self.size = size
        self.storeys = storeys

    def get_mat(self):
        return self.material

    def get_size(self):
        return self.size

    def get_storeys(self):
        return self.storeys

small = house('small', 'wood', 500 , 2)
big = house('big', 'brick', 10000, 3)

print(small.get_mat())
print(small.get_size(), 'sq. metres')
print(small.get_storeys(), 'storeys')

print(big.get_mat())
print(big.get_size(), 'sq. metres')
print(big.get_storeys(), 'storeys')