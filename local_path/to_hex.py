a = ''
while a != 'quit': 
    try:
        a = input()
        print(a.encode().hex())
    except:
        break