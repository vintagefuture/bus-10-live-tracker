import requests, bs4, time, lxml

currentTime = int(time.time())
url = 'http://www.mybustracker.co.uk/?module=consult&mode=busStopQuickSearch&busStopCode=36242849'

while True:
    res = requests.post(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="lxml")

    service_td = soup.find('td', class_='service', string='10')
    mins_span = service_td.find_next('td', class_='time').find('span', class_='mins')
    mins_text = mins_span.get_text()
    print(f'{mins_text} min')
    time.sleep(30)