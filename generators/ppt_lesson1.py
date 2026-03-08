"""PPT Lesson 1: 1スライド1メッセージ
課題: テキストびっしり2枚 → 修正
模範: 分割した7枚構成
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


FONT_NAME = "游ゴシック"
BLUE = RGBColor(0x1F, 0x4E, 0x79)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0x44, 0x72, 0xC4)


def _add_title_slide(prs, title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(8.4), Inches(1.5))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.name = FONT_NAME
    p.font.bold = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(16)
        p2.font.name = FONT_NAME
        p2.font.color.rgb = DARK_GRAY
        p2.alignment = PP_ALIGN.CENTER
    return slide


def _add_text_slide(prs, title, body, font_size=Pt(12)):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(24)
    p.font.name = FONT_NAME
    p.font.bold = True
    p.font.color.rgb = BLUE
    txBox2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(9), Inches(5.5))
    tf2 = txBox2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = body
    p2.font.size = font_size
    p2.font.name = FONT_NAME
    p2.font.color.rgb = DARK_GRAY
    p2.space_after = Pt(6)
    return slide


def _add_message_slide(prs, title, message, details=None):
    """模範: 1スライド1メッセージ形式"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.2))
    shape.fill.solid()
    shape.fill.fore_color.rgb = BLUE
    shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(22)
    p.font.name = FONT_NAME
    p.font.bold = True
    p.font.color.rgb = WHITE
    tf.margin_left = Inches(0.5)
    tf.margin_top = Inches(0.2)

    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(8.4), Inches(1.2))
    tf2 = txBox.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = message
    p2.font.size = Pt(20)
    p2.font.name = FONT_NAME
    p2.font.bold = True
    p2.font.color.rgb = ACCENT
    p2.alignment = PP_ALIGN.LEFT

    if details:
        txBox2 = slide.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(8.4), Inches(3.5))
        tf3 = txBox2.text_frame
        tf3.word_wrap = True
        for i, detail in enumerate(details):
            if i == 0:
                p3 = tf3.paragraphs[0]
            else:
                p3 = tf3.add_paragraph()
            p3.text = f"• {detail}"
            p3.font.size = Pt(14)
            p3.font.name = FONT_NAME
            p3.font.color.rgb = DARK_GRAY
            p3.space_after = Pt(8)

    return slide


