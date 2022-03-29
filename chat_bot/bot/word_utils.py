import pythainlp
import deepcut


def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
<<<<<<< HEAD
    add_keyword = ["ไม่", "คือ", "ต้อง", "เก็บ", "เพื่อ", "คิด", "ที่", "กำหนด", "ค่ะ", "คะ", "ไหน", "เพจ", "ทำ", "การ", "เปิด", "ตี", "ไร", 'ยัง', 'ไง','ตัว','ตะ','เอง','ค้าบ','ชื่อ','บอท','มั้ย']
=======
    add_keyword = [
        "ไม่",
        "คือ",
        "ต้อง",
        "เก็บ",
        "เพื่อ",
        "คิด",
        "ที่",
        "กำหนด",
        "ค่ะ",
        "คะ",
        "ไหน",
        "เพจ",
        "ทำ",
        "การ",
        "เปิด",
        "ตี",
        "ไร",
        "ยัง",
        "ไง",
        "ไม",
        "ทำ",
        "จ่าย",
        "แล้ว",
        "ไป",
        "จาก",
        "การ",
    ]
>>>>>>> d91283b555121c7e015797b2ba531fb000edd9ac
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
    features["คือ"] = "คือ" in words or "กฎหมายภาษี"
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
    features["ไหน"] = "ไหน" in words
    features["หวัด"] = "หวัด" in words
    features["เปิด"] = "เปิด" in words
    features["เพจ"] = "เพจ" in words
    features["ตี"] = "ตี" in words
    features["ไร"] = "ไร" in words
    features["ยัง"] = "ยัง" in words
    features["ไง"] = "ไง" in words
    features["ขอบคุณ"] = "ขอบคุณ" in words
    features["ขอบใจ"] = "ขอบใจ" in words
    features["ใจจ้า"] = "ใจจ้า" in words
    features["ใจนะ"] = "ใจนะ" in words
<<<<<<< HEAD
    features["ตัว"] = "ตัว" in words
    features["ตะ"] = "ตะ" in words
    features["เอง"] = "เอง" in words
    features["ค้าบ"] = "ค้าบ" in words
    features["ชื่อ"] = "ชื่อ" in words
    features["บอท"] = "บอท" in words
    features["มั้ย"] = "มั้ย" in words
=======
    features["Thanks"] = "Thanks" in words
    features["Thank"] = "Thank" in words
    features["thanks"] = "thanks" in words
    features["thank"] = "thank" in words
    features["you"] = "you" in words
    features["hi"] = "hi" in words
    features["hello"] = "hello" in words
    features["Hi"] = "Hi" in words
    features["Hello"] = "Hello" in words
    features["จ่าย"] = "จ่าย" in words
    features["ทำ"] = "ทำ" in words
    features["ไม"] = "ไม" in words
    features["ไป"] = "ไป" in words
    features["จาก"] = "จาก" in words
    features["การ"] = "การ" in words
    features["แล้ว"] = "แล้ว" in words
>>>>>>> d91283b555121c7e015797b2ba531fb000edd9ac

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data
