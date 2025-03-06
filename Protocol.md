# Evemahjong Protocol

Request -> Expected reply

# Client -> Server
## 主动: 这些消息主动发出并期望回复
- CliHello -> SrvHello [玩家id] | SrvDeny
接入服务器, 握手
- Deck -> DeckAck [牌组序列化] | DeckErr
请求此玩家的牌组
- Quit -> QuitAck
报告此玩家退出游戏

- Play [牌id] -> PlayAck | PlayErr
打出一张牌

- Gang [牌id] -> GangAck | GangErr
尝试杠
- Peng [牌id] -> PengAck | PengErr
尝试碰
- Chi [牌id] -> ChiAck | ChiErr
尝试吃

### Optional
- KeepAlive
心跳信号

## 回复: 这些消息在接收到对应的服务端请求后回复
- SendAck
告知服务端已经收到发牌
- TingpaiYes
告知服务端要听牌
- TingpaiNo
告知服务端不要听牌
- Error
接收到无效的消息

# Server -> Client
## 公告: 这些消息主动发出并不接受回复
- Play [客户端id] [牌id]
公布某玩家打了一张牌
- Tingpai [客户端id]
公布某玩家开始听牌
- Victory [客户端id] [方式]
公布某玩家已获胜

## 主动: 这些消息主动发出并期望回复
- Send [玩家id] [牌id] -> SendAck
向某玩家发牌
- PreTingpai -> TingpaiYes | TingpaiNo
询问某玩家要不要听牌

## 回复: 这些消息在接收到对应的客户端请求后回复
- SrvHello [玩家id]
接受玩家进入游戏并回复其玩家id
- SrvDeny
拒绝玩家进入游戏

- DeckAck [牌组序列化]
接受请求牌组并回复牌组的序列化
- DeckErr
拒绝请求牌组
- QuitAck
接受某玩家退出游戏
- PlayAck
接受某玩家打出一张牌
- PlayErr
拒绝某玩家打出一张牌(例如这不是你的回合)
- GangAck, GangErr, PengAck, PengErr, ChiAck, ChiErr
不再赘述
- Error
接收到无效的消息
