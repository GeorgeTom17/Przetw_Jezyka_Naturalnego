import spacy

nlp = spacy.load("en_core_web_sm")
while True:
    doc = nlp(str(input("Sentence : ")))
    tag = []
    pos = []
    dep = []
    for i in doc:
        pos.append(i.pos_)
        tag.append(i.tag_)
        dep.append(i.dep_)
    if 'nsubj' not in dep:
        print("Imperative sentence")