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
    fetch_and_save('https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt', 'data/lives.txt')
    # 获取interface.json文件, tvbox文件
    fetch_and_save('http://xn--ihqu10cn4c.xn--z7x900a.live/%E6%8E%A5%E5%8F%A3%E7%A6%81%E6%AD%A2%E8%B4%A9%E5%8D%96', 'data/tvbox.json', 'okhttp/3.12.11')
