import requests, bs4, time, lxml

currentTime = int(time.time())
url = f'http://www.mybustracker.co.uk/update.php?module=BTTimeConsult&updateId=timesResult&ajaxRequestId={currentTime};timesResult'

headers = {
    "Host": "www.mybustracker.co.uk",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0",
    "Accept": "application/xml, text/xml, */*; q=0.01",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Encoding": 'gzip, deflate',
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "187",
    "Origin": "http://www.mybustracker.co.uk",
    "Connection": "keep-alive",
    "Referer": "http://www.mybustracker.co.uk/?module=consult&mode=busStopQuickSearch&busStopCode=36242849",
    "Cookie": "PHPSESSID=m0e3ajo33kbik54hj7t6jqhe53",
    "Priority": "u=0"
}

payload = {
    'mode': '1',
    'openMap': '0',
    'refresh': '1',
    'autoRefreshCheck': '',
    'fullCheck': '',
    'busStopCode': '36242849',
    'busStopDay': '0',
    'journeyId': '0',
    'journeyTimesDetails': '',
    'busStopService': '17',
    'busStopDest': '1146880',
    'nbDeparture': '1',
    'busStopTime': ''
}

res = requests.post(url, data=payload, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="lxml")

# Find the td with class 'service' and inner text '10'
service_td = soup.find('td', class_='service', string='10')

if service_td:
    # Navigate to the next <td> sibling and find the span with class 'mins'
    mins_span = service_td.find_next('td', class_='time').find('span', class_='mins')

    # Get the text inside the span
    mins_text = mins_span.get_text()
    print(f'{mins_text} min')


