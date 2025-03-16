from datetime import datetime
import base64

# 使用XPath定位到img元素
self.img_element = self.browser.find_elements(By.XPATH, "//div[@id='topicImg0']/img")[0]

# 执行JavaScript代码获取图片的Base64编码
self.base64_image = self.browser.execute_script("""
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    var img = arguments[0];
    canvas.width = 950;
    canvas.height =300;
    ctx.drawImage(img, 0, 0);
    return canvas.toDataURL('image/png').split(',')[1];
""", self.img_element)

# 打印Base64编码的图片
# print(f"Base64 encoded image: {self.base64_image}")

# 将Base64编码的图片数据转换为二进制数据
image_data = base64.b64decode(self.base64_image)

# 获取当前时间并格式化为字符串
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# 定义保存图片的本地路径，以当前时间命名
img_path = f"downloaded_image_{current_time}.png"

# 保存图片到本地
with open(img_path, 'wb') as file:
    file.write(image_data)

print(f"图片已保存到 {img_path}")