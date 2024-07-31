from playwright.sync_api import expect,Page

def test_filter(page:Page):
    page.goto("https://www.taobao.com/")
    page
    assert page.locator('[aria-label="查看更多"]').filter(has_text="女装").get_by_role("link").all_text_contents()[2] =="内衣"
    assert page.locator('[aria-label="查看更多"]').filter(has=page.locator('//a[text()="女装"]')).get_by_role("link").all_text_contents()[2] =="内衣"
    assert page.locator('//li[@aria-label="查看更多"][@data-index="6"]/a').all_inner_texts()[0] =="汽车"