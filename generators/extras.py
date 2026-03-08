"""追加コンテンツ — Excel L0, PPT方法論, 思考プロセス, AIチャット"""


def excel_l0_html():
    '''Returns HTML for Excel Lesson 0: Excel入門 panel.'''
    return '''<div id="excel0" class="lesson-panel">
  <h2 class="lesson-title">📊 Excel Lesson 0: Excel入門</h2>
  <p class="lesson-subtitle">セル・数式・エラーの読み方 — はじめてのExcel</p>
  <div class="textbook">
    <div class="tb-chapter">
      <div class="tb-chapter-icon">0</div>
      <div class="tb-chapter-title">はじめてのExcel — ゼロから学ぶ基本操作</div>
    </div>

    <h4 class="tb-section">1. Excelとは？</h4>
    <p>Excelは、Microsoft社が提供する<strong>表計算ソフト</strong>です。数字や文字をマス目（セル）に入力し、計算・集計・グラフ作成ができます。</p>
    <p>ビジネスでは売上管理、在庫管理、データ分析など、あらゆる場面で使われます。</p>
    <div class="tb-tip">Googleスプレッドシート（Google Sheets）もほぼ同じ操作で使えます。会社によってはこちらを使う場合もあります。</div>

    <h4 class="tb-section">2. 画面の見方</h4>
    <p>Excelを開くと、縦横のマス目が並んでいます。この1つ1つのマス目を<strong>セル</strong>と呼びます。</p>
    <div class="tb-example">
      <span class="label">セルの仕組み</span>
      セルは<strong>列（アルファベット: A, B, C...）</strong>と<strong>行（数字: 1, 2, 3...）</strong>の交差点です。<br>
      例えば「B3」は、B列の3行目のセルを指します。これを<strong>セル参照</strong>（セルのアドレス）と呼びます。
    </div>
    <div class="tb-example">
      <span class="label">画面の主要パーツ</span>
      <strong>名前ボックス:</strong> 今選択しているセルのアドレス（例: A1）が表示される場所<br>
      <strong>数式バー:</strong> セルに入力した内容（数式や値）が表示される場所<br>
      <strong>シート見出し:</strong> 画面下部の「Sheet1」タブ。複数のシートを切り替えて使えます。
    </div>

    <h4 class="tb-section">3. データの入力方法</h4>
    <p>Excelへのデータ入力はとてもシンプルです。</p>
    <div class="tb-example">
      <span class="label">基本操作</span>
      <strong>①</strong> 入力したいセルをクリックする<br>
      <strong>②</strong> キーボードで文字や数字を入力する<br>
      <strong>③</strong> <strong>Enter</strong>キーで確定（下のセルに移動）<br>
      　　　 <strong>Tab</strong>キーで確定（右のセルに移動）
    </div>
    <div class="tb-highlight">
      <strong>覚えておきたい操作:</strong><br>
      <strong>Esc</strong> — 入力をキャンセルして元に戻す<br>
      <strong>Ctrl + Z</strong>（Macは ⌘ + Z）— 直前の操作を取り消す（何度でも戻れる）<br>
      <strong>Delete</strong> — 選択セルの内容を削除
    </div>

    <h4 class="tb-section">4. 数式の入力方法</h4>
    <p>Excelの最大の強みは<strong>自動計算</strong>です。セルに「=」から始まる数式を入力すると、Excelが自動で計算してくれます。</p>
    <div class="tb-example">
      <span class="label">数式入力のステップ（SUM関数の例）</span>
      <strong>① 結果を表示したいセルをクリック</strong><br>
      　　例えば C10 セルをクリック<br><br>
      <strong>② =SUM( と入力する</strong><br>
      　　「=」は「これから数式を書きますよ」という合図です<br><br>
      <strong>③ 範囲の最初のセルをクリック</strong><br>
      　　例えば C1 セルをクリック → 数式バーに =SUM(C1 と表示される<br><br>
      <strong>④ Shiftを押しながら最後のセルをクリック</strong><br>
      　　例えば Shift + C9 クリック → =SUM(C1:C9 と表示される<br>
      　　※ マウスでドラッグしても同じ結果になります<br><br>
      <strong>⑤ ) を入力して閉じる</strong><br>
      　　=SUM(C1:C9) と完成<br><br>
      <strong>⑥ Enterキーで確定</strong><br>
      　　C1からC9の合計値が自動計算されます！
    </div>
    <div class="tb-tip">数式の入力中、参照先のセルが色付きの枠で囲まれます。どのセルを参照しているか視覚的に確認できるので安心です。</div>

    <h4 class="tb-section">5. 簡単な計算例</h4>
    <p>SUM関数以外にも、セル同士で直接計算ができます。</p>
    <div class="tb-example">
      <span class="label">四則演算</span>
      <strong>=A1+B1</strong> → A1とB1の<strong>足し算</strong><br>
      <strong>=A1-B1</strong> → A1からB1を<strong>引き算</strong><br>
      <strong>=A1*B1</strong> → A1とB1の<strong>掛け算</strong>（×ではなく * を使う）<br>
      <strong>=A1/B1</strong> → A1をB1で<strong>割り算</strong>（÷ではなく / を使う）
    </div>
    <div class="tb-highlight">
      <strong>大事なポイント:</strong> 数式にはセル参照（A1, B1 など）を使います。直接数字を書くのではなく、セルを参照することで、<strong>元のデータを変えたら自動で再計算</strong>されます。
    </div>

    <h4 class="tb-section">6. よくあるエラーと対処法</h4>
    <p>数式を間違えるとエラーが表示されますが、慌てなくて大丈夫。エラーには意味があり、原因がわかれば簡単に直せます。</p>
    <div class="tb-example">
      <span class="label">#VALUE! — 文字列が混入</span>
      数値を期待するセルに文字列が入っています。<br>
      <strong>対処:</strong> 参照先のセルに余計な文字（スペースや全角数字）が入っていないか確認しましょう。
    </div>
    <div class="tb-example">
      <span class="label">#REF! — 参照先が削除された</span>
      数式が参照しているセルや行・列が削除されました。<br>
      <strong>対処:</strong> Ctrl + Z で削除を取り消すか、数式を修正して正しいセルを参照し直しましょう。
    </div>
    <div class="tb-example">
      <span class="label">#NAME? — 関数名のスペルミス</span>
      関数名が間違っています（例: =SMU → 正しくは =SUM）。<br>
      <strong>対処:</strong> 関数名のスペルを確認しましょう。入力中に候補が表示されるので、それを選ぶと安全です。
    </div>
    <div class="tb-example">
      <span class="label">#DIV/0! — ゼロで割り算した</span>
      割り算の分母が 0 または空白です。<br>
      <strong>対処:</strong> 分母のセルに値が入っているか確認しましょう。
    </div>
    <div class="tb-example">
      <span class="label">#N/A — 検索値が見つからない</span>
      VLOOKUPなどの検索関数で、探している値が表に存在しません。<br>
      <strong>対処:</strong> 検索値のスペルや全角・半角を確認しましょう。
    </div>
    <div class="tb-warn">
      <strong>######## — これはエラーではありません！</strong><br>
      セルの内容が長すぎて列幅に収まっていないだけです。<br>
      <strong>対処:</strong> 列の境界線をダブルクリックすると自動で幅が調整されます。
    </div>

    <h4 class="tb-section">7. 便利なショートカットキー</h4>
    <p>よく使うショートカットを覚えると作業スピードが格段に上がります。</p>
    <div class="tb-example">
      <span class="label">基本ショートカット（Windows / Mac）</span>
      <strong>Ctrl + C / ⌘ + C</strong> → コピー<br>
      <strong>Ctrl + V / ⌘ + V</strong> → 貼り付け<br>
      <strong>Ctrl + X / ⌘ + X</strong> → 切り取り<br>
      <strong>Ctrl + Z / ⌘ + Z</strong> → 元に戻す（Undo）<br>
      <strong>Ctrl + S / ⌘ + S</strong> → 上書き保存（こまめに！）<br>
      <strong>Ctrl + Home / ⌘ + Home</strong> → シートの先頭（A1）に移動<br>
      <strong>Ctrl + End / ⌘ + End</strong> → データの最終セルに移動<br>
      <strong>Ctrl + ↓ / ⌘ + ↓</strong> → データの最終行にジャンプ
    </div>
    <div class="tb-tip">最初は <strong>Ctrl + Z</strong>（元に戻す）と <strong>Ctrl + S</strong>（保存）だけ覚えれば大丈夫！失敗しても戻せるので、怖がらずにどんどん触ってみましょう。</div>

    <h4 class="tb-section">8. Excelショートカットキー一覧</h4>
    <p>よく使うショートカットをまとめました。最初は上の5つだけ覚えれば十分です。</p>

    <div class="tb-example">
      <span class="label">基本操作（まずこれだけ覚えよう）</span>
      <strong>Ctrl + S / ⌘ + S</strong> → 上書き保存（こまめに！）<br>
      <strong>Ctrl + Z / ⌘ + Z</strong> → 元に戻す（何度でも戻れる）<br>
      <strong>Ctrl + C / ⌘ + C</strong> → コピー<br>
      <strong>Ctrl + V / ⌘ + V</strong> → 貼り付け<br>
      <strong>Ctrl + X / ⌘ + X</strong> → 切り取り
    </div>

    <div class="tb-example">
      <span class="label">セル移動・選択</span>
      <strong>Ctrl + ↓↑←→ / ⌘ + ↓↑←→</strong> → データの端までジャンプ<br>
      <strong>Ctrl + Home / ⌘ + Home</strong> → シートの先頭（A1）に移動<br>
      <strong>Ctrl + End / ⌘ + End</strong> → データの最終セルに移動<br>
      <strong>Ctrl + Shift + ↓ / ⌘ + Shift + ↓</strong> → データの端まで選択<br>
      <strong>Ctrl + Space</strong> → 列全体を選択<br>
      <strong>Shift + Space</strong> → 行全体を選択<br>
      <strong>Ctrl + A / ⌘ + A</strong> → 全セル選択
    </div>

    <div class="tb-example">
      <span class="label">編集・入力</span>
      <strong>F2</strong> → セルを編集モードにする（ダブルクリックと同じ）<br>
      <strong>Enter</strong> → 確定して下に移動<br>
      <strong>Tab</strong> → 確定して右に移動<br>
      <strong>Esc</strong> → 入力をキャンセル<br>
      <strong>Delete</strong> → セルの内容を削除<br>
      <strong>Ctrl + D / ⌘ + D</strong> → 上のセルをコピー（下方向フィル）<br>
      <strong>Ctrl + R / ⌘ + R</strong> → 左のセルをコピー（右方向フィル）<br>
      <strong>Ctrl + Enter / ⌘ + Enter</strong> → 選択した全セルに同じ値を入力
    </div>

    <div class="tb-example">
      <span class="label">書式設定</span>
      <strong>Ctrl + B / ⌘ + B</strong> → 太字<br>
      <strong>Ctrl + 1 / ⌘ + 1</strong> → セルの書式設定ダイアログを開く<br>
      <strong>Ctrl + Shift + 1</strong> → 桁区切り（1,000）書式<br>
      <strong>Ctrl + Shift + 4</strong> → 通貨（¥）書式<br>
      <strong>Ctrl + Shift + 5</strong> → パーセント（%）書式
    </div>

    <div class="tb-example">
      <span class="label">行・列の操作</span>
      <strong>Ctrl + Shift + + / ⌘ + Shift + +</strong> → 行または列を挿入<br>
      <strong>Ctrl + - / ⌘ + -</strong> → 行または列を削除<br>
      <strong>Alt + H → O → I（Win）</strong> → 列幅の自動調整<br>
      <strong>Ctrl + 9</strong> → 選択行を非表示<br>
      <strong>Ctrl + 0</strong> → 選択列を非表示
    </div>

    <div class="tb-example">
      <span class="label">数式・関数</span>
      <strong>=</strong> → 数式の入力を開始<br>
      <strong>Tab</strong> → 関数の候補を確定（入力中に出てくるリストから選択）<br>
      <strong>F4</strong> → セル参照の固定（$マーク切替: A1 → $A$1 → A$1 → $A1）<br>
      <strong>Ctrl + ` / ⌘ + `</strong> → 数式の表示/非表示を切替<br>
      <strong>Alt + = / ⌘ + Shift + T</strong> → オートSUM（選択範囲を自動合計）
    </div>

    <div class="tb-example">
      <span class="label">その他の便利機能</span>
      <strong>Ctrl + F / ⌘ + F</strong> → 検索<br>
      <strong>Ctrl + H / ⌘ + H</strong> → 置換<br>
      <strong>Ctrl + P / ⌘ + P</strong> → 印刷<br>
      <strong>Ctrl + N / ⌘ + N</strong> → 新しいブックを開く<br>
      <strong>Alt + Enter（Win）/ Control + Option + Enter（Mac）</strong> → セル内で改行<br>
      <strong>Ctrl + ; / ⌘ + ;</strong> → 今日の日付を入力<br>
      <strong>Ctrl + Shift + ; / ⌘ + Shift + ;</strong> → 現在の時刻を入力
    </div>

    <div class="tb-tip">まずは <strong>Ctrl+S</strong>（保存）、<strong>Ctrl+Z</strong>（戻す）、<strong>Ctrl+C/V</strong>（コピペ）の4つを体に覚えさせましょう。慣れたら <strong>Ctrl+↓</strong>（端ジャンプ）と <strong>F4</strong>（$固定）を追加すると作業スピードが格段に上がります。</div>

    <h4 class="tb-section">9. 次のステップ</h4>
    <p>基本操作がわかったら、<strong>Lesson 1: 基本関数</strong>に進みましょう！</p>
    <p>Lesson 1 では、SUM（合計）、AVERAGE（平均）、COUNT（件数）など、仕事でよく使う5つの関数を学びます。</p>
    <div class="tb-highlight">
      <strong>練習のコツ:</strong> 読むだけでなく、実際にExcelを開いて手を動かすことが上達の近道です。<br>
      間違えても <strong>Ctrl + Z</strong> で戻せるので、どんどん試してみてください！
    </div>
  </div>
</div>'''


