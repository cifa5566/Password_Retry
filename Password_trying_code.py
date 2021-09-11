#密碼重試程式


i = 1

while i < 4 :
	password=input('請輸入密碼(最多輸入三次): ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤!，還有 %d次機會', 3-i)	
	i=i+1


