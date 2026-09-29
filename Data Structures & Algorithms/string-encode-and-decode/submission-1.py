class Solution:

    def encode(self, strs: List[str]) -> str:
        cc = ""
        
        for i in strs:
            cc += i + "\"\""

        print(cc)
        return cc

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("\"\"")[:-1]