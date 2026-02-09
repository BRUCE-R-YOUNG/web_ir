import streamlit as st
import subprocess
import paho.mqtt.client as mqtt

# タイトル
st.title("照明App")

# 説明
st.write("照明の赤外線リモコンのON/OFFコードを記録し、Streamlitで作成したAPPから照明をコントロールする")

# MQTT接続設定
BROKER_ADDRESS = "192.168.0.187"  # MQTTブローカーのアドレス
TOPIC = "home/light/control"  # MQTTトピック

# MQTTクライアントのセットアップ
client = mqtt.Client()
client.connect(BROKER_ADDRESS, 1883, 60)

# ONボタン
if st.button("ON"):
    # MQTTペイロードを送信
    client.publish(TOPIC, payload="true", qos=1)
    st.success("照明をONにしました！")

    # 赤外線信号送信コマンドを実行
    subprocess.run(["ir-ctl", "-d", "/dev/lirc0",
                   "-s", "light_power"], check=True)

# OFFボタン
if st.button("OFF"):
    # MQTTペイロードを送信
    client.publish(TOPIC, payload="false", qos=1)
    st.success("照明をOFFにしました！")

    # 赤外線信号送信コマンドを実行
    subprocess.run(["ir-ctl", "-d", "/dev/lirc0",
                   "-s", "light_power"], check=True)

    # MQTTクライアントの切断
client.disconnect()
