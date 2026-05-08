class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted_s = self.extractAlphanumeric(s)
        n = len(extracted_s)
        for i in range(0, n//2):
            if extracted_s[i] != extracted_s[n-i-1]:
                return False
        
        return True




    def extractAlphanumeric(self, s: str) -> str:
        response = ""
        alphanumerics = self.getAlphanumerics()
        for char in s:
            if char.lower() in alphanumerics:
                response += char.lower()

        return response
    
    def getAlphanumerics(self) -> set:
        return {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r", 
            "s", 
            "t", 
            "u", 
            "v",
            "w", 
            "x", 
            "y", 
            "z"
        }

