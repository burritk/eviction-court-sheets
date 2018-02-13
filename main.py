import time

from pyscraper.iterator import _gen_tree as gen_tree
from pyscraper.utils import get_xpath_if_exists
from pyscraper.selenium_utils import get_headless_driver, get_headed_driver, wait_for_xpath, wait_for_tag, wait_for_classname


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# first page
driver = get_headed_driver()
driver.get('https://eservices.cmcoh.org/eservices/home.page.2')

# look for button in links
wait_for_xpath(driver, '//*[@id="searchButtonInput"]')
links = driver.find_elements_by_tag_name('a')
button = [link for link in links if link.text == 'Click Here'][0]
button.click()

# get 100 results per page
wait_for_xpath(driver, '//*[@id="mainContent"]/div[2]/div[2]')
form_elements = driver.find_elements_by_class_name('formElement')
number_options = form_elements[0].find_elements_by_tag_name('option')
one_hundred = [option for option in number_options if option.text == '100'][0]
one_hundred.click()

# second page
case_type_search = wait_for_xpath(driver, '//*[@id="id1f"]/div[1]/ul/li[4]/a')
case_type_search.click()

# fill form
form = wait_for_xpath(driver, '//*[@id="caseTypeSearch"]')
form_elements = driver.find_elements_by_class_name('formElement')
for element in form_elements[1:]:
    if 'Begin Date' in element.text:
        begin_date = element.find_element_by_tag_name('input')
        begin_date.send_keys('01012018')
    if 'End Date' in element.text:
        end_date = element.find_element_by_tag_name('input')
        end_date.send_keys('01312018')
    if 'Case Type' in element.text:
        case_type_options = element.find_elements_by_tag_name('option')
        cvg = [option for option in case_type_options if 'CVG' in option.text][0]
        cvg.click()
    if 'Case Status' in element.text:
        case_status_selector = Select(element.find_element_by_tag_name('select'))
        case_status_selector.deselect_all()
        case_status_selector.select_by_visible_text('OPEN')
    if 'Party Type' in element.text:
        select = wait_for_tag(element, 'select')
        options = wait_for_tag(select, 'option')
        party_type_selector = Select(select)
        party_type_selector.deselect_all()
        party_type_selector.select_by_visible_text('PLAINTIFF')



form_buttons = driver.find_elements_by_class_name('formButtons')
search = form_buttons[0].find_element_by_tag_name('input')
search.click()

teears = driver.find_elements_by_tag_name('tr')
for element in teears:
    if ',' in element.text:
        link = element.find_element_by_tag_name('a')
        link.click()
        panel = wait_for_xpath(driver, '//*[@id="ptyInfo"]')
        titlebar = driver.find_elements_by_tag_name('h2')
        cvg = titlebar.text.strip()
        headers = panel.find_elements_by_class_name('subSectionHeader2')
        print 'j'
        pass  # if is name

print(search)


print 'hello'
try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id64"]'))
    )
finally:
    driver.quit()
print 'hello'