def ppt1_methodology():
    '''Returns extra textbook HTML for PPT Lesson 1 methodology.'''
    return '''<h4 class="tb-section">ワーキングメモリの限界</h4>
<p>人間の脳が同時に処理できる情報は<strong>3〜5個</strong>が限界です（ミラーの法則）。</p>
<p>1枚のスライドに10個の情報を詰め込むと、聴衆はどれも記憶に残りません。「全部伝えよう」とすると「何も伝わらない」結果になるのです。</p>
<div class="tb-highlight">
  <strong>鉄則:</strong> 1スライドに伝えるメッセージは<strong>1つだけ</strong>。箇条書きも3〜5個まで。
</div>

<h4 class="tb-section">メッセージ抽出3ステップ</h4>
<div class="tb-example">
  <span class="label">Step 1: 全情報を書き出す</span>
  まず、伝えたい情報を全て箇条書きにします。この段階では量を気にせず、思いつく限り書き出しましょう。
</div>
<div class="tb-example">
  <span class="label">Step 2: 「聴衆が持ち帰る1つ」を決める</span>
  書き出した情報を眺めて、「この発表を聞いた人が<strong>1つだけ覚えて帰る</strong>としたら何か？」を決めます。これがスライドの<strong>メインメッセージ</strong>です。
</div>
<div class="tb-example">
  <span class="label">Step 3: それをタイトルに書く</span>
  決めたメッセージをそのままスライドのタイトルにします。残りの情報はサポート材料として箇条書きに。
</div>

<h4 class="tb-section">タイトルの書き方</h4>
<p>スライドのタイトルは「ラベル」ではなく<strong>「結論」</strong>を書きましょう。</p>
<div class="tb-highlight">
  <strong>悪い例:</strong> 「上半期サマリー」「営業成績」「売上推移」<br>
  <strong>良い例:</strong> 「前年比118%達成」「東京エリアが牛乳カテゴリで牽引」「下半期は5施策で125%を目指す」
</div>
<div class="tb-tip">タイトルだけを上から順に読んで<strong>ストーリーが分かる</strong>のが理想です。忙しい上司はタイトルしか読まないこともあります。</div>'''


