---
title: Django>Form
toc: true
date: 2022-04-06 08:36:27
categories:
- Django
tags:
- Django
---

# Django Form Class

* 우리는 지금까지 HTML form, input 을 통해서 사용자로부터 데이터를 받았다.

* 이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시한다.
  * 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 한다.
* 유효성 검증 : 사용자가 입력한 데이터를 검증하는 것
  * 이 과정을 코드로 모두 구현하는 것은 많은 노력이 필요한 작업이다.
* "Django Form"은 이러한 과중한 작업과 반복 코드를 줄여줌으로써 이 작업을 훨씬 쉽게 만들어준다.



## Django's forms

* Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

* Django는 Form 과 관련된 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하여 개발자로 하여금 직접 작정하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게함

* Django 는 form에 관련된 작업의 아래 세 부분을 처리해줌

  1. 렌더링을 위한 데이터 준비 및 재구성

  2. 데이터에 대한 HTML forms 생성

  3. 클라이언트로부터 받은 데이터 수신 및 처리

## The Django 'Form Class'

* Django Form 관리 시스템의 핵심
* Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field에 관련된 에러 메세지를 결정
* Django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요 시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여줌

### Form 선언하기

* Model을 선언하는 것과 유사하며 같은 필드타입을 사용 (또한, 일부 매개변수도 유사하다)
* forms 라이브러리에서 파생된 Form 클래스를 상속받음

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
  title = form.CharField(max_length=10)
  content = forms.CharFields()
```

### Form 사용하기

```python
# articles/views.py
from .forms import ArticleForm

def new(request):
  	form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- new.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

### Form rendering options

`<label> `& `<input> `쌍에 대한 3가지 출력 옵션

1. as_p()
   * 각 필드가 단락(`<P>`)으로 감싸져서 렌더링 됨
2. as_ul()
   * 각 필드가 목록(`<li>`)으로 감싸져서 렌더링 됨
   * `<ul>`태그는 직접 작성해야 함
3. as_table()
   * 각 필드가 테이블(`<tr>`)행으로 감싸져서 렌더링 됨
   * `<table>`태그는 직접 작성해야 함

## Django의 HTML input 요소 표현 방법 2가지

1. Form fields

   * input 에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용 됨

2. Widgets

   * 웹 페이지의 HTML input 요소 렌더링
   * GET/POST 딕셔너리에서 데이터 추출

   * ⭐️Widgets 은 반드시 Form fields에 할당된다.

   > ❗️Form Fields 와 혼동되어서는 안됨
   >
   > ❗️Form Fields 는 input 유효성 검사를 처리
   >
   > ❗️Widgets 은 웹페이지에서 input element의 단순 raw한 렌더링 처리

   ```python
   # articles/forms.py
   from django import forms
   
   class ArticleForm(forms.Form):
       REGION_A = 'sl'
       REGION_B = 'dj'
       REGION_C = 'gj'
       REGION_CHOICES = [
           (REGION_A,'서울'),
           (REGION_B,'대전'),
           (REGION_C,'광주'),
       ]
       title = forms.CharField(max_length=10)
       content = forms.CharField(widget=forms.Textarea)
       region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())
   ```

   

---

# ModelForm

* Django Form 을 사용하다 보면 Model에 정의한 필드를 유저로부터 입력받기 위해 Form 에서 Model 필드를 재정의하는 행위가 중복될 수 있음
* 그래서 Django는 **Model을 통해 Form Class 를 만들 수 있는 ModelForm 이라는 Helper** 를 제공

## ModelForm Class

* Model을 통해 Form Class를 만들 수 있는 Helper
* 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view 에서 사용 가능

### ModelForm 선언하기

* forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
* 정의한 클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 Form 을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
  * ❗️ 클래스 변수 `fields`와  `exclude` 는 동시에 사용할 수 없음

```python
# articles/forms.py
from django import forms
from .django import Article

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'
    # exclude = ('title',)
```

* Meta class
  * Model의 정보를 작성하는 곳
  * ModelForm을 사용할 경우 사용할 모델이 있어야 하는데 Meta Class가 이를 구성함
    * 해당 Model에 정의한 field 정보를 Form에 적용하기 위함

### ModelFrom 사용하기

```python
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

* **`is_valid()` method**

  * 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

  * 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공

> [참고] 유효성 검사?
>
> - 요청한 데이터가 특정 조건에 충족하는지 확인하는 작업
> - 데이터베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나 저장되지 않도록 하는 것

* **`save()` method**
  * Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장
  * ModelForm 의 하위 클래스는 기존 모델 인스턴스를 키워드 인자 **instance** 로 받아들일 수 있음
    * Instance 제공되면 save() 해당 인스턴스를 수정 (UPDATE)
    * 제공되지 않는 경우 지정된 모델의 새 인스턴스를 만듦 (CREATE)
  * Form 의 유효성이 확인되지 않은 경우, save()를 호출하면 form.errors를 확인하려 에러 확인 가능

```python
def update(request, pk):
    if request.method == 'POST':
        # update
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # edit
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

## Form과 ModelForm 비교

* Form
  * 어떤 Model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
  * Cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 함
  * Model에 연관되지 않은 데이터를 받을 때 사용
* ModelForm
  * Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
  * 어떤 레코드를 만들어야 할 지 알고있으므로 바로 .save() 호출 가능

> Form : 사용자로부터 입력받지만 서버에 저장할 필요 없는 경우 (ex. Login, password 변경)
>
> ModelForm : 사용자로부터 입력받아 서버에 저장하는 경우

### forms.py 파일 위치

Form class는 forms.py 뿐 아니라 다른 어느 위치에 두어도 상관 없지만, 일반적으로 `app/forms.py` 에 작성

### 모델폼이 쉽게 해주는 것 💡

1. 모델 필드 속성에 맞는 html element를 만들어주고
2. 이를 통해 받은 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함

## widgets 활용하기

* 첫번째 방식

  ```python
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = '__all__'
          widgets = {
            'title': forms.TextInput(attrs={
              'class': 'my-title',
              'placeholder': 'Enter the title',
              'maxlength': 10,
            	}
          	)
          }
  ```

* 두번째 방식 (권장)

  ```python
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title form-control',
                  'placeholder': 'Enter the title',
              }
          )
      )
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content form-control',
              }
          ),
          error_messages={
              'required': 'Please enter your content!!!'
          }
      )
      class Meta:
          model = Article
          fields = '__all__'
  ```

  

# Rendering fields manually

## bootstrap 과 함께 사용하기

1. Bootstrap class with widgets

   * Bootstrap Form의 핵심 class(form-control) 를 widget에 작성

   ```python
   class ArticleForm(forms.ModelForm):
       title = forms.CharField(
           widget=forms.TextInput(
               attrs={
                   'class': 'my-title form-control',
                   'placeholder': 'Enter the title',
               }
           )
       )
       class Meta:
           model = Article
           fields = '__all__'
   ```

2. Django Bootstrap 5 Library

   * Django-bootstrap v5 : form class 에 bootstrap 을 적용시켜주는 라이브러리
   * https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html

​	

# 정리

![image-20220406165627393](image-20220406165627393.png)

ModelForm을 사용할 때 렌더링되는 input element 속성은 Django에서 제공해주는 것 이외에도 widget을 사용할 수 있다.

ModelFrom을 사용할 때 Meta 클래스 내부에 model과 fields/exclude 변수는 반드시 작성해야 한다.
