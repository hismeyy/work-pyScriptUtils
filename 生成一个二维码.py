import qrcode

# 定义要编码的URL
url = "https://www.baidu.com"

# 生成二维码
qr = qrcode.QRCode(
    version=1,  # 控制二维码的大小，取值范围是1到40，最小值是1（21x21），最大值是40（177x177）
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制二维码的错误纠正能力
    box_size=10,  # 控制二维码中每个小格子的像素数
    border=4,  # 控制边框（必须至少为4）
)
qr.add_data(url)
qr.make(fit=True)

# 创建一个图像对象
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像到文件
img.save("qrcode.png")

print("二维码已生成并保存为 qrcode.png")
