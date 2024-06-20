# import socket
#
#
# def get_local_ip():
#     try:
#         # 创建一个 UDP 套接字
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         # 连接到一个公共的 IP 地址和端口（例如 Google DNS）
#         s.connect(("8.8.8.8", 80))
#         # 获取套接字的名称，即本地 IP 地址
#         local_ip = s.getsockname()[0]
#     except Exception as e:
#         local_ip = "Unable to get IP address"
#         print(f"Error: {e}")
#     finally:
#         s.close()
#     return local_ip
#
#
# if __name__ == "__main__":
#     ip = get_local_ip()
#     print(f"Local IP address: {ip}")


import socket

def get_local_ip():
    try:
        # 获取主机名
        hostname = socket.gethostname()
        print(hostname)
        # 通过主机名解析 IP 地址
        local_ip = socket.gethostbyname(hostname)
    except Exception as e:
        local_ip = "Unable to get IP address"
        print(f"Error: {e}")
    return local_ip

if __name__ == "__main__":
    ip = get_local_ip()
    print(f"Local IP address: {ip}")

