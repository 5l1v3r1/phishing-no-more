import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
num = string.ascii_letters + string.digits + '1234567890'
email = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com']
rp_type = ['Elite Royale Pass', 'Free Royale Pass']

random.seed = (os.urandom(1024))

url = 'https://selamatkamudapathadiahdaripubglite.000webhostapp.com/completed.php'

names = json.loads(open('nama.json').read())
jumlah = len(names)
kira = 0
for name in names:
	name_baru = ''.join(random.choice(string.digits))
	username = name.lower() + name_baru + random.choice(email)
	password = name + ''.join(random.choice(chars) for i in range(2)) + ''.join(random.choice(num) for i in range(2))
	char_lvl = 'Level ' + str(random.randint(1,100))
	rp_t = random.choice(rp_type)
	rp_lvl = 'Level ' + str(random.randint(1,100))
	
	requests.post(url, data={
		'email': username,
		'pass': password,
		'login': "FACEBOOK",
		'clv': char_lvl,
		'rpt': rp_t,
		'rpl': rp_lvl
		})
	kira = kira + 1
	lebih = jumlah - kira
	print('Sent ' + str(kira))	
	print('Left ' + str(lebih))	
	print(' Username : %s \n Password : %s \n Character %s \n %s \n Royale Pass %s \n' % (username, password, char_lvl, rp_t, rp_lvl))