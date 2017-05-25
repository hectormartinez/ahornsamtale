import argparse
def main():
    parser = argparse.ArgumentParser(description="""Export AMT""")
    parser.add_argument('--input', default="../res/.csv")
    args = parser.parse_args()

    header="DATE,TIME,UNIQUE_STORY_INDEX,EVENT_TYPE,PNAC,STORY_DATE_TIME,TAKE_DATE_TIME,HEADLINE_ALERT_TEXT,ACCUMULATED_STORY_TEXT,TAKE_TEXT,PRODUCTS,TOPICS,RELATED_RICS,NAMED_ITEMS,HEADLINE_SUBTYPE,STORY_TYPE,TABULAR_FLAG,ATTRIBUTION,LANGUAGE"

    nfields = 19 # len(header.split(",")) == 19

    singleline = open("singleline.csv",mode="w")
    multiline = open("multiline.txt",mode="w")

    for line in open(args.input).readlines()[1:]:
        if len(line.split(",")) >= nfields: #some text fields contained not escaped commas
            singleline.write(line)
        else:
            multiline.write(line)
    singleline.close()
    multiline.close()

if __name__ == "__main__":
    main()
