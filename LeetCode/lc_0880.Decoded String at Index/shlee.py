class Structure:
    def __init__(self, s, repeat: int, rest: str):
        self.inner = s
        self.repeat = repeat
        self.rest = rest
        #print("structure ",s,repeat,rest)
    def __len__(self):
        #print("len of ",self.inner, self.repeat, " = ",len(self.inner)*self.repeat)
        return len(self.inner)*self.repeat + len(self.rest)
    def __getitem__(self,key):
        #print(key, self.inner, len(self))
        if key < len(self.inner)*self.repeat:
            key%=len(self.inner)
            return self.inner[key]
        else:
            return self.rest[key - len(self.inner)*self.repeat]
            
    
class Solution:
    def isDigit(self, s: str):
        return s in ['0','1','2','3','4','5','6','7','8','9']
    def decodeAtIndex(self, s: str, k: int) -> str:
        index = 0
        isStruct = False
        struct = ""
        repeat = 0
        i=0
        while index <= k-1 :
            if self.isDigit(s[i]):
                count = 1
                count2 = 1
                repeat = int(s[i])
                while i+count < len(s) and self.isDigit(s[i+count]):
                    repeat*=int(s[i+count])
                    count+=1
                while i+count+count2<len(s) and not self.isDigit(s[i+count+count2]):
                    count2+=1
                struct = Structure(struct if isStruct else s[:i], repeat, s[i+count:i+count+count2])
                i = i+count
                isStruct = True
                index = len(struct)+count
            else:
                index+=1
                i+=1
        if type(struct) is str:
            return s[k-1]
        else:
            return struct[k-1]