def ppt2_methodology():
    '''Returns extra textbook HTML for PPT Lesson 2 methodology.'''
    return '''<h4 class="tb-section">図解化の判断フロー</h4>
<p>「この情報はどう図にすればいいか？」迷ったら、以下の判断フローに当てはめてください。</p>
<div class="tb-example">
  <span class="label">情報の関係性 → 適切な図解</span>
  <strong>順番がある</strong> → フロー図（矢印でつなぐ）<br>
  <strong>割合を示す</strong> → 棒グラフ / 円グラフ<br>
  <strong>比較する</strong> → 表 / 棒グラフ（横並び）<br>
  <strong>関係性を示す</strong> → マトリクス / ベン図<br>
  <strong>階層を示す</strong> → ピラミッド
</div>
<div class="tb-tip">迷ったらまず「この情報は何と何の<strong>関係</strong>を示しているか？」と自問してみましょう。関係性が見えれば、適切な図が自然と決まります。</div>

<h4 class="tb-section">色の使い方3原則</h4>
<div class="tb-example">
  <span class="label">原則① 色は3色まで</span>
  メイン色（例: 青） + アクセント色（例: オレンジ） + グレー（補足情報）。<br>
  4色以上使うと画面がうるさくなり、どこが重要かわからなくなります。
</div>
<div class="tb-example">
  <span class="label">原則② 強調は1箇所だけ</span>
  全部太字にするのは、何も強調していないのと同じです。<br>
  「ここだけは見てほしい」という<strong>1箇所だけ</strong>を目立たせましょう。
</div>
<div class="tb-example">
  <span class="label">原則③ 色に意味を持たせる</span>
  <strong>青 = ポジティブ</strong>（達成、成長、提案）<br>
  <strong>赤 = ネガティブ</strong>（課題、未達、注意）<br>
  <strong>グレー = 補足</strong>（参考値、注釈）<br>
  色の意味を統一すると、聴衆は色だけで情報を直感的に判断できます。
</div>'''


