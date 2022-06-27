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
