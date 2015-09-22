//函数：冒泡排序及其改进
//作者：apq
//日期：2015-09-22

#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
	a=a+b;
	b=a-b;
	a=a-b;
}

void bubble_sort(int *array, int n)
{
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n-i-1;++j)
		{
			if(array[j]>array[j+1])
				swap(array[j],array[j+1]);
		}
	}
}

void show(int *array, int n)
{
	for(int i=0;i<n-1;++i)
		cout<<array[i]<<",";
	cout<<array[n-1]<<endl;
}

void bubble_sort_new(int *array, int n)
{
	int count=0;	//记录比较的次数

	for(int i=0;i<n;++i)
	{
		int flag=0;	//记录每趟发生交换的次数

		for(int j=0;j<n-i-1;++j)
		{
			count++;
			if(array[j]>array[j+1])
			{
				swap(array[j],array[j+1]);
				++flag;
			}		
		}

		cout<<"flag="<<flag<<endl;

		if( 0==flag )
			break;
	}

	cout<<"count="<<count<<endl;
}

int main()
{
	int array[]={1,2,3,4,5,6,7};
	int n=sizeof(array)/sizeof(array[0]);

	bubble_sort_new(array,n);

	show(array,n);

	return 0;
}
