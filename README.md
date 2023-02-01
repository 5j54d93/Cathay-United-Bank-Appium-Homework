# Cathay United Bank Appium Homework

![GitHub](https://img.shields.io/github/license/5j54d93/Cathay-United-Bank-Appium-Homework)
[![GitHub stars](https://img.shields.io/github/stars/5j54d93/Cathay-United-Bank-Appium-Homework)](https://github.com/5j54d93/Cathay-United-Bank-Appium-Homework/stargazers)
![GitHub repo size](https://img.shields.io/github/repo-size/5j54d93/Cathay-United-Bank-Appium-Homework)

Uing [**Appium**](https://appium.io) to remote control Android mobile phone（Pixel 3a）to test some credit card views are appear correctly on [**Cathay United Bank**](https://www.cathaybk.com.tw/cathaybk/) website with [**Chrome**](https://www.google.com/chrome/).

## Preparation

1. Let Android phone and computer connect to the same Wi-Fi
2. Enable「USB Debugging」and「Wireless Debugging」on Android phone
3. Connect to Android phone by commands below in terminal：

```shell
adb connect replace_with_Android_phone's_IP
adb tcpip 5555
```

If it run for a long time and no result, use `killall adb` command and try again.

## Flow Diagram

<img src="https://github.com/5j54d93/Cathay-United-Bank-Appium-Homework/blob/main/.github/assets/Flow%20Chart.png" width='100%' height='100%'/>

- Set up web driver with these capabilities：

```python
desiredCapabilities = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': 'replace_with_Android_phone's_IP:5555',
    'automationName': 'UiAutomator2',
    'browserName': 'Chrome', # use native broswer app
    'noReset': True, # don't reset sttings in Chrome app
    'newCommandTimeout': 60 # if our code do nothing for 60 seconds, the connection will quit
}
```

- Using `try except`, so that if connect is weak and timeout we could use the code below to rerun _main.py_

```python
os.execv(sys.executable, ['python3'] + sys.argv)
```

## Learn More

Use these command line in terminal

- To see all activities of an app when using it.（sometimes main activity isn't the launch activity of an app）

```shell
adb logcat | grep START
```

- To see the current running activity

```shell
adb shell dumpsys activity | grep mCurrentFocus
```

## License：MIT

This package is [MIT licensed](https://github.com/5j54d93/Cathay-United-Bank-Appium-Homework/blob/main/LICENSE).
