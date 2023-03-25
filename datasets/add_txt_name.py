i=0

f = open('output.txt','a',encoding="utf-8")



while i < 100:

	f.write('wavs/1_')

	f.write(str(i))

	.write('.wav|\n')

	i=int(i)

	i=i+1



else:

	f.close()

	print('写入已完成') 作者：符号社Antigone https://www.bilibili.com/read/cv21153903 出处：bilibili