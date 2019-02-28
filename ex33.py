def main():
    nums = [1,3,10,2,15,0]

    num=0
    for counter in range(0,len(nums)):
        if counter==0:
            num=nums[counter]
        else:
            if nums[counter]>num:
                num=nums[counter]
    print("O maior valor da lista é {0}".format(num))
