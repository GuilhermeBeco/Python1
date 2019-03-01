def main():
    nums=[1,10,5,7,15,11,16,9,4]
    total=0
    numOfNums=len(nums)
    media=0
    for counter in range(0,numOfNums):
        total=total+nums[counter]
    media=total/numOfNums
    print("A media é de {0}".format(media))
