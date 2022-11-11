### port & adapter pattern 
- https://engineering.linecorp.com/ko/blog/port-and-adapter-architecture/
- 변경에 영향을 받지 않는 핵심 코드를 만들고 이를 견고하게 관리 가능
- http api & web socket api
  - 다양한 인터페이스를 사용하더라고 변경되는 코드가 적고 많은 코드를 공유할 수 있음
  포트와 어댑터 효과
  - 커맨드 라인
  - 웹 인터페이스 추가
  - db 추가
  -> 개발자는 영속성을 변경하면서 관련 코드를 많이 변경해야 됨
-  포트와 어댑터 아키텍처를 적용하면 인터페이스나 기반 요소가 사용자의 요구 사항에 따라 변경된다 하더라도 애플리케이션의 주요 동작(도메인 로직 & 비지니스 로직)은 영향이 없음

- 포트는 인터페이스 역할 (서비스의 인터페이스)
- 어댑터는 클라이언트에게 제공해야될 인터페이스를 따르면서도 내부 구현에은 서버의 인터페이스로 위임


- domain: 업무 로직을 포함하는 클래스들이 들어섬
- application: 주로 유즈케이스
이 계층엔 업무 로직이 거의 없고, 도메인의 여러 업무 로직을 조합하는 역할
- interfaces: 클라이언트와 약속한 통신 방식의 어댑터를 포함
주로 mvc 컨트롤러나 rpc 서비스 (주어댑터)
- infrastructure: 다른 서비스를 사용하는 어댑터를 포함 (부어댑터)