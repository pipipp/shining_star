import sys
import argparse


# 使用sys获取所有的输入参数
print(f'当前文件路径: {sys.argv[0]}')
print(f'所有的输入参数：{sys.argv[1:]}')


# 定义命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--ip", help="请填入主机IP，例如：-ip 192.168.xx.xx")

# 使用parse_args获取输入值
args = parser.parse_args()
print(f'获取ip值：{args.ip}')
