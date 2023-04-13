import unittest

def highest_number(nums):
  nums = [int(i) for i in nums]
  
  for x in range(len(nums) -1):
    min_var = min(nums)
    nums.remove(min_var)
  return nums[0]

class SimpleTestCase(unittest.TestCase):
  def testA(self):
    assert highest_number([1,-2,-4,-5]) == 1

  def testB(self):
    assert highest_number([5]) == 5
    
  def testC(self):
    assert highest_number([5,46597384]) == 46597384
  
  def testD(self):
    assert highest_number([1,2,3,4, '6']) == 6
  
  def testE(self):
    assert highest_number([1,'2',3,4, '6']) == 6  

  #def testF(self):
    #print(highest_number([-1,'2',-3, '6', '!']))           
    #assert highest_number([-1,'2',-3, '6', '!']) == 6 
    
if __name__ == "__main__":
  unittest.main() # run all tests       
