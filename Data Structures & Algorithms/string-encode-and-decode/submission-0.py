class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "😔"
        return result


    def decode(self, s: str) -> List[str]:
        return s.split("😔")[:-1]
