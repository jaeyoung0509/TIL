### what is context?
- Package context defines the Context type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes
- `context`는 작업 명세서와 같은 역할(작업 가능한 시간, 작업 취소 등) 작업의 흐름을 제어하는데 사용
- 새로운 고루틴으로 작업을 시작할 때 일정 시간 동안만 작업을 지시하거나 외부에서 작업을 취소할 때 사용
- 프로그램 내부에서 `context`를 넘겨주는 개념 
```go
ctx , cancel := context.WithCancel(context.Background())
```
#### best practices
- context.Background는 프로그램의 최상위 레벨에서 사용하는게 바람직
- contex.TODO 아직 구현 못한 것에 대해 (미래)에 대해 사용
- context.cancellation은 주의가 필요 함수가 cleanup하고 exit하는데 시간이 필요 
- context.Value는 optional parameter를 넘기기 위해 사용하지 않음 
- context를 struct에 담지 말 것, function에 넘기게 된다면 첫번째 argument로
- nil context를 pass하지 말 것 -> todo로
- context는 cancel method가 없음 