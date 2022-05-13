# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def MultiplyArray(dlist:list):
        """
        Returns the total product of the integer objects in a given list.
        """
        main = 1
        for i in range(len(dlist)):
            main*= dlist[i]
        return main
            
                    
        
             
             
                
            
         

List1 = [1,2,3,4,5]
 
answer = programmingAlgorithms.MultiplyArray(List1)
print(answer)