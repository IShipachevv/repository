import requests

cookies = {
    'qrator_jsr': '1740736090.818.YVxe1Met5NfBQpM5-nhjng7fri4o2nnj6qqeipld70j6n3v0k-00',
    'qrator_jsid': '1740736090.818.YVxe1Met5NfBQpM5-13oa5tnb8q9bqmd8s95d19sojuhvec8t',
    'qrator_ssid': '1740736091.549.ymg6d3TawAhWx7Q2-2gujcjd2nlaqd9h1sqjqkov3bbi2o1su',
    'current_path': '9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D',
    'rr-testCookie': 'testvalue',
    'rrpvid': '392414950046012',
    'lang': 'ru',
    'city_path': 'moscow',
    'ga_tests': 'actions_3',
    'rcuid': '67c1865c8b27431381ab10fa',
    '_ga': 'GA1.1.2066402361.1740736092',
    'tmr_lvid': 'ee8268bf00312d1b5712fdf8ba27f303',
    'tmr_lvidTS': '1740736092505',
    '_ym_uid': '1740736093598755400',
    '_ym_d': '1740736093',
    'rai': '5e54bb7d618269a406fe5aca84dd17d5',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_ymab_param': 'u8w1VHRSdG_qyNy61epvl5ebA84B9DwOqVeT5GI0larlTjnbWCMKjjmYC0WCj1_VsBuv1f4dXpYR4KQc64O70FB_YQ4',
    'domain_sid': 'XGIucb7sG-4EABl2U12br%3A1740736093856',
    '_ga_FLS4JETDHW': 'GS1.1.1740736092.1.0.1740736094.58.0.462907560',
    'chatNewMessage': '0',
    'tmr_detect': '0%7C1740736095196',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-US;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': 'qrator_jsr=1740736090.818.YVxe1Met5NfBQpM5-nhjng7fri4o2nnj6qqeipld70j6n3v0k-00; qrator_jsid=1740736090.818.YVxe1Met5NfBQpM5-13oa5tnb8q9bqmd8s95d19sojuhvec8t; qrator_ssid=1740736091.549.ymg6d3TawAhWx7Q2-2gujcjd2nlaqd9h1sqjqkov3bbi2o1su; current_path=9565a5103f36ecea17597b8bfe0de40efdc12ecd83502fc6a8abccb573ee963ba%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A116%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22default%22%7D%22%3B%7D; rr-testCookie=testvalue; rrpvid=392414950046012; lang=ru; city_path=moscow; ga_tests=actions_3; rcuid=67c1865c8b27431381ab10fa; _ga=GA1.1.2066402361.1740736092; tmr_lvid=ee8268bf00312d1b5712fdf8ba27f303; tmr_lvidTS=1740736092505; _ym_uid=1740736093598755400; _ym_d=1740736093; rai=5e54bb7d618269a406fe5aca84dd17d5; _ym_isad=2; _ym_visorc=b; _ymab_param=u8w1VHRSdG_qyNy61epvl5ebA84B9DwOqVeT5GI0larlTjnbWCMKjjmYC0WCj1_VsBuv1f4dXpYR4KQc64O70FB_YQ4; domain_sid=XGIucb7sG-4EABl2U12br%3A1740736093856; _ga_FLS4JETDHW=GS1.1.1740736092.1.0.1740736094.58.0.462907560; chatNewMessage=0; tmr_detect=0%7C1740736095196',
}

params = {
    'utm_medium': 'organic',
    'utm_source': 'google',
    'utm_referrer': 'https://www.google.com/',
}

response = requests.get('https://www.dns-shop.ru/', params=params, cookies=cookies, headers=headers)

with open("result.html", "w") as file:
    file.write(response.text)

