class Solution:
    def romanToInt(self, s: str) -> int:
        
        '''Symbol       Value
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000'''

        grand_total = 0
        i = 0

        while i < len(s):
            if s[i] == "M":
                grand_total += 1000
                i += 1

            elif s[i] == "D":
                grand_total += 500
                i += 1

            elif s[i] == "C":
                if i + 1 < len(s) and s[i+1] == "D":
                    grand_total += 400
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "M":
                    grand_total += 900
                    i += 2
                else:
                    grand_total += 100
                    i += 1

            elif s[i] == "L":
                grand_total += 50
                i += 1

            elif s[i] == "X":
                if i + 1 < len(s) and s[i+1] == "L":
                    grand_total += 40
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "C":
                    grand_total += 90
                    i += 2
                else:
                    grand_total += 10
                    i += 1

            elif s[i] == "V":
                grand_total += 5
                i += 1

            elif s[i] == "I":
                if i + 1 < len(s) and s[i+1] == "V":
                    grand_total += 4
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "X":
                    grand_total += 9
                    i += 2
                else:
                    grand_total += 1
                    i += 1

        print(f"{s} = {grand_total}")
        return grand_total

    def romanToInt2(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
