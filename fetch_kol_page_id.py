#以下程式碼是取得 Facebook Page ID，後續將用在 QSearch Trend 搜尋用

import requests

#kol_facebook_url可替換為 Facebook 任一粉絲頁網址
kol_facebook_url = "https://www.facebook.com/peggykimo/"

form =  {
   "query": kol_facebook_url,
   "url":"meimaii_kol_dashboard"
}
method = "http://analytics.qsearch.cc/trendapi/api_analytics_fanpage_convert"
r = requests.post(method, data=form)
print(r.json())