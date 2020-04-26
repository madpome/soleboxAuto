from requet import Requet, Log
import urllib.parse
title = 'mr'
#please replace with a new mail adress if you want to create a new account (this is a temporary email 
# and may not work anymore by the time you read this)
mail = 'kojayo7649@lagsixtome.com'
login =urllib.parse.quote(mail)
mdp = urllib.parse.quote(mail)
name = 'tata'
surname = 'toto'
req = Requet(True, "www.solebox.com", vhttp="1.1")
req.debug = False

req.useragent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'
head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.solebox.com/en',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'TE': 'Trailers',
    } 
###Requete qui n'a pas l'air d'être utile pour set les cookies et autres
"""
reponse = req.requet("/", 
    headers = head
)"""
###Etrangement, si je donne des headers ici il n'en veut pas et me provoque une erreur mais marche bien sans ...
reponse = req.requet("/en_FR/login")
#find the index of the csrf_token
#find between 375k and 385k seems okay? it's just a guess, may want to change that later
find = reponse.find('<input type="hidden" name="csrf_token" value=', 375000,385000)
csrf_token = ""
car = "1"
i = 0
#finding the actual csrf_token
while reponse[find+i+46]!='"':
    csrf_token+=reponse[find+i+46]
    i+=1
csrf_token = urllib.parse.quote(csrf_token)

#Création du compte
bod= 'dwfrm_profile_register_title={}&dwfrm_profile_register_firstName={}&dwfrm_profile_register_lastName={}&dwfrm_profile_register_email={}&dwfrm_profile_register_emailConfirm={}&dwfrm_profile_register_password={}&dwfrm_profile_register_passwordConfirm={}&dwfrm_profile_register_phone=&dwfrm_profile_register_birthday=&dwfrm_profile_register_acceptPolicy=true&csrf_token={}'.format(title,name,surname,login,login,mdp,mdp,csrf_token)
head = {}
head['Referer']= 'https://www.solebox.com/en_FR/registration?rurl=1'
head['Connection']='keep-alive'
head['Accept']='application/json, text/javascript, */*; q=0.01'
head['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
head['X-Requested'] = 'X-Requested-With: XMLHttpRequest'
head['Origin'] ='https://www.solebox.com'
reponse = req.requet('/on/demandware.store/Sites-solebox-Site/en_FR/Account-SubmitRegistration?rurl=1&format=ajax',
    method ="POST",
    body = bod,
    headers = head
)
#Connexion au compte
head['Referer']='https://www.solebox.com/en_FR/login'
head['X-Requested-With'] ='XMLHttpRequest'
bod = 'dwfrm_profile_customer_email={}&dwfrm_profile_login_password={}&csrf_token={}'.format(login,mdp,csrf_token)
reponse = req.requet('/en_FR/authentication?rurl=1&format=ajax', method= 'POST', body = bod, headers = head)

#Ajout d'une sneakers au panier
#choix de la sneakers https://www.solebox.com/en_FR/p/mizuno-gv87_futur-white-01871277.html taille 44.5
head['Referer'] ='https://www.solebox.com/en_FR/…gv87_futur-white-01871277.html'
bod = 'pid=0187127700000007&options=%5B%7B%22optionId%22%3A%22212%22%2C%22selectedValueId%22%3A%2244.5%22%7D%5D&quantity=1'
reponse = req.requet('/en_FR/add-product?format=ajax', method ='POST', body = bod, headers = head)
