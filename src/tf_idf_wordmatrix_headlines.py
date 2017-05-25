import argparse
import pandas as pd
from collections import Counter
from nltk.tokenize import wordpunct_tokenize
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords



def main():
    parser = argparse.ArgumentParser(description="""Export AMT""")
    parser.add_argument('--input', default="../res/headlines.csv")
    args = parser.parse_args()

    header = "DATE,TIME,UNIQUE_STORY_INDEX,EVENT_TYPE,PNAC,STORY_DATE_TIME,TAKE_DATE_TIME,HEADLINE_ALERT_TEXT,ACCUMULATED_STORY_TEXT,TAKE_TEXT,PRODUCTS,TOPICS,RELATED_RICS,NAMED_ITEMS,HEADLINE_SUBTYPE,STORY_TYPE,TABULAR_FLAG,ATTRIBUTION,LANGUAGE"
    header=header.split(",")
    frame = pd.read_csv(args.input, sep=",", names=header)

    stoplist = stopwords.words("english") + "- _ , \" : ' . ; ! ? -'/".split()

    days = dict()
    lex_counter = Counter() #A counter for all words

    for i in range(1,31):
        idx = '{0:02d}'.format(i)
        date = "2013-06-"+idx
        L=[l for l in (frame[(frame.DATE == date) & (frame.LANGUAGE == "EN")].HEADLINE_ALERT_TEXT.values.tolist()) if l]
        L = " ".join(L)
        date_counter = Counter([w for w in wordpunct_tokenize(L) if w.isalpha() and w.lower() not in stoplist])
        lex_counter = lex_counter + date_counter
        days[date]=date_counter #word counter for each day

    M = []
    sortedlex = sorted(lex_counter.keys())
    for i,d in enumerate(days.keys()):
        M.append([days[d][w] for i,w in enumerate(sortedlex)])
    M = np.array(M)
    print(M.shape)
    transformer = TfidfTransformer(smooth_idf=True,sublinear_tf=True)
    M_tfidf = transformer.fit_transform(M).toarray()
    #print(M_tfidf)
    tfidfbest = []
    for i,row in enumerate(M_tfidf):
        top4 = np.argpartition(M_tfidf[i], -1)[-1:]
        topX = np.argpartition(M_tfidf[i], -10)[-10:]

        topX = np.argpartition(M_tfidf[i], -10)[-10:]
        tfidfbest.append([sortedlex[idx] for idx in top4][0])
    topfreq=[w for w,c in lex_counter.most_common(30)]
    for idx,(daywise,overall) in enumerate(zip(tfidfbest,topfreq)):
        print(idx+1,"&",daywise,"&",overall,"\\\\ \hline")


if __name__ == "__main__":
    main()
