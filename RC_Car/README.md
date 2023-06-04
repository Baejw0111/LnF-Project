# LnF-Project For RC - Car

## CheckText.py
- 분실물 Tag 이미지를 텍스트로 전환
  - Naver Clova API에 변환 요청
- 전환한 텍스트와 요청받은 텍스트와 비교
- 비교 결과에 따라 `True` 혹은 `False`를 리턴

## developerMode.py
- RC Car의 작동 상태 확인
- 카메라, 모터 동작을 확인할 수 있다
- QT UI 활용

## Qt.py
- developerMode 의 UI file

## RCcarMovement.py
- DataBase 모니터링하며 명령 수신 대기
- 명령 Table에 수행할 명령이 등록되면 명령 수행
- `CheckText.py` 의 `isSame` 함수를 호출하여 동작
- `isSame == True`
  - 현재 위치의 물건을 가져온다
- `isSame == False`
  - 다음 위치로 움직인다