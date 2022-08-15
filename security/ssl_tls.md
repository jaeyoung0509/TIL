## ssl /tls 

### tls summary 
- tls
  - the short form of transport layer security
  - cryptographic protocol that provides secure communication over a computer network

- the history of ssl /tls 
  - 1996 ssl 3.0
  - 1999 ietf tls 1.0
  - 2006 tls 1.1 
  - 2008 tls 1.2 
  - 2018 tls 1.3

- where tls is used ?
  - website: https = http + tls 
  - email: smtps = smtp + tls 
  - file transfer : ftps = fpt + tls

### why tls (there are three reasons why tls is important)
- authentication
  - verify the identity of the communicating parties with asymmetric cryptography
- confidentiality
  - protect the exchanged data from unauthorized access with symmetric cryptography
- integrity
  - precent alteration of data during transmission with message authentication code 

### how does it work?
-  handshake protocol
   - main purpose of the handshake is for authentication and key exchange
- record protocol (it is called `symmetric bulk encyption`) 
  - messages will be decrypted with the same symmetric secret key
  - encypt outgoing messages with the secret key 
  - transmit the encrpyted messages
  
### why using both symmetric and asymmetric cryptography?
- 대칭키는 인증을 제공할 수  없음 (서로에게 정보를 전달 x)
- 비대칭키는 대칭키보다 느림

#### 대칭키 공격 방법 
- bit-flipping attack (대칭키로 암호화된 문서에 비트를 바꿔 평문을 바꿈)

#### 비대칭키를 사용하자~!
- authenticate the encrypted message
- encrpyion algorithm
- mac algorithm
- aead

#### tls에서 세션별로 임시키를 생성하는 경우 
- 한 세션에서만 사용 가능  
- perfect forward secrecy