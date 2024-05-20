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
    # 获取脚本执行的时间戳
    fetch_and_save('https://quan.suning.com/getSysTime.do', 'data/Script_execution_time.txt')
    # 获取diyp电视直播源接口
    fetch_and_save('https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt', 'data/直播源.txt')
    # 获取TVBox肥猫接口
    fetch_and_save('http://xn--z7x900a.live/', 'data/肥猫.txt', 'okhttp/3.12.11')
    # 获取TVBox巧技接口
    fetch_and_save('http://cdn.qiaoji8.com/tvbox.json', 'data/巧技.txt', 'okhttp/3.12.11')
    # 获取V2rayNG接口
    fetch_and_save('https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt', 'data/VPN.txt')
    # 获取V2ray2接口
    fetch_and_save('https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub', 'data/VPN1.txt')
