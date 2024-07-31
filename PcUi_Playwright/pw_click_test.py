from playwright.sync_api import Page,expect

def test_pw_click(page: Page):
    page.goto("/demo/button")
    # page.wait_for_timeout(2_000)
    # modifiers：click(modifiers= ["control","meta"]) 模拟系统中一些键的操作
    page.get_by_text("点击我试试1").click(modifiers=["Control"])
    # bounding_box：查看元素的大小
    page.get_by_text("点击我试试1").bounding_box()
    page.get_by_text("点击我试试1").click(position={"x": 25,"y": 12})
    # button: click(button="right") 模拟鼠标的左键、中键、右键
    page.get_by_text("点击我试试1").click(button="right")
    # count: click(count = 3) 点击次数，默认值为1
    page.get_by_text("点击我试试1").click(click_count=3)
    # delay：click（delay = 1_000） 按住多久，延迟多久
    page.get_by_text("点击我试试1").click(delay=2_000)
    # 等待时间
    page.get_by_text("点击我试试1").click(timeout=2_00)
    # force: click(force=ture)  不进行auto-wait 检查 直接点击
    page.get_by_text("点击我试试1").click(force=True)
    # no_wait_after：click(no_wait_after=ture)  少数情况下使用，比如说某些js弹窗，有些点击操作就不可用了，避免长时间的等待
    page.get_by_text("点击我试试1").click(no_wait_after=True)
    # trial：click(trial=ture)  不进行点击，进行一个等待
    page.get_by_text("点击我试试1").click(trial=True)
