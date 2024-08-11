'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


def permute(nums):
    result=[]
    if len(nums)==1:
        return [nums.copy()]
    for i in range(len(nums)):
        n=nums.pop(0)
        perms=permute(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result
nums = [1, 2, 3]
print(permute(nums))