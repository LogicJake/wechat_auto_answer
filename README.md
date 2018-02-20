# wechat_auto_answer
智力超人辅助

![pyversions](https://img.shields.io/badge/python%20-3.5%2B-blue.svg)
![Travis](https://img.shields.io/travis/rust-lang/rust.svg)

## 使用方法
1. 下载Fiddler，根据[教程](https://testerhome.com/topics/3939)搭建好抓包环境，最后一步手机上一定要安装好FiddlerRoot证书。安卓手机一般在设置里的安全设置里从SD卡安装证书。至此fiddler可以抓取到手上的https数据包。
如果设置成功，打开微信智力超人可以抓取到下面图中红线框中的数据包。    
![ERROR](https://github.com/LogicJake/wechat_auto_answer/raw/master/pic/success.png)
2. clone本仓库到本地，记住下载位置，以“F:\\Project\\Python\\wechat_auto_answer”为例，各人各异。
3. Fiddler添加脚本，将答题过程中的数据包保存到本地供程序读取。  
Fiddler菜单 >> Rules >> Customize Rules。在打开的文件中找到OnBeforeResponse这个方法，在方法末尾加上如下代码： 
```
if (oSession.fullUrl.Contains("quan.qq.com"))
{
  oSession.utilDecodeResponse();//消除保存的请求可能存在乱码的情况
  var fso;
	var file;
	fso = new ActiveXObject("Scripting.FileSystemObject");
	//文件保存路径，可自定义
	file = fso.OpenTextFile("F:\\Project\\Python\\wechat_auto_answer\\Session.txt",2 ,true, -2);
	file.writeLine(oSession.GetResponseBodyAsString());
	file.close();
}
```
OpenTextFile方法中的第一个参数为第二步项目所在位置，即指定Fiddler将数据包内容保存在项目目录下的的Session.txt中。
![ERROR](https://github.com/LogicJake/wechat_auto_answer/raw/master/pic/js.png)
4. 运行项目中auto_answer.py，打开智力超人开始对战。程序会自动搜索题目，然后显示搜索结果中各个答案出现的次数，以供判断。  
![ERROR](https://github.com/LogicJake/wechat_auto_answer/raw/master/pic/answer.png)
