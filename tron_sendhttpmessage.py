import requests

def get_now_block(node_url):
    try:
        response = requests.post(node_url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch current block. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# 示例使用
# node_url = "http://41.209.10.201:8090/wallet/getnodeinfo"  # 本地 TRON 全节点地址
# node_url="https://tron.twnodes.com/wallet/getnodeinfo"
# node_url="https://tron-mainnet.token.im/wallet/getnodeinfo"
# node_url="https://tron.atomicwallet.io/wallet/getnodeinfo"
# node_url="https://tron.a.exodus.io/wallet/getnodeinfo"
node_url="https://web3.mytokenpocket.vip/wallet/getnodeinfo"


block_info = get_now_block(node_url)

if block_info:
    print(block_info)
