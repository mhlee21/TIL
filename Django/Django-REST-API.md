---
title: Django>REST API
toc: true
date: 2022-04-20 12:53:16
categories:
- Django
tags:
- Django
- REST API
---

# HTTP

* HyperText Transfer Protocol
* 웹 상에서 컨텐츠를 전송하기 위한 약속
* HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
* 웹에서 이루어지는 모든 데이터 교환의 기초
  * 요청 (request) : 클라이언트에 의해 전송되는 메세지
  * 응답 (response) : 서버에서 응답으로 전송되는 메시지
* 기본 특성 : 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함
  * Stateless
  * Connectionless
* HTTP request methods
  * 자원에 대한 행위를 정의
  * 주어진 리소스에 수행하길 원하는 행동을 나타냄
  * GET, POST, PUT, DELETE...

> PATCH
>
> * 리소스의 부분적인 수정을 할 때에 사용된다.
>
> * 멱등성을 가지지 않는다.
>
> 비밀번호 수정의 경우 PUT 메소드를 사용한다.

![image-20220420232423748](image-20220420232423748.png)

* HTTP response status codes

  * 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  * 응답은 5개의 그룹으로 나뉘어짐

  <img src="image-20220420232935302.png" alt="image-20220420232935302" style="zoom:50%;" />

### 웹에서의 리소스 식별

* HTTP 요청의 대상을 리소스(resource, 자원) 라고 함
* 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
* 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는 URI(Uniform Resource Identifier)로 식별됨

### URL

* Uniform Resource Locator
* 통합 자원 위치
* 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
* '웹 주소', '링크' 라고도 불림

### URN

* Uniform Resource Name
* 통합 자원 이름
* URL 과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함

## URI

* Uniform Resource Identifier
* 통합 자원 식별자
* 인터넷의 자원을 식별하는 유일한 주소(정보의 자원을 표현)
* 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
* 하위 개념 : URL, URN
* URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함

### URI의 구조

* Scheme (protocol)

  * 브라우저가 사용해야 하는 프로토콜

  ![image-20220420233803134](image-20220420233803134.png)

* Host (Domain name)

  * 요청을 받는 웹 서버의 이름
  * IP address 를 직접 사용할 수 있지만, 실 사용시 불편하므로 웹에서 자주 사용되지는 않음

  ![image-20220420233821150](image-20220420233821150.png)

* Port

  * HTTP : 80
  * HTTPS : 443

  ![image-20220420233832116](image-20220420233832116.png)

* Path

  * 웹 서버상의 리소스 경로
  * 초기에는 실제 파일이 위치한 물리적인 위치를 나타냈지만, 오늘날은 물리적인 실제 위치가 아닌 추상화 형태의 구조로 표현

  ![image-20220420233843096](image-20220420233843096.png)

* Query(Identifier)

  * Query String Parameters
  * 웹 서버에 제공되는 추가적인 매개변수
  * & 로 구분되는 key-value 목록

  ![image-20220420233854375](image-20220420233854375.png)

* Fragment

  * Anchor
  * 자원 안에서 북마크의 한 종류를 나타냄
  * 브라우저에게 해당 문서의 특정 부분을 보여주기 위한 방법
  * `#` 뒤의 부분은 요청이 서버에 보내지지 않음

  ![image-20220420233905850](image-20220420233905850.png)

# RESTful API

## API

* Application Programming Interface
* 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  * 애플리케이션과 프로그래밍으로 소통하는 방법
  * CLI는 명령줄, GUI는 그래픽, API는 프로그래밍을 통해 특정한 기능 수행

* Web API
  * 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  * 현재 웹 개발은 모든 것을 직접 개발하기 보다 여러 OpenAPI를 활용하는 추세
* 응답 데이터 타입
  * HTML, XML, JSON 등

## REST

* **RE**presentational **S**tate **T**ransfer
* API server를 개발하기 위한 일종의 *소프트웨어 설계 방법론*
* 네트워크 구조(Network Architecture) 원리의 모음
  * 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
