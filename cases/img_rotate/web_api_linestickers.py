'''
請先安裝:
pip install flask flask-cors requests

資料來源:

'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re, json, html
from urllib.parse import unquote_plus

# 建立 Flask 伺服器
app = Flask(__name__)

# 自動處理 CORS
CORS(app)

# 請求標頭
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.80 Safari/537.36"
}

# 自訂路由端點 (Route Endpoint)
@app.route("/linestickers", methods=["GET"])
def linestickers():
    # 放貼圖資訊用
    list_line_stickers = []

    # 取得網址參數 url (來自 Query String)
    url = request.args.get("url").strip()

    # 請求資料
    r = requests.get(url, headers=HEADERS, timeout=10)

    # 以 Regular Expression 取得每一個 li[data-view] 的值
    regex = r"data-preview=['\"](.+?)['\"]"

    # 取得所有匹配的結果
    li_data = re.findall(regex, r.text)

    # 逐一處理每一個貼圖資料
    for data in li_data:
        # 將 data-preview 的字串轉為類似 Object/Dict 的格式
        # html.unescape(): 將 HTML 實體字元轉回原本字元
        dict_data = json.loads(html.unescape(data))

        # 將貼圖資料加入清單
        list_line_stickers.append(dict_data)

    # 轉換回應為 JSON 格式 (將字串轉為類似 Object/Dict 的格式)
    resp = jsonify(
        success=True,
        results=list_line_stickers
    )

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
