#2 min
while True:
    try:
        print(f'hello, {input()}')
    except EOFError:
        break