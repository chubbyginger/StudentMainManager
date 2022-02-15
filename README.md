# StudentMain Manager
[![](https://img.shields.io/badge/language-Python-blue.svg)](https://github.com/python/cpython) [![](https://img.shields.io/badge/version-1.0.2-brightgreen)](https://github.com/yangshunhuai/StudentMainManager/releases) [![](https://img.shields.io/badge/license-Apache--2.0-brightgreen)](https://github.com/yangshunhuai/StudentMainManager/blob/main/LICENSE)

一个专杀极域电子教室的Python程序，具有基于wxPython的GUI。

## **StudentMain Manager将停止支持**
本项目已停止支持。除非有严重问题，否则不会作任何更新。

*[StudentMain Manager 2](https://github.com/yangshunhuai/StudentMainManager2)将会代替StudentMain Manager。*

## 原理
* 使用NTSD调试工具，取得Debug权限后强制结束极域教室（无论极域教室有没有设置任务管理器防杀）。
* 使用微软官方Sysinternals的工具[PsSuspend](https://docs.microsoft.com/zh-cn/sysinternals/downloads/pssuspend)挂起StudentMain进程，可以使得教师端定格画面但不会显示学生端断开。
* 使用IE的全屏模式，将教师端控制屏幕变成一个窗口，可以在进行自己的操作的同时看老师上课。
* 给Windows自带的`sethc.exe`快捷键打补丁，即使不慎被控屏，只需按下5次Shift键即可轻松逃脱控屏。
* 可以配套使用GitHub用户 @快乐的梦鱼 的[JiYuTrainer](https://github.com/imengyu/JiYuTrainer)，取得更好的控制效果。

## 系统要求

目前暂时最低只能在Windows Vista中使用。在Windows 2000及以下，不能保证程序可以正常打开。

> 目前Windows XP的支持还在准备，但是编译工作十分艰难……
> 在Windows XP中Python不断出现各种谜之故障：先是pip提示漏了库，装了库pip又说语法错误，反正pip彻底废了。
> 在手动下载tar.gz安装的时候，先是出现各种依赖库问题，又是有一个叫做buildtools的库只支持Python 2，出现各种语法bug……

如果实在无法支持Windows XP，将会放弃Windows XP的支持。

## 下载
**最近发现我的开发机中了病毒**，而本项目的发行版很有可能被感染了。

**因此，如果有仍然在使用Version 1.0.2 Build 210716及更早版本的用户，请立即停止使用**，并[在此处](https://github.com/yangshunhuai/StudentMainManager/releases)获取重新编译的版本Version 1.0.2 Build 220215。

## 使用协议 & 免责声明

若你使用本程序，即认为你已阅读并同意以下条款：

* 本程序仅供学习交流之用途，**禁止将本程序用于任何不道德、不遵守法律的行为**。如果不遵守，产生的后果自负。
* 本程序从你已经了解老师上课的内容的角度出发。如果你希望使用本软件，请务必保证你已经充分了解老师上课的内容。
  如果因为使用本程序而导致对学业成绩的影响，**后果自负**。
* 请遵守本程序的开源协议。

若你不同意以上条款，请**不要使用此程序**。

## 手动编译
我编写了可以自动编译的脚本build.bat，只需运行，即可按照自己的需求进行编译。

## 有关早期版本
本程序的早期版本由我在六年级时使用批处理编写，具有一个文字界面，缺少一些非常基本的功能，比如说保持最前端显示。

由于代码过于粗鄙，这里就不放出来了。

## 开源许可
Apache-2.0 License（详情请见`/LICENSE`）。
