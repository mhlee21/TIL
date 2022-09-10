# Input

```java
import java.util.Scanner;
Scanner sc = new Scanner(System.in);
```

-   Scanner method
    -   next + {자료형}()
        -   예시에서는 대표적으로 nextInt()와 nextDouble() 을 사용하였다. 뒤에 사용한 자료형에 맞는 값을 받을 수 있다.
    -   nextLine()
        -   한 줄을 통째로 받아온다. 근데 nextLine()은 개행문자까지 받을 수 있기 때문에 위에서 buffer라는 변수에 nextLine()을 받아주지 않는다면 앞에서 남은 개행을 받아와 자기소개는 입력을 받지 못하게 된다. 따라서 buffer 변수로 한 번 더 받아줌으로서 이 문제를 해결하였다.
    -   next()
        -   화이트 스페이스를 기준으로 한 단어를 받아온다.

# Queue

**1.** 먼저 들어간 자료가 먼저 나오는 구조 FIFO(First In FIrst Out) 구조

**2.** 큐는 한 쪽 끝은 프런트(front)로 정하여 삭제 연산만 수행함

**3.** 다른 한 쪽 끝은 리어(rear)로 정하여 삽입 연산만 수행함

**4.** 그래프의 넓이 우선 탐색(BFS)에서 사용

**5.** 컴퓨터 버퍼에서 주로 사용, 마구 입력이 되었으나 처리를 하지 못할 때, 버퍼(큐)를 만들어 대기 시킴

```java
import java.util.LinkedList; //import
import java.util.Queue; //import

Queue<Integer> queue = new LinkedList<>(); //int형 queue 선언, linkedlist 이용
Queue<String> queue = new LinkedList<>(); //String형 queue 선언, linkedlist 이용
```

자바에서 큐는 LinkedList를 활용하여 생성해야 합니다.

그렇기에 Queue와 LinkedList가 다 import되어 있어야 사용이 가능합니다.

`Queue<Element> queue = new LinkedList<>()`와 같이 선언해주면 됩니다.

## [참고] int 와 Integer 의 차이?
int 는 자료형 (primitive type) 이고 Integer 는 Wrapper class 이다.  ([int와 Integer는 무엇이 다른가](https://velog.io/@hadoyaji/int%EC%99%80-Integer%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%B4-%EB%8B%A4%EB%A5%B8%EA%B0%80) )
- Wrapper class : _**기본형을 객체로 다루기 위해 사용하는 클래스**_ 
- 모든 primitive type 은 wrapper class 를 생성할 수 있다. 

**그래서 int 와 Integer 는 어떻게 다른가?** 
- int : 자료형 (primitive type) 
	- null 로 초기화 불가 
	- 산술 연산 가능 
- Integer : Wrapper class 
	- null 값 처리 가능 
	- Unboxing 하지 않을 시 산술 연산 불가능 (JDK 1.5부터는 이것을 자동으로 해주는 기능이 추가되었다.) boxing : primitive type → Wrapper class unboxing : Wrapper class → primitive type 
	- 비교 연산 가능하지만 내용물의 동치 여부 검사할 때 == 기호 대신 equals() 메소드를 이용해야 한다.
```
package tut02;public class Tut02 {
	public static void main(String[] args) {
        Integer iA = new Integer(123);
        Integer iB = new Integer(123);
        int ia = (int)iA; //(1) 언박싱(unboxing)
        int ib = iB; //(2) 오토언박싱(auto unboxing)
        Integer iC = (Integer)456; //(3)박싱(boxing)
        Integer iD = ia; //(4)오토 박싱(auto boxing)
    }
}
```
	


