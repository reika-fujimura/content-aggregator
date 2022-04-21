# Tech News Aggregator streamlit app
# To run the app, type "streamlit run main.py" on terminal.

import streamlit as st

from aggregator import Aggregator


sources = ['TheVerge', 'TechChurch', 'WIRED', 'BuzzFeed']

'''
Streamlit App
'''
# header
st.title('Tech News Aggregator')
st.write("""
Contents in podcast gallary.
""")

# aggregators
for source in sources:
    agg = Aggregator(source)



