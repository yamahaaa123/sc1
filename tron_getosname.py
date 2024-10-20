import requests


def get_node_info(node_url):
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(node_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch node info. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def extract_osname(node_info):
    if 'machineInfo' in node_info:
        return node_info['machineInfo'].get('osName', 'OS name not found')
    else:
        return 'OS name not found'


# 示例使用
# node_url = "http://18.235.35.236:8090/wallet/getnodeinfo"  # 本地 TRON 全节点地址
# node_url="https://tron.twnodes.com/wallet/getnodeinfo"
node_url="https://tron-mainnet.token.im/wallet/getnodeinfo"
# node_url="https://api.trongrid.io/wallet/getnodeinfo"

node_info = get_node_info(node_url)

if node_info:
    osname = extract_osname(node_info)
    print(f"OS name: {osname}")
