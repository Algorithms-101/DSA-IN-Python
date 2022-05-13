# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def BinarySearch(dlist:list,object):
        """
        Returns the index of an object in an array.
        """
         
        for i in range(len(dlist)):
             
            if dlist[i] ==object:
               return '{} found at index {}'.format(object,i)
            elif  dlist[i] !=object:
                pass
            else:
                return '{} not found in array'.format(object)
                
            
         

List1 = [1,2,3,4,5,6,7,8,9,10,11]
List2 = ['a','b','c','d','e','f','g','h','i','j','k']
answer = programmingAlgorithms.BinarySearch(List2,'g')
print(answer)