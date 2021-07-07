# binaries
本目录包含本程序需要用到的二进制程序，包括：
* Symbolic Debugger for Windows 2000 (ntsd.exe)
* Process Suspender (pssuspend.exe)
* Patched Sethc (psethc.exe)
* JiYuTrainer (JiYuTrainer/JiYuTrainer.exe)

## 各个程序的用途
1. Symbolic Debugger for Windows 2000 (ntsd.exe): 用于取得Debug权限并强制结束StudentMain.exe主程序。微软官方工具。
2. Process Suspender (pssuspend.exe): 用于挂起StudentMain.exe而不结束它，使得教师端不会看到学生机离线但教师端连不上学生机。微软官方工具。
3. Patched Sethc (psethc.exe): 这是一个可以使用NTSD强制结束学生端进程的程序，可以根据用户的需求，替换掉`C:\Windows\System32`目录下的`sethc.exe`粘滞键程序，这样一来，只要在老师全屏广播的时候按5次Shift键，学生端就被关闭了。
4. JiYuTrainer (JiYuTrainer/JiYuTrainer.exe): 由GitHub用户 @快乐的梦鱼 提供，可以提供诸如广播窗口化的功能。