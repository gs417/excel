"""全レッスン統合HTML生成 — 1ファイル完結型ビジネススキル自習キット"""

import json, os, subprocess, base64, tempfile
from collections import defaultdict
from . import data
from . import lt_content, extras


def _gen_thumbnails(output_dir):
    """PPTXファイルのサムネイルをbase64で返す"""
    ppt_dir = os.path.join(output_dir, "ppt")
    files = {
        'p1b': 'Lesson1_課題_1スライド1メッセージ.pptx',
        'p1a': 'Lesson1_模範_1スライド1メッセージ.pptx',
        'p2b': 'Lesson2_課題_図解化.pptx',
        'p2a': 'Lesson2_模範_図解化.pptx',
        'p3b': 'Lesson3_課題_提案書作成.pptx',
        'p3a': 'Lesson3_模範_提案書作成.pptx',
    }
    thumbs = {}
    with tempfile.TemporaryDirectory() as tmp:
        for key, fn in files.items():
            path = os.path.join(ppt_dir, fn)
            if not os.path.exists(path):
                thumbs[key] = ''
                continue
            try:
                subprocess.run(['qlmanage', '-t', '-s', '800', '-o', tmp, path],
                               capture_output=True, timeout=10)
                png = os.path.join(tmp, fn + '.png')
                if os.path.exists(png):
                    with open(png, 'rb') as f:
                        thumbs[key] = base64.b64encode(f.read()).decode()
                else:
                    thumbs[key] = ''
            except Exception:
                thumbs[key] = ''
    return thumbs


def generate(output_dir: str):
    thumbs = _gen_thumbnails(output_dir)
    html = _build_html(thumbs)
    path = f"{output_dir}/ビジネススキル自習キット.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {path}")
    return path


def _fmt(n):
    """数値をカンマ区切りに"""
    if isinstance(n, float):
        return f"{n:,.1f}"
    return f"{n:,}"


def _compute():
    """全レッスンのデータと期待値を計算"""
    S = data.SALES
    amounts = [s["amount"] for s in S]
    quantities = [s["quantity"] for s in S]

    # ---- Excel L1 ----
    e1 = [
        {"q": "全売上の合計金額（SUM）", "hint": "=SUM(金額の範囲)", "answer": sum(amounts), "type": "number",
         "formula": "=SUM(H2:H201)"},
        {"q": "売上金額の平均（AVERAGE）", "hint": "=AVERAGE(金額の範囲)", "answer": sum(amounts)/len(amounts),
         "type": "number", "formula": "=AVERAGE(H2:H201)"},
        {"q": "売上データの件数（COUNT）", "hint": "=COUNT(範囲)", "answer": len(S), "type": "number",
         "formula": "=COUNT(A2:A201)"},
        {"q": "地域が「東京」の件数（COUNTIF）", "hint": '=COUNTIF(範囲,"東京")',
         "answer": sum(1 for s in S if s["region"] == "東京"), "type": "number",
         "formula": '=COUNTIF(J2:J201,"東京")'},
        {"q": "カテゴリ「牛乳」の売上合計（SUMIF）", "hint": '=SUMIF(条件範囲,"牛乳",合計範囲)',
         "answer": sum(s["amount"] for s in S if s["category"] == "牛乳"), "type": "number",
         "formula": '=SUMIF(E2:E201,"牛乳",H2:H201)'},
        {"q": "売上金額の最大値（MAX）", "hint": "=MAX(範囲)", "answer": max(amounts), "type": "number",
         "formula": "=MAX(H2:H201)"},
        {"q": "売上金額の最小値（MIN）", "hint": "=MIN(範囲)", "answer": min(amounts), "type": "number",
         "formula": "=MIN(H2:H201)"},
        {"q": "数量（ケース数）の合計（SUM）", "hint": "=SUM(数量の範囲)", "answer": sum(quantities),
         "type": "number", "formula": "=SUM(G2:G201)"},
        {"q": "担当者「田中 太郎」の件数（COUNTIF）", "hint": '=COUNTIF(範囲,"田中 太郎")',
         "answer": sum(1 for s in S if s["rep"] == "田中 太郎"), "type": "number",
         "formula": '=COUNTIF(I2:I201,"田中 太郎")'},
        {"q": "カテゴリ「チーズ」の売上合計（SUMIF）", "hint": '=SUMIF(条件範囲,"チーズ",合計範囲)',
         "answer": sum(s["amount"] for s in S if s["category"] == "チーズ"), "type": "number",
         "formula": '=SUMIF(E2:E201,"チーズ",H2:H201)'},
    ]

    # ---- Excel L2 ----
    s0, s4 = S[0], S[4]
    p003 = data.get_product_by_id("P003")
    c001 = data.get_customer_by_id("C001")
    c010 = data.get_customer_by_id("C010")
    p006 = data.get_product_by_id("P006")
    p001 = data.get_product_by_id("P001")
    c005 = data.get_customer_by_id("C005")
    e2 = [
        {"q": "売上1行目(S0001)の商品名", "hint": "商品マスタのVLOOKUP", "answer": s0["product_name"],
         "type": "text", "formula": "=VLOOKUP(D2,商品マスタ!A:B,2,FALSE)"},
        {"q": "商品ID「P003」の単価", "hint": "商品マスタから検索", "answer": p003["unit_price"],
         "type": "number", "formula": "=VLOOKUP(\"P003\",商品マスタ!A:D,4,FALSE)"},
        {"q": "顧客ID「C001」の顧客名", "hint": "顧客マスタから検索", "answer": c001["name"],
         "type": "text", "formula": "=VLOOKUP(\"C001\",顧客マスタ!A:B,2,FALSE)"},
        {"q": "顧客ID「C010」の地域", "hint": "顧客マスタから検索", "answer": c010["region"],
         "type": "text", "formula": "=VLOOKUP(\"C010\",顧客マスタ!A:C,3,FALSE)"},
        {"q": "商品ID「P006」のカテゴリ（INDEX-MATCH）", "hint": "=INDEX(範囲,MATCH(検索値,範囲,0))",
         "answer": p006["category"], "type": "text",
         "formula": "=INDEX(商品マスタ!C:C,MATCH(\"P006\",商品マスタ!A:A,0))"},
        {"q": "商品ID「P001」の単価（INDEX-MATCH）", "hint": "=INDEX(範囲,MATCH(検索値,範囲,0))",
         "answer": p001["unit_price"], "type": "number",
         "formula": "=INDEX(商品マスタ!D:D,MATCH(\"P001\",商品マスタ!A:A,0))"},
        {"q": "顧客ID「C005」の業種（INDEX-MATCH）", "hint": "=INDEX(範囲,MATCH(検索値,範囲,0))",
         "answer": c005["industry"], "type": "text",
         "formula": "=INDEX(顧客マスタ!D:D,MATCH(\"C005\",顧客マスタ!A:A,0))"},
        {"q": "売上5行目(S0005)の顧客名（2段階参照）", "hint": "売上→顧客マスタ",
         "answer": data.get_customer_by_id(s4["customer_id"])["name"], "type": "text",
         "formula": "=VLOOKUP(C6,顧客マスタ!A:B,2,FALSE)"},
    ]

    # ---- Excel L3 ----
    dept1 = {"田中 太郎", "鈴木 花子"}
    e3 = [
        {"q": "金額100万円以上の件数", "hint": '=COUNTIF(範囲,">=1000000")',
         "answer": sum(1 for s in S if s["amount"] >= 1_000_000), "type": "number"},
        {"q": "金額50万円以上の件数", "hint": '=COUNTIF(範囲,">=500000")',
         "answer": sum(1 for s in S if s["amount"] >= 500_000), "type": "number"},
        {"q": "東京かつ牛乳の売上合計（SUMIFS）", "hint": '=SUMIFS(合計範囲,範囲1,"東京",範囲2,"牛乳")',
         "answer": sum(s["amount"] for s in S if s["region"] == "東京" and s["category"] == "牛乳"), "type": "number"},
        {"q": "大阪かつ田中太郎の件数（COUNTIFS）", "hint": '=COUNTIFS(範囲1,"大阪",範囲2,"田中 太郎")',
         "answer": sum(1 for s in S if s["region"] == "大阪" and s["rep"] == "田中 太郎"), "type": "number"},
        {"q": "数量50以上かつヨーグルトの売上合計", "hint": '=SUMIFS(合計,数量,">=50",カテゴリ,"ヨーグルト")',
         "answer": sum(s["amount"] for s in S if s["quantity"] >= 50 and s["category"] == "ヨーグルト"), "type": "number"},
        {"q": "金額100万以上の件数（確認用）", "hint": "Q1と同じ",
         "answer": sum(1 for s in S if s["amount"] >= 1_000_000), "type": "number"},
        {"q": "2025年4月(2025-04)の売上合計", "hint": '=SUMIF(月範囲,"2025-04",金額範囲)',
         "answer": sum(s["amount"] for s in S if s["month"] == "2025-04"), "type": "number"},
        {"q": "福岡かつチーズの件数", "hint": '=COUNTIFS(範囲1,"福岡",範囲2,"チーズ")',
         "answer": sum(1 for s in S if s["region"] == "福岡" and s["category"] == "チーズ"), "type": "number"},
        {"q": "佐藤健一かつ金額50万以上の件数", "hint": '=COUNTIFS(担当,"佐藤 健一",金額,">=500000")',
         "answer": sum(1 for s in S if s["rep"] == "佐藤 健一" and s["amount"] >= 500_000), "type": "number"},
        {"q": "量販営業部(田中+鈴木)の売上合計", "hint": "2人分のSUMIFを足す",
         "answer": sum(s["amount"] for s in S if s["rep"] in dept1), "type": "number"},
    ]

    # ---- Excel L4 ----
    region_totals = defaultdict(int)
    cat_totals = defaultdict(int)
    rep_counts = defaultdict(int)
    month_totals = defaultdict(int)
    for s in S:
        region_totals[s["region"]] += s["amount"]
        cat_totals[s["category"]] += s["amount"]
        rep_counts[s["rep"]] += 1
        month_totals[s["month"]] += s["amount"]
    top3 = sorted(month_totals.items(), key=lambda x: x[1], reverse=True)[:3]
    tokyo_milk = sum(s["amount"] for s in S if s["region"] == "東京" and s["category"] == "牛乳")

    e4 = {
        "regions": [(r, region_totals[r]) for r in data.REGIONS],
        "categories": [(c, cat_totals[c]) for c in ["牛乳", "ヨーグルト", "チーズ", "バター・生クリーム"]],
        "reps": [(r["name"], rep_counts[r["name"]]) for r in data.SALES_REPS],
        "top3": top3,
        "cross": tokyo_milk,
    }

    # ---- Excel L5 ----
    total_amount = sum(amounts)
    total_deals = len(S)
    avg_deal = total_amount / total_deals
    total_target = sum(r["target"] for r in data.SALES_REPS)
    achievement = total_amount / total_target
    unique_cust = len(set(s["customer_id"] for s in S))
    rep_amounts = defaultdict(int)
    for s in S:
        rep_amounts[s["rep"]] += s["amount"]
    top_rep = max(rep_amounts, key=rep_amounts.get)
    top_rep_amt = rep_amounts[top_rep]
    achievers = sum(1 for r in data.SALES_REPS if rep_amounts[r["name"]] >= r["target"])
    best_month = max(month_totals, key=month_totals.get)
    best_month_amt = month_totals[best_month]
    h1_amt = sum(s["amount"] for s in S if s["month"] <= "2025-09")
    h2_amt = total_amount - h1_amt
    avg_monthly = total_amount / len(month_totals)
    region_amounts = defaultdict(int)
    cat_amounts2 = defaultdict(int)
    for s in S:
        region_amounts[s["region"]] += s["amount"]
        cat_amounts2[s["category"]] += s["amount"]
    top_region = max(region_amounts, key=region_amounts.get)
    top_cat = max(cat_amounts2, key=cat_amounts2.get)

    e5 = [
        {"q": "売上合計", "answer": total_amount, "type": "number"},
        {"q": "取引件数", "answer": total_deals, "type": "number"},
        {"q": "平均取引額", "answer": avg_deal, "type": "number"},
        {"q": "目標達成率（小数で入力 例:0.85）", "answer": achievement, "type": "percent"},
        {"q": "取引顧客数（ユニーク）", "answer": unique_cust, "type": "number"},
        {"q": "売上No.1の担当者名", "answer": top_rep, "type": "text"},
        {"q": "その担当者の売上合計", "answer": top_rep_amt, "type": "number"},
        {"q": "目標達成者数（5名中）", "answer": achievers, "type": "number"},
        {"q": "売上最大月（YYYY-MM）", "answer": best_month, "type": "text"},
        {"q": "その月の売上合計", "answer": best_month_amt, "type": "number"},
        {"q": "上半期(4-9月)売上合計", "answer": h1_amt, "type": "number"},
        {"q": "下半期(10-3月)売上合計", "answer": h2_amt, "type": "number"},
        {"q": "平均月間売上", "answer": avg_monthly, "type": "number"},
        {"q": "売上No.1の地域", "answer": top_region, "type": "text"},
        {"q": "売上No.1のカテゴリ", "answer": top_cat, "type": "text"},
    ]

    # ---- 売上テーブルデータ ----
    sales_rows = []
    for s in S:
        sales_rows.append([
            s["id"], s["date"].strftime("%Y/%m/%d"), s["customer_id"],
            s["product_name"], s["category"], f'¥{s["unit_price"]:,}',
            s["quantity"], f'¥{s["amount"]:,}', s["rep"], s["region"], s["month"]
        ])

    return {
        "e1": e1, "e2": e2, "e3": e3, "e4": e4, "e5": e5,
        "sales_rows": sales_rows,
        "products": data.PRODUCTS,
        "customers": data.CUSTOMERS,
        "reps": data.SALES_REPS,
    }


