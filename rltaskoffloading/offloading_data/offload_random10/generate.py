import os
import sys
import random


fat = [0.1, 0.3, 0.5, 0.7, 0.9]		# fat用于控制DAG的宽度和高度
density = [0.5, 0.6, 0.7, 0.9]	# density用于确定DAG的两个层级之间的边数
regularity = [0.5, 0.7, 0.9]	#regularity用于控制DAG的规则性
ccr = [0.3, 0.4, 0.5]		# ccr表示通信与计算的比率，即通信成本与计算成本之间的比率

# 任务的传输数据大小设置在5KB到50KB之间
mindata = int(5 * (1 * 1024.0 * 1024.0 ))
maxdata = int(50 * (1 * 1024.0 * 1024.0 ))


def main():
	for i in range(1000):
		command = './daggen --dot -n 10'
		file_name = 'random.10.' + str(i) +'.gv'
		command = (command + ' --ccr ' + str(ccr[random.randint(0,len(ccr)-1)])  +
				' --fat ' +  str(fat[random.randint(0,len(fat)-1)])  +
				' --regular ' + str(regularity[random.randint(0,len(regularity)-1)])  +
				' --density ' + str(density[random.randint(0,len(density)-1)]) +
                ' --mindata ' + str(mindata) +
                ' --maxdata ' + str(maxdata))
		print(command)

		os.system( command + '> '+file_name)

if __name__ == '__main__':
	main()

