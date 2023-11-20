from selene import browser


def test_complete_todo():

    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    browser.open('/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all(selector)
