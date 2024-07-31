from playwright.sync_api import expect, Page

def test_get_by_locator_css(page:Page):
    # playwright中的wait_until有四种不同的选项，分别是：
    # “load”：等待页面完全加载，包括所有资源（如图片、样式表、脚本等）。
    # “domcontentloaded”：等待DOM树构建完成，但不包括所有资源的加载。
    # “networkidle”：等待网络空闲，即没有正在进行的网络请求或者网络请求数量低于指定的阈值。
    # “timeout”：等待指定的时间，如果在指定时间内没有完成指定的条件，则抛出超时异常。

    # page.goto("https://www.taobao.com/",wait_until="networkidle")
    page.goto("https://www.taobao.com/")
    # ID # 代表 name
    expect(page.locator("#q")).to_be_visible()
    # .代表 class
    expect(page.locator(".image-search-icon")).to_be_visible()
    # .XX.XX表示多个要求并联
    expect(page.locator(".search-bd.search-suggest.search-suggest-group")).to_be_attached()
    # .xx>元素名.yy 表示从父级找子级
    expect(page.locator(".search-wrap>div.search-bd")).to_be_attached()
    expect(page.locator(".search-wrap>div")).to_have_count(2)
    # .xx[xxx]表示满足两个条件的元素
    expect(page.locator('.btn-search[type="submit"]')).to_be_visible()
    # .xxx,.xxx表示或
    expect(page.locator(".btn-search,.service-bd")).to_have_count(2)
    # .xxx:not(xxx=xxx) 排除到筛选出来的元素
    expect(page.locator('.tb-pick-content-item>a:not([data-spm="d1"])')).to_have_count(23)
    # [class*=XXX]包含xx的元素
    expect(page.locator('[class*="image-search-i"]')).to_be_visible()
    # [class^=XXX]xx开头的元素
    expect(page.locator('[class^="image-search-i"]')).to_be_visible()
    # [class$=XXX]xx结尾的元素
    expect(page.locator('[class$="search-icon"]')).to_be_visible()
    # XXXX:first-child表示一系列元素的第一个
    expect(page.locator('.tb-pick-feeds-container>div.tb-pick-content-item:first-child')).to_be_visible()
    # XXXX:last-child表示一系列元素的第一个
    expect(page.locator('.tb-pick-feeds-container>div.tb-pick-content-item:last-child')).to_be_visible()
    # XXXX:nth-child(5)根据下标来找
    expect(page.locator('.tb-pick-feeds-container>div.tb-pick-content-item:nth-child(5)')).to_be_visible()
    # XXXX:nth-child(2n)找到偶数
    page.wait_for_timeout(5_0000)
    expect(page.locator('.tb-pick-feeds-container>div.tb-pick-content-item:nth-child(2n)')).to_have_count()








