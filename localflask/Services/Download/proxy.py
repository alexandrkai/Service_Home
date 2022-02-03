from Services.Download.download import Download
from lxml import html

# url для определения ip-адресов
# http://ip-address.ru/, https://yandex.ru/internet
#
URLCheckIPAdress = "https://yandex.ru/internet/"
URLProxiList = "https://hidemy.name/ru/proxy-list/?maxtime=1000&type=hs&anon=34#list"


class Proxy():
    def __init__(self, address, port, country, type):
        self.address = address
        self.port = port
        self.type = type
        self.country = country

    @staticmethod
    def getCurrentIPAddress(proxies=None):
        result = None
        content = Download.getContentFromUrl(URLCheckIPAdress, proxies)
        if not content is None:
            tree = html.fromstring(content)
            lis = tree.xpath("//li[@class='parameter-wrapper general-info__parameter']")
            if len(lis) > 0:
                div = lis[0].xpath(".//div")
                if len(div) > 0:
                    return div[1].text
        return result

    @staticmethod
    def getListProxies():  # получение списка прокси серверов
        result = list()
        content = Download.getContentFromUrl(URLProxiList, None, True)
        # with open('proxies.html', 'r', encoding='utf-8') as file:
        #     content = file.read()
        if not content is None:
            tree = html.fromstring(content)
            trs = tree.xpath("//div[@class='table_block']//table//tr")
            if len(trs) > 0:
                for i in range(1, len(trs)):
                    tds = trs[i].xpath(".//td")
                    address = tds[0].text
                    port = tds[1].text
                    country = tds[2].xpath(".//span[@class='country']")
                    if len(country) > 0:
                        country = country[0].text
                    type = None
                    types = tds[4].text.lower().split(',')
                    if len(types) > 1:
                        if 'https' in types:
                            type = 'https'
                        elif 'socks5' in types:
                            type = 'socks5'
                    else:
                        type = types[0]
                    result.append(Proxy(address, port, country, type))
            result = Proxy.checkList(result)
        return result

    def checkList(listiap):
        result = list()
        curripaddress = Proxy.getCurrentIPAddress()
        for proxy in listiap:
            if proxy.type in ['http', 'https']:
                proxies = {proxy.type: 'http://' + proxy.address}
                address = Proxy.getCurrentIPAddress(proxies)
                if curripaddress != address:
                    result.append(proxy)
        return result


if __name__ == "__main__":
    res = Proxy.getListProxies()
    print(res)
    pass
