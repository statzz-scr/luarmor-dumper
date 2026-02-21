import requests

url = "https://api.luarmor.net/files/v4/loaders/3f141dae620fd75848dcf52b972c1795.lua"

attempts = [
    {
        "filename": "1.txt",
        "headers": {
            "User-Agent": "Roblox/WinInet",
        }
    },
    {
        "filename": "2.txt",
        "headers": {
            "User-Agent": "Lua/5.1",
        }
    },
    {
        "filename": "3.txt",
        "headers": {
            "User-Agent": "LuaSocket 3.0-rc1",
        }
    },
    {
        "filename": "4.txt",
        "headers": {
            "User-Agent": "curl/7.68.0",
        }
    },
    {
        "filename": "5.txt",
        "headers": {
            "User-Agent": "Wget/1.20.3",
        }
    },
    {
        "filename": "6.txt",
        "headers": {
            "User-Agent": "",
        }
    },
    {
        "filename": "7.txt",
        "headers": {}
    },
    {
        "filename": "8.txt",
        "headers": {
            "User-Agent": "python-requests/2.28.0",
        }
    },
]

for attempt in attempts:
    try:
        response = requests.get(url, headers=attempt['headers'], timeout=10)
        with open(attempt['filename'], 'w', encoding='utf-8', errors='ignore') as f:
            f.write(response.text)
        
        content = response.text
        if content.startswith('--') or 'local' in content[:100] or 'function' in content[:100]:
            with open("result.lua", 'w') as f:
                f.write(content)
            
    except Exception as e:
        with open(attempt['filename'], 'w') as f:
            f.write(str(e))
