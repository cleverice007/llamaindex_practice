import requests
from bs4 import BeautifulSoup
import os
import urllib

url= "https://docs.llamaindex.ai/en/stable/" 

# 儲存路徑
output_dir = "./llamindex-docs/"
os.makedirs(output_dir, exist_ok=True)
 
# 爬取網頁
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
 
# 找出所有的連結
links = soup.find_all('a', href=True)
 
for link in links:
    href = link['href']
    
    # 下載 html 檔
    if href.endswith('.html'):
        # 增加http，如果只有相對路徑
        if not href.startswith('http'):
            href = urllib.parse.urljoin(url, href)
            
        print(f"downloading {href}")
        file_response = requests.get(href)
        
        # 寫入檔案
        file_name = os.path.join(output_dir, os.path.basename(href))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(file_response.text)

