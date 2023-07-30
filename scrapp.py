from bs4 import BeautifulSoup
import requests



def scrapp(name):


    url = f'https://en.wikipedia.org/wiki/{name}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table', class_='infobox')
    heading = soup.find(id="firstHeading")
    
    data = {}
    data["Name"] = heading.text.strip()
    
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header:
                key = header.text.strip()
                values = []
                cells = row.find_all('td')
                for cell in cells:
                    value = cell.text.strip()
                    if value:
                        values.append(value)
                if values:
                    if len(values) == 1:
                        data[key] = values[0]
                    else:
                        data[key] = values





    return data