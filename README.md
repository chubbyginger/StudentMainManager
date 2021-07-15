# StudentMain Manager
一个专杀极域电子教室的Python程序，具有基于wxPython的GUI。

## 原理
* 使用NTSD调试工具，取得Debug权限后强制结束极域教室（无论极域教室有没有设置任务管理器防杀）。
* 使用微软官方Sysinternals的工具[PsSuspend](https://docs.microsoft.com/zh-cn/sysinternals/downloads/pssuspend)挂起StudentMain进程，可以使得教师端定格画面但不会显示学生端断开。
* 使用IE的全屏模式，将教师端控制屏幕变成一个窗口，可以在进行自己的操作的同时看老师上课。
* 给Windows自带的`sethc.exe`快捷键打补丁，即使不慎被控屏，只需按下5次Shift键即可轻松逃脱控屏。
* 可以配套使用GitHub用户 @快乐的梦鱼 的[JiYuTrainer](https://github.com/imengyu/JiYuTrainer)，取得更好的控制效果。

## 系统要求

* 最低可在Windows XP中使用。在Windows 2000及以下，不能保证程序可以正常打开。

  > 当然了，我觉得各位的电脑再落后也不至于Windows 2000吧。现在主流都是Windows 7了……

## 使用协议 & 免责声明

若你使用本程序，即认为你已阅读并同意以下条款：

* 本程序仅供学习交流之用途，**禁止将本程序用于任何不道德、不遵守法律的行为**。如果不遵守，产生的后果自负。
* 本程序从你已经了解老师上课的内容的角度出发。如果你希望使用本软件，请务必保证你已经充分了解老师上课的内容。
  如果因为使用本程序而导致对学业成绩的影响，**后果自负**。
* 请遵守本程序的开源协议。

若你不同意以上条款，请**不要使用此程序**。

## 手动编译

1. 使用`PyInstaller`编译`main.pyw`的命令：

   ```
   pyinstaller --onefile --icon .\image-res\StudentMainManager.ico -w main.py
   ```

   使用UPX压缩可以使可执行文件减小。先[下载UPX](https://github.com/upx/upx/releases)，然后使用下面命令：

   ```
   pyinstaller --onefile --icon .\image-res\StudentMainManager.ico -w --upx-dir=<UPX路径> main.py
   ```

   如果正在调试，希望有命令行报错输出，把`-w`命令行开关去除。

   应该会看到类似如下输出：

   ```
   138 INFO: PyInstaller: 4.3
   138 INFO: Python: 3.8.1
   138 INFO: Platform: Windows-7-6.1.7601-SP1
   140 INFO: wrote *****\StudentMainManager\main.spec
   219 INFO: UPX is available.
   222 INFO: Extending PYTHONPATH with paths
   ['*****\\StudentMainManager',
    '*****\\StudentMainManager']
   pygame 2.0.1 (SDL 2.0.14, Python 3.8.1)
   Hello from the pygame community. https://www.pygame.org/contribute.html
   293 INFO: checking Analysis
   294 INFO: Building Analysis because Analysis-00.toc is non existent
   294 INFO: Initializing module dependency graph...
   298 INFO: Caching module graph hooks...
   331 INFO: Analyzing base_library.zip ...
   8057 INFO: Processing pre-find module path hook distutils from 'c:\\program files\\python3
   8\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
   8060 INFO: distutils: retargeting to non-venv dir 'c:\\program files\\python38\\lib'
   11784 INFO: Caching module dependency graph...
   12283 INFO: running Analysis Analysis-00.toc
   12324 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final exec
   utable
     required by c:\program files\python38\python.exe
   12866 INFO: Analyzing *****\StudentMainManager\main.pyw
   13888 INFO: Processing module hooks...
   13890 INFO: Loading module hook 'hook-difflib.py' from 'c:\\program files\\python38\\lib\\
   site-packages\\PyInstaller\\hooks'...
   13898 INFO: Loading module hook 'hook-distutils.py' from 'c:\\program files\\python38\\lib
   \\site-packages\\PyInstaller\\hooks'...
   13903 INFO: Loading module hook 'hook-distutils.util.py' from 'c:\\program files\\python38
   \\lib\\site-packages\\PyInstaller\\hooks'...
   13909 INFO: Loading module hook 'hook-encodings.py' from 'c:\\program files\\python38\\lib
   \\site-packages\\PyInstaller\\hooks'...
   14069 INFO: Loading module hook 'hook-heapq.py' from 'c:\\program files\\python38\\lib\\si
   te-packages\\PyInstaller\\hooks'...
   14076 INFO: Loading module hook 'hook-lib2to3.py' from 'c:\\program files\\python38\\lib\\
   site-packages\\PyInstaller\\hooks'...
   14342 INFO: Loading module hook 'hook-multiprocessing.util.py' from 'c:\\program files\\py
   thon38\\lib\\site-packages\\PyInstaller\\hooks'...
   14349 INFO: Loading module hook 'hook-pickle.py' from 'c:\\program files\\python38\\lib\\s
   ite-packages\\PyInstaller\\hooks'...
   14355 INFO: Loading module hook 'hook-sysconfig.py' from 'c:\\program files\\python38\\lib
   \\site-packages\\PyInstaller\\hooks'...
   14360 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from 'c:\\program files\\
   python38\\lib\\site-packages\\PyInstaller\\hooks'...
   14365 INFO: Loading module hook 'hook-xml.py' from 'c:\\program files\\python38\\lib\\site
   -packages\\PyInstaller\\hooks'...
   14483 INFO: Loading module hook 'hook-_tkinter.py' from 'c:\\program files\\python38\\lib\
   \site-packages\\PyInstaller\\hooks'...
   14758 INFO: checking Tree
   14760 INFO: Building Tree because Tree-00.toc is non existent
   14762 INFO: Building Tree Tree-00.toc
   14974 INFO: checking Tree
   14977 INFO: Building Tree because Tree-01.toc is non existent
   14979 INFO: Building Tree Tree-01.toc
   15142 INFO: checking Tree
   15144 INFO: Building Tree because Tree-02.toc is non existent
   15146 INFO: Building Tree Tree-02.toc
   15192 INFO: Looking for ctypes DLLs
   15346 INFO: Analyzing run-time hooks ...
   15354 INFO: Including run-time hook 'c:\\program files\\python38\\lib\\site-packages\\PyIn
   staller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
   15365 INFO: Including run-time hook 'c:\\program files\\python38\\lib\\site-packages\\PyIn
   staller\\hooks\\rthooks\\pyi_rth_win32api.py'
   15404 INFO: Looking for dynamic libraries
   16309 INFO: Looking for eggs
   16311 INFO: Using Python library c:\program files\python38\python38.dll
   16313 INFO: Found binding redirects:
   []
   16324 INFO: Warnings written to *****\StudentMainManager\build\main\war
   n-main.txt
   16449 INFO: Graph cross-reference written to *****\StudentMainManager\b
   uild\main\xref-main.html
   16504 INFO: checking PYZ
   16506 INFO: Building PYZ because PYZ-00.toc is non existent
   16509 INFO: Building PYZ (ZlibArchive) *****\StudentMainManager\build\m
   ain\PYZ-00.pyz
   18201 INFO: Building PYZ (ZlibArchive) *****\StudentMainManager\build\m
   ain\PYZ-00.pyz completed successfully.
   18225 INFO: checking PKG
   18227 INFO: Building PKG because PKG-00.toc is non existent
   18229 INFO: Building PKG (CArchive) PKG-00.pkg
   18243 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-stdio-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-stdio-l1-1-0.dll: NotCompressibleException
   18370 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\python38.dll
   21242 INFO: Disabling UPX for c:\program files\python38\VCRUNTIME140.dll due to CFG!
   21262 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-locale-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-locale-l1-1-0.dll: NotCompressibleException
   21360 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-math-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-math-l1-1-0.dll: NotCompressibleException
   21459 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-heap-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-heap-l1-1-0.dll: NotCompressibleException
   21556 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-runtime-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-runtime-l1-1-0.dll: NotCompressibleException
   21651 INFO: Disabling UPX for C:\Windows\system32\ucrtbase.dll due to CFG!
   21673 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-time-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-time-l1-1-0.dll: NotCompressibleException
   21769 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-conio-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-conio-l1-1-0.dll: NotCompressibleException
   21865 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-string-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-string-l1-1-0.dll: NotCompressibleException
   21962 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-filesystem-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-filesystem-l1-1-0.dll: NotCompressibleException
   22059 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-convert-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-convert-l1-1-0.dll: NotCompressibleException
   22156 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-environment-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-environment-l1-1-0.dll: NotCompressibleException
   22252 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-process-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-process-l1-1-0.dll: NotCompressibleException
   22349 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-timezone-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-timezone-l1-1-0.dll: NotCompressibleException
   22447 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-heap-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-heap-l1-1-0.dll: NotCompressibleException
   22544 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-file-l1-2-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-file-l1-2-0.dll: NotCompressibleException
   22642 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-localization-l1-2-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-localization-l1-2-0.dll: NotCompressibleException
   22743 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-synch-l1-2-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-synch-l1-2-0.dll: NotCompressibleException
   22843 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-processthreads-l1-1-1.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-processthreads-l1-1-1.dll: NotCompressibleException
   22942 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-datetime-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-datetime-l1-1-0.dll: NotCompressibleException
   23039 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-memory-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-memory-l1-1-0.dll: NotCompressibleException
   23139 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-namedpipe-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-namedpipe-l1-1-0.dll: NotCompressibleException
   23238 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-errorhandling-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-errorhandling-l1-1-0.dll: NotCompressibleException
   23335 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-util-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-util-l1-1-0.dll: NotCompressibleException
   23432 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-string-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-string-l1-1-0.dll: NotCompressibleException
   23532 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-handle-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-handle-l1-1-0.dll: NotCompressibleException
   23632 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-processthreads-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-processthreads-l1-1-0.dll: NotCompressibleException
   23730 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-synch-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-synch-l1-1-0.dll: NotCompressibleException
   23827 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-console-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-console-l1-1-0.dll: NotCompressibleException
   23924 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-file-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-file-l1-1-0.dll: NotCompressibleException
   24025 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-libraryloader-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-libraryloader-l1-1-0.dll: NotCompressibleException
   24125 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-processenvironment-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-processenvironment-l1-1-0.dll: NotCompressibleException
   24225 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-interlocked-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-interlocked-l1-1-0.dll: NotCompressibleException
   24323 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-sysinfo-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-sysinfo-l1-1-0.dll: NotCompressibleException
   24424 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-profile-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-profile-l1-1-0.dll: NotCompressibleException
   24528 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-file-l2-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-file-l2-1-0.dll: NotCompressibleException
   24629 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-debug-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-debug-l1-1-0.dll: NotCompressibleException
   24727 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-core-rtlsupport-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-core-rtlsupport-l1-1-0.dll: NotCompressibleException
   24826 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\select.pyd
   24929 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_socket.pyd
   25059 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_overlapped.pyd
   25176 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_ssl.pyd
   25329 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_asyncio.pyd
   25453 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_queue.pyd
   25563 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\unicodedata.pyd
   26292 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_lzma.pyd
   26514 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_bz2.pyd
   26648 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_ctypes.pyd
   26802 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_multiprocessing.pyd
   26916 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\pyexpat.pyd
   27109 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_decimal.pyd
   27342 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\win32evtlog.pyd
   27473 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\win32api.pyd
   27640 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_hashlib.pyd
   27755 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_win32sysloader.pyd
   27858 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_elementtree.pyd
   28038 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\psutil\_psutil_windows.cp38-win_amd64.pyd
   28176 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\_curses.cp38-win_amd64.pyd
   28365 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wx\_adv.cp38-win_amd64.pyd
   29211 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wx\_html.cp38-win_amd64.pyd
   29691 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wx\_msw.cp38-win_amd64.pyd
   29832 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wx\siplib.cp38-win_amd64.pyd
   30040 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wx\_core.cp38-win_amd64.pyd
   35709 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\libssl-1_1.dll
   36187 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\libcrypto-1_1.dll
   38199 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\libffi-7.dll
   38311 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-utility-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-utility-l1-1-0.dll: NotCompressibleException
   38415 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\pywintypes38.dll
   38603 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wxbase315u_vc140_x64.dll
   40395 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wxmsw315u_core_vc140_x64.dll
   46096 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wxmsw315u_html_vc140_x64.dll
   46622 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\wxbase315u_net_vc140_x64.dll
   46833 INFO: Disabling UPX for c:\program files\python38\lib\site-packages\wx\MSVCP140.dll
   due to CFG!
   46856 INFO: Executing - *****
   PX\upx --lzma -q C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache
   01_py38_64bit\api-ms-win-crt-multibyte-l1-1-0.dll
   upx: C:\Users\Administrator.WIN-HM9DRC57VNQ\AppData\Local\pyinstaller\bincache01_py38_64bi
   t\api-ms-win-crt-multibyte-l1-1-0.dll: NotCompressibleException
   48221 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
   48232 INFO: Bootloader c:\program files\python38\lib\site-packages\PyInstaller\bootloader\
   Windows-64bit\runw.exe
   48235 INFO: checking EXE
   48238 INFO: Building EXE because EXE-00.toc is non existent
   48240 INFO: Building EXE from EXE-00.toc
   48249 INFO: Copying icons from ['image-res\\StudentMainManager.ico']
   48255 INFO: Writing RT_GROUP_ICON 0 resource with 20 bytes
   48259 INFO: Writing RT_ICON 1 resource with 4264 bytes
   48274 INFO: Updating manifest in *****\StudentMainManager\build\main\ru
   nw.exe.2joccxzl
   48280 INFO: Updating resource type 24 name 1 language 0
   48290 INFO: Appending archive to EXE *****\StudentMainManager\dist\main
   .exe
   53974 INFO: Building EXE from EXE-00.toc completed successfully.
   ```

   

2. 将无用的`build`文件夹、`__pycache__`和`main.spec`文件删除。

3. 新建一个文件夹，将`dist`文件夹中的`main.exe`复制过去，改名为`StudentMainManager.exe`。

4. 将`config.ini`、`binaries`文件夹复制过去，即可使用。

## 有关早期版本
本程序的早期版本由我在六年级时使用批处理编写，具有一个文字界面，缺少一些非常基本的功能，比如说保持最前端显示。

由于代码过于粗鄙，这里就不放出来了。

## 开源许可
Apache-2.0 License（详情请见`/LICENSE`）。
