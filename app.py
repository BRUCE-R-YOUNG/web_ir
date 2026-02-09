import streamlit as st
import paho.mqtt.client as mqtt

st.title("照明App")

BROKER_ADDRESS = st.secrets["MQTT_HOST"]
TOPIC = "home/light/control"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER_ADDRESS, 1883, 60)

if st.button("ON"):
    client.publish(TOPIC, "true", qos=1)
    st.success("照明ONコマンド送信")

if st.button("OFF"):
    client.publish(TOPIC, "false", qos=1)
    st.success("照明OFFコマンド送信")

client.disconnect()
