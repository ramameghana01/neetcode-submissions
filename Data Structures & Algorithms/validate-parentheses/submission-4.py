class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        brackets={'}':'{',']':'[',')':'('}

        for i in s:
            if i in brackets:
                if st and st[-1]==brackets[i]:
                  st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False
                



        