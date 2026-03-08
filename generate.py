#!/usr/bin/env python3
"""ビジネススキル自習キット — 全課題ファイル生成 & ZIP化"""

import os
import shutil
import sys

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def ensure_dirs():
    """出力ディレクトリを初期化"""
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    for d in ["excel", "ppt", "logical-thinking"]:
        os.makedirs(os.path.join(OUTPUT_DIR, d), exist_ok=True)


def write_hajimeni():
    """はじめに.txt を生成"""
    text = """\
╔══════════════════════════════════════════════════════╗
║         ビジネススキル自習キット                     ║
║         〜 新人営業のための実践トレーニング 〜       ║
╚══════════════════════════════════════════════════════╝

■ このキットについて
  新卒で営業職に就くあなたのための、Excel・PowerPoint・ロジカルシンキングの
  自走型教材です。全て架空の「ミルクネクスト株式会社」（乳業メーカー）を舞台に、
  法人営業の現場で使うスキルを実践的に学べます。

■ 推奨学習順序
  1. Excel Lesson 1 → 5（基本関数 → KPIダッシュボード）
  2. PPT Lesson 1 → 3（スライド改善 → 提案書作成）
  3. ロジカルシンキング演習（HTML）

  ※ 順番は目安です。興味のあるところから始めてもOKです。

■ フォルダ構成
  excel/
    Lesson1_基本関数.xlsx          — SUM/AVERAGE/COUNT 等
    Lesson2_VLOOKUP_INDEX-MATCH.xlsx — テーブル参照
    Lesson3_IF_SUMIFS_COUNTIFS.xlsx   — 条件分岐・複数条件集計
    Lesson4_ピボットテーブル_チャート.xlsx — 集計とグラフ
    Lesson5_KPIダッシュボード.xlsx       — 総合演習

  ppt/
    Lesson1_課題_1スライド1メッセージ.pptx — 修正課題
    Lesson1_模範_1スライド1メッセージ.pptx — 模範解答
    Lesson2_課題_図解化.pptx              — 図解化課題
    Lesson2_模範_図解化.pptx              — 模範解答
    Lesson3_課題_提案書作成.pptx          — 提案書課題
    Lesson3_模範_提案書作成.pptx          — 模範解答

  logical-thinking/
    ロジカルシンキング演習.html — ブラウザで開いて演習

■ Excelの使い方
  1. 「問題」シートの黄色いセルに回答（数式 or 値）を入力
  2. 全問回答したら、採点列（E列 or D列）のフォント色を黒に変更
     → 「✓ 正解」「✗ 不正解」が表示されます
  3. スコアサマリーで正答率を確認
  4. 「解答」シートは非表示になっています
     → シート見出しを右クリック →「再表示」で確認できます

■ PPTの使い方
  1. 課題ファイルを開いて指示に従い修正
  2. 完成したら模範解答ファイルと見比べて自己評価

■ ロジカルシンキングの使い方
  1. HTMLファイルをブラウザ（Chrome/Edge/Safari）で開く
  2. 4レッスン・全16問を順番に解く
  3. 進捗はブラウザに自動保存されるので途中で閉じてもOK

■ データ世界観
  全レッスン共通で以下の架空データを使います:
  - 会社: ミルクネクスト株式会社（乳業メーカー 法人営業部）
  - 取引先: 50社（スーパー/コンビニ/飲食チェーン/給食/卸）
  - 商品: 8種（牛乳/ヨーグルト/チーズ/バター・生クリーム）
  - 売上: 200件（2025年4月〜2026年3月、ケース単位取引）
  - 担当者: 5名（量販営業部・業務用営業部）

がんばってください！ 💪
"""
    path = os.path.join(OUTPUT_DIR, "はじめに.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  ✓ {path}")


def main():
    print("=" * 50)
    print("ビジネススキル自習キット — ファイル生成")
    print("=" * 50)

    ensure_dirs()
    print("\n📁 出力ディレクトリを準備しました\n")

    # はじめに
    print("📝 はじめに.txt")
    write_hajimeni()

    # Excel
    print("\n📊 Excel レッスン")
    from generators import excel_lesson1, excel_lesson2, excel_lesson3, excel_lesson4, excel_lesson5
    excel_lesson1.generate(OUTPUT_DIR)
    excel_lesson2.generate(OUTPUT_DIR)
    excel_lesson3.generate(OUTPUT_DIR)
    excel_lesson4.generate(OUTPUT_DIR)
    excel_lesson5.generate(OUTPUT_DIR)

    # PPT
    print("\n📑 PowerPoint レッスン")
    from generators import ppt_lesson1, ppt_lesson2, ppt_lesson3
    ppt_lesson1.generate(OUTPUT_DIR)
    ppt_lesson2.generate(OUTPUT_DIR)
    ppt_lesson3.generate(OUTPUT_DIR)

    # HTML
    print("\n🧠 ロジカルシンキング")
    from generators import logical_thinking
    logical_thinking.generate(OUTPUT_DIR)

    # 統合HTML
    print("\n📱 統合HTML（1ファイル完結版）")
    from generators import all_in_one_html
    all_in_one_html.generate(OUTPUT_DIR)

    # ZIP化
    print("\n📦 ZIP化")
    zip_path = os.path.join(os.path.dirname(__file__), "ビジネススキル自習キット")
    shutil.make_archive(zip_path, "zip", OUTPUT_DIR)
    print(f"  ✓ {zip_path}.zip")

    print("\n" + "=" * 50)
    print("✅ 完了！")
    print(f"   ZIP: {zip_path}.zip")
    print(f"   出力: {OUTPUT_DIR}/")
    print("=" * 50)


if __name__ == "__main__":
    main()
