"""ロジカルシンキング コンテンツ: all-in-one HTML 統合用パネルHTML + JSコード"""


def lt_panels_html():
    """4つのレッスンパネル (lt1-lt4) の HTML を返す"""
    return '''<div id="lt1" class="lesson-panel">
  <h2 class="lesson-title">🧠 Lesson 1: MECE（漏れなくダブりなく）</h2>
  <p class="lesson-subtitle">分類の基本 — 全5問</p>

  <div class="textbook">
    <div class="tb-chapter">
      <div class="tb-chapter-icon">1</div>
      <div class="tb-chapter-title">MECE（ミーシー）を理解しよう</div>
    </div>

    <h4 class="tb-section">MECEとは何か？</h4>

    <p>MECEは <span class="tb-keyword">Mutually Exclusive, Collectively Exhaustive</span> の頭文字を取った略語で、
    日本語に訳すと<strong>「漏れなく、ダブりなく」</strong>という意味です。</p>

    <p>世界最大のコンサルティング会社「マッキンゼー」で生まれた考え方で、
    ビジネスの世界では最も基本的な思考ツールの一つです。
    何かを分類したり、問題を整理したりするとき、この原則に沿っているかどうかが
    分析の質を大きく左右します。</p>

    <div class="tb-highlight">
      <strong>Mutually Exclusive（ダブりなく）</strong> = 各グループが重なっていないこと<br>
      <strong>Collectively Exhaustive（漏れなく）</strong> = 全部を合わせると全体をカバーしていること
    </div>

    <h4 class="tb-section">身近な例で理解する</h4>

    <p>MECEは難しい概念ではありません。日常生活にもたくさん例があります。</p>

    <div class="tb-example">
      <span class="label">例1: 曜日</span>
      月・火・水・木・金・土・日 → すべての日がどれか1つに当てはまり、重複もない。<strong>これはMECE</strong>です。
    </div>

    <div class="tb-example">
      <span class="label">例2: 血液型</span>
      A型・B型・O型・AB型 → 誰でも必ず1つに当てはまる。<strong>これもMECE</strong>です。
    </div>

    <div class="tb-example">
      <span class="label">例3: 年齢</span>
      「子ども・大人・お年寄り」は一見良さそうですが…<br>
      → 「子ども」は何歳まで？「大人」と「お年寄り」の境目は？曖昧なので<strong>MECEとは言いにくい</strong>です。<br>
      → 「0〜19歳 / 20〜59歳 / 60歳以上」とすれば、明確にMECEになります。
    </div>

    <h4 class="tb-section">ビジネスでなぜMECEが大事なの？</h4>

    <p>仕事では、問題を分析したり、提案資料を作ったりするときに
    「分類」をする場面がとても多いです。</p>

    <p>たとえば、上司に「売上が下がった原因を調べて」と言われたとしましょう。
    このとき、原因の洗い出しに<strong>漏れ</strong>があると大事な原因を見落とし、
    <strong>ダブり</strong>があると同じことを二重に数えてしまいます。
    どちらも、間違った結論につながります。</p>

    <h4 class="tb-section">よくある失敗パターン</h4>

    <div class="tb-compare">
      <div class="tb-bad">
        <strong>ダブりの例</strong><br><br>
        社員を「営業部 / 製造部 / 正社員 / パート」に分類<br><br>
        → 「部署」と「雇用形態」という<strong>2つの違う軸</strong>が混ざっています。
        営業部の正社員は「営業部」にも「正社員」にも入ってしまいます。
      </div>
      <div class="tb-bad">
        <strong>漏れの例</strong><br><br>
        売上低迷の原因を「価格が高い / 品質が悪い」に分類<br><br>
        → 営業力不足、知名度の低さ、流通チャネルの問題…
        <strong>他にもたくさん原因がありえる</strong>のに見落としています。
      </div>
    </div>

    <div class="tb-good">
      <strong>MECEな分類の例</strong><br><br>
      売上低迷の原因を<strong>4P</strong>で分類：<br>
      ① Product（商品の問題）/ ② Price（価格の問題）/ ③ Place（流通の問題）/ ④ Promotion（販促の問題）<br><br>
      → ビジネスの要素を網羅した「型」を使うことで、漏れもダブりもなく整理できます。
    </div>

    <h4 class="tb-section">MECEに分類するコツ</h4>

    <div class="tb-tip">
      <strong>① 分類の「軸」を1つに決める</strong><br>
      「部署別」なら部署だけで分ける。「地域別」なら地域だけ。2つの軸を混ぜない。<br><br>
      <strong>② フレームワーク（型）を使う</strong><br>
      先人が考えた分類の型を使うと、自然にMECEに近づきます。<br><br>
      <strong>③ 「他にないか？」と自問する</strong><br>
      分類ができたら、「この分類に入らないものはないか？」と確認する習慣をつけましょう。
    </div>

    <button class="tb-toggle" onclick="this.nextElementSibling.classList.toggle('show')">
      ＋ ビジネスでよく使うフレームワーク一覧を見る
    </button>
    <div class="tb-hidden">
      <div class="tb-example">
        <span class="label">マーケティングの分析に使う型</span>
        <strong>4P</strong> = Product（商品）/ Price（価格）/ Place（流通）/ Promotion（販促）<br>
        → 自社の戦略を整理するときに使う。「何を・いくらで・どこで・どうやって売るか」<br><br>
        <strong>3C</strong> = Customer（顧客）/ Competitor（競合）/ Company（自社）<br>
        → 市場環境を分析するときに使う。「お客さん・ライバル・自分たち」の3者で考える<br><br>
        <strong>SWOT</strong> = Strengths（強み）/ Weaknesses（弱み）/ Opportunities（機会）/ Threats（脅威）<br>
        → 自社の状況を整理するときに使う。内部要因（強み・弱み）と外部要因（機会・脅威）に分ける
      </div>
    </div>

    <div class="tb-warn">
      フレームワークは便利ですが、最初から型にはめるのではなく、
      まず自分の頭で考えてから、「漏れがないかな？」とフレームワークで検証するのが理想的です。
    </div>
  </div>

  <h3>✏️ 演習問題</h3>
  <div id="mece-questions"></div>
</div>

<div id="lt2" class="lesson-panel">
  <h2 class="lesson-title">🧠 Lesson 2: ロジックツリー</h2>
  <p class="lesson-subtitle">問題を構造的に分解する — 全4問</p>

  <div class="textbook">
    <div class="tb-chapter">
      <div class="tb-chapter-icon">2</div>
      <div class="tb-chapter-title">ロジックツリーで問題を分解しよう</div>
    </div>

    <h4 class="tb-section">ロジックツリーとは何か？</h4>

    <p><span class="tb-keyword">ロジックツリー</span>は、1つの大きな問題やテーマを、
    木の枝のように段階的に分解していく図のことです。</p>

    <p>大きな問題をそのまま考えようとすると、何から手をつけていいかわかりません。
    でも、小さな要素に分解すれば、「どこに問題があるのか」「何をすればいいのか」が
    具体的に見えてきます。</p>

    <div class="tb-highlight">
      ロジックツリーは、Lesson 1で学んだ<strong>MECE</strong>を使って分解します。<br>
      各枝が「漏れなく、ダブりなく」なっていれば、良いロジックツリーです。
    </div>

    <h4 class="tb-section">身近な例で理解する</h4>

    <div class="tb-example">
      <span class="label">例: 「今月お金が足りない」を分解してみる</span>
      <strong>お金が足りない</strong><br>
      ├── <strong>収入が少ない</strong><br>
      │　　├── バイトのシフトが少なかった<br>
      │　　└── 先月の残業代が入っていない<br>
      └── <strong>支出が多い</strong><br>
      　　　├── 友達の結婚式のご祝儀<br>
      　　　├── スマホを買い替えた<br>
      　　　└── 外食が多かった<br><br>
      → こうすると「収入を増やす」のか「支出を減らす」のか、どちらに集中すべきかが明確になります。
    </div>

    <h4 class="tb-section">2種類のロジックツリー</h4>

    <p>ロジックツリーには大きく2つの使い方があります。目的によって使い分けましょう。</p>

    <div class="tb-compare">
      <div class="tb-good" style="border:1px solid #90CAF9; background:#E3F2FD;">
        <strong style="color:var(--accent)">Whyツリー（原因分析型）</strong><br><br>
        「<strong>なぜ</strong>この問題が起きているのか？」<br><br>
        使う場面：問題の原因を探りたいとき<br><br>
        例：「なぜ売上が下がったのか？」<br>
        → 客数が減った / 単価が下がった / 来店頻度が落ちた
      </div>
      <div class="tb-good" style="border:1px solid #A5D6A7; background:#E8F5E9;">
        <strong style="color:#2E7D32">Howツリー（解決策型）</strong><br><br>
        「<strong>どうすれば</strong>目標を達成できるか？」<br><br>
        使う場面：解決策を洗い出したいとき<br><br>
        例：「どうすれば売上を上げるか？」<br>
        → 新規顧客を増やす / 客単価を上げる / リピート率を高める
      </div>
    </div>

    <h4 class="tb-section">分解するときの「切り口」</h4>

    <p>ロジックツリーの質は「どう分解するか」で決まります。
    以下の2つのパターンを覚えておくと、スムーズに分解できます。</p>

    <div class="tb-example">
      <span class="label">パターン①: 掛け算で分解する</span>
      <strong>売上 ＝ 客数 × 客単価</strong><br>
      <strong>客数 ＝ 新規顧客 ＋ 既存顧客</strong><br>
      <strong>客単価 ＝ 1回あたり購入点数 × 商品単価</strong><br><br>
      数値で表せるものは、掛け算や足し算で分解すると自動的にMECEになります。
    </div>

    <div class="tb-example">
      <span class="label">パターン②: カテゴリで分解する</span>
      <strong>問題の原因 → 「商品」「営業」「販促」</strong><br>
      <strong>対象顧客 → 「新規」「既存」</strong><br>
      <strong>時間軸 → 「短期」「中期」「長期」</strong><br><br>
      Lesson 1のフレームワーク（4P、3Cなど）を使うのもこのパターンです。
    </div>

    <h4 class="tb-section">作り方の手順</h4>

    <div class="tb-tip">
      <strong>ステップ① 中心課題を書く</strong><br>
      何を分解するのか、1文で書きます。（例：「棚シェアが低い原因は？」）<br><br>
      <strong>ステップ② 第1階層を決める（大きく2〜3つに分ける）</strong><br>
      ここが最も重要です。MECEになっているか確認しましょう。<br><br>
      <strong>ステップ③ 各枝をさらに2〜3つに分ける</strong><br>
      具体的な原因や施策が見えるレベルまで掘り下げます。<br><br>
      <strong>ステップ④ MECEを確認する</strong><br>
      各階層で「漏れはないか？」「ダブっていないか？」をチェックします。
    </div>

    <div class="tb-warn">
      分解は<strong>2〜3階層が目安</strong>です。4階層以上に深くすると、
      実際に使いにくくなります。「具体的なアクションが見えるレベル」まで分解できれば十分です。
    </div>
  </div>

  <h3>✏️ 演習問題</h3>
  <div id="tree-questions"></div>
</div>

<div id="lt3" class="lesson-panel">
  <h2 class="lesson-title">🧠 Lesson 3: So What? / Why So?</h2>
  <p class="lesson-subtitle">事実から結論を導く — 全4問</p>

  <div class="textbook">
    <div class="tb-chapter">
      <div class="tb-chapter-icon">3</div>
      <div class="tb-chapter-title">So What? / Why So? で論理をつなごう</div>
    </div>

    <h4 class="tb-section">ビジネスで一番言われる言葉「で、結局何？」</h4>

    <p>会議やプレゼンで、データや事実をたくさん並べたのに、
    上司や先輩から<strong>「で、結局何が言いたいの？」</strong>と言われてしまう…。
    これは新人がよく経験する場面です。</p>

    <p>この問題を解決するのが <span class="tb-keyword">So What?</span> と <span class="tb-keyword">Why So?</span> という2つの思考法です。
    セットで使うことで、<strong>説得力のある主張</strong>ができるようになります。</p>

    <h4 class="tb-section">So What?（だから何？）</h4>

    <p><strong>事実やデータ</strong>を見て、そこから<strong>「だから何が言えるのか？」</strong>と
    一段上の結論や示唆を導き出すことです。</p>

    <p>ポイントは、事実をそのまま繰り返すのではなく、
    <strong>「次に何をすべきか」という行動提案</strong>まで踏み込むことです。</p>

    <div class="tb-compare">
      <div class="tb-bad">
        <strong>事実：</strong>ヨーグルトが前年比120%<br><br>
        「ヨーグルトが売れています」<br><br>
        → これは事実をそのまま言い換えただけ。上司は「それは見ればわかるよ」と思います。
      </div>
      <div class="tb-good">
        <strong>事実：</strong>ヨーグルトが前年比120%<br><br>
        「健康志向のトレンドを捉えている。新商品開発を加速して、この波に乗るべき」<br><br>
        → 事実から<strong>示唆と行動提案</strong>を導いている。これが良い So What です。
      </div>
    </div>

    <div class="tb-example">
      <span class="label">So What? の練習方法</span>
      データや事実を見たら、自分に<strong>3回「だから何？」</strong>と問いかけてみてください。<br><br>
      <strong>1回目：</strong>ヨーグルト前年比120% → 「ヨーグルトが伸びている」（まだ浅い）<br>
      <strong>2回目：</strong>→ 「健康志向トレンドに合っている」（少し深くなった）<br>
      <strong>3回目：</strong>→ 「このトレンドに合った新商品を出せば、さらに伸ばせる」（行動提案に到達）
    </div>

    <h4 class="tb-section">Why So?（なぜそう言える？）</h4>

    <p>So What? が「事実 → 結論」の方向だとすると、
    <span class="tb-keyword">Why So?</span> はその<strong>逆方向</strong>です。</p>

    <p>自分の主張や結論に対して<strong>「なぜそう言えるの？」</strong>と根拠を示すことです。
    根拠がなければ、どんな良い提案も「あなたの感想ですよね」で終わってしまいます。</p>

    <div class="tb-compare">
      <div class="tb-bad">
        <strong>主張：</strong>業務用チャネルを強化すべき<br><br>
        「競合がやっているから」<br>
        「なんとなく伸びそうだから」<br><br>
        → 根拠が弱すぎます。
      </div>
      <div class="tb-good">
        <strong>主張：</strong>業務用チャネルを強化すべき<br><br>
        「① 量販チャネルの成長が鈍化している（市場環境）」<br>
        「② 業務用市場が回復傾向にある（機会）」<br>
        「③ 当社に大容量規格の生産余力がある（実現可能性）」<br><br>
        → 3つの根拠で裏付けている。説得力が全然違います。
      </div>
    </div>

    <div class="tb-tip">
      根拠は<strong>3つ</strong>が理想的な数です。1つだと弱く、5つだと多すぎて印象に残りません。<br><br>
      おすすめの3点セット：<br>
      <strong>① 市場環境</strong>（外部の状況はどうか？）<br>
      <strong>② 機会 or 課題</strong>（チャンスや問題は何か？）<br>
      <strong>③ 自社の能力</strong>（自分たちにできるのか？）
    </div>

    <h4 class="tb-section">ピラミッドストラクチャー</h4>

    <p>So What? と Why So? を組み合わせると、
    <span class="tb-keyword">ピラミッドストラクチャー</span>という論理構造ができあがります。
    これは、ビジネス文書やプレゼンの<strong>最も基本的な構成</strong>です。</p>

    <div class="tb-diagram">
      ┌─────────────────────┐<br>
      │ 　<strong>主張（結論）</strong>　 │ ← まず結論を言う<br>
      └────────┬────────────┘<br>
      ┌────────┴────────────┐<br>
      │ 　<strong>根拠（Why So?）</strong>　│ ← なぜそう言えるか<br>
      │ 　① ② ③　　　 　 │<br>
      └────────┬────────────┘<br>
      ┌────────┴────────────┐<br>
      │ 　<strong>具体例・データ</strong>　 │ ← 数字や事例で裏付け<br>
      └─────────────────────┘
    </div>

    <div class="tb-example">
      <span class="label">ピラミッドストラクチャーの実例</span>
      <strong>主張：</strong>ギリシャヨーグルトを重点商品にすべきだ<br><br>
      <strong>根拠①：</strong>高たんぱく食品市場が年15%で成長している（市場トレンド）<br>
      <strong>根拠②：</strong>当社のギリシャヨーグルトは味の評価で競合1位（商品力）<br>
      <strong>根拠③：</strong>製造ラインに余力があり、増産対応が可能（実現可能性）<br><br>
      <strong>具体例：</strong>A社は類似の高たんぱくヨーグルトで売上2倍を達成している
    </div>

    <div class="tb-warn">
      日本の学校教育では「起承転結」（結論は最後）と教わりますが、
      ビジネスでは<strong>「結論ファースト」</strong>が鉄則です。
      まず結論を言い、その後に根拠と具体例を示しましょう。
    </div>
  </div>

  <h3>✏️ 演習問題</h3>
  <div id="sowhat-questions"></div>
</div>

<div id="lt4" class="lesson-panel">
  <h2 class="lesson-title">🧠 Lesson 4: 総合演習</h2>
  <p class="lesson-subtitle">実践ビジネス課題 — 全3問</p>

  <div class="textbook">
    <div class="tb-chapter">
      <div class="tb-chapter-icon">4</div>
      <div class="tb-chapter-title">総合演習 — 実際のビジネス課題を分析しよう</div>
    </div>

    <h4 class="tb-section">この演習で身につけること</h4>

    <p>Lesson 1〜3で学んだ3つのスキルを<strong>組み合わせて</strong>使います。
    実際の仕事では、MECEもSo What?も単独で使うことはほとんどありません。
    <strong>「分解 → 分析 → 提案」</strong>という一連の流れで使いこなすことが大切です。</p>

    <div class="tb-diagram">
      <strong>Step 1</strong> 課題をMECEに分解する（Lesson 1）<br>
      　　↓<br>
      <strong>Step 2</strong> データから So What? を導く（Lesson 3）<br>
      　　↓<br>
      <strong>Step 3</strong> 具体的な改善提案をまとめる（Lesson 2のツリー＋Lesson 3の構造）
    </div>

    <h4 class="tb-section">演習で出てくるビジネス用語</h4>

    <p>この演習ではスーパーへの営業シナリオを扱います。
    出てくる専門用語を先に理解しておきましょう。</p>

    <div class="tb-example">
      <span class="label">棚割り（たなわり）</span>
      スーパーなどの小売店で、<strong>どの商品を、棚のどの位置に、何個並べるか</strong>を決める配置計画のこと。
      売上に直結するため、食品メーカーの営業担当が小売店のバイヤー（仕入担当者）に提案します。<br><br>
      メーカーにとって「自社商品をいい場所にたくさん並べてもらうこと」が営業の重要な仕事です。
    </div>

    <div class="tb-example">
      <span class="label">ゴールデンゾーン</span>
      スーパーの棚で<strong>目の高さ〜手の高さ</strong>にあたる位置のこと。
      お客さんが最も目につきやすく、手に取りやすいので、一番売れる場所です。<br><br>
      逆に、棚の一番上や一番下は目立たないので売れにくいです。
    </div>

    <div class="tb-example">
      <span class="label">フェイス数</span>
      商品が棚の前面に<strong>何列並んでいるか</strong>の数。たとえば牛乳が横に3本並んでいたら「3フェイス」です。<br><br>
      フェイス数が多い＝お客さんの目に入りやすい＝売れやすい。
      フェイス数を増やしてもらうことは、メーカー営業の大事な目標です。
    </div>

    <div class="tb-example">
      <span class="label">SKU（エスケーユー）</span>
      <strong>Stock Keeping Unit</strong> の略で、<strong>商品管理の最小単位</strong>のこと。<br><br>
      たとえば「北海道フレッシュ牛乳 1L」で1SKU、「北海道フレッシュ牛乳 500ml」で別の1SKU。
      同じブランドでもサイズや味が違えば別のSKUとして数えます。<br><br>
      「当店では牛乳は6SKU取り扱っています」＝「6種類の牛乳商品を置いています」という意味。
    </div>

    <div class="tb-example">
      <span class="label">棚回転率</span>
      棚にある商品が<strong>どれくらいの速さで売れるか</strong>を示す数値。<br><br>
      回転率が高い＝よく売れる＝小売店にとって利益になる商品。
      回転率が低い商品は「棚から外される（撤去）」リスクがあります。
    </div>

    <button class="tb-toggle" onclick="this.nextElementSibling.classList.toggle('show')">
      ＋ その他のビジネス用語も見る
    </button>
    <div class="tb-hidden">
      <div class="tb-example">
        <span class="label">ボトルネック</span>
        全体の成果を<strong>最も制約している要因</strong>のこと。ワインのボトルの首（ネック）が一番細く、
        液体の流れを制限することが語源です。<br><br>
        「この問題のボトルネックは棚スペースの不足だ」＝「棚が狭いことが、一番の原因だ」
      </div>
      <div class="tb-example">
        <span class="label">KPI（ケーピーアイ）</span>
        <strong>Key Performance Indicator</strong>（重要業績評価指標）の略。
        目標に向けた進捗を測るための<strong>具体的な数値</strong>のこと。<br><br>
        例：「売上金額」「来店客数」「リピート率」「棚回転率」など。
        「KPIを設定する」＝「何の数字を追いかけるか決める」ということです。
      </div>
      <div class="tb-example">
        <span class="label">エンド陳列</span>
        スーパーの棚の<strong>端（エンド）に設ける特設コーナー</strong>のこと。
        通路に面しているので非常に目立ち、売上アップ効果が高いです。<br><br>
        季節商品やセール品が置かれることが多く、メーカーにとっては「エンドを取れるか」が大きな勝負です。
      </div>
      <div class="tb-example">
        <span class="label">バイヤー</span>
        小売店（スーパーなど）の<strong>仕入れ担当者</strong>のこと。
        どの商品を、いくつ、どの棚に置くかを決める権限を持っています。<br><br>
        メーカーの営業担当にとって、バイヤーは最も重要な交渉相手です。
      </div>
      <div class="tb-example">
        <span class="label">リベート</span>
        メーカーが小売店に支払う<strong>販売報奨金</strong>のこと。
        「この商品を○個以上仕入れてくれたら、仕入額の5%を還元します」といった形で使います。<br><br>
        新商品を導入してもらうための「お願い料」のようなものです。
      </div>
    </div>

    <h4 class="tb-section">演習の進め方</h4>

    <div class="tb-tip">
      Step 1 → 2 → 3 の順番で解いてください。各ステップで自分の考えを書いてから、
      模範解答と見比べましょう。<br><br>
      <strong>模範解答と違っても問題ありません。</strong>論理的に整理できていれば、
      切り口が違うだけで正解です。大事なのは「なぜそう考えたのか」を説明できることです。
    </div>
  </div>

  <h3>✏️ 演習問題</h3>
  <div id="synthesis-section"></div>
</div>'''


