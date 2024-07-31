from playwright.sync_api import expect,Page



def test_get_by_role(page: Page):
    # get_by_role的参数
    # checked适用于checkbox/radio 多选框/单选框是否选中
    # disable :  置灰
    # expanded:  是否展开
    # include_hidden: 是否隐藏
    # level:  文本等级 指定文本等级
    # name : 通过name关联组件元素状态
    # pressed: 是否已经被 按下
    # selected :是否被选中
    # exact: 是否被指定, 如果被指定 以精确指定为准

    """
    ARIA是Accessible Rich Internet Applications得缩写,
    指可访问得富互联网应用程序,role属性是ARIA中一个重要属性,用于定义HTML元素的角色,以增强网页的可访问性和可用性,
    以下是一些常用的ARIA role 属性及其解释:

     alert:表示警告信息,通常用于提示用户重要的信息或错误

    alertdialog:表示模态弹出框,用于显示用户需要关注的信息或提示

    application:表示应用程序,通常用于自定义的应用程序或复杂的用户界面

    button:表示按钮,用于触发操作,或执行特定的功能

    checkbox :表示复选框,用于用户选择多个选项

    combobox:表示下拉组合框,结合了输入框和下拉列表的功能

    grid:表示网格布局,用于显示表格或类似的数据布局

    gridcell: 表示网格单元格 是grid角色中的子元素

    group:表示组合框,用于将相关的元素组合在一起

    heading:表示标题,用于定义页面或章节的标题

    listbox:表示列表框,用于显示可选择得列表项

    log: 表示日志记录,用于显示程序或系统的日志信息

    menu:表示菜单,用于显示一组可选择得操作或者选项

    menubar:表示菜单栏，通常位于页面顶部或侧边，包含多个菜单。

    menuitem:表示菜单项，是menu或menubar中的子元素

    menuitemcheckbox:表示带有复选框的菜单项。

    menuitemradio:表示带有单选按钮的菜单项,

    option:表示选项，通常用于下拉列表或单选按钮组中的选项。

    presentation:表示陈述内容，用于显示只读的文本或信息

    progressbar:表示进度条，用于显示任务或操作的进度

    radio:表示单选按钮，用于允许用户从多个选项中选择一个，

    radiogroup:表示单选按钮组，用于将多个单选按钮组合在一起。

    region:表示区域，用于定义页面的不同部分或区域

    row:表示表格行，用于表格布局中的行元素，

    rowgroup:表示表格行组，用于将多行组合在一起。

    scrollbar:表示滚动条，用于在内容超出显示区域时提供滚动功能
    """
    page.goto("/demo/dialog",wait_until="networkidle")
    page.get_by_text("点我开启一个dialog").click()
    # 通过get_by_role去断言元素是否存在
    expect(page.get_by_role(role="dialog")).to_be_visible()
    page.goto("/demo/checkbox",wait_until="networkidle")
    # 里面参数可以直接根据元素状态取值,
    page.get_by_role("checkbox", name="开发", checked=False).set_checked(True)
    page.get_by_role("checkbox", name="开发", checked=True).set_checked(False)
    page.goto("/demo/table",wait_until="networkidle")
    expect(page.get_by_role("table")).to_be_visible()
    expect(page.get_by_role("cell")).to_have_count(13)
    # include_hidden=True 表示取img这个角色属性是隐藏的个数
    expect(page.get_by_role("img",include_hidden=True)).to_have_count(4)
    page.goto("/demo/grid",wait_until="networkidle")
    expect(page.get_by_role("treegrid")).to_be_visible()
    # filter(has_text="溜达王")这个元素里面包含的文字,定位到元素,, locator("div").nth(1)取这一行里面的第几个
    expect(page.get_by_role("row").filter(has_text="丫丫").locator("div").nth(0)).to_have_text("丫丫")


def test_get_by_text(page: Page):
    """
    以下规则使用条件: 参数中包含exact
    1:规范化空白-换行转空格,前后空格忽略,多个空格按一个空格处理
    2:默认是包含文本
    3:exact可以精确匹配
    4:可以匹配正则表达式
    """
    page.goto("/demo/getbytext",wait_until="networkidle")
    page
