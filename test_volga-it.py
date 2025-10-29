from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestVolgaIT():  
    def test_form(self, browser):
        try:
            link = "https://practice-automation.com/form-fields/"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, '#name-input').send_keys('potc')
            inp_drink = browser.find_element(By.CSS_SELECTOR, '#drink1')
            inp_drink.click()
            browser.execute_script("window.scrollTo(0, 900)")
            select = Select(browser.find_element(By.CSS_SELECTOR, '#automation'))
            select.select_by_value("yes")
            inp_color = browser.find_element(By.CSS_SELECTOR, '#color1')
            browser.execute_script("arguments[0].click();", inp_color)
            li_1 = browser.find_element(By.XPATH, '//li[contains(text(), "Selenium")]').text
            li_2 = browser.find_element(By.XPATH, '//li[contains(text(), "Playwright")]').text
            li_3 = browser.find_element(By.XPATH, '//li[contains(text(), "Cypress")]').text
            li_4 = browser.find_element(By.XPATH, '//li[contains(text(), "Appium")]').text
            li_5 = browser.find_element(By.XPATH, '//li[contains(text(), "Katalon")]').text

            browser.execute_script("window.scrollTo(0, 1500)")
            message_text = li_1 + '\n' + li_2 + '\n' + li_3 + '\n' + li_4 + '\n' + li_5  

            browser.find_element(By.CSS_SELECTOR, '#email').send_keys('potc@example.com')
            browser.find_element(By.CSS_SELECTOR, '#message').send_keys(message_text)

            submit = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-btn"))  
            )
            browser.execute_script("arguments[0].click();", submit)

            alert = browser.switch_to.alert
            alert1 = alert.text
            assert alert1 == "Message received!", f"Анлак"
        except Exception as e:
            print(f'Ошибка, код ошибки {e}')
            raise  

    def test_btns(self, browser):  
        try:
            link = "https://practice-automation.com/click-events/" 
            browser.get(link)
            buttons = browser.find_elements(By.CSS_SELECTOR, ".custom_btn.btn_hover")
            res = ""
            
            for btn in buttons:
                btn.click()
                text = browser.find_element(By.CSS_SELECTOR, "#demo").text
                res += text
                print(text)
                
            assert res == "Meow!Woof!Oink!Moo!", f"Error"
            
        except Exception as e:
            print(f'Ошибка, код ошибки {e}')
            raise  

    def test_popups(self, browser): 
        try:
            link = "https://practice-automation.com/popups/" 
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, "#alert").click()
            alert = browser.switch_to.alert
            alert.accept()
            
            confirm_btn = browser.find_element(By.CSS_SELECTOR, "#confirm")
            confirm_btn.click()
            confirm_modal = browser.switch_to.alert
            confirm_modal.accept()
            assert browser.find_element(By.CSS_SELECTOR, "#confirmResult").text == "OK it is!", f"Error"
            confirm_btn.click()
            confirm_modal = browser.switch_to.alert
            confirm_modal.dismiss()
            assert browser.find_element(By.CSS_SELECTOR, "#confirmResult").text == "Cancel it is!", f"Error"
            
            name = "potc"
            
            prompt_btn = browser.find_element(By.CSS_SELECTOR, "#prompt")
            prompt_btn.click()
            prompt_modal = browser.switch_to.alert
            prompt_modal.send_keys(name)
            prompt_modal.accept()
            assert browser.find_element(By.CSS_SELECTOR, "#promptResult").text == f"Nice to meet you, {name}!", f"Error"
            prompt_btn.click()
            prompt_modal = browser.switch_to.alert
            prompt_modal.dismiss()
            assert browser.find_element(By.CSS_SELECTOR, "#promptResult").text == "Fine, be that way...", f"Error"
        except Exception as e:
            print(f'Ошибка, код ошибки {e}')
            raise  

if __name__ == "__main__":
    pytest.main()