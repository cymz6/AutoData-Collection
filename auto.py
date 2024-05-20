import requests

def visit_website(url):
    response = requests.get(url)
    response.raise_for_status()
    print(f"成功访问网站：{url}")
    print(f"网站内容：\n{response.text}")

if __name__ == "__main__":

    
    # 访问网站 http://home.love.rr.nu/test
    visit_website('http://home.love.rr.nu/test')