def _sales_table_html(rows, max_rows=20, show_month=True):
    headers = ["ID", "日付", "顧客ID", "商品名", "カテゴリ", "単価", "数量", "金額", "担当者", "地域"]
    if show_month:
        headers.append("月")
    h = '<div class="table-scroll"><table class="data-table"><thead><tr>'
    for hd in headers:
        h += f'<th>{hd}</th>'
    h += '</tr></thead><tbody>'
    for i, row in enumerate(rows[:max_rows]):
        cols = row[:10] if not show_month else row
        cls = ' class="stripe"' if i % 2 else ''
        h += f'<tr{cls}>'
        for c in cols:
            h += f'<td>{c}</td>'
        h += '</tr>'
    h += '</tbody></table></div>'
    if len(rows) > max_rows:
        h += f'<p style="color:var(--text-light);font-size:0.85rem;margin:4px 0">※ 先頭{max_rows}件を表示（全{len(rows)}件）</p>'
    return h


def _q_cards(lesson_id, questions):
    """Excel問題カードHTML"""
    h = ''
    for i, q in enumerate(questions):
        imode = 'text' if q["type"] == "text" else 'numeric'
        ph = '回答を入力'
        if q["type"] == "percent":
            ph = "例: 0.85"
        hint_html = ''
        if q.get("hint"):
            hint_html = f'''
      <div class="q-hint-toggle" onclick="toggleHint('{lesson_id}-h{i}')">💡 ヒント</div>
      <div class="q-hint tb-hidden" id="{lesson_id}-h{i}"><code>{q["hint"]}</code></div>'''
        h += f'''
    <div class="question-card">
      <div class="q-header">Q{i+1}. {q["q"]}</div>{hint_html}
      <div class="q-input">
        <input type="text" id="{lesson_id}-q{i}" placeholder="{ph}" inputmode="{imode}" onkeydown="if(event.key==='Enter')gradeQ('{lesson_id}',{i})">
        <button class="grade-btn" onclick="gradeQ('{lesson_id}',{i})">採点</button>
      </div>
      <div class="result" id="{lesson_id}-r{i}"></div>
    </div>'''
    return h


def _answers_block(lesson_id, questions):
    h = f'<button class="show-answers-btn" onclick="toggleEl(\'{lesson_id}-answers\')">📝 模範解答を表示</button>'
    h += f'<div class="tb-hidden" id="{lesson_id}-answers"><div class="tb-example">'
    for i, q in enumerate(questions):
        a = q["answer"]
        if q["type"] == "percent":
            a_str = f"{a*100:.1f}%"
        elif q["type"] == "number":
            a_str = _fmt(a)
        else:
            a_str = str(a)
        formula = q.get("formula", "")
        f_str = f" <code>{formula}</code> →" if formula else ""
        h += f'<p><strong>Q{i+1}:</strong>{f_str} <strong>{a_str}</strong></p>'
    h += '</div></div>'
    return h


