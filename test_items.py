

def test_basket_button_is_displayed(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_xpath('(//button[@type="submit"])[2]')