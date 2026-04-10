class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t, slide_window = {}, {}
        for c in t:
            count_t[c]= 1+ count_t.get(c,0)
        need = len(count_t)
        have = 0
        res = [-1,-1]
        res_length = float('inf')
        left  = 0
        for right in range(len(s)):
            c = s[right]
            slide_window[c] = 1 + slide_window.get(c,0)
            #  check wheather currently a criteria has been meet
            if c in count_t and slide_window[c] == count_t[c]:
                have +=1
            while have == need:
                #possible move the left pointer keeping right where it is 
                # the current window is a valid window
                if (right-left+1) < res_length:
                    res = [left,right]
                    res_length = (right -left+1)
                #Move the left pointer
                #Slidewoindow slide_window[s][left] decrement
                # have has to be decremented
                slide_window[s[left]] -= 1
                if s[left] in count_t and slide_window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
            
        left, right = res

        return s[left:right+1] if res_length != float('inf') else ''
