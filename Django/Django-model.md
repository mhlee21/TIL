---
title: Django>model
date: 2022-03-08 09:04:47
categories:
- Django
tags:
- Django
---

# Model⭐

* 단일한 데이터에 대한 정보를 가짐
  * 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 저장된 데이터베이스의 구조 (layout)
* django는 model을 통해 데이터에 접속하고 관리
* 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

## Database

* 데이터베이스(DB)
  * 체계화된 데이터의 모임
* 쿼리 (Query)
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  * "Query를 날린다" -> DB를 조작한다.
* 데이터베이스 관리 시스템 종류
  * MySQL
  * ORACLE db
  * MariaDB
  * PostgreSQL

## Database의 기본 구조

* 스키마 (Shcema)
  * 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(structure)
  * 데이터데이스의 구조와 제약 조건(자료의 구조, 표현방법, 관계)에 관련한 전반적인 명세를 기술한 것
  * 관계 (1:N, N:N,...)
  
* 테이블(table)
  * 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합. SQL 데이터베이스에서는 테이블을 `관계`라고도 한다.
  * 열(column) : 필드(field) or 속성
    * 각 열에는 고유한 데이터 형식이 지정된다.
    * INTEGER, TEXT, NULL 등
  * 행(row) : 레코드(record) or 튜플
    * 테이블의 데이터는 행에 저장된다.

* PK (기본키)⭐
  * 각 행의 고유값으로 Primary Key로 불린다.
  * 반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용된다.
  * `django는 id가 곧 PK이다.`

![image-20220308123118143](image-20220308123118143.png)

## Model

* 웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구⭐

# ORM⭐

* Object-Relational-Mapping
* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간(Django-SQL)에 데이터를 변환하는 프로그래밍 기술
* OOP프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
* Django는 내장 Django ORM 을 사용함

![image-20220317233751117](image-20220317233751117.png)

## ORM의 장점과 단점⭐

* 장점
  * SQL을 잘 알지 못해도 DB 조작이 가능
  * SQL의 절차적 접근이 아닌 객체지향적 접근으로 인한 높은 생산성
* 단점
  * ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
* 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것 (***생산성***)
  * 개발 속도는 ORM을 쓰는 것이 더 빠르지만, 서비스의 속도는 SQL을 직접 사용하는 것이 더 빠르다.
  * 서비스 런칭 자체는 ORM을 사용하고 서비스를 운영하며 시간이 많이걸리는 부분을 SQL로 최적화 하는 방법을 많이 사용한다.
* 왜 ORM 을 사용할까?
  * **DB를 객체로 조작하기 위해 ORM을 사용한다.**

## model.py 작성

```python
# articles/models.py
class Article(models.Model):
    title = models.CharField(max_length=10) # 길이제한 있는 경우 CharField 사용
    content = models.TextField() # 길이제한 없는 경우 TextField 사용
```

* 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현
  
  * django.db.models.Model 모듈의 Model 클래스를 상속받음
  
* models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의

  * title과 content는 모델의 필드를 나타냄

  * 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

> Model 명 정할땐 단수형으로 생성한다. Django에서 자동으로 복수형을 붙여서 관리해주기 때문이다.

## 사용 모델 필드⭐

* `CharField(max_length=None, **options)`

  * 길이의 제한이 있는 문자열을 넣을 때 사용

  * CharField의 max_length는 필수 인자

  * **필드의 최대 길이(문자)**, 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용

* `TextField(**options)`
  * 글자의 수가 많을 때 사용
  * max_length 옵션 작성 시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음
    * max_length 사용은 CharField에서 사용해야 함

# Migrations⭐⭐⭐

* django가 model에 생긴 변화를 DB에 반영하는 방법

## commands⭐⭐

* 마이그레이션 실행 및 DB 스키마를 다루기 위한 몇가지 명령어 (`python manage.py [command]`)

  * `makemigrations`

    * model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용
    * 'migrations/0001_initial.py' 생성 확인

  * `migrate`

    * 마이그레이션을 DB에 반영하기 위해 사용
    * 설계도를 실제 DB에 반영하는 과정
    * 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
    * 0001_initial.py 설계도를 실제 DB에 반영

  * `sqlmigrate`

    * `python manage.py sqlmigrate app_name 0001`⭐
    * 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    * 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어 동작할 지 미리 확인할 수 있음

  * `showmigrations`

    * 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    * migrations 설계도들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

    

## 추가 모델 필드 작성

### 실습

```python
# articles/models.py

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    # auto_now_add 데이터가 생성될 때 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) 
    # auto_now 현재 시간을 자동으로 저장

## 참고 ## 
# 다른 필드들에 대해서 default 값을 설정하는 대신
# 필드열을 비워두는 것을 허용한다는 의미로 다음과 같이 설정가능하다.
# age = models.IntegerField(null=True)
# null=True : (NULL)
# blank=True : ('')
```

모델에서 필드정보 수정되면 makemigrations 진행

```bash
$ python manage.py makemigrations
You are trying to add the field 'created_at' with 'auto_now_add=True' to student without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option:
```

테이블을 만들 때 created_at 필드에 대한 default 값이 없어서 선택하도록 bash에 출력됨⭐⭐

* 1 : django에서 지금 바로 기본값을 설정해줌
* 2 : makemigrations 종료하고 py파일에서 직접 default 값 설정함



### DataField's options⭐⭐⭐

