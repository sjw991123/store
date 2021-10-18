from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://8.129.91.152:8765/ ")
driver.maximize_window()
# 注册
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]/a").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("17681377581")
sleep(10)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
sleep(5)
# ele=driver.find_element_by_class_name("layui-layer-content").text
# print(ele)
driver.find_element_by_xpath("//*[@name='password']").send_keys("123456sjw")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
ele=driver.find_element_by_xpath('/html/body/div[4]')
driver.switch_to.frame(ele)
driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
#
sleep(10)

# 认证身份证
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[3]/a").click()
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[1]/div/input").send_keys("刘大傻")
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[2]/div/input").send_keys("132628200001263934")
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[3]/div/button").click()
driver.find_element_by_xpath("//*[@id='layui-layer1']/span/a").click()

sleep(3)
# 认证电子邮箱
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[3]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer2']/div[2]/div/form/div[1]/input").send_keys("308373980@qq.com")




