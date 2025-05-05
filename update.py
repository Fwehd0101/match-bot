import json
from datetime import datetime

data = {
    "type": "match",
    "title": "برشلونة × ريال مدريد",
    "time": "22:00",
    "status": "مباشر الآن",
    "source": "اختبار البوت",
    "stream_url": "https://example.com/live/barca-vs-real"
}

with open("latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ تم تحديث الملف!")