* `auto_now_add`
  * 최초 생성 일자
  * Django ORM 이 최초 insert (테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
    (테이블에 어떤 값을 최초로 넣을 때)
* `auto_now`
  * 최종 수정 일자
  * Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신
* DateTimeField가 아닌 DataField의 options를 확인한 이유
  * DataTimeField는 DateField와 동일한 추가 인자(extra argument)를 사용함
  * DataTimeField는 DateField의 서브 클래스

## 반드시 기억해야 할 migration 3단계

1. `models.py`

   model 변경사항 발생 시

2. `$ python manage.py makemigrations`

   migrations 파일 생성

3. `$ python manage.py migrate`

   DB 반영(모델과 DB의 동기화)

# Database API

* "DB를 조작하기 위한 도구"
* Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
* Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
* database-abstract API 혹은 database-access API라고도 함
* [QuerySet API reference](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

## Making Queries

>  [클래스명].objects.[메서드]

![image-20220308134706955](image-20220308134706955.png)

## DB API

* Manager
  * Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  * 기본적으로 모든 Django 모델 클래스에 objects 라는 Manager 를 추가
* QuerySet
  * 데이터베이스로부터 전달받은 객체 목록
  * queryset 안에 객체는 0개, 1개 혹은 여러 개일 수 있음
  * 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음

## Django shell

* 일반 python shell 을 통해서는 장고 프로젝트 환경에 접근할 수 없음
* 그래서 장고 프로젝트 설정이 load된 python shell 을 활용해 DB API 구문 테스트 진행
* 기본 Django shell보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행

1. 라이브러리 설치

   ```bash
   $ pip install ipython
   $ pip install django-extensions
   ```

2. 라이브러리 등록 및 실행

   ```python
   # settings.py
   INSTALLED_APPS = [
     ...,
     'django_extensions',
     ...,
   ]
   ```

   ```bash
   $ python manage.py shell_plus
   ```

# CRUD⭐

* 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 `Create, Read, Update, Delete` 를 묶어서 일컫는 말 

## CREATE⭐

```Python
# 방법 1. 인스턴스 생성 후 인스턴스 변수 설정
>>> article = Article()
>>> article.title = 'first'
>>> article.django = 'django!'
>>> article.save()

# 방법 2. 초기 값과 함께 인스턴스 생성
>>> article = Article(title='first', content='django!')
>>> article.save()

# 방법 3. QuerySet API - create() 사용
# 위 2개 방식과는 다르게 바로 DB 에 저장되며 쿼리 표현식을 리턴한다.
>>> Article.objects.create(title='first', content='django!')
```

1. 인스턴스를 생성 후 인스턴스 변수 설정
2. 초기 값과 함께 인스턴스 생성
3. QuerySet API - create() 사용

### `save()`  method

* Saving objects
* 객체를 데이터베이스에 저장함
* 데이터 생성 시 save() 를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
  * ID 값은 Django 가 아니라 DB에서 계산되기 때문
* **단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save() 가 필요**
* `__str__` : print 호출 시 출력되는 문자열, 작성 후 반드시 shell_plus 를 재시작해야 반영된다.



## READ

```python
# DB에 인스턴스 객체를 얻기 위한 쿼리문 날리기
# 이때, 레코드가 하나만 있으면 인스턴스 객체고, 두개 이상이면 쿼리셋으로 리턴
>>> Ariticle.objects.all()
<QuerySet []>
```

### `all()`

* **현재 QuerySet의 복사본을 반환**

### `get()`

* 주어진 lookup 매개변수와 일치하는 **객체를 반환**
* 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고,  둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴
* 위와 같은 특징을 가지고 있기 때문에 **primary key 와 같이 고유(unique)성을 보장하는 조회에서 사용**해야 함

```python
from django.shortcuts import render, get_object_or_404
stu = get_object_or_404(Student, pk=1)
```

### `filter()`

* 주어진 lookup 매개변수와 일치하는 객체를 포함하는 **새 QuerySet을 반환**

> ⭐ 각각의 리턴받는 값 헷갈리지 않도록 주의



## UPDATE⭐

```python
>>> article = Article.objects.get(pk=1)
>>> article.title
'first'

>>> article.title = 'byebye'
>>> article.save()

>>> article.title
'byebye'
```

1. DB에서 수정할 data를 가져온다.
2. 가져온 데이터의 값을 변경한다.
3. save 한다.



## DELETE

```python
>>> article = Article.objects.get(pk=1)
>>> article.delete()
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```

### `delete()`

* QuerySet 의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환



## Field lookups

* 조회 시 특정 검색 조건을 지정
* QuerySet 메서드 filter(), exclude() 및 get() 에 대한 키워드 인수로 지정됨

```python
Article.objects.filter(pk__gt=2)
Article.objects.filter(content__contains='ja')
```



>💡 데이터 베이스 조작을 위한 다양한 QuerySet API methods 는 해당 공식문서를 반드시 참고하여 학습할 것
>
>https://docs.djangoproject.com/en/3.2/ref/models/querysets/#

# Admin Site

## Automatic admin interface

* 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
* Model class 를 admin.py 에 등록하고 관리
* django.contrib.auth 모듈에서 제공됨
* record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음

## admin 생성⭐

```bash
$ python manage.py createsuperuser
```

* 관리자 계성 생성 후 서버를 실행한 다음 '/admin' 으로 가서 관리자 페이지 로그인
  * 계정만 만든 경우 Django 관리자 화면에서 아무것도 보이지 않음
* 내가 만든 Model 을 보기 위해서는 admin.py 에 작성하여 Django 서버에 등록
* ❗️auth에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 없음

## admin 등록

```python
# article/admin.py
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

# ⭐ admin site에 register 하겠다.
admin.site.register(Article)
```

* admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것
* models.py에 정의한 `__str__` 의 형태로 객체가 표현됨

* `list_display` : models.py 정의한 각각의 속성(칼럼)들의 값(레코드)을 admin 페이지에 출력하도록 설정
