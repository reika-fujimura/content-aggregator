from aggregator import Aggregator

source = 'TheVerge'
source_dic = {
    'TheVerge': 'https://www.theverge.com/tech'
}

txt = '['+source+'](%s)' % source_dic[source] + '\n'

agg = Aggregator(source)
agg.parse_contents()
if len(agg.titles) > 1:
    txt += '**'+agg.titles[0] + '** ' + '([link](%s))' % agg.urls[0] + '\n'
    txt += agg.summarize_text(agg.urls[0],n_sentence = 1)

with open('outputs/test.txt', 'w') as f:
    f.write(txt)

    
