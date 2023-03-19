#python3
def build_heap(data):
    swaps = []
    #TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for k in data:
        for i in range(len(data)//2,-1,-1):
            left=2*i+1
            if 2*i+2<len(data):
                right=2*i+2
                if data[left]<=data[right]:
                    if data[left]<data[i]:
                        swaps.append(i)
                        swaps.append(left)
                        temp=data[i]
                        data[i]=data[left]
                        data[left]=temp
                        #print(data[i])
                else:
                    if data[right]<data[i]:
                        swaps.append(i)
                        swaps.append(right)
                        temp=data[i]
                        data[i]=data[right]
                        data[right]=temp
                        #print(data[i])
    #print(data)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    choise=input()
    if choise=='I':

        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
        swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
        print(len(swaps)//2,sep='')
        for i in range(0,len(swaps),2):
            print(swaps[i], swaps[i+1],sep=' ')
            
    elif choise=='F':
        filename=input()
        filename="tests/"+filename
        with open(filename,"r",encoding="utf8") as f:
            n=f.readlines()[0]
        with open(filename,"r",encoding="utf8") as f:
            data=list(map(int,f.readlines()[1].split()))
            #print(data)
        #assert len(data) == n
        grandlen=0
        for i in range(0,len(data),100):
            part1000=data[i:i+100]
            swaps = build_heap(part1000)
            grandlen=grandlen+len(swaps)//2
        print(grandlen)
    pass
if __name__ == "__main__":
    main()
