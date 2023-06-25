import paho.mqtt.client as mqtt
import boto3
import time

# Infomation of S3
accessKey = 'AKIAZDLFNYZT2RCQNA5G'
secretKey = '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'
region = 'ap-northeast-2'
bucket_name = 'twootest'
prefix = 'test/'


# level : 드론 진행 단계
# 0 : 초기상태
# 1 : 자율주행 
# 2 : 정밀조정
# 3 : 투척
# 4 : 복귀
level = 0

# 7) 영상 처리 결과 수신
def on_message(client, userdata, message): # mqtt 통신 수신 시 동작
    cmd = []
    string = str(message.payload.decode('utf-8'))
    print(string)
    cmd = string.split(',')
    if(cmd[0] == 'report'): # 소방서에서 신고가 접수되면 드론은 소방서로부터 데이터 수신 Ex) report,30,40
        lat = float(cmd[1]) # 위도
        lon = float(cmd[2]) # 경도
        print('lat=' + str(lat) + ', lon=' + str(lon))
        # -------------
        # 자율주행 코드(시동 포함)
        # -------------
    elif(cmd[0] == 'adjust'): # 신고 좌표로 도착 후 정밀 조정단계 AIserver로부터 데이터 수신 EX) adjustment,up
        print('adjust')
        # result값으로 정밀 조정
        if(cmd[1] == 'correct'): # 위치조정 완료 시
            print('turn into throw mode')
            # -------------
            # 아두이노에 투척 명령 송신
            # -------------
        elif(cmd[1] == 'up'): # 영상 처리 결과 전진
            print('move foward')
            # -------------
            # 전진 코드
            # -------------
        elif(cmd[1] == 'down'): # 영상 처리 결과 후진
            print('move backward')
            # -------------
            # 후진 코드
            # -------------
        elif(cmd[1] == 'Rturn'): # 영상 처리 결과 오른쪽 회전
            print('turn Right')
            # -------------
            # 오른쪽 회전 코드
            # -------------
        elif(cmd[1] == 'Lturn'): # 영상 처리 결과 왼쪽 회전
            print('turn Left')
            # -------------
            # 왼쪽 회전 코드
            # -------------


# mqtt
broker = '210.106.192.242'
s_st = mqtt.Client('drone')
s_st.connect(broker, 1883)
s_st.on_message = on_message
s_st.subscribe('data/Drone')

# S3
s3 = boto3.client('s3', aws_access_key_id = accessKey, aws_secret_access_key=secretKey, region_name=region)

s_st.loop_forever()

'''
while(1):
    if(level == 0):
        # 대기
        print('no report')
    elif(level == 1):
        # 지정된 좌표로 이동 
        print('start misson')
        if(도착):
            level = 2
    elif(level == 2):
        # 정밀조정
        print('precisely adjustment')
    elif(level == 3):
        # 투척
        print('throw the bottle')
        level = 4
    elif(level == 4):
        # 복귀
        print('return home')
'''


'''
# 1) 영상 촬영
# 2) 영상 업로드
# 3) 영상 업로드 정보 인공지능 모델 컴에 전송
for i in range(5):

#whlile(끝날때까지)

    # ------------
    # 1) 영상촬영 부분
    # ------------


    # 2) 영상 업로드
    in_file = './testFile/test'+str(i+1)+'.jpg'
    out_file = 'test' + str(i+1)+'.jpg'
    # 업로드할 파일 이름, 버킷 이름 ,0020버킷 내 경로
    s3.upload_file((in_file), bucket_name, 'test/'+out_file)

    # 3) 영상 업로드 정보 인공지능 모델 컴에 전송
    s_st.publish("data", out_file)
time.sleep(5)   

    # ---------------
    # 드론 동작
    # ---------------
    







s_st.loop_start()

'''
