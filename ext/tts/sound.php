<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: *');
header('Content-Type: application/json');

$obj = [];
$obj['success'] = false;
$obj['info'] = '下載失敗'; 

if( apache_request_headers()['Content-Type'] == 'application/json' ){
    $_POST = json_decode(file_get_contents("php://input"), true);
}

if( isset($_POST['q']) && $_POST['q'] !== '' ){
    $headers = [
        'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    ];
    
    $url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=".urlencode($_POST['q']);
    
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $raw_data = curl_exec($ch);
    curl_close($ch);
    
    $fileName = hash('md5', $url);
    
    $file_path = "tmp/{$fileName}.mp3";
    
    if( $fp = fopen($file_path, "w") ){
        fwrite($fp, $raw_data);
        fclose($fp);
    
        $obj['success'] = true;
        $obj['info'] = '下載成功';
        $obj['link'] = "https://darreninfo.cc/tts/{$file_path}";
    }
}

echo json_encode($obj, JSON_UNESCAPED_UNICODE);