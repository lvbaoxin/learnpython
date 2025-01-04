import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
data = {
    "log": "admin",
    "pwd": "123",
    "wp-submit": "登录",
    "redirect_to": "https://wordpress-edu-3autumn.localprod.oc.forchange.cn",
    "testcookie": 1,
}
response = requests.post('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php', headers=headers,
                        params=data)

response.encoding = 'utf-8'

print(response.text)
