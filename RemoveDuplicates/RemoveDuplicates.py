# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def RemoveDuplicates(dlist:list):
        """
        Returns the array without duplicates.
        """
        dlist.sort()
        main =[]
     
        for i in range(len(dlist)):
            try:
                if dlist[i] != dlist[i+1]: 
                    main.append( dlist[i])
            except:pass
            
        return main
                
            
         

List1 = [1,2,5,1,5,2,3,1,9,10,11]
List2 = ['a','b','c','d','e','f','g','h','i','j','k']
answer = programmingAlgorithms.RemoveDuplicates(List1)
print(answer)