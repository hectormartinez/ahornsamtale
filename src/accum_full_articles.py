import argparse
from collections import Counter
from nltk.tokenize import sent_tokenize,wordpunct_tokenize


class Article:
    def __init__(self,headline,body,closing):
        self.headline = headline
        self.body = body
        self.closing = closing
        langid = self.headline.split(",")[-1][1:][:-1]
        if len(langid) > 3 or langid.islower():
            langid = "UNKNOWN"
        self.lang = langid

def main():
    parser = argparse.ArgumentParser(description="""Retrieve the body of English articles for Marmot input""")
    parser.add_argument('--input', default="../res/rna002_RTRS_2013_06.csv")
    args = parser.parse_args()


    headline = ""
    closing=""
    body=[]
    header = "DATE,TIME,UNIQUE_STORY_INDEX,EVENT_TYPE,PNAC,STORY_DATE_TIME,TAKE_DATE_TIME,HEADLINE_ALERT_TEXT,ACCUMULATED_STORY_TEXT,TAKE_TEXT,PRODUCTS,TOPICS,RELATED_RICS,NAMED_ITEMS,HEADLINE_SUBTYPE,STORY_TYPE,TABULAR_FLAG,ATTRIBUTION,LANGUAGE"

    articles = []
    for line in open(args.input).readlines():
        if line.startswith('","'): #Seems an indicator for article end
            closing = line.strip()
            articles.append(Article(headline,body,closing))
            headline = ""
            closing = ""
            body = []
        elif ',"HEADLINE",' in line: #Opens article body
            headline = line.strip()
        elif "STORY_TAKE_OVERWRITE" in line: #First line of article
            body = [line.strip().split(",")[-1]+" "]
        else:
            if "," not in line: #If there are no commas, it is not a CSV row.
                body.append(line.strip()+" ")
            elif line.startswith("2013-06"): #some other CSV line with DELETE or ALERT
                pass
            else:
                body.append(line.strip()+" ")


    #Calculate language distribution
    #C=Counter([art.lang for art in articles if art.lang])
    #for w,i in C.most_common():
    #   print(w,i)

    for art in articles:
        if art.lang == "EN":
            article_text = " ".join(art.body)
            for sentence in sent_tokenize(article_text):
                    print("\n".join(wordpunct_tokenize(sentence)))
                    print()

if __name__ == "__main__":
    main()
