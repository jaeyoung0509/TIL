https://velog.io/@kineo2k/Go-%EC%96%B8%EC%96%B4-%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84-%EB%B6%84%EC%84%9D
https://ultimate-go-korean.github.io/translation/#%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84-%EB%B6%84%EC%84%9Descape-analysis
- go 언어는 탈출 검사를 통해서 인스턴스가 함수 외부로 공개되는것을 분석해내서 스택 메모리가 아닌 힙 메모리에 할당하게 됨
- 고언어는 어떤 타입이나 메모리 할당 함수에 의해서 스택 메모리를 사용할지 힙 메모리를 사용할지 결정하는게 아님 
- 메모리 공간이 함수 외부로 공개되는지 여부를 자동으로 검사
- 고언어 스택메모리는 계속 증가되는 동적 메모리 풀 
- 일정한 크기를 갖는 c, c++보다 효율적, 재귀 호출 때문에 스택메모리가 고갈되는 문제도 발생하지 않음