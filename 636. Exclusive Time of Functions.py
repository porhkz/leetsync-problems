class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        prev = 0

        for log in logs:
            log_list = log.split(':')
            func = int(log_list[0])
            status = log_list[1]
            time = int(log_list[2])

            if status == 'start':
                if stack:
                    result[stack[-1]] += time - prev
                stack.append(func)
                prev = time
            elif status == 'end':
                result[stack[-1]] += time - prev + 1
                prev = time + 1
                stack.pop()

        return result

