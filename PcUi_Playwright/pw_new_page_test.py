import os

from playwright.sync_api import Page,expect

def test_pw_action(page: Page):
    page.goto("/demo/button")
    # page.wait_for_timeout(2_000)
    page.get_by_text("点击我试试1").dblclick()

# 他弹窗消息
def test_pw_notification__message(page: Page):
    # wait_until="networkidle 代表所有网络请求在500毫秒之内没有新的请求才推出goto这个操作
    page.goto("/demo/button",wait_until="networkidle")
    # page.wait_for_timeout(3_000)
    page.get_by_text("点击我试试1").click()
    expect(page.get_by_text("点击成功1")).to_be_visible()

# 新页面
def test_pw_new_page(page: Page):
    page.goto("/demo/link",wait_until="networkidle")
    page.get_by_text("本页跳转到百度").click()
    # get_by_text：默认的文本为包含方式，不适用于存在多个相似内容的情况，这种情况下要使用精确查找，在文本后面加exact=True
    expect(page.get_by_text("百度一下",exact=True)).to_be_visible()
    page.goto("/demo/link", wait_until="networkidle")
    # 使用with as
    # 取出page.expect_popup将其赋值给new_page
    # 重新定义page_new = new_page.value之后 使用断言
    with page.expect_popup() as new_page:
        page.get_by_text("新页面跳转到淘宝").click()
    page_new = new_page.value
    # 在断言时，存在一些元素可见，但是此时并不可用，这时候不使用visible 而是使用to_be_attached
    # locator使用css时候只需要在类名前面加一个点
    # 可通过打断点然后使用对表达式求职，判断这个元素是否可见
    expect(page_new.locator(".search-button")).to_be_attached()

# 鼠标悬浮和事件
def test_pw_hover(page: Page):
    page.goto("/demo/hover",wait_until="networkidle")
    page.locator("#c4").hover()
    page.wait_for_timeout(1_000)
    expect(page.get_by_text("你已经成功悬浮")).to_be_visible()


# 下拉框
def test_pw_dropdown(page: Page):
    page.goto("/demo/dropdown", wait_until="networkidle")
    page.get_by_text("点击选择").click()
    page.get_by_text("playwright").click()
    expect(page.get_by_text("你选择了websocket")).to_be_visible()
    try:
        expect(page.get_by_text("你选择了websocket")).to_be_visible(timeout=3_000)
        你选择了websocket = True
    except:
        你选择了websocket = False
    page.get_by_text("点击选择").click()
    page.get_by_text("selenium").click()
    expect(page.get_by_text("你选择了webdriver")).to_be_visible()

# 输入框
def test_pw_input(page: Page):
    page.goto("/demo/input",wait_until="networkidle")
    # 可以适用于绝大多数存在placeholder的输入框（输入内容为覆盖，可以不管之前输入的值）
    page.get_by_placeholder("不用管我,我是placeholder").fill("随便填写的")
    expect(page.get_by_text("随便填写的")).to_be_visible()
    assert page.get_by_placeholder("不用管我,我是placeholder").input_value()=="随便填写的"
#    label 数字输入专用
#     get_by_label的前提是 上下组合锚点和ID一致 才可以支持定位，for XXX…………ID XXX
    page.get_by_label("也许你可以").fill("lable的定位填写")
    expect(page.get_by_text("lable的定位填写")).to_be_visible()
    assert page.get_by_label("也许你可以").input_value() == "lable的定位填写"
    page.get_by_label("数字输入专用").fill("123.123456789012345678")
    page.get_by_label("数字输入专用").blur()
    page.wait_for_timeout(2_0000)
    assert page.get_by_label("数字输入专用").input_value()=="123.1234567890"