def _build_html(thumbs=None):
    if thumbs is None:
        thumbs = {}
    d = _compute()
    e1, e2, e3, e4, e5 = d["e1"], d["e2"], d["e3"], d["e4"], d["e5"]
    sales_table = _sales_table_html(d["sales_rows"], 20)
    sales_table_10 = _sales_table_html(d["sales_rows"], 10, True)

    # Product table
    pt = '<div class="table-scroll"><table class="data-table"><thead><tr><th>商品ID</th><th>商品名</th><th>カテゴリ</th><th>単価</th></tr></thead><tbody>'
    for p in d["products"]:
        pt += f'<tr><td>{p["id"]}</td><td>{p["name"]}</td><td>{p["category"]}</td><td>¥{p["unit_price"]:,}</td></tr>'
    pt += '</tbody></table></div>'

    # Customer table (first 10)
    ct = '<div class="table-scroll"><table class="data-table"><thead><tr><th>顧客ID</th><th>顧客名</th><th>地域</th><th>業種</th></tr></thead><tbody>'
    for c in d["customers"][:10]:
        ct += f'<tr><td>{c["id"]}</td><td>{c["name"]}</td><td>{c["region"]}</td><td>{c["industry"]}</td></tr>'
    ct += '</tbody></table></div><p style="color:var(--text-light);font-size:0.85rem">※ 先頭10件表示（全50件）</p>'

    # Reps table
    rt = '<div class="table-scroll"><table class="data-table"><thead><tr><th>担当者</th><th>部署</th><th>年間目標</th></tr></thead><tbody>'
    for r in d["reps"]:
        rt += f'<tr><td>{r["name"]}</td><td>{r["department"]}</td><td>¥{r["target"]:,}</td></tr>'
    rt += '</tbody></table></div>'

    # E4 pivot rows
    e4_regions_html = ''
    for label, val in e4["regions"]:
        e4_regions_html += f'''<div class="pivot-row"><span class="pivot-label">{label}</span>
        <input type="text" id="e4-r-{label}" inputmode="numeric" placeholder="金額" onkeydown="if(event.key==='Enter')gradePivot('e4-r-{label}',{val})">
        <button class="grade-btn" onclick="gradePivot('e4-r-{label}',{val})">採点</button>
        <span class="result" id="e4-r-{label}-r"></span></div>'''

    e4_cats_html = ''
    for label, val in e4["categories"]:
        e4_cats_html += f'''<div class="pivot-row"><span class="pivot-label">{label}</span>
        <input type="text" id="e4-c-{label}" inputmode="numeric" placeholder="金額" onkeydown="if(event.key==='Enter')gradePivot('e4-c-{label}',{val})">
        <button class="grade-btn" onclick="gradePivot('e4-c-{label}',{val})">採点</button>
        <span class="result" id="e4-c-{label}-r"></span></div>'''

    e4_reps_html = ''
    for label, val in e4["reps"]:
        e4_reps_html += f'''<div class="pivot-row"><span class="pivot-label">{label}</span>
        <input type="text" id="e4-rp-{label}" inputmode="numeric" placeholder="件数" onkeydown="if(event.key==='Enter')gradePivot('e4-rp-{label}',{val})">
        <button class="grade-btn" onclick="gradePivot('e4-rp-{label}',{val})">採点</button>
        <span class="result" id="e4-rp-{label}-r"></span></div>'''

    e4_answers_html = '<h4>地域別</h4>'
    for label, val in e4["regions"]:
        e4_answers_html += f'<p>{label}: <strong>{_fmt(val)}</strong></p>'
    e4_answers_html += '<h4>カテゴリ別</h4>'
    for label, val in e4["categories"]:
        e4_answers_html += f'<p>{label}: <strong>{_fmt(val)}</strong></p>'
    e4_answers_html += '<h4>担当者別件数</h4>'
    for label, val in e4["reps"]:
        e4_answers_html += f'<p>{label}: <strong>{val}</strong></p>'
    e4_answers_html += '<h4>TOP3月</h4>'
    for i, (m, a) in enumerate(e4["top3"]):
        e4_answers_html += f'<p>{i+1}位: {m} = <strong>{_fmt(a)}</strong></p>'
    e4_answers_html += f'<h4>東京×牛乳</h4><p><strong>{_fmt(e4["cross"])}</strong></p>'

    # JS answer data
    def _js_answers(qs):
        items = []
        for q in qs:
            if q["type"] == "text":
                items.append(f'{{"t":"s","v":"{q["answer"]}"}}')
            elif q["type"] == "percent":
                items.append(f'{{"t":"p","v":{q["answer"]}}}')
            else:
                items.append(f'{{"t":"n","v":{q["answer"]}}}')
        return "[" + ",".join(items) + "]"

    js_data = f'''const A={{
  e1:{_js_answers(e1)},
  e2:{_js_answers(e2)},
  e3:{_js_answers(e3)},
  e5:{_js_answers(e5)}
}};'''

    # --- PPT thumbnails ---
    def _thumb_html(key, label):
        b64 = thumbs.get(key, '')
        if not b64:
            return ''
        return f'<div><p style="font-weight:600;margin-bottom:6px;font-size:.85rem">{label}</p><img src="data:image/png;base64,{b64}" style="width:100%;border-radius:8px;border:1px solid var(--border);box-shadow:0 2px 8px rgba(0,0,0,.08)"></div>'

    ppt1_thumbs = ''
    ppt2_thumbs = ''
    ppt3_thumbs = ''
    if thumbs.get('p1b') or thumbs.get('p1a'):
        ppt1_thumbs = f'<h3>📎 実際のパワーポイント（プレビュー）</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0">{_thumb_html("p1b","🔴 修正前")}{_thumb_html("p1a","🟢 修正後")}</div>'
    if thumbs.get('p2b') or thumbs.get('p2a'):
        ppt2_thumbs = f'<h3>📎 実際のパワーポイント（プレビュー）</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0">{_thumb_html("p2b","🔴 修正前")}{_thumb_html("p2a","🟢 修正後")}</div>'
    if thumbs.get('p3b') or thumbs.get('p3a'):
        ppt3_thumbs = f'<h3>📎 実際のパワーポイント（プレビュー）</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0">{_thumb_html("p3b","🔴 修正前")}{_thumb_html("p3a","🟢 修正後")}</div>'

    # --- New content blocks ---
    l0_html = extras.excel_l0_html()
    ppt1_meth = extras.ppt1_methodology()
    ppt2_meth = extras.ppt2_methodology()
    ppt3_meth = extras.ppt3_methodology()
    ppt1_proc = extras.ppt1_process()
    ppt2_proc = extras.ppt2_process()
    ppt3_proc = extras.ppt3_process()
    ppt_vcss = extras.ppt_visual_css()
    ppt_examples = extras.ppt_slide_examples()
    ppt_frameworks = extras.ppt_frameworks_visual()
    ppt_design = extras.ppt_design_rules()
    ppt_charts = extras.ppt_chart_selector()
    lt_html = lt_content.lt_panels_html()
    lt_js = lt_content.lt_js_code()
    chat_css = extras.ai_chat_css()
    chat_html = extras.ai_chat_html()
    chat_js = extras.ai_chat_js()

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ビジネススキル自習キット</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{{--primary:#1F4E79;--accent:#4472C4;--green:#70AD47;--orange:#ED7D31;--red:#C00000;--bg:#F8F9FA;--card:#FFF;--text:#333;--text-light:#666;--border:#DEE2E6}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.app{{display:grid;grid-template-columns:260px 1fr;min-height:100vh}}
/* Sidebar */
.sidebar{{background:#1a1a2e;color:#fff;padding:0;overflow-y:auto;position:sticky;top:0;height:100vh}}
.sidebar-header{{padding:20px;border-bottom:1px solid rgba(255,255,255,.1)}}
.sidebar-header h1{{font-size:1rem;margin-bottom:4px}}
.sidebar-header p{{font-size:.75rem;opacity:.6}}
.progress-mini{{background:rgba(255,255,255,.15);border-radius:10px;height:8px;margin-top:10px}}
.progress-mini-fill{{background:linear-gradient(90deg,var(--accent),var(--green));height:100%;border-radius:10px;transition:width .3s}}
.nav-section{{padding:16px 20px 6px;font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;opacity:.5;margin-top:8px}}
.nav-item{{display:flex;justify-content:space-between;align-items:center;padding:10px 20px;cursor:pointer;font-size:.88rem;border-left:3px solid transparent;transition:all .15s}}
.nav-item:hover{{background:rgba(255,255,255,.06)}}
.nav-item.active{{background:rgba(68,114,196,.2);border-left-color:var(--accent)}}
.nav-badge{{font-size:.7rem;opacity:.5}}
.nav-badge.done{{color:var(--green);opacity:1}}
.reset-all-btn{{margin:20px;padding:8px;background:none;border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.5);border-radius:6px;cursor:pointer;font-size:.8rem;width:calc(100% - 40px)}}
.reset-all-btn:hover{{background:rgba(255,0,0,.15);border-color:var(--red);color:#fff}}
/* Main */
.main-content{{padding:32px;overflow-y:auto;max-width:960px}}
.lesson-panel{{display:none}}
.lesson-panel.active{{display:block}}
.lesson-title{{color:var(--primary);font-size:1.5rem;margin-bottom:4px}}
.lesson-subtitle{{color:var(--text-light);margin-bottom:20px;font-size:.95rem}}
/* Dashboard */
.dash-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:24px 0}}
.dash-card{{background:var(--card);border-radius:12px;padding:20px;border:1px solid var(--border);text-align:center}}
.dash-card h3{{font-size:.95rem;color:var(--primary);margin-bottom:8px}}
.dash-card .num{{font-size:2rem;font-weight:700;color:var(--accent)}}
.dash-card .den{{font-size:.85rem;color:var(--text-light)}}
/* Textbook */
.textbook{{background:#FAFBFC;border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:28px}}
.tb-chapter{{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid var(--accent)}}
.tb-chapter-icon{{width:36px;height:36px;background:var(--accent);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;flex-shrink:0}}
.tb-chapter-title{{font-size:1.15rem;font-weight:700;color:var(--primary)}}
.tb-section{{font-size:1rem;font-weight:700;color:var(--primary);margin:20px 0 8px;padding-left:10px;border-left:4px solid var(--accent)}}
.textbook p,.textbook li{{font-size:.9rem;line-height:1.85;margin:8px 0}}
.textbook ul{{padding-left:20px}}
.tb-example{{background:#F3F8FF;border-left:4px solid var(--accent);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.88rem;line-height:1.8}}
.tb-example .label{{font-weight:700;color:var(--accent);display:block;margin-bottom:4px;font-size:.8rem}}
.tb-highlight{{background:#FFF8E1;border:1px solid #FFD54F;border-radius:8px;padding:14px 18px;margin:14px 0;font-size:.9rem;line-height:1.8}}
.tb-highlight strong{{color:#E65100}}
.tb-tip{{background:#E8F5E9;border-radius:8px;padding:14px 18px;margin:14px 0;font-size:.88rem;line-height:1.8}}
.tb-tip::before{{content:"💡 ポイント";display:block;font-weight:700;color:#2E7D32;margin-bottom:4px;font-size:.82rem}}
.tb-warn{{background:#FFF3E0;border-radius:8px;padding:14px 18px;margin:14px 0;font-size:.88rem;line-height:1.8}}
.tb-warn::before{{content:"⚠ 注意";display:block;font-weight:700;color:#E65100;margin-bottom:4px;font-size:.82rem}}
.tb-keyword{{display:inline-block;background:#E3F2FD;color:var(--primary);font-weight:700;padding:1px 8px;border-radius:4px;font-size:.88rem}}
.tb-compare{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}}
.tb-bad,.tb-good{{border-radius:8px;padding:14px 16px;font-size:.88rem;line-height:1.7}}
.tb-bad{{background:#FFF0F0;border:1px solid #FFCDD2}}
.tb-bad::before{{content:"✕ よくない例";display:block;font-weight:700;color:var(--red);margin-bottom:6px;font-size:.82rem}}
.tb-good{{background:#F0FFF4;border:1px solid #C8E6C9}}
.tb-good::before{{content:"◯ 良い例";display:block;font-weight:700;color:#2E7D32;margin-bottom:6px;font-size:.82rem}}
.tb-diagram{{text-align:center;padding:18px;margin:14px 0;background:#FAFAFA;border-radius:8px;font-size:.9rem;line-height:2}}
.tb-hidden{{display:none}}.tb-hidden.show{{display:block}}
.tb-toggle{{background:none;border:1px dashed var(--accent);color:var(--accent);padding:8px 16px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:.85rem;margin-top:8px;width:100%;text-align:left}}
.tb-toggle:hover{{background:#F3F8FF}}
/* Tables */
.table-scroll{{overflow-x:auto;margin-bottom:20px;border-radius:8px;border:1px solid var(--border)}}
.data-table{{width:100%;border-collapse:collapse;font-size:.82rem;white-space:nowrap}}
.data-table th{{background:var(--primary);color:#fff;padding:8px 12px;text-align:center;font-weight:600;position:sticky;top:0}}
.data-table td{{padding:6px 12px;border-bottom:1px solid #eee;text-align:center}}
.data-table .stripe{{background:#F8F9FA}}
.data-table tr:hover{{background:#E8F0FE}}
/* Questions */
.question-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px 20px;margin-bottom:12px}}
.q-header{{font-weight:700;color:var(--primary);margin-bottom:8px}}
.q-hint-toggle{{color:var(--accent);cursor:pointer;font-size:.9rem;margin-bottom:6px;user-select:none}}
.q-hint-toggle:hover{{text-decoration:underline}}
.q-hint{{background:#FFF8E1;border-left:3px solid var(--orange);padding:8px 14px;border-radius:4px;margin-bottom:10px;font-size:.9rem}}
.q-input{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}}
.q-input input{{flex:1;min-width:180px;padding:10px 14px;border:2px solid var(--border);border-radius:8px;font-size:1rem;font-family:inherit}}
.q-input input:focus{{outline:none;border-color:var(--accent)}}
.q-input input.ok{{border-color:var(--green);background:#F0FFF0}}
.q-input input.ng{{border-color:var(--red);background:#FFF0F0}}
.grade-btn{{background:var(--green);color:#fff;border:none;padding:10px 18px;border-radius:8px;cursor:pointer;font-weight:600;font-size:.95rem;white-space:nowrap}}
.grade-btn:hover{{opacity:.85}}
.result{{margin-top:6px;font-size:.95rem}}
.rok{{color:#006100;font-weight:700}}.rng{{color:#9C0006;font-weight:700}}
.show-answers-btn{{background:var(--accent);color:#fff;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-weight:600;font-size:.95rem;margin-top:16px}}
.show-answers-btn:hover{{opacity:.85}}
/* Pivot */
.pivot-row{{display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap}}
.pivot-label{{min-width:130px;font-weight:600;color:var(--primary)}}
.pivot-row input{{flex:1;min-width:140px;max-width:220px;padding:8px 12px;border:2px solid var(--border);border-radius:8px;font-size:.95rem;font-family:inherit}}
.pivot-row input:focus{{outline:none;border-color:var(--accent)}}
.pivot-row input.ok{{border-color:var(--green);background:#F0FFF0}}
.pivot-row input.ng{{border-color:var(--red);background:#FFF0F0}}
.kpi-section-header{{background:#D6E4F0;color:var(--primary);font-weight:700;padding:10px 16px;border-radius:8px;margin:16px 0 10px}}
/* PPT Slides */
.slide-card{{border-radius:10px;overflow:hidden;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,.08)}}
.slide-bad{{border:2px solid #FFCDD2}}
.slide-good{{border:2px solid #C8E6C9}}
.slide-header{{background:#f5f5f5;padding:12px 18px;font-weight:700;font-size:1rem;color:var(--primary)}}
.slide-body{{padding:16px 18px}}
.slide-header-bar{{background:var(--primary);color:#fff;padding:10px 18px;font-weight:700;font-size:.95rem}}
.slide-message{{padding:10px 18px;font-weight:700;color:var(--accent);font-size:.95rem}}
.slide-bullets{{padding:4px 18px 14px 36px;font-size:.85rem;line-height:1.7;color:var(--text)}}
.slide-bullets li{{margin:3px 0}}
.scenario-box{{background:#F3F8FF;border:1px solid var(--accent);border-radius:10px;padding:18px 22px;margin:16px 0;font-size:.9rem;line-height:1.8}}
.checklist{{margin:12px 0 20px}}
.checklist label{{display:block;padding:8px 12px;margin:4px 0;border-radius:6px;cursor:pointer;font-size:.9rem;transition:background .2s}}
.checklist label:hover{{background:#E8F0FE}}
.checklist input{{margin-right:8px}}
.reveal-btn{{background:var(--accent);color:#fff;border:none;padding:12px 24px;border-radius:8px;cursor:pointer;font-weight:600;font-size:1rem;margin:8px 0 16px}}
.reveal-btn:hover{{opacity:.85}}
.explanation{{background:#F3F8FF;border-radius:10px;padding:18px 22px;margin:16px 0;font-size:.88rem;line-height:1.8}}
.explanation h4{{color:var(--primary);margin-bottom:8px}}
.explanation li{{margin:6px 0}}
/* LT */
.lt-question{{background:var(--bg);border-radius:8px;padding:16px;margin-bottom:16px;border-left:4px solid var(--accent)}}
.lt-question p{{margin-bottom:12px;font-weight:500}}
.options label{{display:block;padding:8px 12px;margin:4px 0;border-radius:6px;cursor:pointer;border:1px solid transparent;transition:background .2s}}
.options label:hover{{background:#E8F0FE}}
.options input{{margin-right:8px}}
.options label.correct{{background:#C6EFCE;border-color:var(--green)}}
.options label.wrong{{background:#FFC7CE;border-color:var(--red)}}
.feedback{{margin-top:8px;padding:8px 12px;border-radius:6px;font-size:.9rem;display:none}}
.feedback.show{{display:block}}
.feedback.correct{{background:#C6EFCE;color:#006100}}
.feedback.wrong{{background:#FFC7CE;color:#9C0006}}
.check-btn{{background:var(--accent);color:#fff;border:none;padding:8px 20px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:.9rem;margin-top:8px}}
.check-btn:hover{{opacity:.9}}.check-btn:disabled{{opacity:.5;cursor:not-allowed}}
.tree-container{{padding:16px}}
.tree-node{{margin-left:24px;padding:4px 0}}
.tree-node-content{{display:flex;align-items:center;gap:8px;margin-bottom:4px}}
.tree-node-content input{{border:1px solid var(--border);border-radius:4px;padding:6px 10px;font-family:inherit;font-size:.9rem;width:200px}}
.tree-btn{{background:none;border:1px solid var(--border);border-radius:4px;padding:4px 8px;cursor:pointer;font-size:.8rem}}
.tree-btn:hover{{background:#E8F0FE}}.tree-btn.remove{{color:var(--red)}}
.model-answer{{background:var(--bg);border:2px dashed var(--accent);border-radius:8px;padding:16px;margin-top:16px;display:none}}
.model-answer h4{{color:var(--accent);margin-bottom:8px}}.model-answer.show{{display:block}}
.model-tree{{margin-left:0;font-size:.9rem}}.model-tree li{{margin:4px 0;list-style:none}}
.model-tree li::before{{content:"├─ ";color:var(--accent)}}.model-tree>li::before{{content:""}}
.model-tree ul{{margin-left:20px}}
.step-form textarea{{width:100%;min-height:80px;border:1px solid var(--border);border-radius:6px;padding:10px;font-family:inherit;font-size:.9rem;resize:vertical;margin-bottom:8px}}
.step-nav{{display:flex;justify-content:space-between;margin-top:12px}}
.step-indicator{{display:flex;gap:8px;margin-bottom:12px}}
.step-dot{{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;background:var(--border);color:var(--text-light)}}
.step-dot.active{{background:var(--accent);color:#fff}}.step-dot.done{{background:var(--green);color:#fff}}
h3{{color:var(--primary);margin:20px 0 12px;font-size:1.15rem}}
/* Hamburger */
.hamburger{{display:none;position:fixed;top:10px;left:10px;z-index:100;background:var(--primary);color:#fff;border:none;width:40px;height:40px;border-radius:8px;font-size:1.2rem;cursor:pointer}}
@media(max-width:768px){{
  .app{{grid-template-columns:1fr}}
  .sidebar{{position:fixed;left:-280px;top:0;width:280px;z-index:99;transition:left .3s}}
  .sidebar.open{{left:0}}
  .hamburger{{display:flex;align-items:center;justify-content:center}}
  .main-content{{padding:16px;padding-top:56px}}
  .tb-compare{{grid-template-columns:1fr}}
  .dash-grid{{grid-template-columns:1fr}}
}}
{ppt_vcss}
{chat_css}
</style>
</head>
<body>
<button class="hamburger" onclick="document.querySelector('.sidebar').classList.toggle('open')">☰</button>
<div class="app">
<aside class="sidebar">
  <div class="sidebar-header">
    <h1>ビジネススキル自習キット</h1>
    <p>新人営業の実践トレーニング</p>
    <div class="progress-mini"><div class="progress-mini-fill" id="globalProgress" style="width:0%"></div></div>
  </div>
  <div class="nav-section">📊 Excel</div>
  <div class="nav-item active" data-lesson="dashboard" onclick="nav('dashboard')">🏠 ダッシュボード<span class="nav-badge" id="nb-dash"></span></div>
  <div class="nav-item" data-lesson="excel0" onclick="nav('excel0')">L0: Excel入門<span class="nav-badge" id="nb-e0"></span></div>
  <div class="nav-item" data-lesson="excel1" onclick="nav('excel1')">L1: 基本関数<span class="nav-badge" id="nb-e1"></span></div>
  <div class="nav-item" data-lesson="excel2" onclick="nav('excel2')">L2: VLOOKUP<span class="nav-badge" id="nb-e2"></span></div>
  <div class="nav-item" data-lesson="excel3" onclick="nav('excel3')">L3: IF/SUMIFS<span class="nav-badge" id="nb-e3"></span></div>
  <div class="nav-item" data-lesson="excel4" onclick="nav('excel4')">L4: ピボット<span class="nav-badge" id="nb-e4"></span></div>
  <div class="nav-item" data-lesson="excel5" onclick="nav('excel5')">L5: KPI<span class="nav-badge" id="nb-e5"></span></div>
  <div class="nav-section">📑 PowerPoint</div>
  <div class="nav-item" data-lesson="ppt1" onclick="nav('ppt1')">L1: 1スライド1メッセージ<span class="nav-badge" id="nb-p1"></span></div>
  <div class="nav-item" data-lesson="ppt2" onclick="nav('ppt2')">L2: 図解化<span class="nav-badge" id="nb-p2"></span></div>
  <div class="nav-item" data-lesson="ppt3" onclick="nav('ppt3')">L3: 提案書<span class="nav-badge" id="nb-p3"></span></div>
  <div class="nav-section">🧠 ロジカルシンキング</div>
  <div class="nav-item" data-lesson="lt1" onclick="nav('lt1')">L1: MECE<span class="nav-badge" id="nb-l1"></span></div>
  <div class="nav-item" data-lesson="lt2" onclick="nav('lt2')">L2: ロジックツリー<span class="nav-badge" id="nb-l2"></span></div>
  <div class="nav-item" data-lesson="lt3" onclick="nav('lt3')">L3: So What?<span class="nav-badge" id="nb-l3"></span></div>
  <div class="nav-item" data-lesson="lt4" onclick="nav('lt4')">L4: 総合演習<span class="nav-badge" id="nb-l4"></span></div>
  <button class="reset-all-btn" onclick="if(confirm('全進捗リセット?')){{localStorage.removeItem('bsk');localStorage.removeItem('lt-state');location.reload()}}">全進捗リセット</button>
</aside>

<main class="main-content">

<!-- ===== Dashboard ===== -->
<div id="dashboard" class="lesson-panel active">
  <h2 class="lesson-title">ビジネススキル自習キット</h2>
  <p class="lesson-subtitle">ミルクネクスト株式会社 — 新人営業のための実践トレーニング</p>
  <div class="dash-grid">
    <div class="dash-card"><h3>📊 Excel</h3><div class="num" id="dash-e">0</div><div class="den">/ 53 問</div></div>
    <div class="dash-card"><h3>📑 PowerPoint</h3><div class="num" id="dash-p">0</div><div class="den">/ 3 レッスン</div></div>
    <div class="dash-card"><h3>🧠 ロジカルシンキング</h3><div class="num" id="dash-l">0</div><div class="den">/ 16 問</div></div>
  </div>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">📖</div><div class="tb-chapter-title">学習の進め方</div></div>
    <p>左のメニューからレッスンを選んでください。おすすめの順番：</p>
    <ol style="margin:12px 0 12px 20px">
      <li><strong>Excel Lesson 0〜5</strong> — Excel入門からKPIダッシュボードまで</li>
      <li><strong>PPT Lesson 1〜3</strong> — スライド改善から提案書作成まで</li>
      <li><strong>ロジカルシンキング Lesson 1〜4</strong> — MECE・ロジックツリー・So What</li>
    </ol>
    <p>全レッスン共通で「ミルクネクスト株式会社」（架空の乳業メーカー）を舞台にしています。進捗はブラウザに自動保存されます。</p>
  </div>
</div>


{l0_html}

<!-- ===== Excel 1 ===== -->
<div id="excel1" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 1: 基本関数</h2>
  <p class="lesson-subtitle">SUM / AVERAGE / COUNT / COUNTIF / SUMIF</p>
  <p style="margin-bottom:16px"><a href="excel/Lesson1_基本関数.xlsx" download style="display:inline-flex;align-items:center;gap:6px;background:#E8F0FE;color:var(--accent);padding:8px 16px;border-radius:8px;text-decoration:none;font-size:.88rem;font-weight:600">📥 Excelファイルをダウンロード</a></p>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">1</div><div class="tb-chapter-title">Excelの基本関数を学ぼう</div></div>
    <h4 class="tb-section">関数とは？</h4>
    <p>Excelの<span class="tb-keyword">関数</span>は、セルに「=」を入力してから書く<strong>計算命令</strong>のことです。
    たとえば <code>=SUM(A1:A10)</code> と書くと、A1からA10までの合計を自動計算します。</p>
    <div class="tb-highlight"><strong>基本ルール：</strong> 関数は必ず <code>=</code> から始め、<code>関数名(引数)</code> の形で書きます。<br>引数（ひきすう）= 関数に渡すデータのこと。セル範囲や条件を指定します。</div>

    <h4 class="tb-section">この演習で使う5つの関数</h4>
    <div class="tb-example"><span class="label">SUM — 合計</span><code>=SUM(H2:H201)</code><br>指定範囲の数値を全部足します。お小遣い帳の「合計」を出すイメージ。</div>
    <div class="tb-example"><span class="label">AVERAGE — 平均</span><code>=AVERAGE(H2:H201)</code><br>指定範囲の平均値。テストの平均点を出すイメージ。</div>
    <div class="tb-example"><span class="label">COUNT — 件数</span><code>=COUNT(A2:A201)</code><br>数値が入っているセルの個数を数えます。「データは何件あるか？」を知りたいとき。</div>
    <div class="tb-example"><span class="label">COUNTIF — 条件付き件数</span><code>=COUNTIF(J2:J201,"東京")</code><br>条件に合うセルだけを数えます。「東京の売上は何件？」のような絞り込み。</div>
    <div class="tb-example"><span class="label">SUMIF — 条件付き合計</span><code>=SUMIF(E2:E201,"牛乳",H2:H201)</code><br>条件に合う行だけの合計。「牛乳の売上合計は？」のような絞り込み計算。</div>
  </div>
  <h3>📋 売上データ（参照用）</h3>
  {sales_table}
  <h3>✏️ 問題（10問）</h3>
  {_q_cards("e1", e1)}
  {_answers_block("e1", e1)}
</div>

<!-- ===== Excel 2 ===== -->
<div id="excel2" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 2: VLOOKUP / INDEX-MATCH</h2>
  <p class="lesson-subtitle">テーブル参照 — 別の表からデータを引っ張る</p>
  <p style="margin-bottom:16px"><a href="excel/Lesson2_VLOOKUP_INDEX-MATCH.xlsx" download style="display:inline-flex;align-items:center;gap:6px;background:#E8F0FE;color:var(--accent);padding:8px 16px;border-radius:8px;text-decoration:none;font-size:.88rem;font-weight:600">📥 Excelファイルをダウンロード</a></p>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">2</div><div class="tb-chapter-title">VLOOKUP で表を検索しよう</div></div>
    <h4 class="tb-section">VLOOKUPとは？</h4>
    <p>電話帳で名前から電話番号を調べるように、<strong>ある表の中からキーワードで値を検索する</strong>関数です。</p>
    <div class="tb-example"><span class="label">書式</span><code>=VLOOKUP(検索値, 範囲, 列番号, FALSE)</code><br>
    <strong>検索値:</strong> 探したい値（例："P003"）<br>
    <strong>範囲:</strong> 検索する表の範囲<br>
    <strong>列番号:</strong> 見つかった行の何列目を返すか<br>
    <strong>FALSE:</strong> 完全一致で検索（必ずFALSEを指定）</div>
    <h4 class="tb-section">INDEX-MATCH とは？</h4>
    <p>VLOOKUPの上位互換です。検索列が表の左端でなくても使えます。</p>
    <div class="tb-example"><span class="label">書式</span><code>=INDEX(取得範囲, MATCH(検索値, 検索範囲, 0))</code><br>
    MATCH: 検索値が何行目にあるか調べる<br>
    INDEX: その行の値を返す</div>
  </div>
  <h3>📋 商品マスタ</h3>{pt}
  <h3>📋 顧客マスタ（先頭10件）</h3>{ct}
  <h3>✏️ 問題（8問）</h3>
  {_q_cards("e2", e2)}
  {_answers_block("e2", e2)}
</div>

<!-- ===== Excel 3 ===== -->
<div id="excel3" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 3: IF / SUMIFS / COUNTIFS</h2>
  <p class="lesson-subtitle">条件分岐と複数条件の集計</p>
  <p style="margin-bottom:16px"><a href="excel/Lesson3_IF_SUMIFS_COUNTIFS.xlsx" download style="display:inline-flex;align-items:center;gap:6px;background:#E8F0FE;color:var(--accent);padding:8px 16px;border-radius:8px;text-decoration:none;font-size:.88rem;font-weight:600">📥 Excelファイルをダウンロード</a></p>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">3</div><div class="tb-chapter-title">条件を使った集計をマスターしよう</div></div>
    <h4 class="tb-section">IF関数 — 条件分岐</h4>
    <p>「もし〜なら A、そうでなければ B」を実現します。</p>
    <div class="tb-example"><code>=IF(H2>=1000000, "大型案件", "通常")</code><br>金額が100万以上なら「大型案件」、それ以外は「通常」。</div>
    <h4 class="tb-section">SUMIFS — 複数条件の合計</h4>
    <p>SUMIFの複数条件版。<strong>注意: 引数の順番がSUMIFと違います</strong>。</p>
    <div class="tb-example"><code>=SUMIFS(合計範囲, 条件範囲1, "条件1", 条件範囲2, "条件2")</code><br>
    例: <code>=SUMIFS(H:H, J:J, "東京", E:E, "牛乳")</code> → 東京×牛乳の合計</div>
    <h4 class="tb-section">COUNTIFS — 複数条件の件数</h4>
    <div class="tb-example"><code>=COUNTIFS(範囲1, "条件1", 範囲2, "条件2")</code></div>
    <div class="tb-tip">比較演算子の使い方: <code>"&gt;=500000"</code> で「50万以上」を指定できます。</div>
  </div>
  <h3>📋 売上データ</h3>{_sales_table_html(d["sales_rows"], 15, True)}
  <h3>✏️ 問題（10問）</h3>
  {_q_cards("e3", e3)}
  {_answers_block("e3", e3)}
</div>

<!-- ===== Excel 4 ===== -->
<div id="excel4" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 4: ピボットテーブル + チャート</h2>
  <p class="lesson-subtitle">データを様々な軸で集計する</p>
  <p style="margin-bottom:16px"><a href="excel/Lesson4_ピボットテーブル_チャート.xlsx" download style="display:inline-flex;align-items:center;gap:6px;background:#E8F0FE;color:var(--accent);padding:8px 16px;border-radius:8px;text-decoration:none;font-size:.88rem;font-weight:600">📥 Excelファイルをダウンロード</a></p>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">4</div><div class="tb-chapter-title">ピボットテーブルの考え方</div></div>
    <h4 class="tb-section">ピボットテーブルとは？</h4>
    <p>大量のデータを<strong>地域別・カテゴリ別・月別</strong>など、様々な切り口で集計する機能です。</p>
    <p>この演習では理解を深めるため<strong>手動集計</strong>してもらいます。SUMIF/COUNTIFを使って各値を求めてください。</p>
    <h4 class="tb-section">クロス集計</h4>
    <div class="tb-example">2つの軸を掛け合わせる集計です。例:「東京×牛乳」の売上合計。<br>SUMIFSで <code>=SUMIFS(金額, 地域, "東京", カテゴリ, "牛乳")</code></div>
  </div>
  <h3>📋 売上データ</h3>{_sales_table_html(d["sales_rows"], 15, True)}
  <h3>✏️ タスク1: 地域別売上合計</h3>
  {e4_regions_html}
  <h3>✏️ タスク2: カテゴリ別売上合計</h3>
  {e4_cats_html}
  <h3>✏️ タスク3: 担当者別売上件数</h3>
  {e4_reps_html}
  <h3>✏️ タスク4: 月別売上TOP3</h3>
  <p style="color:var(--text-light);font-size:.9rem;margin-bottom:12px">月別売上を計算し、上位3ヶ月の月名(YYYY-MM)と金額を入力</p>
  <div class="pivot-row"><span class="pivot-label">1位</span>
    <input type="text" id="e4-top-m0" placeholder="YYYY-MM" style="max-width:120px">
    <input type="text" id="e4-top-a0" placeholder="金額" inputmode="numeric" onkeydown="if(event.key==='Enter')gradeTop3(0)">
    <button class="grade-btn" onclick="gradeTop3(0)">採点</button><span class="result" id="e4-top-r0"></span></div>
  <div class="pivot-row"><span class="pivot-label">2位</span>
    <input type="text" id="e4-top-m1" placeholder="YYYY-MM" style="max-width:120px">
    <input type="text" id="e4-top-a1" placeholder="金額" inputmode="numeric" onkeydown="if(event.key==='Enter')gradeTop3(1)">
    <button class="grade-btn" onclick="gradeTop3(1)">採点</button><span class="result" id="e4-top-r1"></span></div>
  <div class="pivot-row"><span class="pivot-label">3位</span>
    <input type="text" id="e4-top-m2" placeholder="YYYY-MM" style="max-width:120px">
    <input type="text" id="e4-top-a2" placeholder="金額" inputmode="numeric" onkeydown="if(event.key==='Enter')gradeTop3(2)">
    <button class="grade-btn" onclick="gradeTop3(2)">採点</button><span class="result" id="e4-top-r2"></span></div>
  <h3>✏️ タスク5: 東京×牛乳 クロス集計</h3>
  <div class="pivot-row"><span class="pivot-label">東京 × 牛乳</span>
    <input type="text" id="e4-cross" inputmode="numeric" placeholder="金額" onkeydown="if(event.key==='Enter')gradePivot('e4-cross',{e4['cross']})">
    <button class="grade-btn" onclick="gradePivot('e4-cross',{e4['cross']})">採点</button>
    <span class="result" id="e4-cross-r"></span></div>
  <button class="show-answers-btn" onclick="toggleEl('e4-answers')">📝 模範解答を表示</button>
  <div class="tb-hidden" id="e4-answers"><div class="tb-example">{e4_answers_html}</div></div>
</div>

<!-- ===== Excel 5 ===== -->
<div id="excel5" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 5: KPIダッシュボード</h2>
  <p class="lesson-subtitle">総合演習 — 全体KPI・担当者・時系列・エリア分析</p>
  <p style="margin-bottom:16px"><a href="excel/Lesson5_KPIダッシュボード.xlsx" download style="display:inline-flex;align-items:center;gap:6px;background:#E8F0FE;color:var(--accent);padding:8px 16px;border-radius:8px;text-decoration:none;font-size:.88rem;font-weight:600">📥 Excelファイルをダウンロード</a></p>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">5</div><div class="tb-chapter-title">KPIダッシュボードを完成させよう</div></div>
    <h4 class="tb-section">KPIとは？</h4>
    <p><span class="tb-keyword">KPI</span>（Key Performance Indicator）= 目標達成度を測る数値指標です。</p>
    <div class="tb-example">営業のKPI例: 売上合計・取引件数・平均取引額・目標達成率・顧客数</div>
    <h4 class="tb-section">達成率の計算</h4>
    <div class="tb-example"><strong>目標達成率 = 実績 ÷ 目標</strong><br>
    例: 目標5,000万、実績2,400万 → 0.48（48%）<br>この演習では<strong>小数で入力</strong>してください（48% → 0.48）</div>
    <h4 class="tb-section">上半期・下半期</h4>
    <div class="tb-example">上半期: 2025年4月〜9月 / 下半期: 2025年10月〜2026年3月</div>
  </div>
  <h3>📋 売上データ</h3>{sales_table_10}
  <h3>📋 担当者目標</h3>{rt}
  <div class="kpi-section-header">■ 全体KPI（Q1-Q5）</div>
  {_q_cards("e5", e5[:5])}
  <div class="kpi-section-header">■ 担当者分析（Q6-Q8）</div>
  {_q_cards_offset("e5", e5[5:8], 5)}
  <div class="kpi-section-header">■ 時系列分析（Q9-Q13）</div>
  {_q_cards_offset("e5", e5[8:13], 8)}
  <div class="kpi-section-header">■ エリア・カテゴリ分析（Q14-Q15）</div>
  {_q_cards_offset("e5", e5[13:], 13)}
  {_answers_block("e5", e5)}
</div>

<!-- ===== PPT 1 ===== -->
<div id="ppt1" class="lesson-panel">
  <h2 class="lesson-title">📑 PPT Lesson 1: 1スライド1メッセージ</h2>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">1</div><div class="tb-chapter-title">1枚のスライドに伝えることは1つだけ</div></div>
    <h4 class="tb-section">なぜ大事？</h4>
    <p>聴衆は同時に複数のメッセージを処理できません。<strong>1枚に詰め込むと全部伝わらない</strong>のです。</p>
    <div class="tb-compare">
      <div class="tb-bad">情報を全部1枚に押し込む<br>→ 文字が小さく、読む気が失せる</div>
      <div class="tb-good">1スライド1メッセージに分割<br>→ 10秒で理解できる</div>
    </div>
    <div class="tb-tip"><strong>ルール:</strong> ①タイトルにメッセージを書く ②箇条書きは3〜5個 ③文字は最低24pt</div>
    {ppt1_meth}
    {ppt_design}
    {ppt_frameworks}
  </div>
  <h3>🔴 Before（修正前）</h3>
  <div class="slide-card slide-bad"><div class="slide-header">上半期営業成績サマリー</div><div class="slide-body"><p style="font-size:.75rem;line-height:1.6">当社ミルクネクスト株式会社の法人営業部は、2025年度上半期において前年同期比118%の売上を達成しました。特に東京エリアのスーパーマーケット向け牛乳カテゴリの伸びが顕著で、新規取引先獲得数は前期比30%増加しています。一方、大阪エリアではヨーグルト製品の需要が高まっており、ギリシャ濃密ヨーグルトの採用店舗が150店を超えました。名古屋エリアでは飲食チェーン向けチーズ案件が進行中。福岡エリアはコンビニ本部への新規提案が課題。札幌エリアはバター・生クリームの業務用アップセルに注力。SFAツール活用度向上の研修を予定。欠品・配送遅延への不満も増加。</p></div></div>
  <div class="slide-card slide-bad" style="margin-top:8px"><div class="slide-header">下半期重点施策</div><div class="slide-body"><p style="font-size:.75rem;line-height:1.6">5つの重点施策を推進。第1に量販店への棚割り提案強化。第2にPB受注の拡大。第3に業務用市場の開拓。第4に給食・病院向けの安定供給体制。第5に新商品（プロテインヨーグルト）の市場投入。これらで下半期125%達成を目指す。</p></div></div>
  <h3>🤔 考えるポイント</h3>
  <div class="checklist">
    <label><input type="checkbox" id="ppt1-c0" onchange="pptCheck('ppt1')"> 1枚に何個のメッセージが入っているか数えてみよう</label>
    <label><input type="checkbox" id="ppt1-c1" onchange="pptCheck('ppt1')"> 10秒で理解できるか？</label>
    <label><input type="checkbox" id="ppt1-c2" onchange="pptCheck('ppt1')"> どこで分割すれば1スライド1メッセージになるか</label>
    <label><input type="checkbox" id="ppt1-c3" onchange="pptCheck('ppt1')"> タイトルだけで内容がわかるか</label>
  </div>
  <button class="reveal-btn" onclick="revealPpt('ppt1')">📝 模範解答を見る</button>
  <div class="tb-hidden" id="ppt1-model">
    <h3>🟢 After（7枚に分割）</h3>
    <div class="slide-card slide-good"><div class="slide-header-bar">上半期ハイライト</div><div class="slide-message">前年同期比118%達成、新規取引先30%増</div><ul class="slide-bullets"><li>東京: 牛乳カテゴリがスーパー向けに好調</li><li>大阪: ギリシャヨーグルト採用150店突破</li><li>名古屋: 飲食チェーン向けチーズ大型案件進行中</li><li>福岡: コンビニ本部への提案が課題</li><li>札幌: バター・生クリームの業務用アップセル注力</li></ul></div>
    <div class="slide-card slide-good" style="margin-top:8px"><div class="slide-header-bar">下半期戦略</div><div class="slide-message">5つの重点施策で前年同期比125%を目指す</div><ul class="slide-bullets"><li>① 量販店の棚割り提案強化</li><li>② PB受注拡大（コンビニ3社）</li><li>③ 業務用市場開拓（ホテル・レストラン）</li><li>④ 給食・病院の安定供給体制</li><li>⑤ 新商品投入（プロテインヨーグルト 10月）</li></ul></div>
    <div class="explanation"><h4>なぜ良いのか？</h4><ul><li><strong>2枚→7枚に分割:</strong> 各スライドの情報量が適切になり理解しやすい</li><li><strong>タイトル=メッセージ:</strong> 「前年同期比118%達成」など、タイトルだけで要点がわかる</li><li><strong>箇条書き3〜5個:</strong> 10秒で全体を把握できる量</li></ul>{ppt1_proc}</div>
  </div>
{ppt1_thumbs}
</div>

<!-- ===== PPT 2 ===== -->
<div id="ppt2" class="lesson-panel">
  <h2 class="lesson-title">📑 PPT Lesson 2: 図解化</h2>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">2</div><div class="tb-chapter-title">箇条書きを「図」に変換する力</div></div>
    <h4 class="tb-section">図解化とは？</h4>
    <p>テキストや箇条書きを<strong>図・矢印・チャート</strong>に変換すること。人間は文字より図の方が<strong>6倍記憶に残りやすい</strong>（ピクチャー・スーペリオリティ効果）。</p>
    <h4 class="tb-section">4つのパターン</h4>
    <div class="tb-example"><strong>① プロセス図:</strong> 順番がある情報 → 矢印でつなぐ<br><strong>② 構成比:</strong> 割合 → 棒/円グラフ<br><strong>③ マトリクス:</strong> 2軸で分類 → 4象限<br><strong>④ ピラミッド:</strong> 階層構造</div>
    <div class="tb-tip">「この情報は何の関係性を示しているか？」→ 順番ならプロセス図、割合なら構成比。</div>
    {ppt2_meth}
    {ppt_charts}
  </div>
  <h3>🔴 Before</h3>
  <div class="slide-card slide-bad"><div class="slide-header">営業プロセス</div><div class="slide-body"><p style="font-size:.75rem;line-height:1.7">・ステップ1: ターゲット選定 — 商圏分析で30件/月リストアップ<br>・ステップ2: 初回訪問 — バイヤー面談、仕入先・棚状況ヒアリング<br>・ステップ3: 試食・サンプル — 品質を体感してもらう<br>・ステップ4: 棚割り交渉 — リベート・棚位置・エンド陳列<br>・ステップ5: 納品・フォロー — 2週間後に売場チェック</p></div></div>
  <div class="slide-card slide-bad" style="margin-top:8px"><div class="slide-header">カテゴリ別売上構成</div><div class="slide-body"><p style="font-size:.75rem;line-height:1.7">・牛乳35% 前年比112%安定成長<br>・ヨーグルト28% 健康志向層に好評<br>・チーズ22% 飲食チェーンで評価高い<br>・バター・生クリーム15% 業務用安定</p></div></div>
  <h3>🤔 考えるポイント</h3>
  <div class="checklist">
    <label><input type="checkbox" id="ppt2-c0" onchange="pptCheck('ppt2')"> スライド1は「ステップ」→ プロセス図が適切？</label>
    <label><input type="checkbox" id="ppt2-c1" onchange="pptCheck('ppt2')"> スライド2は「割合」→ 棒グラフが適切？</label>
    <label><input type="checkbox" id="ppt2-c2" onchange="pptCheck('ppt2')"> キーワードだけで伝わるか？</label>
    <label><input type="checkbox" id="ppt2-c3" onchange="pptCheck('ppt2')"> 色で区別するとしたらどこに？</label>
  </div>
  <button class="reveal-btn" onclick="revealPpt('ppt2')">📝 模範解答を見る</button>
  <div class="tb-hidden" id="ppt2-model">
    <h3>🟢 After</h3>
    <div class="slide-card slide-good"><div class="slide-header-bar">営業プロセス</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:0;padding:16px 8px;flex-wrap:wrap">
        <div style="background:#4472C4;color:#fff;border-radius:10px;padding:10px;text-align:center;flex:1;max-width:120px"><div style="font-weight:700;font-size:.78rem">1. ターゲット<br>選定</div><div style="font-size:.65rem;margin-top:4px;opacity:.9">商圏分析<br>30件/月</div></div>
        <div style="color:#999;padding:0 2px">→</div>
        <div style="background:#ED7D31;color:#fff;border-radius:10px;padding:10px;text-align:center;flex:1;max-width:120px"><div style="font-weight:700;font-size:.78rem">2. 初回訪問<br>ヒアリング</div><div style="font-size:.65rem;margin-top:4px;opacity:.9">バイヤー面談<br>棚状況</div></div>
        <div style="color:#999;padding:0 2px">→</div>
        <div style="background:#70AD47;color:#fff;border-radius:10px;padding:10px;text-align:center;flex:1;max-width:120px"><div style="font-weight:700;font-size:.78rem">3. 試食<br>サンプル</div><div style="font-size:.65rem;margin-top:4px;opacity:.9">品質を体感<br>ヨーグルト・チーズ</div></div>
        <div style="color:#999;padding:0 2px">→</div>
        <div style="background:#FFC000;color:#fff;border-radius:10px;padding:10px;text-align:center;flex:1;max-width:120px"><div style="font-weight:700;font-size:.78rem">4. 棚割り<br>条件交渉</div><div style="font-size:.65rem;margin-top:4px;opacity:.9">リベート<br>エンド陳列</div></div>
        <div style="color:#999;padding:0 2px">→</div>
        <div style="background:#A5A5A5;color:#fff;border-radius:10px;padding:10px;text-align:center;flex:1;max-width:120px"><div style="font-weight:700;font-size:.78rem">5. 納品<br>フォロー</div><div style="font-size:.65rem;margin-top:4px;opacity:.9">2週間後確認<br>リピート提案</div></div>
      </div>
    </div>
    <div class="slide-card slide-good" style="margin-top:8px"><div class="slide-header-bar">カテゴリ別売上構成</div>
      <div style="display:flex;margin:14px 16px 8px;border-radius:6px;overflow:hidden;height:36px">
        <div style="width:35%;background:#4472C4;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700">牛乳 35%</div>
        <div style="width:28%;background:#ED7D31;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700">ヨーグルト 28%</div>
        <div style="width:22%;background:#70AD47;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700">チーズ 22%</div>
        <div style="width:15%;background:#FFC000;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700">バター 15%</div>
      </div>
    </div>
    <div class="explanation"><h4>なぜ良いのか？</h4><ul><li>プロセスは<strong>フロー図</strong>に → 順番と全体像が一目</li><li>構成比は<strong>棒グラフ</strong>に → 大きさが直感的</li><li>長い文章はキーワードだけに絞った</li></ul>{ppt2_proc}</div>
  </div>
{ppt2_thumbs}
</div>

<!-- ===== PPT 3 ===== -->
<div id="ppt3" class="lesson-panel">
  <h2 class="lesson-title">📑 PPT Lesson 3: 提案書作成</h2>
  <div class="textbook">
    <div class="tb-chapter"><div class="tb-chapter-icon">3</div><div class="tb-chapter-title">取引先への提案書を作る</div></div>
    <h4 class="tb-section">提案書の基本構成</h4>
    <div class="tb-highlight"><strong>① 現状の課題</strong>「こんな問題がありますよね」<br><strong>② 解決策</strong>「こうすれば解決できます」<br><strong>③ 期待効果</strong>「するとこんないいことがあります」</div>
    <div class="tb-tip"><strong>数字で語る:</strong>「売上が上がります」ではなく「月額120万円の売上増（15%アップ）」と具体的に。<br><strong>相手目線:</strong> 主語を「弊社」から「御社」に変えるだけで印象が変わります。</div>
    <p><span class="tb-keyword">バイヤー</span> = スーパーの仕入れ担当者。棚に何を並べるか決める人。</p>
    <p><span class="tb-keyword">リベート</span> = メーカー→小売への販売報奨金。導入のインセンティブ。</p>
    {ppt3_meth}
    {ppt_examples}
  </div>
  <div class="scenario-box"><strong>🏢 シナリオ</strong><br>あなた: ミルクネクスト法人営業担当<br>取引先: グリーンバスケット（スーパー、関東50店舗）<br>状況: 乳製品売上95%で低迷、棚2本、健康志向ニーズ未対応<br>提案: ギリシャヨーグルト+牛乳の重点導入 → 棚3本化+月次試食 → 15%UP見込み</div>
  <h3>🤔 考えるポイント</h3>
  <div class="checklist">
    <label><input type="checkbox" id="ppt3-c0" onchange="pptCheck('ppt3')"> 課題を3つに絞るなら何を選ぶ？</label>
    <label><input type="checkbox" id="ppt3-c1" onchange="pptCheck('ppt3')"> 取引先のメリット中心に書けている？</label>
    <label><input type="checkbox" id="ppt3-c2" onchange="pptCheck('ppt3')"> 数字で語れている？（何%、何万円）</label>
    <label><input type="checkbox" id="ppt3-c3" onchange="pptCheck('ppt3')"> 自分がバイヤーなら受け入れる？</label>
  </div>
  <button class="reveal-btn" onclick="revealPpt('ppt3')">📝 模範解答を見る</button>
  <div class="tb-hidden" id="ppt3-model">
    <h3>🟢 After（模範の提案書）</h3>
    <div class="slide-card slide-good"><div style="background:#1F4E79;padding:30px;text-align:center;border-radius:6px"><div style="color:#fff;font-size:1.3rem;font-weight:700;margin-bottom:12px">乳製品売場活性化のご提案</div><div style="color:rgba(255,255,255,.8);font-size:.9rem">グリーンバスケット 御中</div><div style="color:rgba(255,255,255,.6);font-size:.8rem;margin-top:12px">ミルクネクスト株式会社 法人営業部</div></div></div>
    <div class="slide-card slide-good" style="margin-top:8px"><div class="slide-header-bar">1. 現状の課題</div><div style="padding:14px 20px">
      <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:12px"><div style="background:#ED7D31;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0">1</div><div><strong style="font-size:.88rem">乳製品売上の伸び悩み</strong><br><span style="font-size:.8rem;color:#666">前年比95%で低下傾向</span></div></div>
      <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:12px"><div style="background:#ED7D31;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0">2</div><div><strong style="font-size:.88rem">棚スペース不足</strong><br><span style="font-size:.8rem;color:#666">棚2本分、競合中心の品揃え</span></div></div>
      <div style="display:flex;gap:10px;align-items:flex-start"><div style="background:#C00000;color:#fff;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;flex-shrink:0">3</div><div><strong style="font-size:.88rem">集客施策の欠如</strong><br><span style="font-size:.8rem;color:#666">週末の来店動機が弱い</span></div></div>
    </div></div>
    <div class="slide-card slide-good" style="margin-top:8px"><div class="slide-header-bar">2. ソリューション提案</div><div style="display:grid;grid-template-columns:1fr auto 1fr;gap:0;padding:14px 12px;align-items:start">
      <div style="background:#E8F0FE;border:2px solid #4472C4;border-radius:10px;padding:12px"><div style="font-weight:700;color:#4472C4;text-align:center;margin-bottom:8px">棚割りリニューアル</div><ul style="font-size:.78rem;padding-left:16px;margin:0;line-height:1.7"><li>棚2本→3本に拡大</li><li>当社商品で1本分確保</li><li>牛乳をゴールデンゾーンに</li><li>ヨーグルトに健康訴求POP</li></ul></div>
      <div style="display:flex;align-items:center;font-size:1.5rem;color:#999;padding:30px 6px 0">+</div>
      <div style="background:#E8F8E8;border:2px solid #70AD47;border-radius:10px;padding:12px"><div style="font-weight:700;color:#70AD47;text-align:center;margin-bottom:8px">販促施策</div><ul style="font-size:.78rem;padding-left:16px;margin:0;line-height:1.7"><li>月次試食販売イベント</li><li>販売スタッフ2名派遣</li><li>季節限定先行販売権</li><li>SNS連動キャンペーン</li></ul></div>
    </div></div>
    <div class="slide-card slide-good" style="margin-top:8px"><div class="slide-header-bar">3. 導入効果</div><div style="padding:14px 20px">
      <table style="width:100%;border-collapse:collapse;font-size:.8rem;margin-bottom:14px"><tr style="background:#f0f4fa"><td style="padding:6px 12px;border:1px solid #ddd;font-weight:700">カテゴリ売上</td><td style="padding:6px 12px;border:1px solid #ddd">月額800万→<strong style="color:#4472C4">920万（15%UP）</strong></td></tr><tr><td style="padding:6px 12px;border:1px solid #ddd;font-weight:700">年間増収</td><td style="padding:6px 12px;border:1px solid #ddd"><strong style="color:#4472C4">約1,440万円</strong></td></tr><tr style="background:#f0f4fa"><td style="padding:6px 12px;border:1px solid #ddd;font-weight:700">導入月リベート</td><td style="padding:6px 12px;border:1px solid #ddd">仕入額の5%（<strong style="color:#4472C4">約50万円</strong>）</td></tr></table>
      <div style="display:flex;align-items:center;justify-content:center;gap:0">
        <div style="background:#4472C4;color:#fff;border-radius:8px;padding:10px;text-align:center;flex:1;max-width:140px"><div style="font-weight:700;font-size:.8rem">Month 1</div><div style="font-size:.65rem;margin-top:3px">棚割り変更</div></div>
        <div style="color:#999;padding:0 4px">→</div>
        <div style="background:#70AD47;color:#fff;border-radius:8px;padding:10px;text-align:center;flex:1;max-width:140px"><div style="font-weight:700;font-size:.8rem">Month 2</div><div style="font-size:.65rem;margin-top:3px">導入・試食</div></div>
        <div style="color:#999;padding:0 4px">→</div>
        <div style="background:#ED7D31;color:#fff;border-radius:8px;padding:10px;text-align:center;flex:1;max-width:140px"><div style="font-weight:700;font-size:.8rem">Month 3</div><div style="font-size:.65rem;margin-top:3px">効果検証</div></div>
      </div>
    </div></div>
    <div class="explanation"><h4>なぜ良いのか？</h4><ul><li>課題→提案→効果の<strong>3段階</strong>で論理展開</li><li>全て<strong>具体的な数字</strong>で語っている</li><li><strong>相手のメリット</strong>（カテゴリ売上）が主語</li></ul>{ppt3_proc}</div>
  </div>
{ppt3_thumbs}
</div>

<!-- ===== LT 1-4（ロジカルシンキング）===== -->
<!-- この部分は既存の logical_thinking.py と同じ内容を埋め込む。長いため省略し、
     実際には generate.py から logical_thinking.py を別途生成して、
     ユーザーはどちらでも使える形にする -->
{lt_html}

{chat_html}
</main>
</div>

<script>
{js_data}
const TOP3=[{",".join(f'["{m}",{a}]' for m,a in e4["top3"])}];
function nav(id){{document.querySelectorAll('.lesson-panel').forEach(p=>p.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));document.querySelector('[data-lesson="'+id+'"]')?.classList.add('active');document.querySelector('.sidebar').classList.remove('open')}}
function toggleEl(id){{var e=document.getElementById(id);e&&e.classList.toggle('tb-hidden')}}
function toggleHint(id){{toggleEl(id)}}
function parseNum(v){{if(!v)return NaN;v=v.replace(/[,\\s\\u3000]/g,'').replace(/円$/,'').replace(/%$/,'');return parseFloat(v)}}
function gradeQ(lid,qi){{var inp=document.getElementById(lid+'-q'+qi),res=document.getElementById(lid+'-r'+qi);if(!inp||!res)return;var ans=A[lid];if(!ans||!ans[qi])return;var e=ans[qi],uv=inp.value.trim();if(!uv){{res.innerHTML='<span class="rng">入力してください</span>';return}}var ok=false;if(e.t==='s'){{ok=uv===e.v}}else if(e.t==='p'){{var n=parseNum(uv);if(isNaN(n)){{res.innerHTML='<span class="rng">数値を入力</span>';return}}ok=Math.abs(n-e.v)<0.02||Math.abs(n/100-e.v)<0.02}}else{{var n=parseNum(uv);if(isNaN(n)){{res.innerHTML='<span class="rng">数値を入力</span>';return}}var tol=Math.abs(e.v*0.015);if(tol<1)tol=1;ok=Math.abs(n-e.v)<tol}}res.innerHTML=ok?'<span class="rok">✓ 正解！</span>':'<span class="rng">✗ 不正解</span>';inp.classList.remove('ok','ng');inp.classList.add(ok?'ok':'ng')}}
function gradePivot(id,expected){{var inp=document.getElementById(id),res=document.getElementById(id+'-r');if(!inp||!res)return;var n=parseNum(inp.value);if(isNaN(n)){{res.innerHTML='<span class="rng">数値を入力</span>';return}}var tol=Math.abs(expected*0.015);if(tol<1)tol=1;var ok=Math.abs(n-expected)<tol;res.innerHTML=ok?'<span class="rok">✓ 正解！</span>':'<span class="rng">✗ 不正解</span>';inp.classList.remove('ok','ng');inp.classList.add(ok?'ok':'ng')}}
function gradeTop3(i){{var mi=document.getElementById('e4-top-m'+i),ai=document.getElementById('e4-top-a'+i),r=document.getElementById('e4-top-r'+i);if(!mi||!ai||!r)return;var um=mi.value.trim(),ua=parseNum(ai.value);if(!um||isNaN(ua)){{r.innerHTML='<span class="rng">月と金額を入力</span>';return}}var em=TOP3[i][0],ea=TOP3[i][1];var mok=um===em,aok=Math.abs(ua-ea)<ea*0.015;if(mok&&aok){{r.innerHTML='<span class="rok">✓ 正解！</span>';mi.classList.add('ok');ai.classList.add('ok')}}else{{var msg=!mok&&!aok?'月と金額が不正解':!mok?'月が不正解':'金額が不正解';r.innerHTML='<span class="rng">✗ '+msg+'</span>';mi.classList.remove('ok','ng');mi.classList.add(mok?'ok':'ng');ai.classList.remove('ok','ng');ai.classList.add(aok?'ok':'ng')}}}}
function pptCheck(id){{}}
function revealPpt(id){{var el=document.getElementById(id+'-model');el&&el.classList.toggle('tb-hidden')}}
{lt_js}
{chat_js}
</script>
</body>
</html>'''


def _q_cards_offset(lesson_id, questions, offset):
    """Excel問題カード（オフセット付き）"""
    h = ''
    for i, q in enumerate(questions):
        idx = i + offset
        imode = 'text' if q["type"] == "text" else 'numeric'
        ph = '回答を入力'
        if q["type"] == "percent":
            ph = "例: 0.85"
        h += f'''
    <div class="question-card">
      <div class="q-header">Q{idx+1}. {q["q"]}</div>
      <div class="q-input">
        <input type="text" id="{lesson_id}-q{idx}" placeholder="{ph}" inputmode="{imode}" onkeydown="if(event.key==='Enter')gradeQ('{lesson_id}',{idx})">
        <button class="grade-btn" onclick="gradeQ('{lesson_id}',{idx})">採点</button>
      </div>
      <div class="result" id="{lesson_id}-r{idx}"></div>
    </div>'''
    return h