def ppt3_methodology():
    '''Returns extra textbook HTML for PPT Lesson 3 methodology.'''
    return '''<h4 class="tb-section">提案書の型（課題→提案→効果）を深掘り</h4>
<div class="tb-example">
  <span class="label">課題スライド</span>
  相手が「そうそう、それが困ってるんだよ」と思うように書くのがコツです。<br>
  自分の提案を押し付けるのではなく、<strong>相手の痛みに共感する</strong>ところから始めましょう。<br>
  課題は3つに絞ると記憶に残りやすくなります。
</div>
<div class="tb-example">
  <span class="label">提案スライド</span>
  提案は3つの要素で構成します:<br>
  <strong>What（何を）:</strong> 何を導入・実施するのか<br>
  <strong>How（どうやって）:</strong> 具体的にどう実行するのか<br>
  <strong>Why（なぜ効くか）:</strong> なぜこの方法で課題が解決するのか
</div>
<div class="tb-example">
  <span class="label">効果スライド</span>
  効果は「感覚」ではなく「数字」で語ります:<br>
  <strong>Before / After:</strong> 現状と導入後の比較<br>
  <strong>数字:</strong> 具体的な金額・パーセンテージ<br>
  <strong>タイムライン:</strong> いつまでに効果が出るのか
</div>

<h4 class="tb-section">相手目線への変換</h4>
<div class="tb-highlight">
  <strong>✕</strong>「弊社の新商品を導入いただきたい」<br>
  <strong>◯</strong>「御社の乳製品売上を15%改善する施策のご提案」<br><br>
  ポイントは2つ:<br>
  ① 主語を<strong>「弊社」から「御社」</strong>に変える<br>
  ② メリットを<strong>相手側で語る</strong>（自社の売上ではなく、相手の売上改善）
</div>

<h4 class="tb-section">数字で語る4パターン</h4>
<div class="tb-example">
  <span class="label">① 絶対値</span>
  「月額120万円の増収」 — 具体的な金額で効果の大きさを示す
</div>
<div class="tb-example">
  <span class="label">② 比率</span>
  「前年比115%」 — 成長度合いを割合で示す
</div>
<div class="tb-example">
  <span class="label">③ 比較</span>
  「競合A社より回転率1.3倍」 — 他社との差で優位性を示す
</div>
<div class="tb-example">
  <span class="label">④ 期間</span>
  「3ヶ月で投資回収」 — いつまでに元が取れるかを示す
</div>
<div class="tb-tip">数字は「大きく見せる」のではなく「正確に、でもインパクトのある切り口で」伝えましょう。嘘の数字は信頼を失います。</div>'''


