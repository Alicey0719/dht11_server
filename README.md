# dht11_server
DHT11で温湿度情報を返却するサーバ

## setting(docker&plain)
- app/.env
```sh
PIN=14 # your GPIO PIN
```

## setting(kubernetes)
- manifests.yaml
```yaml
~~~
env:
    - name: PIN
      value: "14" # your GPIO PIN
~~~
```
## sample case
- Zabbixに値を取得させて室温監視する
<img width="1443" alt="image" src="https://user-images.githubusercontent.com/54524362/176112433-483716eb-a572-488a-9185-1157b133d8a3.png">
