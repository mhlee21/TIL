---
title: Django>CRUD with views
date: 2022-03-10 23:01:52
categories:
- Django
tags:
- Django
---

# HTTP method

## GET⭐

* 특정 리소스를 가져오도록 요청할 때 사용
* 반드시 데이터를 가져올 때만 사용해야 함
* DB에 변화를 주지 않음
* CRUD 에서 R 역할을 담당

## POST⭐

* 서버로 데이터를 전송할 때 사용
* 리소스를 생성/변경하기 위해 데이터를 HTTP body 에 담아 전송
* 서버에 변경사항을 만듦
* CRUD 에서 C/U/D 역할을 담당

## Cross-site request forgery (CSRF)

* 사이트간 요청 위조
* 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
* Django는 CSRF에 대항하여 middleware와 template tag 를 제공
* CSRF 라고도 함

### CSRF 공격 방어⭐

* Security Token 사용 방식 (CSRF Token)
  * 사용자의 데이터에 임의의 난수값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함
  * 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
* 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용 (GET 제외)
* Django는 CSRF token 템플릿 태그를 제공

### `csrf_token` template tag

* `{% csrf_token %}`⭐
* CSRF 보호에 사용
* input type 이 hidden 으로 작성되며, value 는 Django에서 생성한 hash 값으로 설정됨
* 해당 태그 없이 요청을 보낸다면 Django 서버는 403 forbidden 을 응답

> ⭐ method가 POST 일때 반드시 설정해야 한다.

### CSRF Middleware

![image-20220310231941366](image-20220310231941366.png)

* CSRF 공격 관련 보안 설정은 settings.py 에서 MIDDLEWARE에 작성 되어있음
* 실제로 요청 과정에서 urls.py 이전에 middleware의 설정 사항들을 순차적으로 거치며 응답은 반대로 하단에서 상단으로 미들웨어를 적용시킴

```text
💡 Middleware
- 공통 서비스 및 기능을 애플리케이션에 제공하는 소프트웨어
- 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 주로 미들웨어를 통해 처리
- 개발자들이 애플리케이션을 보다 효율적으로 구축할 수 있도록 지원하며, 애플리케이션, 데이터 및 사용자 사이를 연결하는 요소처럼 작동
```

# Django shortcut function

## `redirect()`⭐

* 새 URL 로 요청을 다시 보냄
* 인자에 따라 `HttpResponseRedirect` 를 반환
* 브라우저는 현재 경로에 따라 전제 URL 자체를 재구성(reconstruct)
* 사용가능한 인자
  * model
  * view name
  * absolute or relative URL
* `return redirect('articles:detail', article.id)`⭐⭐⭐



# CRUD 직접 작성해보기

* 프로젝트 이름 : crud

* 앱 이름 : articles

* 앱 등록 (crud/settings.py)

  ```python
  # Application definition
  
  INSTALLED_APPS = [
      'articles',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  

## base 템플릿 작성 및 추가 

* templates/base.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  
  <div class="container">
    {% block content %}
    
    {% endblock content %} 
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
```

* crud/settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
```

## READ

### 전체 게시글 조회

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```

* articles/views.py

```python
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

* templates/articles/index.html

```html
{% extends 'base.html' %}
{% block content %}
<h1 class="fw-bold">INDEX</h1>
<a href="{% url 'articles:new' %}" class="text-decoration-none">NEW</a>
<br>
<br>
{% for article in articles %}
  <h2>제목: {{ article.title }}</h2>
  내용 : {{ article.content }}
  <br>
  <a href="{% url 'articles:detail' article.id %}" class="text-decoration-none">DETAIL</a>
  <hr>
{% endfor %}
{% endblock content %}
```

```text
💡 게시글 정렬 순서 변경
1. DB로부터 받은 쿼리셋을 이후에 파이썬이 변경
articles = Article.objects.all()[::-1]
2. 처음부터 내림차순 쿼리셋으로 받음 (DB가 조작)
articles = Article.objects.order_by('-pk')
```

## CREATE

### new views

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]
```

* articles/views.py

```python
def new(request):
    return render(request, 'articles/new.html')
```

* templates/articles/new.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1 class="fw-bold">NEW</h1>
  <form action="{% url 'articles:create' %}" method="post">
    {% csrf_token %}
    <label for="title">TITLE: </label>
    <input type="text" name='title'>
    <br>
    <label for="content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <br>
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'articles:index' %}" class="text-decoration-none">BACK</a>
{% endblock content %}
```



### create views

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```

* articles/views.py

```python
def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.id)
```

* create 후 detail 페이지로 이동하도록 redirect

## DETAIL

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
]
```

* articles/views.py

```python
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

* templates/articles/detail.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1 class="fw-bold">DETAIL</h1>
  <hr>
  <h2>{{ article.title }}</h2>
  <div>{{ article.content }}</div>
  <br>
  <p>작성일 : {{ article.created_at }}</p>
  <p>수정일 : {{ article.updated_at }}</p>
  <div class="d-flex">
    <a href="{% url 'articles:edit' article.id %}" class="text-decoration-none align-self-center">EDIT</a>
    <form action="{% url 'articles:delete' article.id %}" method="post">
      {% csrf_token %}
      <button class="btn btn-link text-decoration-none">DELETE</button>
    </form>
  </div>
  <a href="{% url 'articles:index' %}" class="text-decoration-none">BACK</a>
{% endblock content %}
```



## EDIT

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>', views.edit, name='edit'),
]
```

* articles/views.py

```python
def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

```

* templates/articles/edit.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1 class="fw-bold">EDIT</h1>
  <form action="{% url 'articles:update' article.id %}" method="post">
    {% csrf_token %}
    <label for="title">TITLE: </label>
    <input type="text" name="title" value="{{ article.title }}">
    <br>
    <label for="content">CONTENT: </label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
    <br>
    <input type="submit" value="수정">
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```



## UPDATE

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('update/<int:article_id>', views.update, name='update'),
]
```

* articles/views.py

```python
def update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.id)
```

* CREATE 와 마찬가지로 별도의 '글이 수정되었습니다' 라는 메시지를 출력하는 template 는 필요하지 않음

## DELETE

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('update/<int:article_id>', views.update, name='update'),
    path('delete/<int:article_id>', views.delete, name='delete'),
]
```

* articles/views.py

```python
def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST': # HTTP method POST 시에만 삭제하도록 조건 작성
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.id)
```



# 정리

* Model
  * 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
  * ⭐ 필드, 옵션
* Database
  * 체계화 된 데이터의 모임 (집합)
* Migrations⭐
  * Django가 model 에 생긴 변화 (필드를 추가, 모델 삭제 등) 를 반영하는 방법
* ORM
  * OOP 언어를 사용하여 데이터베이스와 OOP 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
  * ⭐CRUD
* Database API
  * DB 를 조작하기 위한 도구 (QuerySet API, CRUD)
* Admin Site
  * 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
