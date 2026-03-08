from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length))

        question = body.get('question', '')
        context = body.get('context', '')

        if not question:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': '質問を入力してください'}).encode())
            return

        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY', ''))

            system_prompt = """あなたはミルクネクスト株式会社の優しい先輩社員です。新人の後輩がビジネススキル（Excel、PowerPoint、ロジカルシンキング）について質問してきます。

ルール:
- 答えを直接教えず、ヒントと考え方で導いてください
- 励ましながら、簡潔に回答してください（3-5文程度）
- 初心者にもわかりやすい言葉を使ってください
- 具体例を交えて説明してください
- ミルクネクスト株式会社（架空の乳業メーカー）の世界観に沿ってください

知識:
- Excel: SUM/AVERAGE/COUNT/COUNTIF/SUMIF/VLOOKUP/INDEX-MATCH/IF/SUMIFS/COUNTIFS/ピボットテーブル/KPIダッシュボード
- PPT: 1スライド1メッセージ/図解化/提案書作成
- ロジカルシンキング: MECE/ロジックツリー/So What?・Why So?/ピラミッドストラクチャー
- データ: 商品8種（牛乳/ヨーグルト/チーズ/バター・生クリーム）、顧客50社、担当5名、売上200件"""

            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=500,
                system=system_prompt,
                messages=[{"role": "user", "content": f"[現在のレッスン: {context}]\n\n{question}"}]
            )

            answer = response.content[0].text

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'answer': answer}).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': f'エラーが発生しました: {str(e)}'}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
