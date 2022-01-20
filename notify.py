import os
import requests
import urllib.request

current_ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
past_ip = open("./last_ip.txt", 'r').read().strip()

if current_ip != past_ip:

	r = requests.post('https://maker.ifttt.com/trigger/server_ip_address_change/with/key/dNTTJmpYA-7GNdeoo_xCLoMQjdx9w5xd5Xdy2ohHHAv', data={'value1': current_ip})
	open("./last_ip.txt", 'w').write(current_ip)

