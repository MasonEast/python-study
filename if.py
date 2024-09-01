# -*- coding: utf-8 -*-

height = float(input('身高(cm): '))
weight = float(input('体重(kg): '))

bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')

if 18.5 <= bmi < 24:
  print('你的身体很棒！') # 使用缩进的方式来表示代码的层次结构
else:
  print('你的身材不够标准！')

if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:  # elif的用法
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')

# match和case构造分支结构

status_code = int(input('响应码: '))
match status_code:
    case 400: dsc = 'Bad Request'
    case 401: dsc = 'Unauthorized'
    case 403 | 404: description = 'Forbidden'
    case 405: description = 'Method Not Allowed'
    case _: description = 'Unknown Status Code' # _为通配符

print('状态码描述: ', dsc)