def lt_js_code():
    """ロジカルシンキングの全JavaScriptコードを返す（all-in-one統合用）"""
    return '''// ===== Logical Thinking Data =====
var meceQuestions = [
  {
    q: "取引先を「スーパー」「コンビニ」「飲食店」「大口顧客」に分類しました。問題点は？",
    options: [
      "漏れがある（給食・卸が入っていない）",
      "ダブりがある（大口顧客はスーパーにもコンビニにもいる）",
      "漏れもダブりもある",
      "問題なし（MECE）"
    ],
    answer: 2,
    explanation: "「大口顧客」は業態ではなく取引規模の軸なので、スーパーの大口顧客は重複します（ダブり）。また給食・卸が抜けています（漏れ）。分類軸を統一しましょう。"
  },
  {
    q: "乳製品カテゴリを「牛乳」「ヨーグルト」「チーズ」「バター」「生クリーム」に分類。問題点は？",
    options: [
      "漏れがある（乳飲料やアイスが抜けている）",
      "ダブりがある",
      "漏れもダブりもある",
      "問題なし（MECE）"
    ],
    answer: 0,
    explanation: "自社の商品ラインナップとしては問題ないですが、乳製品全体としては乳飲料・練乳・粉乳などが漏れています。対象範囲を明確にすることが大切です。"
  },
  {
    q: "売上低迷の原因を「価格が高い」「品質が悪い」「競合が強い」に分類。問題点は？",
    options: [
      "漏れがある（営業力・棚割り・認知度等が未考慮）",
      "ダブりがある",
      "漏れもダブりもある",
      "問題なし（MECE）"
    ],
    answer: 0,
    explanation: "営業力の不足、棚割りの問題、認知度の低さなど、他の要因が抜けています。4P（Product/Price/Place/Promotion）のフレームワークを使うとMECEに近づきます。"
  },
  {
    q: "社員を「量販営業部」「業務用営業部」「製造部」「正社員」「パート」に分類。問題点は？",
    options: [
      "漏れがある",
      "ダブりがある（部署と雇用形態が混在）",
      "漏れもダブりもある",
      "問題なし（MECE）"
    ],
    answer: 1,
    explanation: "「部署」と「雇用形態」という2つの異なる軸が混在しています。量販営業部の正社員は両方に該当するのでダブりです。分類は1つの軸で行うべきです。"
  },
  {
    q: "配送エリアを「北海道」「東北」「関東」「中部」「近畿」「中国」「四国」「九州・沖縄」に分類。問題点は？",
    options: [
      "漏れがある",
      "ダブりがある",
      "漏れもダブりもある",
      "問題なし（MECE）"
    ],
    answer: 3,
    explanation: "正解！日本の全地域をカバーしており、重複もありません。これはMECEな分類の良い例です。"
  }
];

var treeQuestions = [
  {
    q: "「スーパーの乳製品棚で自社商品のシェアが低い」原因をロジックツリーで分解してください",
    hint: "まず大きく2-3つに分け、それぞれをさらに分解します",
    modelAnswer: {
      root: "棚シェアが低い原因",
      children: [
        { label: "商品力の問題", children: [
          { label: "競合と比較した味・品質の差" },
          { label: "パッケージの訴求力不足" },
          { label: "価格帯が合っていない" }
        ]},
        { label: "営業力の問題", children: [
          { label: "バイヤーへの提案頻度が少ない" },
          { label: "棚割り提案のデータ不足" },
          { label: "競合の営業が強い" }
        ]},
        { label: "販促の問題", children: [
          { label: "試食・サンプル配布の不足" },
          { label: "POP・販促物の魅力不足" },
          { label: "消費者認知度の低さ" }
        ]}
      ]
    }
  },
  {
    q: "「取引先（スーパー）の乳製品売上を伸ばす」方法をロジックツリーで分解してください",
    hint: "売上＝客数×客単価で分解するのが基本です",
    modelAnswer: {
      root: "乳製品売上を伸ばす",
      children: [
        { label: "買上客数を増やす", children: [
          { label: "試食イベントで新規購入を促進" },
          { label: "健康訴求POPで非購入者にアプローチ" },
          { label: "レシピ提案で購入シーンを拡大" }
        ]},
        { label: "客単価を上げる", children: [
          { label: "高付加価値品（ギリシャヨーグルト等）の拡充" },
          { label: "まとめ買い促進（複数購入割引）" },
          { label: "クロスセル（牛乳+ヨーグルトの関連陳列）" }
        ]},
        { label: "購入頻度を上げる", children: [
          { label: "賞味期限の短い商品の鮮度訴求" },
          { label: "週替わりの特売ローテーション" },
          { label: "季節限定フレーバーで来店動機を創出" }
        ]}
      ]
    }
  }
];

var sowhatQuestions = [
  {
    q: "事実: 「当社の牛乳カテゴリは売上の35%を占めるが、市場全体の牛乳消費量は年々減少している」\\nSo What?（この事実から導かれる結論は？）",
    options: [
      "牛乳の値上げで利益を確保すべき",
      "牛乳以外に注力すべきだ",
      "主力カテゴリの市場縮小により、中長期的な売上構成の見直しが必要",
      "特に問題はない"
    ],
    answer: 2,
    explanation: "「So What?」は事実から示唆・結論を導くこと。主力カテゴリの市場縮小は、ヨーグルト・チーズ等の成長カテゴリへのシフトや高付加価値牛乳への転換の必要性を示唆します。"
  },
  {
    q: "結論: 「業務用チャネル（飲食・ホテル）を強化すべきだ」\\nWhy So?（この結論を支える根拠として最も適切な組み合わせは？）",
    options: [
      "量販チャネルの成長鈍化 + 業務用市場の回復傾向 + 当社に大容量規格の生産余力がある",
      "競合が業務用を強化しているから + 営業部長がやりたがっている",
      "利益率が高そうだから + 新しいチャレンジだから",
      "インバウンド需要が増えているから"
    ],
    answer: 0,
    explanation: "「Why So?」は結論の根拠を示すこと。①市場環境（量販の頭打ち）、②機会（業務用の回復）、③実現可能性（自社の生産力）の3点が揃うのが良い根拠です。"
  },
  {
    q: "以下のうち「So What?」が最も弱い（事実の繰り返しに過ぎない）のはどれ？",
    options: [
      "ヨーグルトの売上が前年比120%なので、棚スペース拡大を提案すべき",
      "ヨーグルトの売上が前年比120%なので、ヨーグルトが売れている",
      "ヨーグルトの売上が前年比120%なので、健康志向トレンドを捉えた新商品開発を加速すべき",
      "ヨーグルトの売上が前年比120%なので、このペースが続けば2年後にチーズを抜く"
    ],
    answer: 1,
    explanation: "「ヨーグルトが売れている」は事実の言い換えであり、新しい示唆（So What）になっていません。良いSo Whatは事実から一段上の結論や行動提案を導きます。"
  },
  {
    q: "次のうち、ロジカルな主張構造になっているのはどれ？\\n（主張→根拠→具体例の構造）",
    options: [
      "ギリシャヨーグルトを重点商品にすべきだ → 高たんぱく市場が年15%成長している → A社は類似商品で売上2倍を達成",
      "ギリシャヨーグルトは良い → 流行っている → おいしいから",
      "ギリシャヨーグルトを重点商品にすべきだ → 利益率が高い → 工場の稼働率が低い",
      "A社がギリシャヨーグルトで成功した → だから当社もやるべき → 業界トレンドだ"
    ],
    answer: 0,
    explanation: "①は「主張（重点化すべき）→根拠（市場成長のデータ）→具体例（A社の実績）」の構造。②は根拠が弱く、③は根拠がバラバラ、④は1社の事例だけで一般化しています。"
  }
];

var synthesisSteps = [
  {
    title: "Step 1: 課題をMECEに分解",
    scenario: "あなたの会社（ミルクネクスト株式会社）の量販営業部で、主要取引先スーパー「グリーンバスケット」での自社商品売上が前年比85%に低下しています。この問題をMECEに分解してください。",
    hint: "ヒント: 売上＝取扱SKU数 × 棚回転率 × 単価 で分解するか、4P（Product/Price/Place/Promotion）で考えると整理しやすいです。",
    modelAnswer: "【分解例】\\n1. 商品（Product）の問題\\n  - SKUの鮮度（新商品投入が少ない）\\n  - 競合品との品質・味の差\\n  - 健康志向トレンドへの対応遅れ\\n2. 棚割り（Place）の問題\\n  - 棚位置が悪い（下段に追いやられている）\\n  - フェイス数の減少\\n  - 競合の棚割り提案が強い\\n3. 販促（Promotion）の問題\\n  - 試食販売の頻度低下\\n  - POP・販促物の更新がされていない\\n  - 季節施策の提案が遅い"
  },
  {
    title: "Step 2: So What?（分析から示唆を導く）",
    scenario: "Step 1の分解を踏まえ、以下のデータから「So What?」を導いてください。\\n\\n【データ】\\n・当社SKU数: 前年と同じ6SKU\\n・棚フェイス数: 8→5に減少（競合が3フェイス獲得）\\n・当社商品の棚回転率: 前年比90%（やや低下）\\n・競合A社のヨーグルト新商品: 発売3ヶ月で棚回転率当社の1.5倍",
    hint: "ヒント: 最大のボトルネックはどこか？数字から読み取れる本質的な課題は何か？",
    modelAnswer: "【So What】\\n売上低下の最大の原因は「棚フェイス数の減少」にある。8→5フェイスと37%減少しており、これが直接的に売上減に繋がっている。\\n\\n競合A社が新商品で棚を奪っていることから、「新商品の投入と棚割り提案の積極性で負けている」のが本質的な課題。\\n\\n→ 健康志向の新商品（プロテインヨーグルト等）を武器にした棚割り提案で、失った3フェイスを奪還する必要がある。"
  },
  {
    title: "Step 3: 改善提案をまとめる",
    scenario: "Step 1-2の分析を踏まえて、具体的な改善提案を3つ作成してください。それぞれ「施策名」「具体的な内容」「期待効果」を記載してください。",
    hint: "ヒント: 短期（すぐできる）と中期（1-3ヶ月）の施策を組み合わせましょう。",
    modelAnswer: "【改善提案】\\n\\n1. 新商品を武器にした棚割り再提案（短期）\\n  内容: プロテインヨーグルトの先行導入を提案、POSデータ付きの棚割りシミュレーションを提示\\n  期待効果: 2フェイス奪還、売上前年比95%まで回復\\n\\n2. 月次試食販売イベントの実施（短期〜中期）\\n  内容: 毎月第1土曜に当社販売員を派遣、試食+クーポン配布\\n  期待効果: 棚回転率10%改善、リピート購入の促進\\n\\n3. 季節MD提案の先行実施（中期）\\n  内容: 3ヶ月先の季節提案を毎月バイヤーに提出（鍋シーズンのチーズ、夏のドリンクヨーグルト等）\\n  期待効果: 競合に先行して棚を確保、バイヤーからの信頼向上"
  }
];

// ===== LT State =====
var ltState = JSON.parse(localStorage.getItem('lt-state') || '{}');
if (!ltState.mece) ltState.mece = {};
if (!ltState.tree) ltState.tree = {};
if (!ltState.sowhat) ltState.sowhat = {};
if (!ltState.synthesis) ltState.synthesis = { step: 0, answers: {} };

function ltSaveState() {
  localStorage.setItem('lt-state', JSON.stringify(ltState));
  ltUpdateProgress();
}

function ltCountCompleted() {
  var count = 0;
  // MECE: 5
  for (var i = 0; i < 5; i++) if (ltState.mece[i] !== undefined) count++;
  // Tree: 4 (2 build + 2 compare = counted as 4)
  for (var i = 0; i < 2; i++) if (ltState.tree[i]) count++;
  count += Object.keys(ltState.tree).filter(function(k) { return ltState.tree[k] === 'compared'; }).length;
  // SoWhat: 4
  for (var i = 0; i < 4; i++) if (ltState.sowhat[i] !== undefined) count++;
  // Synthesis: 3 steps
  count += Object.keys(ltState.synthesis.answers).length;
  return Math.min(count, 16);
}

function ltUpdateProgress() {
  var done = ltCountCompleted();
  // Update sidebar badges
  var m = 0; for (var i=0;i<5;i++) if(ltState.mece[i]!==undefined) m++;
  var el = document.getElementById('nb-l1');
  if(el) el.textContent = m===5 ? '✓' : m+'/5';
  if(el && m===5) el.className = 'nav-badge done';

  var t = 0; for (var i=0;i<2;i++) { if(ltState.tree[i]) t++; if(ltState.tree[i]==='compared') t++; }
  t = Math.min(t, 4);
  el = document.getElementById('nb-l2');
  if(el) el.textContent = t===4 ? '✓' : t+'/4';
  if(el && t===4) el.className = 'nav-badge done';

  var s = 0; for (var i=0;i<4;i++) if(ltState.sowhat[i]!==undefined) s++;
  el = document.getElementById('nb-l3');
  if(el) el.textContent = s===4 ? '✓' : s+'/4';
  if(el && s===4) el.className = 'nav-badge done';

  var synth = Object.keys(ltState.synthesis.answers).length;
  el = document.getElementById('nb-l4');
  if(el) el.textContent = synth===3 ? '✓' : synth+'/3';
  if(el && synth===3) el.className = 'nav-badge done';

  // Update dashboard
  var dashEl = document.getElementById('dash-l');
  if(dashEl) dashEl.textContent = done;
}

// ===== Lesson 1: MECE =====
function renderMece() {
  var container = document.getElementById('mece-questions');
  if (!container) return;
  container.innerHTML = '';
  meceQuestions.forEach(function(q, qi) {
    var div = document.createElement('div');
    div.className = 'lt-question';
    div.innerHTML = '<p>Q' + (qi+1) + '. ' + q.q + '</p><div class="options" id="mece-opts-'+qi+'"></div>' +
      '<button class="check-btn" id="mece-btn-'+qi+'" onclick="checkMece('+qi+')">回答する</button>' +
      '<div class="feedback" id="mece-fb-'+qi+'"></div>';
    container.appendChild(div);

    var opts = div.querySelector('#mece-opts-'+qi);
    q.options.forEach(function(opt, oi) {
      var label = document.createElement('label');
      label.innerHTML = '<input type="radio" name="mece'+qi+'" value="'+oi+'"' +
        (ltState.mece[qi] !== undefined && ltState.mece[qi] == oi ? ' checked' : '') + '> ' + opt;
      opts.appendChild(label);
    });

    if (ltState.mece[qi] !== undefined) showMeceFeedback(qi, ltState.mece[qi]);
  });
}

function checkMece(qi) {
  var sel = document.querySelector('input[name="mece'+qi+'"]:checked');
  if (!sel) return;
  var val = parseInt(sel.value);
  ltState.mece[qi] = val;
  ltSaveState();
  showMeceFeedback(qi, val);
}

function showMeceFeedback(qi, val) {
  var q = meceQuestions[qi];
  var fb = document.getElementById('mece-fb-'+qi);
  var isCorrect = val === q.answer;
  fb.className = 'feedback show ' + (isCorrect ? 'correct' : 'wrong');
  fb.textContent = (isCorrect ? '✓ 正解！' : '✗ 不正解。') + ' ' + q.explanation;

  var opts = document.querySelectorAll('#mece-opts-'+qi+' label');
  opts.forEach(function(label, i) {
    label.className = '';
    if (i === q.answer) label.className = 'correct';
    else if (i === val && !isCorrect) label.className = 'wrong';
  });
  document.getElementById('mece-btn-'+qi).disabled = true;
}

// ===== Lesson 2: Logic Tree =====
function renderTree() {
  var container = document.getElementById('tree-questions');
  if (!container) return;
  container.innerHTML = '';
  treeQuestions.forEach(function(tq, ti) {
    var div = document.createElement('div');
    div.className = 'lt-question';
    div.innerHTML = '<p>Q' + (ti+1) + '. ' + tq.q + '</p>' +
      '<p style="font-size:0.85rem;color:var(--text-light);margin-bottom:12px">💡 ' + tq.hint + '</p>' +
      '<div class="tree-container" id="tree-container-'+ti+'"></div>' +
      '<button class="check-btn" onclick="compareTree('+ti+')" style="margin-right:8px">模範解答と比較</button>' +
      '<button class="check-btn" onclick="resetTree('+ti+')" style="background:var(--border);color:var(--text)">リセット</button>' +
      '<div class="model-answer" id="tree-model-'+ti+'"></div>';
    container.appendChild(div);
    renderTreeNode(ti);
    renderModelAnswer(ti);
  });
}

function getTreeData(ti) {
  if (!ltState.tree['data_'+ti]) {
    ltState.tree['data_'+ti] = { label: '', children: [{ label: '', children: [] }] };
  }
  return ltState.tree['data_'+ti];
}

function renderTreeNode(ti) {
  var container = document.getElementById('tree-container-'+ti);
  container.innerHTML = '';
  var tree = getTreeData(ti);
  container.appendChild(buildTreeDOM(tree, ti, []));
}

function buildTreeDOM(node, ti, path) {
  var div = document.createElement('div');
  div.className = 'tree-node';
  var content = document.createElement('div');
  content.className = 'tree-node-content';

  var input = document.createElement('input');
  input.type = 'text';
  input.value = node.label;
  input.placeholder = path.length === 0 ? '中心課題を入力' : 'ノードを入力';
  input.oninput = function() {
    node.label = this.value;
    ltState.tree['data_'+ti] = getTreeData(ti);
    ltSaveState();
  };
  content.appendChild(input);

  var addBtn = document.createElement('button');
  addBtn.className = 'tree-btn';
  addBtn.textContent = '+ 子ノード';
  addBtn.onclick = function() {
    if (!node.children) node.children = [];
    node.children.push({ label: '', children: [] });
    ltSaveState();
    renderTreeNode(ti);
  };
  content.appendChild(addBtn);

  if (path.length > 0) {
    var rmBtn = document.createElement('button');
    rmBtn.className = 'tree-btn remove';
    rmBtn.textContent = '×';
    rmBtn.onclick = function() {
      var parent = getNodeByPath(getTreeData(ti), path.slice(0, -1));
      parent.children.splice(path[path.length-1], 1);
      ltSaveState();
      renderTreeNode(ti);
    };
    content.appendChild(rmBtn);
  }

  div.appendChild(content);

  if (node.children) {
    node.children.forEach(function(child, ci) {
      div.appendChild(buildTreeDOM(child, ti, path.concat([ci])));
    });
  }
  return div;
}

function getNodeByPath(tree, path) {
  var node = tree;
  for (var i = 0; i < path.length; i++) node = node.children[path[i]];
  return node;
}

function compareTree(ti) {
  ltState.tree[ti] = 'compared';
  ltSaveState();
  document.getElementById('tree-model-'+ti).classList.add('show');
}

function resetTree(ti) {
  ltState.tree['data_'+ti] = { label: '', children: [{ label: '', children: [] }] };
  delete ltState.tree[ti];
  ltSaveState();
  renderTreeNode(ti);
  document.getElementById('tree-model-'+ti).classList.remove('show');
}

function renderModelAnswer(ti) {
  var ma = treeQuestions[ti].modelAnswer;
  var container = document.getElementById('tree-model-'+ti);
  container.innerHTML = '<h4>模範解答</h4>';
  var ul = document.createElement('ul');
  ul.className = 'model-tree';
  var rootLi = document.createElement('li');
  rootLi.innerHTML = '<strong>' + ma.root + '</strong>';
  var subUl = document.createElement('ul');
  ma.children.forEach(function(c) {
    var li = document.createElement('li');
    li.innerHTML = '<strong>' + c.label + '</strong>';
    if (c.children) {
      var sub2 = document.createElement('ul');
      c.children.forEach(function(gc) {
        var gli = document.createElement('li');
        gli.textContent = gc.label;
        sub2.appendChild(gli);
      });
      li.appendChild(sub2);
    }
    subUl.appendChild(li);
  });
  rootLi.appendChild(subUl);
  ul.appendChild(rootLi);
  container.appendChild(ul);
  container.innerHTML += '<p style="margin-top:8px;font-size:0.85rem;color:var(--text-light)">※ 模範解答は一例です。異なる切り口でも、MECEに分解できていれば正解です。</p>';
}

// ===== Lesson 3: So What / Why So =====
function renderSoWhat() {
  var container = document.getElementById('sowhat-questions');
  if (!container) return;
  container.innerHTML = '';
  sowhatQuestions.forEach(function(q, qi) {
    var div = document.createElement('div');
    div.className = 'lt-question';
    var qText = q.q.replace(/\\n/g, '<br>');
    div.innerHTML = '<p>Q' + (qi+1) + '. ' + qText + '</p><div class="options" id="sw-opts-'+qi+'"></div>' +
      '<button class="check-btn" id="sw-btn-'+qi+'" onclick="checkSoWhat('+qi+')">回答する</button>' +
      '<div class="feedback" id="sw-fb-'+qi+'"></div>';
    container.appendChild(div);

    var opts = div.querySelector('#sw-opts-'+qi);
    q.options.forEach(function(opt, oi) {
      var label = document.createElement('label');
      label.innerHTML = '<input type="radio" name="sw'+qi+'" value="'+oi+'"' +
        (ltState.sowhat[qi] !== undefined && ltState.sowhat[qi] == oi ? ' checked' : '') + '> ' + opt;
      opts.appendChild(label);
    });

    if (ltState.sowhat[qi] !== undefined) showSoWhatFeedback(qi, ltState.sowhat[qi]);
  });
}

function checkSoWhat(qi) {
  var sel = document.querySelector('input[name="sw'+qi+'"]:checked');
  if (!sel) return;
  var val = parseInt(sel.value);
  ltState.sowhat[qi] = val;
  ltSaveState();
  showSoWhatFeedback(qi, val);
}

function showSoWhatFeedback(qi, val) {
  var q = sowhatQuestions[qi];
  var fb = document.getElementById('sw-fb-'+qi);
  var isCorrect = val === q.answer;
  fb.className = 'feedback show ' + (isCorrect ? 'correct' : 'wrong');
  fb.textContent = (isCorrect ? '✓ 正解！' : '✗ 不正解。') + ' ' + q.explanation;

  var opts = document.querySelectorAll('#sw-opts-'+qi+' label');
  opts.forEach(function(label, i) {
    label.className = '';
    if (i === q.answer) label.className = 'correct';
    else if (i === val && !isCorrect) label.className = 'wrong';
  });
  document.getElementById('sw-btn-'+qi).disabled = true;
}

// ===== Lesson 4: Synthesis =====
function renderSynthesis() {
  var container = document.getElementById('synthesis-section');
  if (!container) return;
  container.innerHTML = '';

  // Step indicators
  var indicators = document.createElement('div');
  indicators.className = 'step-indicator';
  for (var i = 0; i < 3; i++) {
    var dot = document.createElement('div');
    dot.className = 'step-dot' + (i === ltState.synthesis.step ? ' active' : '') +
      (ltState.synthesis.answers[i] ? ' done' : '');
    dot.textContent = i + 1;
    indicators.appendChild(dot);
  }
  container.appendChild(indicators);

  var step = synthesisSteps[ltState.synthesis.step];
  var div = document.createElement('div');
  div.className = 'lt-question';
  var scenarioText = step.scenario.replace(/\\n/g, '<br>');
  div.innerHTML = '<h3 style="color:var(--accent);margin-bottom:8px">' + step.title + '</h3>' +
    '<p>' + scenarioText + '</p>' +
    '<p style="font-size:0.85rem;color:var(--text-light);margin:8px 0">' + step.hint + '</p>' +
    '<div class="step-form">' +
    '<textarea id="synth-answer" placeholder="ここに回答を入力...">' +
    (ltState.synthesis.answers[ltState.synthesis.step] || '') + '</textarea>' +
    '<button class="check-btn" onclick="saveSynthStep()">保存して模範解答を見る</button>' +
    '</div>' +
    '<div class="model-answer" id="synth-model">' +
    '<h4>模範解答</h4><pre style="white-space:pre-wrap;font-family:inherit;font-size:0.9rem">' +
    step.modelAnswer.replace(/\\n/g, '\\n') + '</pre>' +
    '<p style="margin-top:8px;font-size:0.85rem;color:var(--text-light)">※ これは一例です。異なるアプローチでも論理的に整理されていればOKです。</p>' +
    '</div>';
  container.appendChild(div);

  // Nav
  var nav = document.createElement('div');
  nav.className = 'step-nav';
  if (ltState.synthesis.step > 0) {
    var prev = document.createElement('button');
    prev.className = 'check-btn';
    prev.style.background = 'var(--border)';
    prev.style.color = 'var(--text)';
    prev.textContent = '← 前のステップ';
    prev.onclick = function() { ltState.synthesis.step--; ltSaveState(); renderSynthesis(); };
    nav.appendChild(prev);
  } else {
    nav.appendChild(document.createElement('span'));
  }
  if (ltState.synthesis.step < 2) {
    var next = document.createElement('button');
    next.className = 'check-btn';
    next.textContent = '次のステップ →';
    next.onclick = function() { ltState.synthesis.step++; ltSaveState(); renderSynthesis(); };
    nav.appendChild(next);
  }
  container.appendChild(nav);

  if (ltState.synthesis.answers[ltState.synthesis.step]) {
    document.getElementById('synth-model').classList.add('show');
  }
}

function saveSynthStep() {
  var val = document.getElementById('synth-answer').value.trim();
  if (!val) return;
  ltState.synthesis.answers[ltState.synthesis.step] = val;
  ltSaveState();
  document.getElementById('synth-model').classList.add('show');
}

// ===== LT Init =====
function ltInit() {
  renderMece();
  renderTree();
  renderSoWhat();
  renderSynthesis();
  ltUpdateProgress();
}
ltInit();'''
