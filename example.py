from requet import Requet, Log

req		= Requet(True, 'www.google.com')

req.requet('/',
	headers={
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'DNT': '1',
		'Pragma': 'no-cache',
		'Upgrade-Insecure-Requests': '1',
	}
)

# Desactive le mode debug
req.debug = False
req.requet('/',
	headers={
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		'DNT': '1',
		'Pragma': 'no-cache',
		'Upgrade-Insecure-Requests': '1',
	}
)

google		 = Requet(True, 'www.google.com')
google.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'

google.requet('/post.html',
	method='post',
	headers={
		'Authaurization': 'Bearer blabla',
		'Content-Type': 'application/x-www-form-urlencoded'
	},
	body='field1=value1&field2=value2'
)
