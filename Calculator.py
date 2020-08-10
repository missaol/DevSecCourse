while True:
    username = input ('What is your username?') 
    if username != 'admin':
        continue
    password = input ('What is your password?')
    if password == 'topsecret':
        break
print ('Authorised')
