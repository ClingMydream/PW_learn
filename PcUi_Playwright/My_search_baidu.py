# 引入page类和expect断言方法
from playwright.sync_api import  Page,expect

# 实例化page类 调用方法
def test_baidu(page: Page):
    # page.goto方法:跳转对应的 url
    page.goto(url="http://baidu.com")
    # page.wait_for_timeout 等待时间 2S
    page.wait_for_timeout(2_000)
    #  page.locator 元素定位 支持CSS Xpath selector
    #  flii 输入文本
    page.locator('//input[@name="wd"]').fill("playwright")
    # page.get_by_text 元素定位 支持文本定位
    # click 点击
    page.get_by_text("百度一下").click()
    # expect 断言
    # to_be_visible是否存在该元素
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()