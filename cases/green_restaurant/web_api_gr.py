'''
請先安裝:
pip install flask flask-cors requests

資料來源:
https://data.taipei/

Web API 範例 -- 綠色餐廳
https://data.taipei/dataset/detail?id=845818d9-c432-44b4-85dd-03d71bd867b2
'''

from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json

# 建立 Flask 伺服器
app = Flask(__name__)

# 自動處理 CORS
CORS(app)

# Web API
URL = "https://data.taipei/api/v1/dataset/d706f428-b2c7-4591-9ebf-9f5cd7408f47?scope=resourceAquire"

# 請求標頭
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.80 Safari/537.36"
}

# 自訂路由端點 (Route Endpoint)
@app.route("/green_restaurants", methods=["GET"])
def green_restaurants():
    # 請求資料
    r = requests.get(URL, headers=HEADERS, timeout=10)

    # 轉換回應為 JSON 格式 (將字串轉為類似 Object/Dict 的格式)
    resp = jsonify(r.json())

    # 回傳結果
    return resp


# 主程式
if __name__ == "__main__":
    # 開發測試用
    app.run(
        host="0.0.0.0", # 允許外部存取
        port=5000, # 服務 port 號
        debug=True # 除錯模式 (開發時使用，正式上線請移除或設為 False)
    )
