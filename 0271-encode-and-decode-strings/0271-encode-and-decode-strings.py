class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = '!#%&(@$^*)'.join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        s = s.split('!#%&(@$^*)')
        return s