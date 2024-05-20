import requests

def fetch_and_save(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # 获取good.json文件
    fetch_and_save('https://raw.githubusercontent.com/shidahuilang/shuyuan/shuyuan/good.json', 'data/good.json')
    # 获取book.json
    fetch_and_save('https://raw.githubusercontent.com/shidahuilang/shuyuan/shuyuan/book.json', 'data/book.json')
