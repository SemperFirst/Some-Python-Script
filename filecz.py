import os
#文件操作练习
#创建文本
if __name__ == '__main__':

    with open("test.txt","w") as f:
        f.write("创建成功")
        f.close()
    #读取文本
    with open("test.txt","r") as f:
        print(f.read())
        f.close()
#显示文本除井号行
    while 1:
        with open("student.txt",'r',encoding='UTF-8') as f:
            content=f.readlines()
        for i in content:
            if(i[0]=="#"):
                continue
            else:
                print(i)
        break
    f.close()
    while 1:
        with open('student.txt','r',encoding='UTF-8') as f:
            for line in iter(f):
                print(line)
        break
    f.close()
#对数字文本排列
    number=[]
    with open('number.txt','r') as f:
        for i in f.read():
            print(i,end='\t')
            number.append(i)
    print()
    number.sort()
    print(number)
    f.close()