# 文本框
def test_pw_textarea(page: Page):
    page.goto("/demo/textarea",wait_until="networkidle")
    # 可以通过locator去定位textarea文本框的内容
    page.locator("textarea").fill("文本框")
    # assert page.locator("textarea").input_value() =="文本框"
    # 可以通过\n来进行换行的操作
    page.locator("textarea").fill("文本框\n换行")
    # 可以通过”“”XXX +换行空格XXX “”“来进行换行操作
    page.locator("textarea").fill("""123
    456""")
    expect(page.locator("textarea")).to_have_value("""123
    456""")
    # 可以通过press_sequentially来进行新增 而非清楚再输入的操作
    page.locator("textarea").press_sequentially("789",delay=2_000)
    # 可以通过to_have_value来获取文本框的内容进行断言
    # 优先使用to_have_value，to_have_value不好用才使用assert
    expect(page.locator("textarea")).to_have_value("""123
    456789""")

# 单选框
def test_pw_radio(page: Page):
    page.goto("/demo/radio",wait_until="networkidle")
    # 先通过文本定位到选项框,再通过locator定位到选项
    page.get_by_text("草莓").locator("input").click()
    # 对选项进行断言to_be_checked
    expect(page.get_by_text("草莓").locator("input")).to_be_checked()
    page.wait_for_timeout(2_000)
    page.get_by_text("香蕉").locator("input").click()
    expect(page.get_by_text("香蕉").locator("input")).to_be_checked()
    page.wait_for_timeout(2_000)
    page.get_by_text("苹果").locator("input").click()
    expect(page.get_by_text("苹果").locator("input")).to_be_checked()

# 多选框
def test_pw_checkbox(page: Page):
    page.goto("/demo/checkbox",wait_until="networkidle")
    page.wait_for_timeout(2_000)
    # set_checked(True) 选中
    # set_checked(False) 不选
    # not_to_be_checked() 没有勾选
    page.get_by_text("美团").locator("input").set_checked(True)
    expect(page.get_by_text("美团").locator("input")).to_be_checked()
    page.wait_for_timeout(2_000)
    page.get_by_text("测试").locator("input").set_checked(True)
    expect(page.get_by_text("测试").locator("input")).to_be_checked()
    page.wait_for_timeout(2_000)
    page.get_by_text("开发").locator("input").set_checked(False)
    expect(page.get_by_text("开发").locator("input")).not_to_be_checked()

# 按钮开关
def test_pw_switch(page: Page):
    page.goto("/demo/switch",wait_until="networkidle")
    page.locator('//div[@aria-checked]').click()
    page.wait_for_timeout(2_000)
    expect(page.locator('//div[@aria-checked="true"]')).to_be_visible()
    expect(page.get_by_text("已经学会了~")).to_be_visible()
    page.locator('//div[@aria-checked]').click()
    expect(page.locator('//div[@aria-checked="false"]')).to_be_visible()


# 文件上传
def test_pw_upload(page: Page):
    page.goto("/demo/upload",wait_until="networkidle")
    # 定位到元素之后,用set_input_files上传文件
    page.locator('//input[@type="file"]').set_input_files("main.py")
    with page.expect_file_chooser() as chooser:
        # 页面中存在多个元素时,使用last可定位到最后一个
        page.locator("a").last.click()
    # 使用chooser上传文件chooser.value.set_files
    CHOR = chooser.value
    CHOR.set_files("main.py")

def test_pw_download(page: Page):
    page.goto("/demo/download",wait_until="networkidle")
    page.locator("textarea").fill("测试文案")
    # 1用with来监听下载文件，获取文件的值。其中使用expect_download
    with page.expect_download() as downloader:
        page.get_by_text("Download").click()
    # 2.通过with获取到file后，将其保存为某个文件1.txt
    # 3.使用assert（非playwright，为自带）来判断文件1.txt是否存在
    downloader.value.save_as("Test.txt")
    assert os.path.exists("Test.txt")

def test_pw_drag(page: Page):
    page.goto("/demo/drag",wait_until="networkidle")
    # drag_to用法
    page.get_by_text("完成playwright教学").drag_to(page.get_by_text("下一步要做"))
    page
    page.get_by_text("街霸6天梯到达大师").drag_to(page.get_by_text("正在做"))
    page
    # AA.locator("xpath=/..").bb 表示这个A元素下有B
    expect(page.get_by_text("下一步要做").locator("xpath=/..").get_by_text("完成playwright教学").last).to_be_visible()
    expect(page.get_by_text("正在做").locator("xpath=/..").get_by_text("街霸6天梯到达大师").last).to_be_visible()





