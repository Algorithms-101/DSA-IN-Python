# Name: Teddy Oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free to contact for enquires or more info

class programmingAlgorithms:
    """
    Programming Algorithms To Make Your Codes More Effective.
    """
    def flatten2DList(dlist:list):
        """
        Reducing the dimensionality of a 2D Array.
        """
        listlen = len(dlist)
        main = []
        for i in range(listlen):
            for j in range(len(dlist[i])):
                main.append(dlist[i][j])
        return main

List3D1 = [[1,2,3],[4,5],[6,7,8],[9,10,11]]
List3D2 = [['a','b','c'],['d','e'],['f','g','h'],['i','j','k']]
answer = programmingAlgorithms.flatten2DList(List3D2)
print(answer)