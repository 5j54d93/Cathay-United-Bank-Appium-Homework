# Cathay United Bank Appium Homework

![GitHub](https://img.shields.io/github/license/5j54d93/Cathay-United-Bank-Appium-Homework)
[![GitHub stars](https://img.shields.io/github/stars/5j54d93/Cathay-United-Bank-Appium-Homework)](https://github.com/5j54d93/Cathay-United-Bank-Appium-Homework/stargazers)
![GitHub repo size](https://img.shields.io/github/repo-size/5j54d93/Cathay-United-Bank-Appium-Homework)

Uing [**Appium**](https://appium.io) to remote control Android mobile phone（Pixel 3a）to test some credit card views are appear correctly on [**Cathay United Bank**](https://www.cathaybk.com.tw/cathaybk/) website with [**Chrome**](https://www.google.com/chrome/).

## Preparation

1. Let Android phone and computer connect to the same Wi-Fi

## Flow Diagram

<img src="https://github.com/5j54d93/Cathay-United-Bank-Appium-Homework/blob/main/.github/assets/Flow%20Chart.png" width='100%' height='100%'/>

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
