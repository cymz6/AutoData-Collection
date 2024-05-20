import requests
import os

def fetch_and_save(url, save_path, user_agent=None):
    # 确保保存路径的目录存在，如果不存在则创建
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if user_agent:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # 获取lives.txt文件, IPTV电视直播文件
    fetch_and_save('https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt', 'data/直播源.txt')
    # 获取interface.json文件, tvbox文件
    fetch_and_save('http://xn--z7x900a.live/', 'data/肥猫TVBox.txt', 'okhttp/3.12.11')
