# translator_py
This module translating between 2 languages

## Translating usage
```python
>>> from translator import Translater
>>> t = Translater()
>>> t.translate(txt="Hello, i'm translater", src="auto", dest="tr") 
'merhaba ben tercüman'
```

## Using proxy
```python
>>> from translator import Translater
>>> proxy = {"http":"http://sampleproxy.com:80"}
>>> t = Translater(proxies=proxy)
```

## TODO
Code will be optimized
Get languages and other methods will be added
