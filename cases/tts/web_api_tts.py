'''
請先安裝:
pip install flask flask-cors requests
'''
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from urllib.parse import quote_plus
import requests, uuid
from pathlib import Path

# 建立 Flask 伺服器
app = Flask(__name__)

# 自動處理 CORS
CORS(app)  

# 儲存目錄
SAVE_DIR = Path("tmp")
SAVE_DIR.mkdir(exist_ok=True)

# Web API 參數
URL = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.80 Safari/537.36"
}

# 路由: 提供靜態檔案服務
@app.route("/tmp/<path:filename>")
def serve_tmp(filename):
    return send_from_directory(SAVE_DIR, filename, mimetype="audio/mpeg")

# 路由: TTS 文字轉語音服務
@app.route("/tts", methods=["POST"])
def tts_post():
    # 取得文字參數
    q = request.json.get("q").strip()

    # 請求 TTS 服務
    r = requests.get(URL + quote_plus(q), headers=HEADERS, timeout=10)

    # 產生唯一檔名並儲存
    fn = f"{uuid.uuid4().hex}.mp3"
    (SAVE_DIR / fn).write_bytes(r.content)

    # 轉換回應為 JSON 格式
    '''
    回傳格式類似 Object/Dict:
    {
        "success": true,
        "link": "http://127.0.0.1:5000/tmp/{fn}"
    }
    '''
    return jsonify(
        success=True, 
        link=f"http://127.0.0.1:5000/tmp/{fn}"
    )


# 主程式
if __name__ == "__main__":
    # 開發測試用
    app.run(
        host="0.0.0.0", # 允許外部存取
        port=5000, # 服務 port 號
        debug=True # 除錯模式 (開發時使用，正式上線請移除或設為 False)
    )