* RESTful : REST 원리를 따르는 시스템
* 자원을 정의하는 방법에 대한 고민 : 정의된 자원을 어디에 위치 시킬 것인가

### REST의 자원과 주소의 지정 방법

1. 자원 : URI
2. 행위 : HTTP Method
3. 표현
   - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
   - JSON으로 표현된 데이터를 제공

### JSON

* JSON (JavaScript Object Notaion)
  * JSON is a lightweight data-interchange format
  * JavaScript 의 표기법을 따른 단순 문자열
* 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
* 파이썬의 dictionary, 자바스크립트의 object 처럼 C계열의 언어가 갖고있는 자료구조로 쉽게 변화할 수 있는 key-value 형태의 구조를 갖고 있음

### REST

* REST의 핵심 규칙
  1. '정보'는 URI로 표현
  2. 자원에 대한 '행위'는 HTTP method로 표현 (GET, POST, PUT, DELETE)
* 설계 방법론은 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음
  * 단, 설계 방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지는 않음

### RESTful API

* REST 원리를 따라 설계한 API
* RESTful services, 혹은 simply REST services 라고도 부름
* 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성
  * 지금까지 사용자의 입장에서 썼던 API를 제공자의 입장이 되어 개발해보기

# Response

### Create Dummy Data

* Django-seed 라이브러리를 사용해 모델구조에 맞는 데이터 생성

```bash
python manage.py migrate
python manage.py seed articles --number=20
```

## 1. HTML

```python
# views.py
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```



## 2. JsonResponse

* JsonResponse 객체를 활용한 JSON 데이터 응답

```python
# views.py
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)
```

* **JsonResponse** objects

  * JSON-encoded response 를 만드는 HttpResponse의 서브 클래스

  * "safe" parameter

    * True (기본값)
    * dict 이외의 객체를 직렬화(Serialization) 하려면 False로 설정해야 함

    ```python
    response = JsonResponse({'foo': 'bar'})
    response = JsonResponse([1,2,3], safe=False)
    ```

### 🔍 Serialization 

* 직렬화
* 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
* Serializers in Django
  * Queryset 및 Model Instance 와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌

## 3. Django Serializer

* Django의 내장 HttpResponse를 활용한 JSON 응답
* 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요 없음

```python
# views.py
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```



## 4. Django REST Framework

* Django REST Framework(DFR) 라이브러리를 사용한 JSON 응답

```bash
pip install djangorestframework
```

``` python
INSTALLED_APPS = [
		...
    'rest_framework',
]
```

* Article 모델에 맞춰 자동으로 필드를 생성해 serialize 해주는 ModelSerializer 확인

```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

* DRF 의 Response() 를 활용해 Serialize 된 JSON 객체 응답

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```



## Django REST Framework (DRF)

* Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리

* DRF 의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

* Web API

  * 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

* Django ModelForm vs. DRF Serializer

  ![image-20220420152255984](image-20220420152255984.png)



# Single Model

## DRF with Single Model

* 단일 모델 data를 직렬화(Serialization)하여 JSON으로 변환하는 방법에 대한 학습
* 단일 모델을 두고 CRUD 로직을 수행 가능하도록 설계
* API 개발을 위한 핵심 기능을 제공하는 도구 활용
  * DRF built-in form
  * Postman

## ModelSerializer

* 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
* 아래 핵심 기능을 제공
  1. 모델 정보에 맞춰 자동으로 필드 생성
  2. Serializer 에 대한 유효성 검사기를 자동으로 생성
  3. `.create()` & `.update()` 의 간단한 기본 구현이 포함됨

* Model 필드를 어떻게 '직렬화' 할 지 설정하는 것이 핵심
* 이 과정은 Django 에서 Model 의 필드를 설정하는 것과 동일함

```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArtlcleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)
```

### `'many'` argument

* `many=True`
  * Serializing multiple objects
  * 단일 인스턴스 대신 QuerySet 등을 직렬화 하기 위해서는 serializer를 인스턴스화 할 때 `many=True`를 키워드 인자로 전달해야 한다.

