# aggregator.

import requests
from bs4 import BeautifulSoup

from summarizer import summarize


class Aggregator:
    '''
    Parse contents and summarize text.
    '''
    def __init__(
        self,
        source_name: str,
        ) -> None:

        source_dic = {
            'TheVerge': 'https://www.theverge.com/tech',
            'TechChurch': 'https://techcrunch.com/',
            'WIRED': 'https://www.wired.com/',
            'BuzzFeed': 'https://www.buzzfeed.com/tech'
        }

        if source_name not in source_dic.keys():
            raise ValueError('Source Name must be chosen from TheVerge, TechChurch, WIRED, or BuzzFeed.')
        self.source_name = source_name
        self.source = source_dic[source_name]
        self.elements = []
        self.titles = []
        self.urls = []

    
    def parse_contents(self) -> None:
        '''
        Parse titles and urls of 6 articles
        '''
        r = requests.get(self.source)
        if r.status_code != 200:
            raise ValueError('The status_code of the request is {}'.format(r.status_code))
        soup = BeautifulSoup(r.content, 'html.parser')

        if self.source_name == 'TheVerge':
            self.elements = soup.find_all('a', attrs={"data-analytics-link": "article"})
            for i in range(min(len(self.elements), 6)):
                self.titles.append(self.elements[i].text)
                self.urls.append(self.elements[i].get('href'))

        elif self.source_name == 'TechChurch':
            self.elements = soup.find_all('a', attrs={"class": "post-block__title__link"})
            for i in range(min(len(self.elements), 6)):
                self.titles.append(self.elements[i].text.replace('\n','').replace('\t',''))
                self.urls.append(self.elements[i].get('href'))

        elif self.source_name == 'WIRED':
            elements1 = soup.find_all('a', attrs={"class": "SummaryItemHedLink-cgPsOZ cEGVhT summary-item-tracking__hed-link summary-item__hed-link"})
            elements2 = soup.find_all('a', attrs={"class": "SummaryItemHedLink-cgPsOZ cnoEIb summary-item-tracking__hed-link summary-item__hed-link"})
            for i in range(min(3, len(elements1))):
                self.elements.append(elements1[i])
            for i in range(min(3, len(elements2))):
                self.elements.append(elements2[i])
            self.elements = list(set(self.elements))
            for i in range(len(self.elements)):
                self.titles.append(self.elements[i].text)
                self.urls.append('https://www.wired.com' + self.elements[i].get('href'))

        elif self.source_name == 'BuzzFeed':
            self.elements = soup.find_all('a', attrs={"class": "js-card__link link-gray"})
            for i in range(min(len(self.elements), 6)):
                self.titles.append(self.elements[i].text)
                self.urls.append(self.elements[i].get('href'))


    def summarize_text(
        self,
        url: str,
        n_sentence = 2,
        ) -> str:
        '''
        Given the url of an article, Returns a summary.
        '''
        r = requests.get(url)
        if r.status_code != 200:
            raise ValueError('The status_code of the request is {}'.format(r.status_code))
        soup = BeautifulSoup(r.content, 'html.parser')
        txt = ''

        if self.source_name == 'TheVerge':
            for e in soup.find_all('p', id=True, attrs={'class':''}):
                txt += e.text
                txt += ' '
        elif self.source_name == 'TechChurch':
            for e in soup.find_all('p', attrs={'class':''}):
                txt += e.text
                txt += ' '
        elif self.source_name == 'WIRED':
            for e in soup.find_all('p',attrs={"class":"paywall"}):
                txt += e.text
                txt += ' '
        elif self.source_name == 'BuzzFeed':
            for e in soup.find_all('p', attrs={"class": ""}):
                txt += e.text
                txt += ' '

        summary = summarize(txt, n_sentence)
        
        summary = summary.replace('$','\$')
        
        return summary


