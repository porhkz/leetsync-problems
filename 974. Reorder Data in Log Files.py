class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []

        for log in logs:
            content = log.split(' ', 1)[1]

            if content[0].isalpha():
               letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda letter: (letter.split(' ', 1)[1], letter.split(' ', 1)[0]))

        return letters + digits