from django.db import models


class Profile(models.Model):
    """个人信息模型"""
    name = models.CharField(max_length=100, verbose_name="姓名")
    title = models.CharField(max_length=100, verbose_name="职位/头衔")
    bio = models.TextField(verbose_name="个人简介")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length=20, blank=True, verbose_name="电话")
    location = models.CharField(max_length=100, blank=True, verbose_name="所在地")
    github_url = models.URLField(blank=True, verbose_name="GitHub链接")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn链接")
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name="头像")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Project(models.Model):
    """项目展示模型"""
    title = models.CharField(max_length=200, verbose_name="项目名称")
    description = models.TextField(verbose_name="项目描述")
    image = models.ImageField(upload_to='projects/', blank=True, verbose_name="项目图片")
    github_url = models.URLField(blank=True, verbose_name="GitHub链接")
    live_url = models.URLField(blank=True, verbose_name="在线演示链接")
    technologies = models.CharField(max_length=200, verbose_name="使用技术", help_text="用逗号分隔")
    is_featured = models.BooleanField(default=False, verbose_name="是否推荐")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "项目展示"
        verbose_name_plural = verbose_name
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """博客文章模型"""
    title = models.CharField(max_length=200, verbose_name="文章标题")
    slug = models.SlugField(unique=True, verbose_name="URL别名")
    content = models.TextField(verbose_name="文章内容")
    excerpt = models.TextField(max_length=300, blank=True, verbose_name="摘要")
    cover_image = models.ImageField(upload_to='blog/', blank=True, verbose_name="封面图片")
    is_published = models.BooleanField(default=True, verbose_name="是否发布")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    """工作经历模型"""
    company = models.CharField(max_length=200, verbose_name="公司名称")
    position = models.CharField(max_length=100, verbose_name="职位")
    description = models.TextField(verbose_name="工作描述")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(null=True, blank=True, verbose_name="结束日期")
    is_current = models.BooleanField(default=False, verbose_name="是否当前职位")
    technologies = models.CharField(max_length=200, blank=True, verbose_name="使用技术", help_text="用逗号分隔")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "工作经历"
        verbose_name_plural = verbose_name
        ordering = ['-is_current', '-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    """教育经历模型"""
    school = models.CharField(max_length=200, verbose_name="学校名称")
    degree = models.CharField(max_length=100, verbose_name="学位")
    major = models.CharField(max_length=100, verbose_name="专业")
    description = models.TextField(blank=True, verbose_name="描述")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(null=True, blank=True, verbose_name="结束日期")
    gpa = models.CharField(max_length=10, blank=True, verbose_name="GPA")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "教育经历"
        verbose_name_plural = verbose_name
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} - {self.school}"
