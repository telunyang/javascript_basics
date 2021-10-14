<?php
//回應標頭 (Response Headers)
header('Access-Control-Allow-Origin: *'); //開放所有網域請求
header('Content-Type: application/json'); //告訴前端，回傳格式為 JSON (前端接到，會是物件型態)

//預設回傳訊息
$obj = [];
$obj['success'] = false;
$obj['info'] = '下載失敗'; 

//如果 q 存在且不為空，則開始進行聲音下載、命名與回傳
if( isset($_GET['url']) && $_GET['url'] !== '' ){
    //建立標頭 (Request Headers)
    $headers = [
        'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    ];
    
    //請求網址
    $url = $_GET['url'];
    
    //模擬網路請求，取得從 LINE 貼圖網站回傳的 html
    $ch = curl_init(); //curl 初始化
    curl_setopt($ch, CURLOPT_URL, $url); //設定 URL
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); //若有轉址，一路轉到正常顯示的頁面
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); //指定 Request Headers
    $html = curl_exec($ch); //取得 html
    curl_close($ch); //關閉 curl

    //取代斷行字串，讓過濾文字的效率提高
    $html = str_replace(["\r", "\n"], '', $html);

    //以 Regular Expression 取得每一個 li[data-view] 的值
    $regex = "/<li.+?data-preview='(.+?)'>/";

    //執行正規表達式
    if( preg_match_all($regex, $html, $matches) ){
        //設定成功訊息
        $obj['success'] = true;
        $obj['info'] = '下載成功';
        $obj['results'] = []; //設定 result => array

        //將比對到的資料，各別放至 $obj['result'] 當中 
        for($i = 0; $i < count($matches[1]); $i++){
            //將特殊符號，轉成正常的文字 (例如 $nbsp; 和 &quot; 等)
            $strJson = htmlspecialchars_decode($matches[1][$i]);

            //將字串格式的 json，轉成 物件 (object)
            $o = json_decode($strJson, true);

            //將比對到的每一張貼圖資訊，附在陣列尾端
            $obj['results'][] = [
                "animationUrl" => $o["animationUrl"],
                "id" => $o["id"],
                "popupUrl" => $o["popupUrl"],
                "soundUrl" => $o["soundUrl"],
                "staticUrl" => $o["staticUrl"]
            ];   
        }
    }
}

//將 $obj 轉成 json，並加以輸出
echo json_encode($obj, JSON_UNESCAPED_UNICODE);