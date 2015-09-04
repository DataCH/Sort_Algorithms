#-*- cosing:ut-8 -*-
#功能：冒泡排序算法

import sys

def Bubble_Sort(array):
	n_length=len(array)
	for i in range(0,n_length):
		for j in range(1,n_length-i):
			if array[j-1]>array[j]:
				temp=array[j]
				array[j]=array[j-1]
				array[j-1]=temp
	return array

def Improved_Bubble_Sort(array):
	n_length=len(array)
	for i in range(0,n_length):
		isSorted=True
		print array
		for j in range(1,n_length-i):
			if array[j-1]>array[j]:
				isSorted=False;
				temp=array[j]
				array[j]=array[j-1]
				array[j-1]=temp
		if isSorted:
			return array
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
	Bubble_Sort(array)
	Show(array)

	Improved_Bubble_Sort(array)

if __name__=="__main__":
	main()
