import requests
import os
from datetime import datetime

def fetch_and_save(url, save_path, file_name, user_agent=None):
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
    
    # 记录下载时间
    update_time_path = os.path.join(directory, 'updatetime.txt')
    with open(update_time_path, 'a') as f:  # 'a'模式表示追加写入
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{file_name} downloaded at {current_time}\n")

    # 删除旧的updatetime.txt文件
    if os.path.exists(update_time_path):
        os.remove(update_time_path)

if __name__ == "__main__":
    # 获取lives.txt文件, IPTV电视直播文件
    fetch_and_save('https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt', 'data/lives.txt', 'lives.txt')
    # 获取interface.json文件, tvbox文件
    fetch_and_save('http://xn--z7x900a.live/', 'data/tvbox_feimao.txt', 'tvbox_feimao.txt', 'okhttp/3.12.11')