def ppt1_process():
    '''Returns 思考プロセス HTML for PPT Lesson 1 model answer.'''
    return '''<h4>💭 思考プロセス</h4>
<p><strong>Step 1:</strong> Before スライドを読み、含まれるメッセージを数える → 1枚目に7つ以上の情報</p>
<p><strong>Step 2:</strong> メッセージごとにグループ化 → 「上半期実績」と「下半期戦略」に大別</p>
<p><strong>Step 3:</strong> 各グループで「聴衆が持ち帰る1つ」を決める → タイトルに結論を書く</p>'''


def ppt2_process():
    '''Returns 思考プロセス HTML for PPT Lesson 2 model answer.'''
    return '''<h4>💭 思考プロセス</h4>
<p><strong>Step 1:</strong> 情報の「関係性」を見極める → スライド1は「順番」、スライド2は「割合」</p>
<p><strong>Step 2:</strong> 判断フローに当てはめる → 順番→フロー図、割合→棒グラフ</p>
<p><strong>Step 3:</strong> テキストからキーワードだけ抽出 → 長い説明文を短いラベルに圧縮</p>'''


def ppt3_process():
    '''Returns 思考プロセス HTML for PPT Lesson 3 model answer.'''
    return '''<h4>💭 思考プロセス</h4>
<p><strong>Step 1:</strong> シナリオから「相手の困りごと」を特定 → 乳製品売上95%、棚不足、集客施策なし</p>
<p><strong>Step 2:</strong> 困りごとに対する解決策を「相手のメリット」で語る → 売上15%UP、年間1,440万円増収</p>
<p><strong>Step 3:</strong> 実行の具体性を示す → 3ヶ月のタイムライン、Month 1→2→3のステップ</p>'''


