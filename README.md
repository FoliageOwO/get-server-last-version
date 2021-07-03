# get-server-last-version
方便快捷地获取 `Paper` `Spigot` `Vanilla` 三个 Minecraft 服务端最新构建版本及下载链接

使用 ***BeautifulSoup*** 对网页进行快速爬取, 并且不需要 `headers` 与 `proxy` 即可获取

## 使用方法

执行 `python main.py` 可以快速查看 `Paper` `Spigot` `Vanilla` 的最新版本的 dict 字典

```python
# paper, spigot, vanilla 的用法一样

from paper import get_paper

print(get_paper()) # 获取整个 dict 字典
print(get_paper()['version']) # 获取最新版本号
print(get_paper()['download_url']) # 获取下载链接
```

将其添加至项目, 只需将 `custom_typing.py` 与 `util.py` 嵌入进去或修改文件名后直接导入即可

## All in one

如果你认为嵌入文件或修改导入的方法太麻烦, 不如直接使用 `get_server_last_version.py`, 使用方法如下:

```python
from get_server_last_version import get_paper # get_spigot, get_vanilla

print(get_paper()) # 获取整个 dict 字典
# ...
```

这样就可以直接添加至项目, 无需多余的操作
