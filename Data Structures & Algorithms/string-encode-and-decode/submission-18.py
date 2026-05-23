class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for str in strs:
            encoded_str = f"{encoded_str}{len(str)}#{str}"

        return encoded_str


    def decode(self, s: str) -> List[str]:

        print(s)

        res, i = [], 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
            
            
            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]

            res.append(string)
            i = j +1 + length

            j += 1

            



            # for j in range(i, len(s)):

            #     if s[j] == "#":

                    
            #         length = int(s[j -1])

            #         string = s[j + 1: j + 1 + length]

            #         print(f"j = {j}")
            #         print(f"s[j] = {s[j]}")
            #         print(f"string= {string}")

            #         res.append(string)

            #         # 3#foo3#bar
            #         # j = 1
            #         # length = 3
            #         # string = s[2:5]

            #         i = j +1 + length

            #         next


        return res
