from flask import Flask, request, render_template
#from regex import P
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tkinter import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

#name = "https://www.gramedia.com/"


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/result", methods = ['post',"get"])
def result():
    output = request.form.to_dict()
    name = output["name"]
    global name1
    name1 = "https://"+name+"/"

    grberanda()
    return render_template("homegr.html",name = name1)

@app.route('/brnd', methods=['GET','POST'])
def grberanda():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options,desired_capabilities=caps)
    driver.get(name1)
    output = request.form.to_dict()
    return render_template('homegr.html')
    

@app.route('/cri', methods=['POST'])
def grcari():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options)
    driver.get(name1)
    cari = driver.find_element_by_name("search")
    req_cari = request.form.get('cri')
    cari.send_keys(req_cari)
    cari.submit()
    output = request.form.to_dict()
    cri = output["cri"]
    return render_template('crigr.html')

@app.route('/lgin', methods=['POST'])
def grlogin():
    #chr_options = Options()
    #chr_options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options)
    #driver.get(name1)
    #login
    #element1 = driver.find_element_by_id("login-button").click()
    #element2 = driver.find_element_by_name("email")
    #element2.send_keys("achmadrizki15@gmail.com")
    #element3 = driver.find_element_by_name("password")
    #element3.send_keys("asdadadad")
    #submit = driver.find_element_by_xpath("//header/div[1]/div[2]/gm-auth-button[1]/div[2]/gm-auth-dialog[1]/div[1]/div[2]/gm-login-popup[1]/div[1]/form[1]/button[1]")
    #submit.click()
    output = request.form.to_dict()
    lg = output["lg"]
    return render_template('isianlogin.html')

@app.route('/frlgin', methods=['POST'])
def grformlgin():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options,desired_capabilities=caps)
    req_tj = request.form.get('tj')
    driver.get(name1+req_tj)
    #login
    #element1 = driver.find_element_by_id("login-button").click()
    req_elemail = request.form.get('lem')
    element2 = driver.find_element_by_name(req_elemail)
    req_email = request.form.get('em')
    element2.send_keys(req_email)
    req_elepass = request.form.get('emp')
    element3 = driver.find_element_by_name(req_elepass)
    req_password = request.form.get('pwd')
    element3.send_keys(req_password)
    submit = driver.find_element_by_xpath("//button[contains(.,'MASUK')]")
    submit.click()
    output = request.form.to_dict()
    return render_template('isianlogin.html')


@app.route('/dtr', methods=['POST'])
def grdaftar():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options)
    req_cari = request.form.get('cari')
    driver.get(name1+req_cari)
    #register
    nama = driver.find_element_by_id("mat-input-0")#('//*[@id="mat-input-0"]')
    nama.send_keys("Achmad Rizki Firdaus")
    email = driver.find_element_by_id("mat-input-1")#('//*[@id="mat-input-1"]')
    email.send_keys("achmadrizki15@gmail.com")
    kunci = driver.find_element_by_id("mat-input-2")#('//*[@id="mat-input-2"]')
    kunci.send_keys("asdadawdawdah")
    checkbox = driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
    checkbox.click()
    #tmbdaftar = driver.find_element_by_xpath('//*[@id="content"]/gm-sign-up2/div/div[1]/div/form/button')
    #tmbdaftar.click()
    output = request.form.to_dict()
    dt = output["dt"]
    try:
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"mat-input-0")))
        print("Register is filled")
    except:
        print("Timeout Exception: Register unable to filled.")
    return render_template('dtrgr.html')

@app.route('/efi', methods=['POST'])
def effi():
    output = request.form.to_dict()
    return render_template('isianefi.html')

@app.route('/frefi', methods=['POST'])
def freffi():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options)
    req_info = request.form.get('info')
    driver.get(name1+req_info)
    output = request.form.to_dict()
    return render_template('isianefi.html')

@app.route('/flex', methods=['POST'])
def flexx():
    output = request.form.to_dict()
    return render_template('isianflex.html')

@app.route('/frflx', methods=['POST'])
def frex():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options,desired_capabilities=caps)
    driver.get(name1)
    cari = driver.find_element_by_name("search")
    req_cari = request.form.get('crfx')
    cari.send_keys(req_cari)
    cari.submit()
    #element2 = driver.find_element_by_name('email')
    #req_email = request.form.get('emfx')
    #element2.send_keys(req_email)
    #element3 = driver.find_element_by_name('password')
    #req_password = request.form.get('pwfx')
    #element3.send_keys(req_password)
    #submit = driver.find_element_by_xpath("//button[contains(.,'MASUK')]")
    #submit.click()
    #element4 = driver.find_element_by_css_selector(".ion-person")
    #element4.click()
    #element5 = driver.find_element_by_xpath("//button[contains(.,'Akun Saya')]")
    output = request.form.to_dict()
    return render_template('isianflex.html')

@app.route('/us', methods=['POST'])
def uss():
    output = request.form.to_dict()
    return render_template('isianusa.html')

@app.route('/frus', methods=['POST'])
def frusa():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe',options=chr_options,desired_capabilities=caps)
    req_about = request.form.get('crusa')
    driver.get(name1+req_about)
    output = request.form.to_dict()
    return render_template('isianusa.html')








    


if __name__ == '__main__':
    app.run(debug=True)