import nltk
import pprint
import random
import pandas
import word_utils
import pickle

dfs = pandas.read_excel("response.xlsx")

responses = {}
for df in dfs.to_dict("records"):
    if df["tag"] not in responses:
        responses[df["tag"]] = []
    responses[df["tag"]].append(df["response"])

pprint.pprint(responses)
## To load later:
f = open("my_classifier.pickle", "rb")
classifier = pickle.load(f)
f.close()

while True:
    q = input("Type: ")
    if q == "quit":
        break
    feature = word_utils.get_features(q)
    result = classifier.prob_classify(feature)
    if result.prob(result.max()) < 0.5:
        print(random.choice(responses["unknow-message"]))
        continue

    print("prob ->", result.max(), round(result.prob(result.max()), 2))
    print("ans:", random.choice(responses[result.max()]))