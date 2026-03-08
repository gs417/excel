"""共通ダミーデータ: ミルクネクスト株式会社（乳業メーカー 法人営業部）"""

import random
from datetime import date, timedelta

random.seed(42)

COMPANY_NAME = "ミルクネクスト株式会社"

# --- 地域 ---
REGIONS = ["東京", "大阪", "名古屋", "福岡", "札幌"]

# --- 営業担当者 ---
SALES_REPS = [
    {"name": "田中 太郎", "department": "量販営業部", "target": 48_000_000},
    {"name": "鈴木 花子", "department": "量販営業部", "target": 42_000_000},
    {"name": "佐藤 健一", "department": "業務用営業部", "target": 52_000_000},
    {"name": "山田 美咲", "department": "業務用営業部", "target": 45_000_000},
    {"name": "高橋 翔太", "department": "業務用営業部", "target": 50_000_000},
]

# --- 商品マスタ ---
PRODUCTS = [
    {"id": "P001", "name": "北海道フレッシュ牛乳 1L",    "category": "牛乳",         "unit_price": 4_800},
    {"id": "P002", "name": "濃厚4.2牛乳 1L",            "category": "牛乳",         "unit_price": 6_200},
    {"id": "P003", "name": "毎日プレーンヨーグルト 400g", "category": "ヨーグルト",   "unit_price": 3_600},
    {"id": "P004", "name": "ギリシャ濃密ヨーグルト 100g", "category": "ヨーグルト",   "unit_price": 5_400},
    {"id": "P005", "name": "とろけるスライスチーズ 7枚",  "category": "チーズ",       "unit_price": 4_200},
    {"id": "P006", "name": "熟成カマンベール 100g",       "category": "チーズ",       "unit_price": 8_500},
    {"id": "P007", "name": "北海道バター 200g",           "category": "バター・生クリーム", "unit_price": 7_200},
    {"id": "P008", "name": "純生クリーム 200ml",          "category": "バター・生クリーム", "unit_price": 5_800},
]

# --- 顧客マスタ (50件: スーパー/コンビニ/飲食/給食/卸) ---
_CUSTOMERS_RAW = [
    # スーパー (20)
    ("フレッシュマート", "スーパー"), ("グリーンバスケット", "スーパー"),
    ("デイリーライフ", "スーパー"), ("サンフード", "スーパー"),
    ("まるいち", "スーパー"), ("フードパレス", "スーパー"),
    ("スマイルマート", "スーパー"), ("タウンストア", "スーパー"),
    ("ナチュラルフーズ", "スーパー"), ("ビッグバリュー", "スーパー"),
    ("ファミリーマルシェ", "スーパー"), ("セーブモア", "スーパー"),
    ("ハッピーフレッシュ", "スーパー"), ("グッドプライス", "スーパー"),
    ("リバーサイドストア", "スーパー"), ("くらしの市場", "スーパー"),
    ("モーニングマート", "スーパー"), ("トップフーズ", "スーパー"),
    ("ライフデリ", "スーパー"), ("さくらマーケット", "スーパー"),
    # コンビニ本部 (5)
    ("デイリーショップ本部", "コンビニ"), ("クイックマート本部", "コンビニ"),
    ("エブリワン本部", "コンビニ"), ("ミニステーション本部", "コンビニ"),
    ("タウンコンビニ本部", "コンビニ"),
    # 飲食チェーン (10)
    ("カフェ・ド・ミルク", "飲食"), ("レストランひまわり", "飲食"),
    ("ベーカリーサンライズ", "飲食"), ("パスタハウスRosso", "飲食"),
    ("スイーツガーデン", "飲食"), ("居酒屋たんぽぽ", "飲食"),
    ("ホテルグランド東京", "飲食"), ("洋菓子工房プティ", "飲食"),
    ("ピッツェリアナポリ", "飲食"), ("カフェブリーズ", "飲食"),
    # 給食・病院 (10)
    ("東日本スクールサービス", "給食"), ("メディカルフーズ", "給食"),
    ("シルバーケア食品", "給食"), ("学校給食センター", "給食"),
    ("ウェルネスダイニング", "給食"), ("セントラルキッチン東海", "給食"),
    ("ヘルシーミール", "給食"), ("栄養サポート", "給食"),
    ("フードサービス北海道", "給食"), ("ケアフード九州", "給食"),
    # 卸 (5)
    ("大和食品卸", "卸"), ("中央フードディストリ", "卸"),
    ("北海道デリバリー", "卸"), ("関西食材センター", "卸"),
    ("九州フードネット", "卸"),
]

CUSTOMERS = []
for i, (name, industry) in enumerate(_CUSTOMERS_RAW):
    CUSTOMERS.append({
        "id": f"C{i+1:03d}",
        "name": name,
        "region": REGIONS[i % 5],
        "industry": industry,
    })

# --- 売上データ (200件, 2025/4 ~ 2026/3) ---
# 単位はケース（箱）単位の取引
_START = date(2025, 4, 1)
_END = date(2026, 3, 31)
_DAYS = (_END - _START).days

SALES = []
for i in range(200):
    d = _START + timedelta(days=random.randint(0, _DAYS))
    product = random.choice(PRODUCTS)
    qty = random.randint(10, 200)  # ケース単位
    SALES.append({
        "id": f"S{i+1:04d}",
        "date": d,
        "customer_id": random.choice(CUSTOMERS)["id"],
        "product_id": product["id"],
        "product_name": product["name"],
        "category": product["category"],
        "unit_price": product["unit_price"],
        "quantity": qty,
        "amount": product["unit_price"] * qty,
        "rep": random.choice(SALES_REPS)["name"],
        "region": random.choice(REGIONS),
        "month": d.strftime("%Y-%m"),
    })

# Sort by date
SALES.sort(key=lambda s: s["date"])


def get_product_by_id(pid: str) -> dict:
    for p in PRODUCTS:
        if p["id"] == pid:
            return p
    return {}


def get_customer_by_id(cid: str) -> dict:
    for c in CUSTOMERS:
        if c["id"] == cid:
            return c
    return {}
