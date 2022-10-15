import requests
from bs4 import BeautifulSoup
import config
import lxml
from backend.models import Working_Sites


def update_sites_attrs():
    site_urls = Working_Sites.objects.values_list('url')
    for urls in site_urls:
        obj = Working_Sites.objects.get(url = urls[0])
        response = requests.get(urls[0])
        soup = BeautifulSoup(response.text, features='lxml')
        #contact = soup.find_all('p', {'class':'person-phone'})[0]
        try:
            for contact in soup.find_all('p', {'class':'person-phone'}):
                number = contact.find('span', {'class':'right'}).span.text.strip()
                if '@' in number:
                    continue
                else:
                    obj.contact = number
                    break
            adrs = soup.find('p', {'id': 'court_address'}).text.strip()
            obj.adress = adrs
            obj.save()
        except:
            continue

update_sites_attrs()