# **貼文 Post API**

[TOC] 

---


## HTTP Request

```json
GET /api/trend/v1/posts
Host: api.qsearch.cc
```



## API Key

```
1d7016605dcbd5fe717b61cd39c737bba4cc3095345557313eff8c92de45bd53
```



## Parameters

| parameter Name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| st             | string | 起日，YYYY-MM-DD                                             |
| et             | string | 迄日，YYYY-MM-DD                                             |
| channels       | string | 渠道，填寫範例如下：["MEDIA","FORUM", "FB", "YT", "IG"]      |
| nation         | string | 國家，以下選擇：<br/>TW。<sub>[註1]</sub> |
| q              | string | 關鍵字，以 JSON 方式傳送關鍵字陣列，例：["keyword1","keyword2"] |
| key            | string | API key                                                      |

 <sub>[註1] HK: Hong Kong, ID: Indonesia, JP: Japan, MY: Malaysia, PH: Philippines, SG: Singapore, TH: Thailand, TW: Taiwan, VN: Viet Nam</sub>



## 呼叫範例

```
https://api.qsearch.cc/api/trend/v1/posts?st=2021-9-01&et=2021-9-19&nation=TW&q=["id:{粉絲頁Id}"]&channels=["FB"]&key=1d7016605dcbd5fe717b61cd39c737bba4cc3095345557313eff8c92de45bd53
```



## Response

- Response 200

```json
{
  "q": [
    "蔡英文",
    "趙少康"
  ],
  "et": "2021-09-19",
  "st": "2021-09-01",
  "data": [
    {
      "keyword": "蔡英文",
      "fb_raw": [...],
      "forum_raw": [...],
      "media_raw": [
        {
          "title": "新頭殼 Newtalk",
          "permalink": "https://newtalk.tw/news/view/2021-09-19/638985",
          "zh_site_name": "新頭殼 Newtalk",
          "pid": "543d413ea2e0d589765b",
          "ts": 1632066210000.0,
          "content": "中國繼今年2月宣布禁止台灣鳳梨進口後，昨(18)日再宣布禁止台灣釋迦、蓮霧進口，對此，根據日媒《朝日新聞》報導指出，這次禁止釋迦、蓮霧和先前禁止鳳梨的原因都是「發現害蟲」，質疑背後是為「政治施壓」。\n...",
          "negative_score": 0.43360963463783264,
          "comment_count": null,
          "ts_iso_8601": "2021-09-19T23:43:30+08:00",
          "positive_score": 0.00043838017154484987,
          "label_sentiment": "NEUTRAL",
          "site_code": "newtalk.tw",
          "neutral_score": 0.565935492515564
          ...
        },
        {...},...        
      ]
    },
    {...}
   ]
}
```



## 欄位



### 臉書粉專 Facebook Fan Page

| 欄位名稱             | 說明                                          |
| -------------------- | --------------------------------------------- |
| ts                   | 發文時間 (以 unix timestamp 表示，單位為微秒) |
| ts_iso_8601          | 發文時間 (以 ISO8601 格式表示)                |
| id                   | Facebook 貼文 ID                              |
| content              | Facebook 貼文文字內容                         |
| type                 | Facebook 貼文型態                             |
| share_count          | Facebook 貼文分享數                           |
| comment_count        | Facebook 貼文留言數                           |
| reaction_all_count   | Facebook 貼文各心情總數                       |
| reaction_like_count  | Facebook 按讚數                               |
| reaction_love_count  | Facebook 愛心                                 |
| reaction_wow_count   | Facebook 哈                                   |
| reaction_sad_count   | Facebook 哇                                   |
| reaction_haha_count  | Facebook 哭                                   |
| reaction_angry_count | Facebook 怒                                   |
| engagement_score     | Facebook 貼文 engagement score                |
| from_id              | Facebook 貼文粉專來源 (粉專 ID)               |
| from_name            | Facebook 貼文粉專來源 (粉專名稱)              |
| talking_about_count  | Facebook 提供，該粉專被提及的次數             |
| fan_count            | 粉絲數                                        |
| follower_count       | 追蹤人數                                      |
| ig_username          | 對應之 IG 帳號                                |




