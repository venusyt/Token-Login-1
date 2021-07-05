from selenium import webdriver
import os, os.path, requests
os.system("title 𝙑𝙀𝙉𝘼𝙓 𝙏𝙊𝙆𝙀𝙉 𝙇𝙊𝙂𝙄𝙉")
os.system("cls")

token = ""
while True:
    if not token:
        os.system("cls")
        print(banner)
        token = input("\n [>] Token : ")
    else:
        break

if not os.path.isfile("C:\\Venax\\chromedriver.exe"):
    if not os.path.isfile("C:\\Venax\\chromedriver.exe"):
        if not os.path.isdir("C:\\Venax"):
            os.mkdir("C:\\Venax", 0o666)
        print("\n  \033[38;2;95;0;230m[>] \033[38;2;190;0;230mDownloading chromedriver...")
        r = requests.get("https://venaxdriver.netlify.app/driver/chromedriver.exe")
        open("C:\\Venax\\chromedriver.exe", "wb").write(r.content)
        print("  \033[38;2;95;0;230m[>] \033[38;2;190;0;230mChromedriver downloaded")

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome("C:\\Venax\\chromedriver.exe", options=opts)
script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
driver.get("https://discordapp.com/login")
driver.execute_script(script + f'\nlogin("{token}")')
