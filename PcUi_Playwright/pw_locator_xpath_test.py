from playwright.sync_api import  expect,Page

def test_playwright_locator_xpath_test(page:Page):
    page.goto('https://www.taobao.com')
    # //标签名[@属性名=值]
    expect(page.locator('//input[@id="q"]')).to_be_visible()
    # //标签名[text()="值"]
    expect(page.locator('//div[text()="潮电数码"]')).to_be_visible()
    # //标签名[contains(@属性名,值)]  标签名[contains(text(),"值")]
    expect(page.locator('//div[contains(text(),"潮电数码")]')).to_be_visible()
    expect(page.locator('//input[contains(@id,"q")]')).to_be_visible()
    # //标签名[@属性名=值 and @属性名="值"] 同时满足两种属性
    expect(page.locator('//div[@class="tbh-service J_Module"][@data-name="service"]')).to_have_count(1)
    # //标签名[@属性名=值]|//标签名[@属性名="值"] 满足其中一种
    expect(page.locator('//div[@class="tbh-service J_Module"]|//ul[@class="service-bd"]')).to_have_count(2)
    # 父节点
    expect(page.locator('//div[contains(@class,"service2024")]/parent::div')).to_have_count(1)
    # 上属所有节点
    expect(page.locator('//div[contains(@class,"service2024")]/ancestor::div')).to_have_count(2)
    #当前节点之上所有的节点
    expect(page.locator('//div[contains(@class,"layer")]/preceding::button')).to_have_count(8)
    #当前节点之上所有的兄弟节点
    expect(page.locator('//div[contains(@class,"layer")]/preceding-sibling::button')).to_have_count(0)
    # 当前节点之下所有的节点
    expect(page.locator('//div[contains(@class,"layer")]/following::span')).to_have_count(96)
    # 当前节点之下所有兄弟节点
    expect(page.locator('//div[contains(@class,"layer")]/following-sibling::div')).to_have_count(8)

    expect(page.locator('//div[contains(@class,"layer")][last()-1]')).to_be_visible()


