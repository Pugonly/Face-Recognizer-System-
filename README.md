# Face-Recognizer-System-

組員

410421242 許畯堯

410421243 陳鼎勳

(a)訓練相關使用

語言 - Python

工具 - Keras , PIL

神經網路結構 - CNN

Model - Sequential

Batch size - 8

Optimizer - Adam

相關技術

Conv2D

Dropout

MaxPooling2D

activation - Relu , Softmax

Same Padding

Crossentropy

(b)the modules enclosed in your recognizer and their functions

<img src="https://github.com/Pugonly/Face-Recognizer-System-/blob/master/pic1.jpg">

上圖是我們使用的model。

<img src="https://github.com/Pugonly/Face-Recognizer-System-/blob/master/pic2.jpg">
這裡是資料預先處理的部分,扣除掉被抽出來demo用的兩張照片,剩下的全部丟入訓練

(c)how we test our recognizer to evaluate its recognition rate

在1~15之間隨機取兩個數字(除了5和9)的照片作為validation set,並將全部13*50張照片丟進model訓練,再將測試照片丟入訓練好的model觀察辨識率。

(d)the problems suffered in our development

因為數字辨識時Adam的辨識率為最佳，所以optimizer決定用Adam。
batch size一開始是用64，但CPU跑太慢，最後用8。

辨識成果

辨識準確	
<img src="https://github.com/Pugonly/Face-Recognizer-System-/blob/master/pic4.jpg">

辨識不準確
<img src="https://github.com/Pugonly/Face-Recognizer-System-/blob/master/pic3.jpg">

(e)心得感想

許畯堯: 一開始安裝套件卡了一些時間,然後batch_size的設定也不確定怎麼抓最好,最後是在執行時間跟正確率平衡下決定用8,所以辨識率似乎不是很高。

陳鼎勳: 這次作業我覺得還挺難的，畢竟專題不是做這塊的，過程中只能瘋狂爬文並去試著微調參數，我們其實都靠著那5個最高機率去取分的，辨識率其實沒很高。
