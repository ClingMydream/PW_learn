from playwright.sync_api import expect,Page

def test_and_or_visible(page:Page):
    page.goto("https://taobao.com")
    # 同时满足
    expect(page.get_by_text("电脑").and_(page.get_by_role("link"))).to_have_count(1)
    # 满足其中之一
    expect(page.get_by_text("电脑").and_(page.get_by_role("link")).or_(page.locator("#q"))).to_have_count(2)
    # 满足元素在
    expect(page.get_by_text("电脑").locator("visible=True")).to_be_visible()

def test_nth_all(page:Page):
    page.goto("https://taobao.com")
    expect(page.locator('[aria-label="查看更多"]').last).not_to_contain_text("鲜花")
    expect(page.locator('[aria-label="查看更多"]').first).not_to_contain_text("电脑")
    expect(page.locator('[aria-label="查看更多"]').nth(4)).not_to_contain_text("男装")
    for _ in    page.locator('[aria-label="查看更多"]').all():
        page(_.text_content())

def test_visible(page:Page):
    page.goto("/demo/iframe",wait_until="networkidle")
    baidu = page.frame("https://www.baidu.com")
    baidu.fill("#kw","playwright")
    page.frame_locator('//[src="wwww.自动化测试.com"]').get_by_text("B站视频").click()
