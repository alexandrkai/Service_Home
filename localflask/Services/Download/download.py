import random,logging
import requests as requests

logger = logging.getLogger(__name__)
headers=[
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux; rv:74.0) Gecko/20100101 Firefox/74.0'},
            {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko'},
            {'User-Agent': 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'},
            {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'}
        ]


class Download():
    @staticmethod
    def getBrowsersHeaders():
        return random.choices(headers)[0]

    @staticmethod  # загрузка контента с использованием прокси, заголовков популярных браузеров
    def getContentFromUrl(url, proxies=None, isheaders=False):
        logger.info(f"Получение данных с адреса {url}")
        content, headers = None, None
        if isheaders:
            headers = Download.getBrowsersHeaders()
        try:
            if headers is None and proxies is None:
                response = requests.get(url)
            if proxies == None and not headers is None:
                response = requests.get(url, headers=headers)
            elif not headers is None and not proxies is None:
                response = requests.get(url, proxies=proxies, headers=Download.getBrowsersHeaders())
            if response.status_code == 200:
                content = response.text
        except:
            logger.error(f"Не удалось загрузить страницу с {url} c прокси {proxies} c заголовком {headers}")
        return content


if __name__ == "__main__":
    url = 'https://hidemy.name/ru/proxy-list/?maxtime=1000&anon=34#list'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    for head in headers:
        response = requests.get(url, headers=head)
        if response.status_code==200:
            print('хорошо')
            print(head)
        else:
            print('хорошо')
            print(head)

