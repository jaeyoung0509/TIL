## ssl /tls 
### tls summary 
- tls
  - ssl stands for secure socket layer
  - the short form of transport layer security
  - cryptographic protocol that provides secure communication over a computer network

- the history of ssl /tls (only tls1.2 and 1.3 are active) 
  - 1996 ssl 3.0
  - 1999 ietf tls 1.0
  - 2006 tls 1.1 
  - 2008 tls 1.2 
  - 2018 tls 1.3

- where is tls being used ?
  - website: `https` = http + tls 
  - email: `smtps` = smtp + tls 
  - file transfer : `ftps` = fpt + tls

### why tls (there are three reasons why tls is important)
- `authentication`
  - verify the identity of the communicating parties with asymmetric cryptography
- `confidentiality`
  - protect the exchanged data from unauthorized access with symmetric cryptography
- `integrity`
  - tls recognizes any alteration of data during transmission by checking the message authentication code
  - precent alteration of data during transmission with message authentication code 

### how does it work?
- tls consists of 2 phases, or 2 protocols
##### handshake protocol
- negotiate the protocol version 
- select cryptographic algorithm(or cipher suites)
- authenticate each other by asymmetric cryptography
- establish a shared key
#### record protocol 
- all outgoing messages will be encrypted with the shared secret key established in the handshake
- Then the encrypted messages are transmited to the other side
- They will be verified to see if there’s any modification during transmission or not
- message will be decrypted with the same symmetric secret key 

### why using both symmetric and asymmetric cryptography?
#### symmetric cryptography(대칭키)
- 만약 대칭키로만 암호화를하면 , 입증할 방법이 없음  
- 대중에게 공개하지 않고 어떻게 같은 키를 사용하는지 알 수 없다 
#### asymmetric cryptography 
- 좋은 후보지만 , 대칭키에 비해 (100~ 1000)배 더 느림
- 대량 암호화에 적합하지 않음

### symmetric cryptography
- 서로 같은키를 공유하여 비밀을 암호화 복호화 (대칭키)
- 아래와 같은 공격을 막기 위해서는 인증된 암호를 사용하자 (`암호화` + `암호화 된 메시지를 인증`)
#### 대칭키 공격 방법 
- bit-flipping attack (대칭키로 암호화된 문서에 비트를 바꿔 평문을 바꿈)
#### AE (authenticated encrpyion)
- 암호화
  - `aes-256-gcm` , `chacha20` 같은 대칭 암호화 알고리즘을 거쳐 암호화 
- 인증 
  - mac 알고리즘을 이용  (mac은 메시지 인증 코드)
  - mac 알고리즘은 해시 함수처럼 작동하며 출력은 인증 코드
    - mac 알고리즘은 비밀 키를 입력받고, 임의-길이의 메시지를 인증
  - 이 때 이 mac은 암호화된 메시지와 함께 태그가 지정 -> `MAC an authentication tag`
- 복호화 및 mac 검증 
  - mac으로 암호화된 메시지로부터 시작하여 암호화된 메시지에서 mac태그를 헤제
  - 그런다음 공유 비밀키 및 nonce와 함께 mac 알고리즘을 통해 복호화
    - `nonce`: 암호화에서 nonce는 암호화 통신에서 한 번만 사용할 수 있는 임의의 숫자
#### 비밀키 교환 
- 그럼 어떻게 서로의 비밀키를 유출없이 공유 할 수 있을까? (공개키 알고리즘을 통해서)
- 주로 `Diffie-Hellman Ephemeral ` 또는 ` Elliptic-Curve Diffie-Hellman Ephemeral`을 사용

#### Diffie-Hellman Ephemeral
- 설명 추가하기 

####  Elliptic-Curve Diffie-Hellman Ephemeral
- 설명 추가하기 


### 비대칭 암호화 

#### 비대칭키를 사용하자~!
- authenticate the encrypted message
- encrpyion algorithm
- mac algorithm
- aead

#### tls에서 세션별로 임시키를 생성하는 경우 
- 한 세션에서만 사용 가능  
- perfect forward secrecy