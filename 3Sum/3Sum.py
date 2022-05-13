# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info
class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def Sum3(dlist:list,target):
        """
        Returns the 3 objects in an array whose sum equals a desired target.
        """
        main = []
        for i in range(len(dlist)):
            for j in range(len(dlist)):
                for k in range(len(dlist)):
                    if dlist[i]+dlist[j] +dlist[k] == target:
                         
                        return dlist[i],dlist[j],dlist[k]
                    
                    else:pass
             
             
                
            
         

List1 = [1,2,3,4,5,6,7,8,9,10,11]
 
answer = programmingAlgorithms.Sum3(List1,14)
print(answer)