```python
>>> article = Article.objects.all()
>>> serializer = ArticleListSerializer(article)
>>> serializer.data
...
AttributeError: Got AttributeError when attempting to get a value for field `title` on serializer `ArticleListSerializer`.
The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
Original exception text was: 'QuerySet' object has no attribute 'title'.
>>> serializer = ArticleListSerializer(articles, many=True)
>>> serializer.data
[OrderedDict([('id', 1), ('title', 'Agree learn two position threat hope these speak.')]), OrderedDict([('id', 2), ('title', 'Brother per six source full which west training.')]), OrderedDict([('id', 3), ('title', 'Evidence tend learn door issue.')]), OrderedDict([('id', 4), ('title', 'Body option standard manager key best across.')]), OrderedDict([('id', 5), ('title', 'Determine food concern prevent wind report play person.')]), OrderedDict([('id', 6),
...
)]
>>> 
```

## Build RESTful API

![image-20220421133400608](image-20220421133400608.png)

### GET

```python
from rest_framework.decorators import api_view

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all() 
    # DB가 비어있는 경우 404 리턴보다 빈 리스트를 보여주기 위해 get_list_or_404 대신 all 사용
    # articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

* `api_view` decorator
  * 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
  * View 함수가 응답해야 하는 HTTP 메서드의 목록을 리스트의 인자로 받음
  * DRF에서는 선택이 아닌 ***필수적으로 작성***해야 해당 view 함수가 정상적으로 동작함

```python
# articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

* Article List와 Article Detail 을 구분하기 위해 추가 Serailizer 정의
* 모든 필드를 직렬화하기 위해 fields 옵션을 `__all__` 로 설정

```python
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```



### POST

* 201 Created 상태코드 및 메시지 응답
* RESTful 구조에 맞게 작성
  1. URI는 자원을 표현
  2. 자원을 조작하는 행위는 HTTP Method
* article_list 함수로 게시글을 조회하거나 생성하는 행위를 모두 처리 가능

```python
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

* Status Codes in DRF
  * DRF에는 status code 를 보다 명확하고 읽기 쉽게 만드는데 사용할 수 있는 정의된 상수 집합을 제공
  * status 모듈에 HTTP status code 집합이 모두 포함되어 있음
* `raise_exception` argument
  * Raising an exception on invalid data
    * `is_valid()` 는 유효성 검사 오류가 있는 경우 serializers.ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
    * DRF 에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP status code 400을 응답으로 반환함

### DELETE

```python
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```

* 204 No Content 상태 코드 및 메시지 응답
* Article_detail 함수로 상세 게시글을 조회하거나 삭제하는 행위 모두 처리 가능

### PUT

```python
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    ...
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```



# 1:N Relation

* 1:N 관계에서의 모델 data를 직렬화(serialization) 하여 JSON으로 변화하는 방법에 대한 학습
* 2개 이상의 1:N 관계를 맻는 모델을 두고 CRUD 로직을 수행 가능하도록 설계하기

### GET

* Comment model 추가
* Single model 과 동일

### POST

* Article 생성과 달리 Comment 생성은 생성 시에 참조하는 모델의 객체 정보가 필요

* 1:N 관계에서 N은 어떤 1을 참조하는지에 대한 정보가 필요하기 때문(외래키)

* `.save()` method

  * 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
  * 인스턴스를 저장하는 시점에 추가 데이터 삽입이 필요한 경우

  ![image-20220421230724584](image-20220421230724584.png)

* `read_only_fields`

  * 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 직렬화하는 과정에서 article 필드가 유효성 검사(is_valid) 를 통과하지 못함
  * 이때, 읽기 전용 필드 설정을 통해 직렬화하지 않고 반환값에만 해당 필드가 포함되도록 설정할 수 있음

  ![image-20220421230926993](image-20220421230926993.png)



### DELETE & PUT

Single model 과 동일





