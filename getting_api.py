import requests
url = "https://seat.tpml.edu.tw/sm/service/getAllArea"
def get_info():
 try:
    response = requests.get(url)
    response.raise_for_status()  # 如果 HTTP 錯誤會拋例外
    data = response.json()
    return data
 except requests.exceptions.RequestException as e:
    print("⚠️ API 請求失敗：", e)
def data_classiy(branch):
    raw_data=get_info()
    data = []
    for c in raw_data:
        if branch==c["branchName"]:
           data.append(c)
    return data
