"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            times = {
                "00": "Twelve",
                "01": "One",
                "1": "One",
                "02": "Two",
                "2": "Two",
                "03": "Three",
                "3": "Three",
                "04": "Four",
                "4": "Four",
                "05": "Five",
                "5": "Five",
                "06": "Six",
                "6": "Six",
                "07": "Seven",
                "7": "Seven",
                "08": "Eight",
                "8": "Eight",
                "09": "Nine",
                "9": "Nine",
                "10": "Ten",
                "11": "Eleven",
                "12": "Twelve",
                "13": "Thirteen",
                "14": "Fourteen",
                "15": "Fifteen",
                "16": "Sixteen",
                "17": "Seventeen",
                "18": "Eighteen",
                "19": "Nineteen",
                "20": "Twenty",
                "30": "Thirty",
                "40": "Fourty",
                "50": "Fifty",
            }

            if(input_time[:2] != "00"):
                h = int(input_time[:2])
            h = "00"
            m = input_time[3:]
            suffix = "am"
            if(int(h) >= 12): suffix = "pm"
            if(int(h) > 12): h -= 12

            hour = times[str(h)]

            if(int(m) >= 20):
                minuites = times[str(input_time[3:4] + "0")] + " "
                minuites += times[str(int(m) % 10)] + " "
            elif(int(m) >= 10):
                minuites = times[m] + " "
            else:
                minuites = "oh " + times[m] + " "

            if(minuites == "Twelve" or minuites == "oh Twelve "): minuites = ""

            final = hour + " " + minuites + suffix
            return "It's " + final.lower()

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        