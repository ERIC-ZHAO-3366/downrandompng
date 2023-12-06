import os
import requests
import shutil

url_dir = '/path/to/directory'  # 图片目录的路径
save_dir = '/path/to/save'  # 下载图片的目录路径

# 获取指定目录下的所有文件
def get_files(dir):
    files = []
    for root, dirs, filenames in os.walk(dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

# 判断文件是否为图片
def is_image(file):
    file_lower = file.lower()
    return file_lower.endswith('.jpg') or file_lower.endswith('.jpeg') or file_lower.endswith('.png') or file_lower.endswith('.gif')

# 下载图片
def download_image(file, save_dir):
    file_url = file.replace("\\", "/")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        save_path = os.path.join(save_dir, os.path.basename(file))
        with open(save_path, 'wb') as f:
            f.write(response.content)

# 遍历目录，下载图片
if __name__ == '__main__':
    files = get_files(url_dir)
    for file in files:
        if is_image(file):
            download_image(file, save_dir)
