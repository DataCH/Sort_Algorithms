#-*- coding:utf-8 -*
#选择排序

def find_min(L, index):
    small_index=index
    for i in range(index+1,len(L)):
        if L[small_index]>L[i]:
            small_index=i
    return small_index

def Select_Sort(L):
    for i in range(len(L)):
        smallest_index = find_min(L,i)
        if smallest_index != i:
            L[i],L[smallest_index]=L[smallest_index],L[i]
