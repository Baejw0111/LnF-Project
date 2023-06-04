import requests
import uuid
import time
import json
import cv2
import time
import picamera

def isSame(date, times, name, place):

  def parsing(src):
      ret = ""
      for i in src:
          if i == ' ' or i == ':':
              continue
          ret += i
      return ret
  
  cap = cv2.VideoCapture(0)
  cap.set(3,3280)
  cap.set(4,2464)
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  cv2.imwrite('image.jpg',frame)
  cap.release()
  raw_src = cv2.imread('image.jpg')  

  # 이미지 cropping ~ pixel 기준 (x,y) 임에 유의
  # 리스트에서는 [y, x, channel] 임
  # 크롭핑 좌표는 하드코딩
  src = raw_src[240:650,800:1800, :]
  dst = cv2.resize(src, (480, 320))
  cv2.imwrite('pre_image.jpg', dst)

  api_url = 'your_api_url'
  secret_key = 'your_secret_key'
  image_file = 'pre_image.jpg'

  request_json = {
      'images': [
          {
              'format': 'jpg',
              'name': 'demo'
          }
      ],
      'requestId': str(uuid.uuid4()),
      'version': 'V2',
      'timestamp': int(round(time.time() * 1000))
  }

  payload = {'message': json.dumps(request_json).encode('UTF-8')}
  files = [
    ('file', open(image_file,'rb'))
  ]
  headers = {
    'X-OCR-SECRET': secret_key
  }

  response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
  res = response.text
  res_J = json.loads(res)
  now_str = ""
  for i in range(len(res_J['images'][0]['fields'])):
      now_str += res_J['images'][0]['fields'][i]['inferText'] + " "

  # string sample
  # Form : date, time, name, place 
  # now_str = '분실일자 : 2023년 5월 22일 분실시간 : 18시 30분 분실물: 갤럭시S23 분실장소 : 역삼역 1번출구 기타 : 없음'
  try:
    now_str = parsing(now_str)
    pos_date = now_str.find("분실일자")
    pos_time = now_str.find("분실시각")
    pos_name = now_str.find("분실물")
    pos_loc = now_str.find("분실장소")
    #pos_else = now_str.find("기타")
    tagDate = parsing(now_str[pos_date+4:pos_time])
    tagTime = parsing(now_str[pos_time+4:pos_name])
    tagName = parsing(now_str[pos_name+3:pos_loc])
    tagLoc = parsing(now_str[pos_loc+4:])
  except:
    # print("태그 인식이 올바르지 않습니다.")
    return False
  else:
     # try 성공하면 문자 비교 수행
     # 단순 비교; 인식률 낮으면 알고리즘 설계하기
     print("==now String==")
     print("원문 : {}".format(now_str))
     print("날짜 결과 :{}".format(tagDate))
     print("시간  결과 : {}".format(tagTime))
     print("분실물 결과 : {}".format(tagName))
     print("장소 결과 : {}".format(tagLoc))
     ret = True
     if tagDate != date :
        ret = False
     if tagTime != times:
        ret = False
     if tagName != name:
        ret = False
     if tagLoc != place:
        ret = False
     return ret
