import requests
import os
import zipfile
from datetime import datetime

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
    # 获取V2rayNG0接口
    fetch_and_save('https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt', 'data/VPN0.txt')
    # 获取V2rayNG1接口
    fetch_and_save('https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub', 'data/VPN1.txt')
    # 获取V2rayNG2接口
    fetch_and_save('https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2', 'data/VPN2.txt')
    # 获取V2rayNG3接口
    fetch_and_save('https://www.xrayvip.com/free.txt', 'data/VPN3.txt')

    # 获取当前日期
    current_date = datetime.now().strftime("%Y%m%d")
    zip_filename = f"{current_date}.zip"

    # 创建zip备份文件
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历data目录下的所有文件和目录
        for root, dirs, files in os.walk('data'):
            for file in files:
                # 获取文件的完整路径
                full_path = os.path.join(root, file)
                # 将文件添加到zip文件中
                zipf.write(full_path, os.path.relpath(full_path, 'data'))

    # 将zip文件移动到codebak目录
    codebak_dir = 'codebak'
    if not os.path.exists(codebak_dir):
        os.makedirs(codebak_dir)
    zip_dest = os.path.join(codebak_dir, zip_filename)
    os.rename(zip_filename, zip_dest)

    print(f"Zip file '{zip_dest}' created successfully.")