def ai_chat_css():
    '''Returns CSS for the AI chat floating button and panel.'''
    return '''.ai-chat-toggle{position:fixed;bottom:24px;right:24px;width:56px;height:56px;border-radius:50%;background:var(--accent);color:#fff;border:none;font-size:1.5rem;cursor:pointer;z-index:200;box-shadow:0 4px 16px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center;transition:transform .2s}
.ai-chat-toggle:hover{transform:scale(1.08)}
.ai-chat-panel{position:fixed;bottom:90px;right:24px;width:360px;height:480px;background:#fff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.18);display:none;flex-direction:column;z-index:201;overflow:hidden}
.ai-chat-panel.open{display:flex}
.ai-chat-header{background:var(--primary);color:#fff;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:.95rem}
.ai-chat-close{background:none;border:none;color:#fff;font-size:1.2rem;cursor:pointer;padding:0 4px;opacity:.8}
.ai-chat-close:hover{opacity:1}
.ai-chat-messages{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
.ai-msg{display:flex}
.ai-msg.user{justify-content:flex-end}
.ai-msg.assistant{justify-content:flex-start}
.ai-bubble{max-width:80%;padding:10px 14px;border-radius:12px;font-size:.88rem;line-height:1.6;word-break:break-word}
.ai-msg.user .ai-bubble{background:var(--accent);color:#fff;border-bottom-right-radius:4px}
.ai-msg.assistant .ai-bubble{background:#F0F2F5;color:var(--text);border-bottom-left-radius:4px}
.ai-chat-input{display:flex;gap:8px;padding:12px;border-top:1px solid var(--border);background:#FAFBFC}
.ai-chat-input input{flex:1;padding:10px 14px;border:2px solid var(--border);border-radius:8px;font-size:.9rem;font-family:inherit;outline:none}
.ai-chat-input input:focus{border-color:var(--accent)}
.ai-chat-input button{background:var(--accent);color:#fff;border:none;padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;font-size:.9rem;white-space:nowrap}
.ai-chat-input button:hover{opacity:.85}
.ai-chat-input button:disabled{opacity:.5;cursor:not-allowed}
@media(max-width:768px){
  .ai-chat-panel{bottom:0;right:0;width:100%;height:100%;border-radius:0}
  .ai-chat-toggle{bottom:16px;right:16px}
}'''


