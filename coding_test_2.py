# Given an array of integers nums and an integer target, return indices of the two numbers such that 
# they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# You can return the answer in any order.

def find_indices_given_target(nums: list[int], target: int) -> list[int]:
    '''Find two elements in a list of numbers, which sum is a given target number, 
    and return the indices of those elements in a list.

    Args:
        nums (list of int): A list with numbers.
        target (int): The value of the sum.

    Returns:
        list: A list with the indices of elements in nums that add up to target.
    '''
    N = len(nums)
    for i in range(N):
        for j in range(N):
            if i != j and nums[i] + nums[j] == target:
                return [i,j]


if __name__ == "__main__":
    assert find_indices_given_target([2,7,11,15], 9) == [0,1]
    assert find_indices_given_target([3,2,4], 6) == [1,2]
