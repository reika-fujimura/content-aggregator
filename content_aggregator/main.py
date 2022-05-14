# Tech News Aggregator streamlit app
# To run the app, type "streamlit run main.py" on terminal.

import streamlit as st
import spacy

from aggregator import Aggregator

spacy.cli.download("en_core_web_sm")

sources = ['TheVerge', 'TechChurch', 'WIRED', 'BuzzFeed']
source_dic = {
    'TheVerge': 'https://www.theverge.com/tech',
    'TechChurch': 'https://techcrunch.com/',
    'WIRED': 'https://www.wired.com/',
    'BuzzFeed': 'https://www.buzzfeed.com/tech'
}

# header
st.title('Tech News Aggregator')
# st.image('images/image.jpg')    
htp = 'https://raw.githubusercontent.com/reika-fujimura/content-aggregator/main/content_aggregator/images/image.jpg'
st.image(htp)

# aggregators
col1, col2 = st.columns(2)

for i in range(len(sources) // 2):
    col1.header('['+sources[i]+'](%s)' % source_dic[sources[i]])
    c = col1.container()
    agg = Aggregator(sources[i])
    agg.parse_contents()
    for j in range(len(agg.titles)):
        txt = agg.summarize_text(agg.urls[j],n_sentence = 1)
        print(i,j,txt)
        if not txt:
            print(i,j)
            continue
        c.write('**'+agg.titles[j] + '** ' + '([link](%s))' % agg.urls[j])
        c.write(txt)

for i in range(len(sources) // 2, len(sources)):
    col2.header('['+sources[i]+'](%s)' % source_dic[sources[i]])
    c = col2.container()
    agg = Aggregator(sources[i])
    agg.parse_contents()
    for j in range(len(agg.titles)):
        txt = agg.summarize_text(agg.urls[j],n_sentence = 1)
        print(i,j,txt)
        if not txt:
            print(i,j)
            continue
        c.write('**'+agg.titles[j] + '** ' + '([link](%s))' % agg.urls[j])
        c.write(txt)


