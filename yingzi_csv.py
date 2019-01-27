import csv
import os

# csv文件路径
path = './csv/'


# 定义数据清洗函数data_wash, 接收filename[文件名], la_max[最大纬度], ln_max[最大精度]参数,
def data_wash(filename, la_max, ln_max):
    # 定义csv文件和写入器,用于保存生成的csv文件,保存的文件名为:原文件文件名+_output
    csv_out_file = open(path + filename + '_output', 'w')
    csv_writer = csv.writer(csv_out_file)

    # 打开要处理文件
    with open(path + filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

        # 获取csv行数
        for line in csv_reader:
            line_count += 1
        print('文件:{} 共有 {} 行'.format(filename, line_count))

        if line_count < 50:  # 小于50行数据的文件删除
            print('文件少于 50行数据,删除...')
            os.remove(path + filename)

    with open(path + filename, 'r') as csv_file:
        csv_reader2 = csv.reader(csv_file)

        # 读取每行csv数据
        for item in csv_reader2:

            # 因为读出来的都是string类型的数据,要转换成float类型比较大小,这里使用try捕获异常,防止文件内容异常转换失败导致程序终止
            try:
                # 每行第一个数据(纬度)大于la_max的,或每行第二个数据(经度)大于ln_max的打印提示
                if float(item[0]) > la_max or float(item[1]) > ln_max:
                    print('这条数据:{} 超出经纬范围'.format(item))
                else:  # 不大于的保存到新csv文件中
                    csv_writer.writerow(item)
            except BaseException as e:
                print('文件数据内容异常不符合规范(纬度,经度,其他字段,....),或磁盘已满')
                print(e)


# 获取目录下的文件列表
file_list = os.listdir(path)
print('.csv目录下文件列表:{}'.format(file_list))

# 遍历每个文件调用data_wash函数进行处理
for file in file_list:
    print('正处理文件:{}'.format(file))
    data_wash(file, 41, 117)
