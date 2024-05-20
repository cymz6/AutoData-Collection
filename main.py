import requests

def fetch_and_save(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # 获取lives.txt文件
    fetch_and_save('https://raw.githubusercontent.com/cymz6/iptv/main/lives.txt', 'data/lives.txt')
