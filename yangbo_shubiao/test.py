import pyautogui
import time
import os
import pyperclip

def move_and_click(x, y, duration=1):
    """
    将鼠标移动到指定位置并单击，移动速度由 duration 参数控制
    :param x: 目标位置的 x 坐标
    :param y: 目标位置的 y 坐标
    :param duration: 鼠标移动到目标位置所需的时间（秒）
    """
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

def automate_login(username, password):
    """
    自动化登录淘宝卖家中心的完整流程
    :param username: 预设的账号
    :param password: 预设的密码
    """
    # 确保你有足够的时间切换到浏览器窗口
    time.sleep(2)

    # 模拟按下 Ctrl + T 打开新标签页
    pyautogui.hotkey('ctrl', 't')

    # 等待新标签页加载
    time.sleep(1)

    # 复制 URL 到剪贴板
    url = "https://loginmyseller.taobao.com/?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fmyseller.taobao.com%2Fhome.htm"
    pyperclip.copy(url)

    # 模拟按下 Ctrl + V 粘贴 URL
    pyautogui.hotkey('ctrl', 'v')

    # 模拟按下回车键
    pyautogui.press('enter')

    # 等待页面加载
    time.sleep(5)

    # 将鼠标移动到指定位置并单击，移动速度变慢
    move_and_click(1329, 436)  # 移动到账号输入框

    # 输入账号
    pyautogui.write(username)

    # 将鼠标移动到指定位置并单击，移动速度变慢
    move_and_click(1303, 578)  # 移动到密码输入框

    # 输入密码
    pyautogui.write(password)

    # 将鼠标移动到指定位置并单击，移动速度变慢
    move_and_click(1371, 710)  # 移动到登录按钮

def read_accounts_from_files():
    """
    读取当前目录下所有 .txt 文件中的账号和密码
    :return: 返回一个包含账号和密码的列表，每个元素是一个包含账号和密码的元组
    """
    accounts = []
    for filename in os.listdir('.'):
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    username = lines[0].strip()
                    password = lines[1].strip()
                    accounts.append((username, password))
    return accounts

# 读取所有账号和密码
accounts = read_accounts_from_files()

# 循环调用 automate_login 函数
for username, password in accounts:
    automate_login(username, password)
    time.sleep(10)  # 每次调用后等待10秒