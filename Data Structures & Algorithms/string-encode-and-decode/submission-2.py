class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ''
        for st in strs:
            en=en + st + "₹"
        return en


    def decode(self, s: str) -> List[str]:
        res=s.split("₹")
        return res[:-1]

