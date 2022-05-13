# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def LongestConsecutive(object,k):
        """
        Returns the longest consecutive str or int of an object.
        """
        object = str(object)
        main = 0
        for i in range(len(object)):
            #print(i)
            try: 
                if object[i] == object[i+1] :
                   main+=1
            except:pass
        return main
            
      
            
                    
        
             
             
                
            
         

Str = 'teddyddd'
Int = 10001000001001
 
answer = programmingAlgorithms.LongestConsecutive(Int,0)
print(answer)