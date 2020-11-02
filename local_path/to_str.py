a = ''
while a != 'quit': 
    try:
        a = input()
        print(bytearray.fromhex(a).decode())
    except:
        break