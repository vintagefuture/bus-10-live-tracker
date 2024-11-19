import requests, bs4, time
from microdotphat import write_string, show, clear

currentTime = int(time.time())
url = 'http://www.mybustracker.co.uk/?module=consult&mode=busStopQuickSearch&busStopCode=36242849'

while True:
    clear()
    
    try:
        res = requests.post(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        service_td = soup.find('td', class_='service', string='10')
        dest_td = service_td.find_next('td', class_='dest', string='Bonaly')
        mins_span = dest_td.find_next('td', class_='time').find('span', class_='mins')
        mins_text = mins_span.get_text()
        print(f'{mins_text} min')
        if mins_text != 'DUE':
            write_string(f'{mins_text} min', kerning=False)
        else:
            write_string(mins_text, kerning=False)
        show()
    except Exception as e:
        clear()
        print("ERROR", e)
        write_string('ERROR', kerning=False)
        show()
    
    time.sleep(30)
