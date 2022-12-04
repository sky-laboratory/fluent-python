# Fluent-python

## 파이썬 시퀀스를 단일하게 처리하는 ABC의 특징을 물려받음 
----------
+ 문자열, 리스트, 바이트 시퀀스, 배열
  + DB결과에는 모두 반복, 슬라이싱, 정렬, 연결 등 공통된 연산을 적용할 수 있음 


## 파이썬에서 제공하는 다양한 시퀀스를 이해하면 코드를 새로 구현할 필요 없음 
----------
+ 공통 인터페이스를 따라 적절히 활용할 수 있게 API 정의 가능 

+ 컨테이너 시퀀스 (data container and data structure)
  + 객체에 참조를 담고있으며 어떠한 자료형도 될 수 있음 
  + list, tuple, collections, deque 등등 

+ 균일 시퀀스 (flat sequence)
  + 객체에 대한 참조 대신 자신의 메모리 공간에 각 항목의값을 직접 담음 
  + str, bytes, bytearray, memoryview, array.array(python list X) 
  + 균일 시퀀스가 메모리를 더 적게 사용하지만 기본적인 자료형만 저장할 수 있다는게 단점 

### 퀀스형은 다음과 같이 가변성에 따라 분류도 가능 
----------
+ 가변 시퀀스 
  + list, bytearray, array.array, collections.deque, memoryview형 
+ 불변 시퀀스 
  + tuple, str, byte형  
