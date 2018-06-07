# pyphen-online-hyphenator

http server for hyphenation using [pyphen](http://pyphen.org/)

## API

Only one route requiring following URL params:
- lang: language
- alter: string for marking soft hyphen
- content: URL-encoded string to be hyphenated

Example - for czech lang:

```
localhost:5000/?lang=cs&alter=%26phy%3B&content=Společnost%20E.ON%20dělá%20kampaň
```

Running heroku instance is on:

```
https://pyphen-online-hyphenator.herokuapp.com/?lang=cs&alter=%26phy%3B&content=Společnost%20E.ON%20dělá%20kampaň
```
