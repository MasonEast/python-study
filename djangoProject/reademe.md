# django

## 创建步骤

1. django-admin startproject xxx
2. python manage.py runserver
3. python manage.py startapp polls

## 问题

当使用django-admin提示：

```bash
from distutils.version import LooseVersion
ModuleNotFoundError: No module named 'distutils'
```

可以尝试使用：

```bash
pip install setuptools # 因为setuptools是管理python软件包的工具包，它依赖于distutils
```
