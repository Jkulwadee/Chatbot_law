import pythainlp
import deepcut


def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    not_delete = ["ไม่", "คือ"]
    data = []
    for word in words:
        word = word.strip()
        if word not in stopwords:
            data.append(word)
        if word in not_delete:
            data.append(word)
    return data


def get_features(data):
    words = deepcut.tokenize(data)
    words = clean_words(words)

    features = {}
    features["ภาษี"] = "ภาษี" in words
    features["คือ"] = "คือ" in words  # or "กฎหมายภาษี"
    features["ประเภท"] = "ประเภท" in words
    features["สิทธิ"] = "สิทธิ" in words
    features["อากร"] = "อากร" in words
    features["ไม่"] = "ไม่" or "โทษ" or "ไม่เสียภาษี" or "ไม่จ่ายภาษี" in words
    features["หน่วย"] = "หน่วย" in words
    features["งาน"] = "งาน" in words

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data
