import requests
from bs4 import BeautifulSoup
import csv
import time


#returns link to next page, or END if last page
def getUrl(soup_var):
    link_inner = soup_var.findAll('a', class_='_1li8g8e')
    for i in range(len(link_inner)):
        if (link_inner[i]['aria-label'] == 'Next'):
            link = 'https://www.airbnb.com' + link_inner[i]['href']
            return(link)
    return('END')

#Removes non-ascii chars -- converts to ascii, then decodes to remove added chars  
def decodeText(text):
    text = text.encode('ascii', errors='ignore')
    text = text.decode(encoding='UTF-8',errors='ignore')
    return text

#----------------------------------------------------------------------------------------------------

#csv entering
file = csv.writer(open('rooms.csv', 'a', newline=''))
file.writerow(['city','title', 'location', 'rating','room_type','price','guests','beds','bathrooms']) 

#starting params
URL = 'https://www.airbnb.com/s/Miami--FL--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=search_query&query=Miami%2C%20FL&place_id=ChIJEcHIDqKw2YgRZU-t3XHylv8'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
print()

while getUrl(soup) != 'END':
    URL = getUrl(soup)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')

    results = soup.find("div", {"class": "_fhph4u"})
    rooms = results.find_all('div', class_='_8ssblpx')

    for room in rooms:
        #scrape each data piece
        title_elem = room.find('div', class_='_1c2n35az')
        location_type_elem = room.find('div', class_='_167qordg')
        rating_elem = room.find('span', class_='_10fy1f8')
        price_elem_str = room.find('span', class_='_1p7iugi')
        details_elem_str = room.find('div', class_='_kqh46o')

        if None in (title_elem, location_type_elem, price_elem_str,rating_elem, details_elem_str):
            continue

        #splitting necessary data from strings
        loc_type_list = location_type_elem.text.split(" in ")
        location_elem = loc_type_list[1]
        type_elem = loc_type_list[0]
        price_elem = price_elem_str.text.split(":$")[1]
        details_elem = details_elem_str.text.split(" · ")
        guests = details_elem[0].split()[0] #get first value (number) of the first split
        bedrooms = details_elem[1].split()[0]
        beds = details_elem[2].split()[0]
        #bathroom tag is optional -- test that it exists
        if(len(details_elem) > 3):
            bathrooms = details_elem[3].split()[0]

        #write to file
        file.writerow(['MIA',decodeText(title_elem.text.strip()),decodeText(location_elem),decodeText(rating_elem.text.strip()),decodeText((type_elem)),price_elem,guests,beds,bathrooms])
print(getUrl(soup))