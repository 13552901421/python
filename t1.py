#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
#生成全网页快照
driver = webdriver.PhantomJS('D:\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
driver.set_window_size(1400,900)
driver.get('https://image.baidu.com/')
driver.save_screenshot('baidu_img.png')

# element = driver.find_element_by_css_selector("#wrapper_head_box")
#定位图片元素
# element = driver.find_element_by_css_selector("a[data-id='0'] img")
element = driver.find_element(By.CSS_SELECTOR,"a[data-id='9'] img")
print(element.location)
print(element.size)

img = Image.open('baidu_img.png')
#计算图片边界像素left,top,right,bottom,裁剪
left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']
box=(left,top,right,bottom)
img = img.crop(box)
img.save('img2.png')

time.sleep(10)
driver.quit()
