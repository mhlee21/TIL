# Swagger 란?

Swagger(스웨거)는 개발자가 REST API 서비스를 설계, 빌드, 문서화할 수 있도록 하는 프로젝트이다.Swagger는 다음과 같은 경우에 유용하게 사용된다.

-   다른 개발팀과 협업을 진행할 경우
-   이미 구축되어있는 프로젝트에 대한 유지보수를 진행할 경우
-   백엔드의 API를 호출하는 프론트엔드 프로그램을 제작할 경우

# Springfox vs Springdoc

[Swagger 란 ? (이론 + Spring boot 적용)](https://velog.io/@soyeon207/%EC%9A%B0%EB%8B%B9%ED%83%95%ED%83%95-Swagger-%EC%A0%81%EC%9A%A9%EA%B8%B0)

두개 모두 Swagger 를 사용하되 API 문서를 쉽게 쓸 수 있도록 해주는 라이브러리다.

Springfox-Swagger 가 선발 주자, Springdoc 가 후발주자 이다.

Springfox-Swagger 는 2018년 까지 많은 사람들이 사용하다가 2018년 6월을 마지막으로 업데이트가 중지되었고 그 사이인 2019년 7월에 springdoc 가 나와서 많은 사람들이 springdoc 를 많이 사용하기 시작한다. 그러던 중 2020년 6월에 Springfox 가 신 버전을 내놓아서 현재는 두개를 혼용해서 사용하고 있다.

springdoc 이 공식문서 읽기가 더 편하고, API 별 그룹핑이 더 편리하다고 한다.

[Spring boot Swagger 3.0 적용하기](https://dev-youngjun.tistory.com/258)

# Springdoc 적용하기

[OpenAPI 3 Library for spring-boot](https://springdoc.org/)

[OpenAPI 3.0을 이용한 Spring REST API 문서화](https://webgori.github.io/spring/2020/02/09/OpenAPI-3.0%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-Spring-REST-API-%EB%AC%B8%EC%84%9C%ED%99%94.html)

## build.gradle dependencies 설정

```java
// springdoc 설정
implementation group: 'org.springdoc', name: 'springdoc-openapi-ui', version: '1.6.11'
```

## application.yml 설정

```java
springdoc:
  api-docs:
    groups:
      enabled: true
  swagger-ui:
    path: /swagger-ui.html
    displayRequestDuration: true
    groups-order: DESC
```

## SwaggerConfig.java

```java
//com/d210/alphagom/config/SwaggerConfig.java

package com.d210.alphagom.api;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;

@RestController
@RequestMapping("/api/v1/test")
public class TestController {
    @GetMapping("/")
    private ResponseEntity test() {
        return ResponseEntity.ok().body(LocalDate.now());
    }
}
```

## swagger 페이지

[http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)

![[Pasted image 20220831232221.png]]

---

# 참고

## Spring Rest Docs을 사용한 API 문서화
[Spring Rest Docs 적용 | 우아한형제들 기술블로그](https://techblog.woowahan.com/2597/)

![[Pasted image 20220831232246.png]]