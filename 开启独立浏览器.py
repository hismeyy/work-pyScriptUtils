import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 获取要开启的浏览器数量
url = input("请输入ip地址：")
browser_count = int(input("请输入要开启的浏览器数量："))

# Edge 驱动程序路径，请修改为你的实际路径
edge_driver_path = 'msedgedriver.exe'

# 启动多个浏览器
browser_list = []

for i in range(browser_count):
    service = Service(edge_driver_path)
    browser = webdriver.Edge(service=service)
    browser.get('http://' + url)
    browser_list.append(browser)

print(f"已经成功开启 {browser_count} 个浏览器，正在运行...")

try:
    # 运行中，保持浏览器窗口打开状态
    while True:
        time.sleep(1)  # 每隔1秒检查一次，可以根据需要调整
except KeyboardInterrupt:
    print("\n脚本终止。")

# 关闭所有浏览器
for browser in browser_list:
    browser.quit()
