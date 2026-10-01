class Member:
    """
    https://pilab-textbook.fly.dev/#/python/lab/py-lab10b-classvar

    가입할 때마다 번호가 1부터 자동으로 붙는 회원.

    번호를 매기려면 "지금까지 몇 명 가입했는가"를 어딘가 적어둬야 합니다.
    그 자리는 **인스턴스가 아니라 클래스**입니다 — 회원 한 명이 아니라
    Member 전체가 아는 값이니까요.
    """

    # 여기에 "지금까지 몇 명"을 담을 클래스 변수를 만드세요
    count = 0

    def __init__(self, name):
        if not Member.is_valid_name(name):
            print("이름은 두 글자 이상이어야 합니다.")
            # raise ValueError()
            return

        self.name = name
        # 가입할 때마다 하나 늘리고, 그 번호를 자기 번호로 삼습니다
        Member.count += 1
        self.number = self.count

    def get_info(self):
        print(f"이름: {self.name}, 번호: {self.number}")

    @classmethod  # 클래스 변수에 접근
    def total(cls):
        """지금까지 가입한 사람 수를 돌려줍니다."""
        return cls.count

    @staticmethod
    def is_valid_name(name: str):
        """이름은 두 글자 이상이어야 합니다."""
        return len(name) >= 2


minsoo = Member("민수")
yeonwoo = Member("연우")
jiiho = Member("지호")

# print(minsoo.number)
yeonwoo.get_info()
print(jiiho.number)

print("전체 회원 수: ", Member.total())
