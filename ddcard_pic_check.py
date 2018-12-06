import requests 
from bs4 import BeautifulSoup
import re
url='https://www.dcard.tw/f'
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
html_doc = requests.get(url,headers=header)
resp = html_doc.text
soup = BeautifulSoup(resp,'lxml')
html_doc.status_code

man = """<div class="AnonymousAvatar_female_swqLg"></div>"""
woman = """<div class="AnonymousAvatar_male_3mpl_"></div>"""
sman = """<div class="InitialAvatar_initial_15lap InitialAvatar_F_1wnuz">(\w+)</div>"""
swoman = """<div class="InitialAvatar_initial_15lap InitialAvatar_M_AsssI">(\w+)</div>"""
for i in post2:
    print(str(i['class']))
    print(str(i))
    if re.match(woman,str(i)) :
        print('女')
    elif re.match(man,str(i)):
        print('男')
    elif re.match(swoman,str(i)):
        print('板塊女')
    elif re.match(sman,str(i)):
        print('板塊男')
    else:
        print('贊助者')
		
		
#['AnonymousAvatar_female_swqLg']
#<div class="AnonymousAvatar_female_swqLg"></div>
#男
#-----------------重點----------小坑--------------
#['InitialAvatar_initial_15lap', 'InitialAvatar_F_1wnuz']
#<div class="InitialAvatar_initial_15lap InitialAvatar_F_1wnuz">C</div>
#板塊男
#----------------------------------------------------
#['AnonymousAvatar_male_3mpl_']
#<div class="AnonymousAvatar_male_3mpl_"></div>
#女
#['AnonymousAvatar_male_3mpl_']
#<div class="AnonymousAvatar_male_3mpl_"></div>
#女
#['AnonymousAvatar_male_3mpl_']
#<div class="AnonymousAvatar_male_3mpl_"></div>
#女
#['InitialAvatar_initial_15lap', 'InitialAvatar_D_2yS7h']
#<div class="InitialAvatar_initial_15lap InitialAvatar_D_2yS7h">D</div>
#贊助者
