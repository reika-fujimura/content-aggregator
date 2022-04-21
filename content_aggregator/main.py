# Tech News Aggregator streamlit app
# To run the app, type "streamlit run main.py" on terminal.

import streamlit as st

from aggregator import Aggregator


sources = ['TheVerge', 'TechChurch', 'WIRED', 'BuzzFeed']

# header
st.title('Tech News Aggregator')
st.write("""
Contents in popular tech sites.
""")

# aggregators
col1, col2 = st.columns(2)


for i in range(len(sources) // 2):
    col1.header(sources[i])
    c = col1.container()
    agg = Aggregator(sources[i])
    agg.parse_contents()
    for i in range(len(agg.titles)):
        c.write(agg.titles[i] + ' ' + '([link](%s))' % agg.urls[i])

for i in range(len(sources) // 2, len(sources)):
    col2.header(sources[i])
    c = col2.container()
    agg = Aggregator(sources[i])
    agg.parse_contents()
    for i in range(len(agg.titles)):
        c.write(agg.titles[i] + ' ' +'([link](%s))' % agg.urls[i])