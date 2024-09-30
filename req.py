#trying requests package to bypass logging in

import requests
from bs4 import BeautifulSoup

# response_login_page = requests.get('https://ipgpassport.lenovo.com/cas/login?service=http%3A%2F%2Ftdms.lenovo.com%2Ftdms%2FloginAction%21login.do')
response_welcome_page = requests.get('http://tdms.lenovo.com/tdms/loginAction!login.do')
# response_home_page = requests.get('http://tdms.lenovo.com/tdms/homeAction.action?sysPageId=page_common_home')

soup = BeautifulSoup(response_welcome_page.title, 'html.parser')
print(soup.title.string)