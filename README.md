# 个人主页 - Django 项目

这是一个基于 Django 的个人主页网站，包含简历展示、项目展示和博客功能。

## 功能特性

- 个人简介展示
- 工作经历展示
- 教育经历展示
- 项目展示
- 博客文章
- 响应式设计
- 打印友好的简历页面

## 本地运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 创建超级用户（用于管理后台）

```bash
python manage.py createsuperuser
```

### 4. 运行开发服务器

```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000/ 查看网站

## 管理后台

访问 http://127.0.0.1:8000/admin/ 登录管理后台，可以添加：
- 个人信息（Profile）
- 工作经历（Experience）
- 教育经历（Education）
- 项目展示（Project）
- 博客文章（BlogPost）

## 部署到 Render

### 1. 推送代码到 GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. 在 Render 上创建新项目

1. 访问 https://dashboard.render.com/
2. 点击 "New +" → "Web Service"
3. 连接你的 GitHub 仓库
4. 配置：
   - **Name**: 你的项目名称
   - **Region**: Singapore（推荐亚洲用户）
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn mysite.wsgi:application`

### 3. 配置环境变量

在 Render 的环境变量中添加：
- `DJANGO_SECRET_KEY`: 生成一个随机密钥
- `DEBUG`: `False`

### 4. 配置自定义域名

1. 在阿里云域名管理中，添加 DNS 记录：
   - **类型**: CNAME
   - **主机记录**: @
   - **记录值**: 你的 Render 应用的域名（如：your-app.onrender.com）

2. 在 Render 的设置中添加自定义域名

### 5. 配置 HTTPS

Render 会自动为自定义域名配置 HTTPS 证书。

## 项目结构

```
mysite/
├── home/                    # 主应用
│   ├── migrations/         # 数据库迁移文件
│   ├── templates/          # 模板文件
│   │   └── home/          # HTML 模板
│   ├── admin.py           # 管理后台配置
│   ├── apps.py            # 应用配置
│   ├── models.py          # 数据模型
│   ├── urls.py            # URL 路由
│   └── views.py           # 视图函数
├── mysite/                 # 项目配置
│   ├── settings.py        # Django 设置
│   ├── urls.py            # 项目 URL 路由
│   └── wsgi.py            # WSGI 配置
├── staticfiles/           # 静态文件（部署后生成）
├── .gitignore            # Git 忽略文件
├── Procfile              # Render 部署配置
├── requirements.txt      # Python 依赖
└── runtime.txt           # Python 版本
```

## 许可证

MIT License