import random

def calculateSellingPrice(costPrice: float):
    sellingPrice = 2 * costPrice
    print('Cost Price: $%.2f' % costPrice)
    print('Selling Price: $%.2f' % sellingPrice)

for i in range(4):
    testPrice = random.randint(1000, 10000) / 100
    calculateSellingPrice(testPrice)