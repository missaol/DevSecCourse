list = ['forteen', 'fifteen', 16, 'seventeen']
for item in list:
    try:
        msg = 'processing' + item
        print(msg)
        continue
    except TypeError:
        print('something went wrong!')
        break
    finally:
        print('finally block')
    print('next item please!')
