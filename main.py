import requests
import os

def fetch_and_save(url, save_path, user_agent=None):
    # 确保保存路径的目录存在，如果不存在则创建
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 根据是否提供了用户代理，发送请求
    if user_agent:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)

    # 确保请求成功
    response.raise_for_status()

    # 将内容写入文件
    with open(save_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # 获取lives.txt文件, diyp电视直播接口
    fetch_and_save('https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt', 'data/lives.txt')
    # 获取interface.json文件, tvbox肥猫接口
    fetch_and_save('http://xn--z7x900a.live/', 'data/tvbox_feimao.txt', 'okhttp/3.12.11')
