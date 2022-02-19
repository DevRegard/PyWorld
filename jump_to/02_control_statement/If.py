trafficLightRed = True

if trafficLightRed:
    print("자동차 STOP, 보행자 CROSS")
else:
    print("자동차 GO, 보행자 STOP")


# [비교 연산자]
#   <
#   >
#   ==
#   !=
#   >=
#   <=

#   or
#   and
#   not

#   in      : [a] 가 [리스트, 튜플, 문자열] 안에 있는가?
#   not in  : [a] 가 [리스트, 튜플, 문자열] 안에 없는가?
trafficLight = ['red', 'green', 'yellow']
light = "green"
if light not in trafficLight:
    print("신호등 작동중!")
    pass
else:
    print("신호등 고장남..")


# [elif]
if light == 'yellow':
    print("둘 다 멈춰!")
elif light == 'red':
    print("운전자 멈춰!")
elif light == 'green':
    print("보행자 멈춰!")
else:
    print("신호등 고장!")


# [조건부 표현식]
#   [참일 때] if [조건문] else [거짓일 때]
lightStatus = "working" if light in trafficLight else "let_fix"
print(lightStatus)
