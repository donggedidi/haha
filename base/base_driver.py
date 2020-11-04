from appium import webdriver

def base_driver():
    desired_caps = dict()
    # 手机参数
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555' # 应用参数
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['noReset'] = True
    # 获取driver
    return webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)