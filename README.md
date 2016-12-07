# てまー部屋の温度と音楽bot

bot
https://twitter.com/Tkon_bot

1時間に一度部屋の温度をツイートします。
play, stop, repeat, sleepをリプライすることで部屋の音楽を操作できます。

@Tkon_sec以外のアカウントからのリプライでは動きません。


## token.json
Twitter認証用の`Consumer Key`等は`token.json`に記入して下さい。

### [token.json](./token_sample.json)
```json
{
  "client_key"            : "Consumer Key",
  "client_secret"         : "Consumer Secret",
  "resource_owner_key"    : "Access Token",
  "resource_owner_secret" : "Access Token Secret"
}
```
