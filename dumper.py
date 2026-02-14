import requests
import os

url = "https://api.luarmor.net/files/v4/loaders/bdbb256085cd59f12cf401606ae14b0e.lua"
outputt = "output"

os.makedirs(outputt, exist_ok=True)

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
        output_path = os.path.join(outputt, attempt['filename'])
        with open(output_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(response.text)
        
        content = response.text
        if content.startswith('--') or 'local' in content[:100] or 'function' in content[:100]:
            lua_output = os.path.join(outputt, "result.lua")
            with open(lua_output, 'w') as f:
                f.write(content)
            
    except Exception as e:
        error_path = os.path.join(outputt, attempt['filename'])
        with open(error_path, 'w') as f:
            f.write(str(e))
