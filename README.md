＃ CMDB
### 需要对templates目录之下的四个文件进行修改
- 页面介绍
 - home.html   主页面
 - department.html 展示部门的页面
 - website.html 展示所有域名页面
 - department_website.html 展示部门网站

### 静态文件配置
- 在根目录下创建static文件夹
- 打开一开始下载解压后的文件,找到dist文件夹,将里面的的3个文件夹css,fonts,js进行复制
    在untitled/static/下新建文件夹bootstrap,将刚才复制的3个文件夹复制到里面,

    从一开始下载的bootstrap的解压文件找到docs/examples里面选择一个本次测试的模板,本次我们选择docs/examples/blog/下的index.html,复制粘贴到mydjango/testdj/templates/下,然后改名为base.html,然后用编辑器打开

    找到
    (<link href="../../dist/css/bootstrap.min.css" rel="stylesheet">)
    改为
    (<link href="/static/bootstap/css/bootstrap.css" rel="stylesheet">)

    找到
    (<link href="blog.css" rel="stylesheet">)
    改为
    (<link href="/static/bootstrap/css/blog.css" rel="stylesheet">)

    找到
    (<script src="../../dist/js/bootstrap.min.js"></script>)
    改为 (<script src="/static/bootstrap/js/bootstrap.js"></script>)

    我们更改成了自己的路径,可以更好的适应我们的项目结构
    
### 项目运行
- 安装mysql 命令 pip install mysqlclient一下
- 创建名叫domain的库
- 更改数据库配置 在settings.py中DATABASES选项里更改password和port  （默认为123555 开放3306端口）
- 进入项目 python manage.py migrate 一下
- python mannage.py runserver启动服务

### urls
- http://127.0.0.1:8000/home/  ->  主页面
- http://127.0.0.1:8000/website/  ->  展示所有域名页面
- http://127.0.0.1:8000/department/  ->  展示所有部门页面
- http://127.0.0.1:8000/depart_web/  ->  部门下域名页面
