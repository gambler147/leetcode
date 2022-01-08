class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
            if len(words[i]) > 2:
                words[i] = words[i][0].upper() + words[i][1:]
        return ' '.join(words)
    
