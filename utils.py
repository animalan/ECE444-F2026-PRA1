class utils:
    @staticmethod
    def reversed(num: int) -> int:
        sign = -1 if num < 0 else 1
        num = abs(num)
        reversed_num = int(str(num)[::-1])
        return sign * reversed_num

    @staticmethod
    def formatter(num: int) -> tuple[str, str]:
        return bin(num), oct(num)
