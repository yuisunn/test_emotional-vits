import os
path='D:\\_AI\\so-vits-svc-4.0\\dataset_raw\\redrabbit\\'

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

n=0

for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
    
    #设置新文件名
    newname=path + os.sep +'redrabbit_'+str(n+1)+'.wav'
    #D:\_AI\so-vits-svc-4.0\dataset_raw
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    n+=1
    