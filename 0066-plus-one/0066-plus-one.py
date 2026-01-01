class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        liczba =0
        for i in range(0,len(digits)):
            liczba=liczba+((10**(len(digits)-i-1))*digits[i])

        liczba=liczba+1

        tablica=[]
        while liczba>0:
                tablica.append(liczba%10)
                liczba//=10
        return(tablica[::-1])

        
            
        