import argparse


def main():
    parser = argparse.ArgumentParser(description="""Export AMT""")
    parser.add_argument('--input', default="../res/multiline.txt")
    args = parser.parse_args()


    header = "DATE,TIME,UNIQUE_STORY_INDEX,EVENT_TYPE,PNAC,STORY_DATE_TIME,TAKE_DATE_TIME,HEADLINE_ALERT_TEXT,ACCUMULATED_STORY_TEXT,TAKE_TEXT,PRODUCTS,TOPICS,RELATED_RICS,NAMED_ITEMS,HEADLINE_SUBTYPE,STORY_TYPE,TABULAR_FLAG,ATTRIBUTION,LANGUAGE"
    for line in open(args.input).readlines():
        if line.startswith('","'):
            pass
        elif "STORY_TAKE_OVERWRITE" in line:
            print(line)


if __name__ == "__main__":
    main()
