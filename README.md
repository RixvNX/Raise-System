#### 组册部分
1. Kernel 系统内核,用于对系统进程进行调度和数据分析
1. TaskManager 任务管理器,用于手动改变任务的优先级,状态等信息
1. User 用户管理器,注册系统级进程以供登录后的用户应用集成从而组成进程树
1. SimpleLogic 简单逻辑返回器,在简单的逻辑中进行快速高效的逻辑处理
1. ValueTemplate 数据值模版, 通过访问Register项和内置的值组成映射表,将"$(RVT.值名称)"格式化为值
1. Character 字节盒,用于对字节及字符串信息的处理
1. Register 注册表,统计信息及快速访问量路径
1. Installer 安装器,安装应用程序的程序
1. Logger 日志记录器,统计系统的错误和操作
1. Executor 启动应用及应用检查
1. CommandLine 命令行,用于基本的命令读取和简单操作
1. Signer 签名器,用于对软件进行权限签名和信息标注

#### 启动结构
```php
[Kernel] -> 创建默认系统进程"Kernel(com.raise.system.Kernel)"
[Kernel] -> 设定系统进程的优先级以及改为系统级进程,与Kernel进程自己组成系统级进程树
[kernel] -> 启用进程"Executor(com.raise.system.Executor)"
[Executor] -> 检测"com.raise.system"下的所有系统级应用 (只读)
{
    !True通过:
        $braek跳出循环
    ?False否则:
        $throw抛出异常:SystemException(系统级错误)
        $outstream:out() 使用输出流将错误信息显示在屏幕上
        $^exit() 退出 
} {
    !onOut当语句被跳出:
}
[kernel] -> 启用进程"Logger(com.raise.system.Logger)"
[Kernel] -> 启用进程"User(com.raise.system.User)"
{$loop循环:}
[User] -> 更新"User(com.raise.system.User)"进程状态
[User] -> 等待用户登录信息
[Kernel] -> 启用进程"SimpleLogic(com.raise.system.SimpleLogic)"
[SimpleLogic] -> 将"User(com.raise.system.User)"传入的信息进行逻辑分析
[User] -> 捕获"SimpleLogic(com.raise.system.SimpleLogic)"返回的逻辑数据并分析
{
    !True通过:
        $braek跳出循环
    ?False否则:
        $continue跳过这次
} {
    !onOut当语句被跳出:
}
[User] -> 请求"Kernel(com.raise.system.Kernel)"对"Register(com.raise.system.Register)"编入登录信息值
[Kernel] -> 接受来自"User(com.raise.system.User)"的请求
[Kernel] -> 结束起始系统引导.
```

#### 默认系统级进程包
```yaml
Kernel  :  com.raise.system.Kernel
TaskManager  :  com.raise.system.TaskManager
User  :  com.raise.system.User
SimpleLogic  :  com.raise.system.SimpleLogic
ValueTemplate  :  com.raise.system.ValueTemplate
Character  :  com.raise.system.Character
Register  :  com.raise.system.Register
Installer  :  com.raise.system.Installer 
Logger  :  com.raise.system.Logger
CommandLine: com.raise.system.CommandLine
Signer : com.raise.system.Signer
```

#### [Installer]如何解析安装包(.rp)
将Raise(Application)Package(.rp)文件视作为一个目录, 其中必须包括必要文件,以软件TestRaiser:
```yaml
(file) appInfo.info : 包信息,里面包括了软件名,作者,版本,描述,主要类,继承关系,所需环境等必要信息
(file) TestRaiser.app : 必要类,用于整个app的启动类,必须与"appInfo.info"中的"主要类"项名称相同
(dir)  bin : 用于存放软件所需的自写包
(dir)  temp : 缓存文件夹,允许安装器时此处会被清空,后将用于安装时产生的临时数据
(dir)  data : 数据文件夹,用于软件一开始所用的初始化数据的文件夹
```
当然,如果你想为其他程序提供接口服务,可以格外创建下面的目录:
```yaml
(dir)  api : 程序外部接口,用于提供接口以供其他程序使用
```
其中对appInfo.info文件的要求是极其严格的,下面是一个实例:
```json
{
    "Name": "APPName",
    "Author": ["Author"],
    "Class": "com.test.raiseapp.testAPP",
    "From": "",
    "Runtime": "",
    "Description": "It is used for task scheduling and task processing in the whole Raise system.",
    "DefalutSigns": ["a.sign", "b.sign", "c.sign"]
}
```
当要求全部符合时,安装器将开始安装软件包.

#### 关于签名权限(Signs)
签名器(Signer)所需要的参数有"signer sign <APP名称> <签名权限> <可用值>"
若"APP名称"未在注册表(Register)中注册关联项,则该条命令会被直接忽略,因为签名器无法确定APP的位置以及APP是否被保护,
若"可用值"为"True"或"1"时,则该APP的"签名权限"签名为允许使用状态,若为"False"或"2"为禁止状态,若APP请求权限则会被直接拒绝,
若为"Default"或"0",则APP索取权限时,给出提示并得到返回值.
下面还有一些系统内置的权限:
| 名称  | 描述  | 默认值 |
|:----------|:----------|:----------|
| Application.API.use | 使用其他程序的API    | False |
| Application.API.make | 提供API供其他程序使用 | False |
| Application.Update | 安装与自己同主类的更新版本 | False |
| Application.Update.Older | 覆盖该版本而安装旧版本 | False |
| Application.Notice | 允许应用发送通知 | False |
| Keyboard.Input | 允许读取键盘的操作 | False |
| File.Readme | 允许自己的应用信息文件被读取 | True |
| File.Read | 允许读取系统中的文件 | False |
| File.Out | 允许写入和创建文件 | False |
| File.Remove | 允许删除系统中的文件 | False |
| RecycleBin.Restore | 允许还原回收站中的文件 | False |
| RecycleBin.Clear | 允许删除回收站中的文件 | False |
