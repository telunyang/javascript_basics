/**
 * 威力彩 遊戲介紹
 * https://www.taiwanlottery.com.tw/Superlotto638/index.asp
 */

//取得亂數
function getRandom(x) {
    /**
     * 假設 x 為 38，產生的值就落在 0 - 37 之間，
     * 此時程式後面再加 1，
     * 代表產生的值落在 1 - 38 之間，
     * 再進行回傳
     */
    return Math.floor(Math.random() * x) + 1;
}

//放置第一區 6 個號碼的陣列變數
let arr = [];

//放置第二區 1 個號碼的數值變數
let n = 0;

//產生威力彩號碼
function getPowerNum() {
    //一注威力彩號碼有 6 個所以我們讓迴圈跑六次
    for (i = 1; i <= 6; i++) {
        /** 
         * 用 indexOf 判斷該數字之前有沒有出現過，
         * 如果有，就將 i 遞減，等於讓這輪重跑一次。
         */

        //隨機取得 1 ~ 38 之間的數字
        let num = getRandom(38);

        //檢查是否有出現過(重複)
        if (arr.indexOf(num) > -1) {
            i--;
            continue;
        } else {
            //沒出現過的話就寫進陣列裡
            arr.push(num);
        }
    }

    /**
     * 排序陣列當中的值，由小至大
     * 
     * 參考網頁:
     * https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
     */
    arr.sort(function(a, b) {
        /**
         * 用數字排序
         * a - b 指的是由小到大
         * b - a 指的是由大到小
         * 
         * 若只有 arr.sort()，括號裡面沒有排序用的 function，
         * 則以字串作為排序依據，例如 [20, 5, 9, 10]，
         * 就會變成 [10, 20, 5, 9]
         */
        return a - b;
    });

    //第二區號碼
    n = getRandom(8);

    //因為威力彩有分兩區，第二區為 01 ~ 08 隨機一數字，所以我們在回傳時加上。
    return `第一區號碼為： ${arr.join(",")}，第二區號碼為： ${n}`;
}

/**
 * 回傳結果範例
 *   第一區號碼為： 8,9,22,25,35,37，第二區號碼為： 7
 *   第一區號碼為： 3,14,17,18,31,36，第二區號碼為： 4
 */
alert(getPowerNum());