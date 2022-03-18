import pythainlp
import deepcut


def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    data = []
    for word in words:
        word = word.strip()
        if word not in stopwords:
            data.append(word)
    return data


def get_features(data):
    words = deepcut.tokenize(data)
    words = clean_words(words)

    features = {}
    features["คือ"] = "คือ" in words
    features["ประเภท"] = "ประเภท" in words
    features["สิทธิ"] = "สิทธิ" in words

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data