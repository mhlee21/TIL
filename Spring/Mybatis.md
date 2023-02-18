
### JDBC
- Java Database Connectivity
- 자바에서 데이터베이스에 접속할 수 있도록 하는 자바 API

Java 에서 DB 프로그래밍을 하기 위해서 JDBC가 제공되었다. JDBC는 RDB 사용을 위한 다양한 API를 제공하지만, DB가 방대해지고 각 data 간 관계가 복잡해짐에 따라 다수의 메소드를 호출하고 관련 객체를 해제해야하는 문제점이 심화되었다. (=> 기존에는 JDBC 연동과정도 복잡하고 SQL문이 코드 내에 섞여있어 코드가 상당히 복잡해졌다.) 이러한 문제점을 해결하고 더욱 효과적으로 DB를 관리하기 위해 MyBatis 가 고안되었다.

## Mybatis
마이바티스는 개발자가 지정한 SQL, 저장 프로시저 그리고 고급 매핑을 지원하여 개발 생산성을 높이는 persistence framework 이다. 기존 JDBC 만을 이용한 방식은 프로그램 소스 안에서 직접 connection을 맺고 SQL문을 처리하고 rs.next() 등을 이용하여 하나씩 받아와야해서 코드가 길어지고 SQL의 변경이 필요한 경우에도 java 프로그램을 수정하기 때문에 유연성이 좋지 못했다. 
그러나 마이바티스에서는 상당부분의 코드와 파라미터 설정 및 ResultSet 결과를 대신해주어 코딩의 중복과 무의미한 코드 작성을 생략할 수 있으면서도, SQL 문을 xml 파일에 작성하여 변환이 자유롭고 가독성이 좋다.

즉, Mybatis는 RDB를 더욱 편하게 이용할 수 있도록 개발된 persistence framework 이다.


### 마이바티스의 특징
- sql 실행 결과를 map 객체에 매핑해준다.
- sql을 소스코드가 아닌 xml로 분리하여 작성한다.
- 데이터 소스 기능과 트랜잭션 처리 기능을 제공해준다.
- 스프링에서 데이터베이스 연동을 도와주는 프레임워크
- 자바와 SQL 사이의 자동 매핑 기능을 지원하는 ORM(Object Relational Mapping) 프레임워크

SQL을 별도의 파일로 분리해서 관리하게 해준다.
Hibernate 나 JPA 처럼 새로운 DB 프로그래밍 패러다임을 익혀야하는 부담없이 SQL을 그대로 이용하면서 JDBC 코드 작성의 불편함도 제거해주고, 도메인 객체나 VO 객체를 중심으로 개발이 가능하다는 장점이 있다.


### 사용 방식
MyBatis 를 이용할 때 SQL문을 사용하는 방식은 크게 3가지로 나뉠 수 있다.

1. XML 만을 이용한 SQL문을 설정, DAO 에서는 XML을 찾아서 실행하는 코드로 작성
	1. 장점 : SQL문은 별도로 XML로 작성되어 SQL문의 수정이나 유지보수에 적합
	2. 단점 : 개발 시 코드 양이 많아지고, 복잡성이 증가

2. annotation 과 인터페이스만을 이용하여 SQL 문 설정
	1. 장점 : 별도의 DAO 없이도 개발 가능하여 생산성이 크게 증가
	2. 단점 : SQL 문을 annotation으로 작성하므로, 매번 수정이 일어나는 경우 다시 컴파일 필요

3. 인터페이스와 XML로 작성된 SQL문의 활용
	1. 장점 : 간단한 SQL문은 annotation으로 복잡한 SQL문은 XML로 처리하여 유연성이 좋음
	2. 단점 : 개발자에 따라 개발 방식 차이로 인해 유지보수가 중요한 프로젝트에서는 부적합



# 참고

https://velog.io/@changyeonyoo/Mybatis%EB%9E%80-%EC%9E%A5%EC%A0%90-%ED%8A%B9%EC%A7%95-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8

https://oingdaddy.tistory.com/202