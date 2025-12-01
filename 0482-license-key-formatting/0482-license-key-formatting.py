class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        string = s.replace('-', '').upper()
        mod = len(string) % k
        parts = []
        if mod > 0:
            parts.append(string[:mod])
        for i in range(mod, len(string), k):
            parts.append(string[i:i+k])
        return '-'.join(parts)