<?php
//回應標頭 (Response Headers)
header('Access-Control-Allow-Origin: *'); //開放所有網域請求
header('Content-Type: application/json'); //告訴前端，回傳格式為 JSON (前端接到，會是物件型態)

$headers = [
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
];

//Web API
$url = 'https://cafenomad.tw/api/v1.2/cafes/taipei';

//模擬網路請求，取得從 LINE 貼圖網站回傳的 html
$ch = curl_init(); //curl 初始化
curl_setopt($ch, CURLOPT_URL, $url); //設定 URL
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); //若有轉址，一路轉到正常顯示的頁面
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); //指定 Request Headers
$result = curl_exec($ch); //取得 html
curl_close($ch); //關閉 curl

//輸出 ($result 本身就是 json 字串，在檔案最上面放 response header，告訢前端 js 我回傳給你的是 object 型態)
echo $result;