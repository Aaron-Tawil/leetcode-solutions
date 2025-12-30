class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Key: character, Value: first index seen OR float('inf') if duplicate
        char_map = {}
        
        # Only one pass over the potentially long string 's'
        for i, char in enumerate(s):
            if char not in char_map:
                char_map[char] = i
            else:
                # Mark as duplicate
                char_map[char] = float('inf')
                
        # Iterate over the map values (max 26 entries)
        first_index = min(char_map.values())
        
        return first_index if first_index != float('inf') else -1