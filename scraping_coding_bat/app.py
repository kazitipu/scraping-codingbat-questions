from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


user_agent=UserAgent()

url='https://codingbat.com/java'
base_url='https://codingbat.com'

page= requests.get(url, headers={'user-agent':user_agent.chrome})
soup=BeautifulSoup(page.content, 'lxml')

all_divs=soup.find_all('div', attrs={'class':'summ'})

inner_link=[base_url+div.a['href'] for div in all_divs]
for link in inner_link:
    inner_page=requests.get(link, headers={'user-agent':user_agent.chrome})
    inner_soup=BeautifulSoup(inner_page.content, 'lxml')
    inner_div= inner_soup.find('div', class_='tabin')

    qs_link=[base_url+td.a['href'] for td in inner_div.table.find_all('td')]
    for link in qs_link:
        final_page=requests.get(link, headers={'user-agent':user_agent.chrome})
        final_soup=BeautifulSoup(final_page.content, 'lxml')
        indent_div=final_soup.find('div', class_='indent')
        print(indent_div.table.div.p.string)
        examples= indent_div.table.div.next_siblings
        for example in examples:
            if example.string is not None:
                print(example)

        print('\n\n\n')
       
