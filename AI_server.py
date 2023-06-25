import paho.mqtt.client as mqtt
import boto3

# Info of S3
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'
broker = '210.106.192.242'
cnt = 1
#in_file = 'test.jpg'
#out_file = 'test.jpg'


# 4) 영상 업로드 정보 수신
# 5) 영상 처리
# 6) 영상 처리 결과 명령 전송



def on_message(client, userdata, message):
    # 4) 영상 업로드 정보 수신
    global cnt
    in_file = 'test'+str(cnt) +'.jpg'
    cnt+=1
    string = str(message.payload.decode('utf-8'))
    # 버킷이름 , 다운 받을 파일 경로 + 이름, 저장할 파일 (절대경로)
    s3.download_file(bucket_name, 'test/' + string, 'Practice/s3practice/mqtt_test/tt/'+in_file)
    

    # --------------
    # 5) 영상 처리 부분
    # --------------
    
    # 6) 영상 처리 결과 명령 전송
    s_st.publish("data/Drone", "adjustment,명령(전진, 후진, 오른쪽, 왼쪽) ")
    
    
# S3
s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name = region)

# mqtt
s_st = mqtt.Client("AI")

s_st.connect(broker, 1883)
s_st.on_message = on_message
s_st.subscribe("data/AI")


s_st.loop_forever()