def generate(output_dir: str):
    # ========== 課題ファイル ==========
    prs_q = Presentation()
    prs_q.slide_width = Inches(10)
    prs_q.slide_height = Inches(7.5)

    _add_title_slide(prs_q, "課題: 以下のスライドを修正してください",
                     "「1スライド1メッセージ」の原則に従い、読みやすく分割してください")

    # スライド1: 詰め込みすぎ
    dense_text1 = (
        "当社ミルクネクスト株式会社の法人営業部は、2025年度上半期において前年同期比118%の売上を達成しました。"
        "特に東京エリアのスーパーマーケット向け牛乳カテゴリ（北海道フレッシュ牛乳1L / 濃厚4.2牛乳1L）の伸びが顕著で、"
        "新規取引先獲得数は前期比で30%増加しています。一方、大阪エリアではヨーグルト製品の需要が"
        "高まっており、ギリシャ濃密ヨーグルトの採用店舗が150店を超えました。名古屋エリアについては、"
        "飲食チェーン向けのチーズ製品（熟成カマンベール）の案件化が進んでおり、第3四半期には大型受注が見込まれます。"
        "福岡エリアではコンビニ本部への新規提案が課題となっており、地域限定商品の企画を計画しています。"
        "札幌エリアは前年並みで推移していますが、バター・生クリームの業務用販路を中心に"
        "既存顧客へのアップセルに注力する方針です。全体として営業チームの訪問効率向上が求められており、"
        "SFAツールの活用度を高めるための研修を全メンバーに実施予定です。また、取引先満足度調査の結果、"
        "欠品・配送遅延への不満が増加していることが判明したため、Q3からは物流体制の改善も並行して進めます。"
    )
    _add_text_slide(prs_q, "2025年度上半期 営業成績サマリー", dense_text1)

    # スライド2: 同じく詰め込み
    dense_text2 = (
        "下半期の営業戦略として、以下の5つの重点施策を推進します。"
        "第1に、量販店への棚割り提案強化です。秋冬の鍋需要に合わせたチーズ・バターのエンド陳列提案を行い、"
        "定番棚の拡大を目指します。"
        "第2に、PB（プライベートブランド）受注の拡大です。大手コンビニ3社のPBヨーグルトの受注を目指し、"
        "製造ラインの柔軟性とコスト競争力を訴求します。"
        "第3に、業務用市場の開拓です。ホテル・レストラン・カフェ向けの生クリーム・バター提案を強化し、"
        "業務用営業部の売上20%増を目標とします。"
        "第4に、給食・病院向けの安定供給体制の構築です。学校給食センターや病院への納品ルートを新設し、"
        "安定的な需要基盤を確保します。"
        "第5に、新商品の市場投入です。プロテインヨーグルト（高たんぱく）を10月に発売予定で、"
        "フィットネス層・健康志向層をターゲットにSNSプロモーションと店頭試食を展開します。"
        "これらの施策を通じて、下半期の売上目標である前年同期比125%の達成を目指します。"
    )
    _add_text_slide(prs_q, "下半期重点施策", dense_text2)

    path_q = f"{output_dir}/ppt/Lesson1_課題_1スライド1メッセージ.pptx"
    prs_q.save(path_q)
    print(f"  ✓ {path_q}")

    # ========== 模範解答ファイル ==========
    prs_a = Presentation()
    prs_a.slide_width = Inches(10)
    prs_a.slide_height = Inches(7.5)

    _add_title_slide(prs_a, "2025年度 営業レビュー & 下半期戦略",
                     "ミルクネクスト株式会社 法人営業部")

    _add_message_slide(prs_a,
                       "上半期ハイライト",
                       "前年同期比118%の売上を達成、新規取引先は30%増",
                       [
                           "東京: 牛乳カテゴリがスーパー向けに好調、エリア売上No.1",
                           "大阪: ギリシャ濃密ヨーグルト採用150店突破",
                           "名古屋: 飲食チェーン向けチーズ大型案件が進行中",
                           "福岡: コンビニ本部への新規提案が課題、地域限定商品を企画",
                           "札幌: バター・生クリームの業務用アップセルに注力",
                       ])

    _add_message_slide(prs_a,
                       "上半期の課題",
                       "欠品・配送遅延と営業訪問効率に改善余地",
                       [
                           "取引先満足度調査: 欠品・配送遅延への不満が増加",
                           "SFAツール活用率: 入力率55%で改善の余地大",
                           "Q3から物流体制改善 + SFA研修を実施予定",
                       ])

    _add_message_slide(prs_a,
                       "下半期戦略",
                       "5つの重点施策で前年同期比125%を目指す",
                       [
                           "1. 量販店の棚割り提案強化（秋冬チーズ・バターのエンド陳列）",
                           "2. PB受注拡大（大手コンビニ3社のPBヨーグルト）",
                           "3. 業務用市場開拓（ホテル・レストラン・カフェ向け）",
                           "4. 給食・病院の安定供給体制（新規納品ルート構築）",
                           "5. 新商品投入（プロテインヨーグルト、10月発売）",
                       ])

    _add_message_slide(prs_a,
                       "施策①② 量販店 & PB",
                       "定番棚の拡大とPB受注で量販チャネルを強化",
                       [
                           "棚割り提案: 秋冬の鍋需要に合わせたチーズ・バターのエンド陳列",
                           "PB: 大手コンビニ3社へ、製造ライン柔軟性とコスト競争力を訴求",
                           "目標: 量販チャネル売上15%増",
                       ])

    _add_message_slide(prs_a,
                       "施策③④ 業務用 & 給食",
                       "ホテル・飲食 × 給食・病院で新しい売上の柱を構築",
                       [
                           "業務用: 生クリーム・バターの大容量規格を提案",
                           "給食: 学校・病院への納品ルート新設で安定需要を確保",
                           "目標: 業務用営業部の売上20%増",
                       ])

    _add_message_slide(prs_a,
                       "施策⑤ 新商品投入",
                       "プロテインヨーグルトで健康志向層を開拓",
                       [
                           "10月発売、フィットネス層・健康志向層がターゲット",
                           "SNSプロモーション + 店頭試食で認知拡大",
                           "KPI: 初月1,000ケース出荷、取扱店舗500店突破",
                       ])

    _add_message_slide(prs_a,
                       "まとめ",
                       "上半期の成長を土台に、下半期は125%達成へ",
                       [
                           "上半期実績: 118%達成、特に牛乳カテゴリが牽引",
                           "下半期目標: 前年同期比125%",
                           "5施策を同時推進し、チャネル多角化で成長を加速",
                       ])

    path_a = f"{output_dir}/ppt/Lesson1_模範_1スライド1メッセージ.pptx"
    prs_a.save(path_a)
    print(f"  ✓ {path_a}")

    return [path_q, path_a]
