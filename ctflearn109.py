import requests

url = "http://165.227.106.113/header.php"

headers = { "User-Agent": "Sup3rS3cr3tAg3nt",
            "Referer": "awesomesauce.com"}

response = requests.get(url, headers=headers).text

print(response)
