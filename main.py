# This password generator is prsent thanks to python.hub and my boyfriend

import random
lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '!@#%^&*()-_=+[]{}?'

whole_password = lower + upper + numbers + symbols
length = 10
password = ''.join(random.sample(whole_password, length))
print(password)