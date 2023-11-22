import os

from selene import browser, have, be, by


def test_complete_todo():
    browser.open('automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').should(be.blank).type('Mariya')
    browser.element('#lastName').should(be.blank).type('Mokretsova')
    browser.element('#userEmail').should(be.blank).type('cameron105@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').should(be.blank).type('9066507373')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().type('June').press_enter()
    browser.element('.react-datepicker__year-select').click().type('1989').press_enter()
    browser.element('.react-datepicker__day--027').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').double_click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        'pictures/run_girl.png'))
    browser.element('#currentAddress').should(be.blank).type('Sant-Peterburg')

    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaiselmer').press_enter()
    browser.element('#submit').press_enter()


    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
        'Mariya Mokretsova' and 'cameron105@mail.ru'
        and 'Male' and '9066507373' and '27 June,1989'
        and 'English' and 'run_girl.png'
        and 'Sant-Peterburg' and 'Rajasthan Jaiselmer'))