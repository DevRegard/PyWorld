dic = {'name': 'KIM', 'nation': 'KOREA', 'age': '25', 'programing language': 'python'}

print(dic['name'])
print(dic['programing language'])
del dic['age']

print(dic)

# [Dictionary 함수]
#   keys()  : dict_keys 객체
#   value() : dict_values 객체
#   items() : dict_items 객체
#   clear() : 전부 삭제 => '{}'
#   get()   : key 로 values 값 얻기 => 없을 시, NONE 반환
#   ['key'] in [객체]
