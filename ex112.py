def sort(lst):
    sortHelper(lst,0,len(lst)-1)

def sortHelper(lst,l,h):
    if l<h:
        #lst[l...h] 사이에서 가장 작은 원소와 원소의 인덱스를 찾는다.
        indexofMIN = l
        min = lst[l]
        for i in range(l+1,h+1):        #<= // < 구간이라고 생각해줘야 한다...(for문)
            if lst[i]<min:
                min = lst[i]
                indexofMIN = i
        lst[indexofMIN] = lst[l]
        lst[l] = min

def main():
    lst = [3,2,1,5,9,8]
    sort(lst)
    print(lst)

    mlist = []
    list_size = eval(input("input list size : "))
    for i in range(list_size):
        mlist.append(eval(input("input integer : ")))
    print(mlist)
    newlist = sort(mlist)
    print(newlist)
main()