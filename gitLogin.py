import sys
from selenium import webdriver

username = "maheshgopi08" #Insert your github username here
password = "Gm9640962989" #Insert your github password here
reponame = "new1"
desc="To develop"+reponame

browser = webdriver.Chrome()
browser.get('http://github.com/login')

def remove():
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/new/')
    browser.find_elements_by_xpath("//input[@name='repository[name]']")[0].send_keys(reponame)
    # + reponame + '/settings')
    browser.find_elements_by_xpath("//input[@name='repository[description]']")[0].send_keys(desc)

    browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0].click()
    browser.find_elements_by_xpath("//input[@type='submit']")[0].click()

    browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(reponame)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + username)

if __name__ == "__main__":
    remove()