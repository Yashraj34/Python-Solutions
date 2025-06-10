def search(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print("key element is found")
            break
    else:
        print("element is not found")


list1=[34,23,5,6,7,1,23,8]
key=int(input("Enter the key element:"))
search(list1,key)


    