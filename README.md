# Tech News Content Aggregator

Content aggregating Python Streamlit app.

Most recent articles are aggregated from several popular tech news sites and summaries are displayed!

---

## Summary

Most recent articles are aggregated from popular tech news sites by website scraping.

For each article, summary of the content is displayed using spacy's text summarizer model.

The news aggregator is deployed as an app using Streamlit.

---

## How to run

Run the command below on terminal.

1. Create environment from Pipfile

    ```pipenv sync```

    Or, create the environment by yourself.

    ```pipenv --python 3.8```

    ```pipenv install -r requirements.txt```

    ```pipenv shell```

2. Download 'en_core_web_sm'

    ```python3 -m spacy download en_core_web_sm```

3. Run streamlit app

    ```streamlit run main.py```

---

## View

![alt text](content_aggregator/images/view.png?raw=true)

---

## Tools

Python app: [Streamlit](https://streamlit.io/)

Content Summarizer: [spacy](https://scapy.net/)

Web Scraping: [requests](https://docs.python-requests.org/en/latest/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)