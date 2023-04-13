import unittest

def take_out_second_highest(nums):
  return nums[-2]

def sort_for(nums):
  nums.sort(reverse = True)
  return nums

def filter_for(nums):
  filtered = list(filter(lambda num: isinstance(num,int) ,nums))
  return filtered
  
def second_highest_number(nums):
  if len(nums) <= 1:
    return None
  var1 = filter_for(nums)
  var2 = sort_for(var1)
  return take_out_second_highest(var2)

    
class SimpleTestCase(unittest.TestCase):
  def testA(self):
    assert second_highest_number([1,0,2]) == 1
  
  def testB(self):
    assert second_highest_number([5]) == None
  
  def testC(self):
    assert second_highest_number([5,46597384]) == 46597384
  
  def testD(self):
    assert second_highest_number([1,2,4, '6']) == 2

  def testE(self):
    assert second_highest_number([1,'2',3,4, '6']) == 3  

  #def testF(self):
    #print(highest_number([-1,'2',-3, '6', '!']))           
    #assert highest_number([-1,'2',-3, '6', '!']) == 6 
    
if __name__ == "__main__":
  unittest.main() # run all tests       
