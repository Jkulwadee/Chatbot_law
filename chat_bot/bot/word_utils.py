import pythainlp
import deepcut


def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    add_keyword = ["ไม่", "คือ", "ต้อง", "เก็บ", "เพื่อ", "คิด", "ที่", "กำหนด", "ค่ะ", "คะ", "ไหน"]
    data = []
    for word in words:
        word = word.strip()
        if word not in stopwords:
            data.append(word)
        if word in add_keyword:
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
    features["หน่วย"] = "หน่วย" or "งาน" in words
    features["เก็บ"] = "เก็บ" in words
    features["ต้อง"] = "ต้อง" in words
    features["เพื่อ"] = "เพื่อ" in words
    features["คำนวณ"] = "คำนวณ" or "คำนวน" in words
    features["คิด"] = "คิด" in words
    features["ช่วง"] = "ช่วง" in words
    features["เวลา"] = "เวลา" in words
    features["ตอน"] = "ตอน" in words
    features["ที่"] = "ที่" in words
    features["สถานที่"] = "สถานที่" in words
    features["ยื่น"] = "ยื่น" in words
    features["เงิน"] = "เงิน" in words
    features["เดือน"] = "เดือน" in words
    features["ไหร่"] = "ไหร่" in words
    features["กำหนด"] = "กำหนด" in words
    features["เสีย"] = "เสีย" in words

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data
