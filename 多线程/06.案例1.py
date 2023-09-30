import os
import multiprocessing

# 定义源文件夹和目标文件夹
source_dir = "D:/视频成品"
dest_dir = "D:/123"

def copy_file (file_name,source,dest) :
    # 拼接路径
    source_path = source + "/" + file_name
    dest_path = dest +"/" + file_name

    # 打开文件
    with open (source_path,"rb") as source_file :
        with open (dest_path,"wb") as dest_file :
            # 循环读取源文件到目标路径
            while True :
                data = source_file.read (1024)
                if data :
                    dest_file.write (data)
                else :
                    break

if __name__ == "__main__" :
    # 创建目标文件夹
    try :
        os.mkdir (dest_dir)
    except :
        print ("True")
    
    # 读取目标文件夹的文件列表
    file_list = os.listdir (source_dir)

    # 遍历文件列表实现拷贝
    for file_name in file_list :
        # 调用函数完成拷贝
        sub_copy = multiprocessing.Process (target=copy_file,args=(file_name,source_dir,dest_dir))
        sub_copy.start ()
