import requests
import config
from bs4 import BeautifulSoup
import lxml
from backend.models import Working_Sites


#topshiriqni uzi, qoshimcha bonus uchun update_backend.py file da

MAIN_URL = 'https://sudrf.ru/index.php?id=300&act=go_ms_search&searchtype=ms&var=true&ms_type=ms&court_subj=0'


def check_sites(url)->bool:
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return True
        return False
    except:
        return False


def parse_working_sites(url = MAIN_URL):
    response = requests.get(url = url, verify=False)
    soup = BeautifulSoup(response.text, features='lxml')
    a_tags = soup.find_all('a', {'style':'cursor:pointer; cursor:hand;'})
    for a in a_tags:
        sites_title = a.text.strip()
        div_tag = a.next_sibling.next_sibling
        sites_url = div_tag.find('a', {'target':'_blank'}).attrs['href'].strip()
        if not check_sites(sites_url):
            continue
        else:
            # print(sites_title, sites_url) tekshirish uchun ishlab turgan saytlar
            try:
                obj, bol = Working_Sites.objects.get_or_create(url = sites_url)
                if bol == True:
                    obj.title = sites_title
                    obj.save()
                else:
                    continue
            except:
                continue


parse_working_sites()