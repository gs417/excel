"""Excel Lesson 3: IF / SUMIFS / COUNTIFS — 10問"""

import openpyxl
from openpyxl.utils import get_column_letter
from . import data, styles


def generate(output_dir: str):
    wb = openpyxl.Workbook()

    # ========== 売上データシート ==========
    ws_data = wb.active
    ws_data.title = "売上データ"
    ws_data.sheet_properties.tabColor = "70AD47"

    headers = ["売上ID", "日付", "顧客ID", "商品名", "カテゴリ", "単価", "数量", "金額", "担当者", "地域", "月"]
    for col, h in enumerate(headers, 1):
        ws_data.cell(row=1, column=col, value=h)
    styles.style_header_row(ws_data, 1, 1, len(headers))

    for i, s in enumerate(data.SALES, 2):
        row_data = [
            s["id"], s["date"], s["customer_id"], s["product_name"],
            s["category"], s["unit_price"], s["quantity"], s["amount"],
            s["rep"], s["region"], s["month"],
        ]
        for col, val in enumerate(row_data, 1):
            cell = ws_data.cell(row=i, column=col, value=val)
            cell.font = styles.FONT_NORMAL
            cell.border = styles.THIN_BORDER
            if col == 2:
                cell.number_format = "YYYY/MM/DD"
            elif col in (6, 8):
                cell.number_format = styles.NUMBER_FORMAT_YEN

    col_widths = [10, 12, 10, 24, 14, 14, 8, 14, 14, 10, 10]
    for i, w in enumerate(col_widths, 1):
        ws_data.column_dimensions[get_column_letter(i)].width = w

    # ========== 期待値計算 ==========
    # Q1: 金額100万以上の件数
    high_value_count = sum(1 for s in data.SALES if s["amount"] >= 1_000_000)
    # Q2: 金額50万以上なら「大型」、それ以外「通常」→ 大型の件数
    large_deal_count = sum(1 for s in data.SALES if s["amount"] >= 500_000)
    # Q3: 東京 かつ 牛乳 の売上合計
    tokyo_milk = sum(s["amount"] for s in data.SALES if s["region"] == "東京" and s["category"] == "牛乳")
    # Q4: 大阪 かつ 田中太郎 の件数
    osaka_tanaka = sum(1 for s in data.SALES if s["region"] == "大阪" and s["rep"] == "田中 太郎")
    # Q5: 数量50ケース以上 かつ ヨーグルト の売上合計
    yog_qty50 = sum(s["amount"] for s in data.SALES if s["quantity"] >= 50 and s["category"] == "ヨーグルト")
    # Q6: 金額100万以上の件数
    rank_a = sum(1 for s in data.SALES if s["amount"] >= 1_000_000)
    # Q7: 2025-04 の売上合計
    apr_amount = sum(s["amount"] for s in data.SALES if s["month"] == "2025-04")
    # Q8: 福岡 かつ チーズ の件数
    fukuoka_cheese = sum(1 for s in data.SALES if s["region"] == "福岡" and s["category"] == "チーズ")
    # Q9: 佐藤健一 かつ 金額50万以上 の件数
    sato_large = sum(1 for s in data.SALES if s["rep"] == "佐藤 健一" and s["amount"] >= 500_000)
    # Q10: 量販営業部(田中/鈴木)の売上合計
    dept1_reps = {"田中 太郎", "鈴木 花子"}
    dept1_total = sum(s["amount"] for s in data.SALES if s["rep"] in dept1_reps)

    questions = [
        ("Q1", "金額が100万円以上の売上件数を求めてください（COUNTIF）",
         '=COUNTIF(売上データ!H:H,">="&1000000)', high_value_count),
        ("Q2", "金額が50万円以上の売上件数を求めてください（COUNTIF）",
         '=COUNTIF(売上データ!H:H,">="&500000)', large_deal_count),
        ("Q3", "地域「東京」かつカテゴリ「牛乳」の売上合計（SUMIFS）",
         '=SUMIFS(金額範囲,地域範囲,"東京",カテゴリ範囲,"牛乳")', tokyo_milk),
        ("Q4", "地域「大阪」かつ担当者「田中 太郎」の件数（COUNTIFS）",
         '=COUNTIFS(地域範囲,"大阪",担当者範囲,"田中 太郎")', osaka_tanaka),
        ("Q5", "数量50ケース以上かつカテゴリ「ヨーグルト」の売上合計（SUMIFS）",
         '=SUMIFS(金額範囲,数量範囲,">="&50,カテゴリ範囲,"ヨーグルト")', yog_qty50),
        ("Q6", "金額100万円以上の件数を求めてください（Q1と同じ、確認用）",
         '=COUNTIF(売上データ!H:H,">="&1000000)', rank_a),
        ("Q7", "2025年4月（2025-04）の売上合計を求めてください（SUMIF）",
         '=SUMIF(売上データ!K:K,"2025-04",売上データ!H:H)', apr_amount),
        ("Q8", "地域「福岡」かつカテゴリ「チーズ」の件数（COUNTIFS）",
         '=COUNTIFS(地域範囲,"福岡",カテゴリ範囲,"チーズ")', fukuoka_cheese),
        ("Q9", "担当者「佐藤 健一」かつ金額50万以上の件数（COUNTIFS）",
         '=COUNTIFS(担当者範囲,"佐藤 健一",金額範囲,">="&500000)', sato_large),
        ("Q10", "量販営業部（田中太郎+鈴木花子）の売上合計を求めてください",
         '=SUMIF(...,"田中 太郎",...)+SUMIF(...,"鈴木 花子",...)', dept1_total),
    ]

    hints = [
        '=COUNTIF(範囲,">="&1000000)',
        '=COUNTIF(範囲,">="&500000)',
        '=SUMIFS(合計範囲,条件範囲1,"条件1",条件範囲2,"条件2")',
        '=COUNTIFS(範囲1,"条件1",範囲2,"条件2")',
        '=SUMIFS(合計範囲,範囲1,">="&50,範囲2,"条件")',
        'Q1と同じ条件で確認',
        '=SUMIF(月範囲,"2025-04",金額範囲)',
        '=COUNTIFS(範囲1,"条件1",範囲2,"条件2")',
        '=COUNTIFS(範囲1,"条件1",範囲2,">="&500000)',
        '2人分のSUMIFを足す or SUMPRODUCT',
    ]

    # ========== 問題シート ==========
    ws = wb.create_sheet("問題")
    styles.setup_problem_sheet(ws, "Lesson 3: IF / SUMIFS / COUNTIFS")
    ws.cell(row=3, column=1,
            value="「売上データ」シートを参照して回答してください。複数条件の集計がポイントです。").font = styles.FONT_NORMAL

    row = 5
    for col, h in enumerate(["No.", "問題", "ヒント", "あなたの回答", "採点"], 1):
        ws.cell(row=row, column=col, value=h)
    styles.style_header_row(ws, row, 1, 5)

    answer_col = 4
    grading_col = 5
    start_row = row + 1

    for i, (qno, question, formula, expected) in enumerate(questions):
        r = start_row + i
        ws.cell(row=r, column=1, value=qno).font = styles.FONT_BOLD
        ws.cell(row=r, column=1).border = styles.THIN_BORDER
        ws.cell(row=r, column=2, value=question).font = styles.FONT_NORMAL
        ws.cell(row=r, column=2).border = styles.THIN_BORDER
        ws.cell(row=r, column=3, value=hints[i]).font = styles.FONT_NORMAL
        ws.cell(row=r, column=3).border = styles.THIN_BORDER
        styles.mark_answer_cell(ws, r, answer_col)
        styles.add_grading_cell(ws, r, grading_col, f"D{r}", expected)

    end_row = start_row + len(questions) - 1
    styles.apply_grading_format(ws, grading_col, start_row, end_row)
    styles.add_score_summary(ws, end_row + 2, 1, grading_col, start_row, end_row, len(questions))

    ws.cell(row=end_row + 4, column=1,
            value="💡 全問回答後、E列のフォント色を黒に変更すると採点結果が見えます。").font = styles.FONT_NORMAL

    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 55
    ws.column_dimensions["C"].width = 42
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 14

    # ========== 解答シート ==========
    ws_ans = styles.create_answer_sheet(wb, ws)
    ws_ans.cell(row=1, column=1, value="No.").font = styles.FONT_BOLD
    ws_ans.cell(row=1, column=2, value="模範解答").font = styles.FONT_BOLD
    ws_ans.cell(row=1, column=3, value="期待値").font = styles.FONT_BOLD
    for i, (qno, _, formula, expected) in enumerate(questions):
        ws_ans.cell(row=i + 2, column=1, value=qno)
        ws_ans.cell(row=i + 2, column=2, value=formula)
        ws_ans.cell(row=i + 2, column=3, value=expected)

    wb.move_sheet("問題", offset=-2)

    path = f"{output_dir}/excel/Lesson3_IF_SUMIFS_COUNTIFS.xlsx"
    wb.save(path)
    print(f"  ✓ {path}")
    return path