def ai_chat_html():
    '''Returns HTML for the AI chat UI.'''
    return '''<button class="ai-chat-toggle" onclick="toggleAiChat()" title="AI先生に質問">🤖</button>
<div class="ai-chat-panel" id="chatPanel">
  <div class="ai-chat-header">
    <span>🤖 AI先生に質問</span>
    <button class="ai-chat-close" onclick="toggleAiChat()">✕</button>
  </div>
  <div class="ai-chat-messages" id="chatMessages">
    <div class="ai-msg assistant"><div class="ai-bubble">こんにちは！ミルクネクストの先輩社員です。Excel・PPT・ロジカルシンキングの質問、なんでも聞いてくださいね。</div></div>
  </div>
  <div class="ai-chat-input">
    <input type="text" id="chatInput" placeholder="質問を入力..." onkeydown="if(event.key==='Enter')sendAiChat()">
    <button onclick="sendAiChat()" id="chatSendBtn">送信</button>
  </div>
</div>'''


def ai_chat_js():
    '''Returns JavaScript for the AI chat functionality.'''
    return '''function toggleAiChat(){
  var panel=document.getElementById('chatPanel');
  if(!panel)return;
  panel.classList.toggle('open');
  if(panel.classList.contains('open')){
    var inp=document.getElementById('chatInput');
    if(inp)inp.focus();
  }
}

function getCurrentLessonContext(){
  var active=document.querySelector('.lesson-panel.active');
  if(!active)return '';
  var title=active.querySelector('.lesson-title');
  return title?title.textContent:'';
}

function escapeHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function sendAiChat(){
  var inp=document.getElementById('chatInput');
  var msgs=document.getElementById('chatMessages');
  var btn=document.getElementById('chatSendBtn');
  if(!inp||!msgs)return;
  var question=inp.value.trim();
  if(!question)return;
  inp.value='';

  var userDiv=document.createElement('div');
  userDiv.className='ai-msg user';
  userDiv.innerHTML='<div class="ai-bubble">'+escapeHtml(question)+'</div>';
  msgs.appendChild(userDiv);

  var loadDiv=document.createElement('div');
  loadDiv.className='ai-msg assistant';
  loadDiv.innerHTML='<div class="ai-bubble">考え中...</div>';
  msgs.appendChild(loadDiv);
  msgs.scrollTop=msgs.scrollHeight;

  if(btn)btn.disabled=true;

  var context=getCurrentLessonContext();
  fetch('/api/ask',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({question:question,context:context})
  })
  .then(function(res){return res.json()})
  .then(function(data){
    loadDiv.querySelector('.ai-bubble').innerHTML=escapeHtml(data.answer||'回答を取得できませんでした。');
    msgs.scrollTop=msgs.scrollHeight;
  })
  .catch(function(err){
    loadDiv.querySelector('.ai-bubble').innerHTML='エラーが発生しました。もう一度お試しください。';
    msgs.scrollTop=msgs.scrollHeight;
  })
  .finally(function(){
    if(btn)btn.disabled=false;
  });
}'''
