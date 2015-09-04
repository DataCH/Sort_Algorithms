#-*- coding:utf-8 -*-
#功能：插入排序算法

import sys

def Insert_Sort(array):
	n_length=len(array)
	for i in range(1,n_length):
		temp_value=array[i]
		temp_index=i
		for j in range(i-1,-1,-1):
			if array[j]>temp_value:
				array[j+1]=array[j]
				temp_index=j
			else:
				break
		array[temp_index]=temp_value
	return array

def Show(array):
	n_length=len(array)
	for i in range(0,n_length-1):
		sys.stdout.write(str(array[i]))
		sys.stdout.write(",")
		sys.stdout.flush()
	print array[n_length-1]

def main():
	array=[60,71,49,11,24,3,66]
	Insert_Sort(array)
	Show(array)

if __name__=="__main__":
	main()
