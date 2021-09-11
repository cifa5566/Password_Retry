#密碼重試程式


i = 1

while i < 4 :
	password=input('請輸入密碼(最多輸入三次): ')
	if password == 'a123456':
		print('登入成功')
		break
	elif i >= 1 and i < 3:
		print('密碼錯誤!，還有',3-i,'次機會')	
		
	else:
		print("沒有機會了")
	i=i+1


