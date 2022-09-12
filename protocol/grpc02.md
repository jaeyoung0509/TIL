## agenda 
- motivation
- grpc 
    - unary grpc
    - server streaming
    - client streaming
    - bidirectional 
- grpc pros & cons 

### the problem with client libarires 
- any communication protocol needs client library for the lanugae of choice 
- hard to maintaion and patch client libarires
  - http1.1 http2 bla bla
### why grpc was invented 
- client library : one library
- protocol: http2 (**hidden implemantaion**)
- message format: protocol buffers as format

### grpc modes 
#### unary rpc 
- request to a server synchronously wait and then the server does some processing
maybe calls another service maybe query a database maybe we just calculate
- 클라이언트는 서버에 싱글 리퀘스트, 다시 싱글 리스폰스 
  
#### server streaming rpc 
- 클라이언트가 서버에 리퀘스트를 보내고 스트림을 가져와 일련의 메시지를 읽는다
- 리턴되는 스트림이 더 이상 메시지가 없을때 까지 읽음 
- grpc는 개별적인 rpc call에 대해 메시지 순서를 보증 

#### client streaming rpc 
https://breezymind.com/grpc-client-streaming-rpc/

#### bidirectional streaming rpc


### grpc pros & cons 
#### pros 
- fast compact
- one clinet library
- progress feddback
- cancel request
#### cons 
- schema 
- thick client 
- proxies
- error handling 
- no native browser support