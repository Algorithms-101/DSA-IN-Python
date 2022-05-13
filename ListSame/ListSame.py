# Name: Teddy Oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def ListSame(dlist:list):
        """
       Checks if items in a list are all the same.
        """
        
        global main
     
        for i in range(len(dlist)):
            if dlist[0] != dlist[i]:
              main = False
            else: main = True
        return main
                
            
         

List1 = ['a','b','c']
List2 = ['a','a','a']
answer = programmingAlgorithms.ListSame(List2)
print(answer)