import os
import hashlib
import time
import datetime
import json
import pytz
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
import requests
RTSP_RESTREAM_HOST=""
STREAM_CONTROLLER_HOST=""
KAFKA_HOST=""
AI_TOPIC=""
STREAM_TOPIC=""

def random_sha256():
    random_bytes = os.urandom(32)
    sha256 = hashlib.sha256()
    sha256.update(random_bytes)
    return sha256.hexdigest()   

def get_data(url,number_retry=3):
    print("url: ",url)
    check=False
    for i in range(number_retry):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('Lay du lieu thanh cong!')
                check=True
                break
            else:
                print('Lay du lieu khong thanh cong.')
                time.sleep(3)
        except:
            print("Loi request")
    if check:
        return response.json()
    return None

def send_db(url , headers , data):
    check = False
    for i in range(3):
        try:
            response = requests.post(url, headers=headers, json=data)
            if (response.status_code == 200):
                print('Gui du lieu toi database thanh cong')
                check= True
                return True
        except: 
            print("loi request")
            

def serializer(message):
    return json.dumps(message).encode('utf-8')

def send_to_AI(camera_id, path, time_start, fps, record_filename):
    try:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_HOST],
            value_serializer=serializer,
        )
        message={"camera_id":camera_id,"path":f"{path}","time_start":time_start,"fps":fps,"record_filename":record_filename}        
        print("kafka data:",message)
        future = producer.send(AI_TOPIC, value=message)
        producer.flush()
        print("AI path: "+path)
        print("Gui AI kafka thanh cong")
    except Exception as e:
       print(e)
       print("Loi gui AI kafka") 
       
        
def send_stream_path_to_sse(camera_id,stream_path,time_start,rtsp_phu=None,message_ai=None):
    try:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_HOST],
            value_serializer=serializer,
        )
        message={"camera_id":camera_id,"stream_path":f"{stream_path}","time_start":time_start,"rtsp_phu":rtsp_phu}
        # message["rtsp_phu"]=rtsp_phu    
        if message_ai is not None:
            message["message_ai"]=message_ai
        print("kafka data:",message)
        future = producer.send(STREAM_TOPIC, value=message)
        producer.flush()
        print("Stream path: "+stream_path)
        print("Gui stream path thanh cong")
    except:
        print("Loi gui stream path kafka")
        
def get_fps(camera_id):
    fps_stream = 13
    fps_record = 13
    
    return fps_stream, fps_record

def get_quality_stream(camera_id, main_resolution="720p"):
    resolution_stream="720p"
    force_not_copy_mode=True
    return resolution_stream,force_not_copy_mode

def get_quality_record(camera_id,main_resolution="720p"):
    return main_resolution, True

def get_quality(camera_id, main_reolution="720p"):
    return "720p",True,"720p",True

def get_aspect_ratio(width,height):
    aspect_ratio=None
    if width is None or height is None or width == 0 or height == 0:
        print("Loi width hoac height")
        return aspect_ratio
    try:
        width = int(width)
        height = int(height)
        result=width/height
        if abs(result-16/9) < 0.1:
            aspect_ratio="16/9"
        elif abs(result-4/3) < 0.1:
            aspect_ratio="4/3"
        elif abs(result-11/9) < 0.1:
            aspect_ratio="11/9"
        return aspect_ratio
    except:
        print("Loi tinh aspect ratio")
        return None