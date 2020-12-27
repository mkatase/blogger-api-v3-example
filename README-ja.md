# Google Blogger API v3 のためのPython Example
PythonによるBlogger API v3ベースのサンプル

## 準備
* Googleアカウント
* Bloggerサインイン
* GoogleによるAPIの使用方法 [getting started](https://developers.google.com/blogger/docs/3.0/getting_started) with Blogger API v3
* 認証のための[Credential Json File](https://console.developers.google.com/apis/credentials)

## 追加で必要となるPython Module (pip install)
* Python 3.8.6 (on Fedora 32)
* google-api-python-client 1.12.8
* google-auth-oauthlib 0.4.2

```
$ pip install -r requirements.txt
```

## スクリプト群
* insert.py: Bloggerに投稿をアップロードするサンプル
* update.py: Bloggerにアップロードされている投稿を更新するサンプル
* delete.py: Bloggerにアップロードされている投稿を削除するサンプル

## 参照
* [google-api-python-client example](https://github.com/googleapis/google-api-python-client/tree/master/samples/blogger)

## ライセンス
このソフトウェアは、MITライセンスのもとで公開しています。
