# read_captcha
用于获取验证码数据集(OCR加上人工辅助)

## 使用
* 安装依赖(注：本地化使用了ddddocr库，在此感谢[Boris-code](https://github.com/Boris-code/feapder))
```
requests
opencv-python
numpy
pillow
onnxruntime
```
* 修改`capurl`，定位到验证码图片对应的url，运行后会显示出下载的验证码图片，标题为识别结果。
* 识别正确可直接按Enter即可保存。
* ddddocr库对大小写识别准确率较低，可在图片窗口输入正确的验证码，命令行中实时显示，按回车结束输入。(小bug：无法识别长按Shift键输入多个大写)
* 按Esc键可退出。
![](https://s3.bmp.ovh/imgs/2022/05/28/62b76e069da05992.png)