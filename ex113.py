#이진검색.
#list 가 기본적으로 정렬이 되어있어야 한다.

def recursiveBinarySearch(lst,key):
    low = 0
    high = len(lst)-1
    return recursiveBinarySearchHelper(lst,key,low,high)

def recursiveBinarySearchHelper(lst,key,l,h):
    if l>h:     #만약 근접해도 일치하는 항목이 없으면 결과적으로 l>h가 되는 현상이 발생하게 된다.
        return -l-1     #return 음수 값의 abs가 원래 찾는 수가 있어야 할 자리 !

    mid = (l+h)//2
    if key<lst[mid]:
        return recursiveBinarySearchHelper(lst,key,l,mid-1)
    elif key == lst[mid]:
        return mid
    else:
        return recursiveBinarySearchHelper(lst,key,mid+1,h)

def main():
    lst = [3,5,6,8,9,12,34,36]
    print(recursiveBinarySearch(lst,3))
    print(recursiveBinarySearch(lst,4))

main()