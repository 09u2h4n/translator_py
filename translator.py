class Translater(object):
    
    def __init__(self, proxies=None):
        if proxies is not None:
           self.proxies = proxies
        else:
            self.proxies = None

    def translate(self, txt="", src="auto", dest="en"):
        import requests
        from urllib import parse
        from lxml.html import fromstring

        parsed_txt = parse.quote(txt)
        url = f"https://translate.google.com/m?sl={src}&tl={dest}&q={parsed_txt}"

        response = requests.get(url, proxies=self.proxies)

        data = fromstring(response.text).find_class("result-container")

        for translated_text in data:
            if translated_text.text is None:
                return ""
            else:
                return translated_text.text
