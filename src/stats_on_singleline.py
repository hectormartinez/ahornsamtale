import argparse
import csv
import pandas as pd
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description="""Export AMT""")
    parser.add_argument('--input', default="../res/headlines.csv")
    args = parser.parse_args()


    header = "DATE,TIME,UNIQUE_STORY_INDEX,EVENT_TYPE,PNAC,STORY_DATE_TIME,TAKE_DATE_TIME,HEADLINE_ALERT_TEXT,ACCUMULATED_STORY_TEXT,TAKE_TEXT,PRODUCTS,TOPICS,RELATED_RICS,NAMED_ITEMS,HEADLINE_SUBTYPE,STORY_TYPE,TABULAR_FLAG,ATTRIBUTION,LANGUAGE"
    header=header.split(",")
    frame = pd.read_csv(args.input, quoting=csv.QUOTE_NONE, names=header)

    unique_story_index_counter = Counter()


    with open(args.input) as f:
        reader = csv.DictReader(f,fieldnames=header) #I could be using pandas but with csv I have less notation worries
        for row in reader:
                #print(row["UNIQUE_STORY_INDEX"],row["LANGUAGE"])
                unique_story_index_counter[row["NAMED_ITEMS"]] += 1

    print(unique_story_index_counter.most_common(20))



if __name__ == "__main__":
    main()
