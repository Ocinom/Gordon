def stopgo(status : str):
    if status.lower() == 'stop':
        return 'red'
    elif status.lower() == 'go':
        return 'green'

print(stopgo('stop'))
print(stopgo('go'))