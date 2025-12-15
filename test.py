with open("dataset/pubmed/01.txt","r") as f:
    content = f.read()
    papers = content.split("\nDOI: ")
    print(len(papers))