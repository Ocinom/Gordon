hours = float(input('Type hours with a decimal point: '))
minutes = hours % 1 * 60
seconds = minutes % 1 * 60

print('hours: %d\nminutes: %d\nseconds: %d' % (int(hours), int(minutes), int(seconds)))
