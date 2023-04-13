import unittest

def highest_number(nums):
  filtered_list = []
  for n in nums:
    if n != '!':
      filtered_list.append(n)
  mapping_my_list = list(map(int, filtered_list))  
  return max(mapping_my_list)

class SimpleTestCase(unittest.TestCase):
  def testA(self):
    assert highest_number([1,-2,-4,-5]) == 1

  def testB(self):
       assert highest_number([5]) == 5
    
  def testC(self):
    assert highest_number([5.4,46597384]) == 46597384
  
  def testD(self):
    assert highest_number([1,2,3,4, '6']) == 6
  
  def testE(self):
    assert highest_number([1,'2',3,4, '6']) == 6  

  # def testF(self):
  #   print(highest_number([-1,'2',-3, '6', '!']))
  #   assert highest_number([-1,'2',-3, '6', '!']) == 6 
    
if __name__ == "__main__":
  unittest.main() # run all tests       
