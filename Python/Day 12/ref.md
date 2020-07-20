## python
>>> import requests
>>> url = "https://www.boxofficemojo.com/year/world/?ref_=bo_nb_di_tab"
>>> r = requests.get(url)
>>> r.status_code
200
>>> r.text
...
## python -i scrape.py
>>> html_text
...
>>> from requests_html import HTML
>>> r_html = HTML(html=html_text)
>>> r_html
<HTML url='https://example.org/'>
>>> r_html.find("table")
[<Element 'table' class=('a-bordered', 'a-horizontal-stripes', 'a-size-base', 'a-span12', 'mojo-body-table', 'mojo-table-annotated')>]
>>> r_html.find("p")
[<Element 'p' >, <Element 'p' class=('mojo-help-row',)>, <Element 'p' >, <Element 'p' >]
>>> r_html.find("div")
[<Element 'div' id='a-page'>, <Element 'div' class=('a-section', 'a-spacing-none', 'mojo-navigation', 'mojo-header', 'mojo-flex', 'mojo-flex-h')>, <Element 'div' class=('a-section', 'mojo-logo')>, <Element 'div' class=('a-section', 'a-spacing-none', 'mojo-nav-elements', 'mojo-flex', 'mojo-flex-h', 'mojo-flex-1')>, <Element 'div' class=('a-section', 'a-spacing-none', 'mojo-search-bar', 'mojo-flex', 'mojo-flex-h')>, <Element 'div' class=('a-section', 'a-spacing-none', 'mojo-search')>, <Element 'div' class=('a-section', 'a-spacing-none', 'mojo-mobile-options')>,

## inspect (ctrl+shift+i) ...web
## classes
python -i scrape.py
[<Element 'div' id='table' class=('a-section', 'imdb-scroll-table', 'mojo-gutter')>]
>>> 

# python -m pip install pandas ~~python3~~
* csv files
* this tutorial is to save files

## python scrape.py 2005 5  
* this is passing start n duration

# pip install requests-html

# python scrape.py 2020 30