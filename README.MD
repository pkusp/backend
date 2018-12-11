## Web后端

### 启动项目
- 创建项目
`django-admin startproject <project_name>`
- 创建app
`cd <project_name>`
`python manage.py startapp <app_name>`
- 启动服务器
`python manage.py runserver 0.0.0.0:8080`



### 问题解决记录
- [内网穿透（使内网服务器公网可访问）](https://github.com/Wisdom-Projects/holer)
Holer是一个将局域网中的应用映射到公网访问的端口映射软件，支持转发基于TCP协议的报文。
- [linux对外开放端口](http://www.cnblogs.com/blog-yuesheng521/p/7198829.html)
- [使Django外网可访问](https://blog.csdn.net/luojie140/article/details/76708797)
- [外网无法访问解决](https://www.cnblogs.com/sunjor/p/4887961.html)
- [django+ecs举例](https://blog.csdn.net/dieson1027/article/details/78750794)


### 设置

- 添加app
```python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
 	'app_name', # add app_name here
]

```

### 教程

- [自强学堂Django基础教程](https://code.ziqiangxuetang.com/django/django-cms-develop.html)


- 编写model.py
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
 
 
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 按照哪个栏目排序
 
 
@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
 
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
 
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
 
    published = models.BooleanField('正式发布', default=True)
 
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
```
- 创建数据库
```
(py36) root@sp:~/pku-ssm-2019/ecs-backend/crust# python manage.py makemigrations news
Migrations for 'news':
  news/migrations/0001_initial.py
    - Create model Article
    - Create model Column
    - Add field column to article
```
### 其他
- [Tomcat快速入门](https://www.cnblogs.com/jingmoxukong/p/8258837.html?utm_source=gold_browser_extension)

