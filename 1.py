from selenium import webdriver

browser =webdriver.Chrome()     # 打开谷歌浏览器
browser.get('http://www.baidu.com/')       # 访问百度

elem_id = browser.find_element_by_id("kw")
elem_name = browser.find_element_by_name("wd")
elem_cls = browser.find_element_by_class_name("s_ipt")
elem_btn = browser.find_element_by_id("su")   # 定位搜索按钮

elem_id.send_keys("python")   # 在输入框输入搜索内容 python
elem_btn.click()   # 点击搜索按钮
