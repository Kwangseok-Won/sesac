def test_오만원이면_무료다(run_solution):
    assert run_solution(cart_total=50000, is_member=False)["shipping"] == 0, (
        "5만원 '이상'이므로 정확히 50000원도 무료입니다."
    )


def test_오만원_넘는_회원도_무료다(run_solution):
    assert run_solution(cart_total=80000, is_member=True)["shipping"] == 0, (
        "회원 여부를 먼저 검사하면 여기서 틀립니다. 무료 조건을 먼저 거르세요."
    )


def test_회원은_이천오백원이다(run_solution):
    assert run_solution(cart_total=25000, is_member=True)["shipping"] == 2500


def test_비회원은_삼천오백원이다(run_solution):
    assert run_solution(cart_total=25000, is_member=False)["shipping"] == 3500


def test_사만구천구백구십구원은_유료다(run_solution):
    assert run_solution(cart_total=49999, is_member=True)["shipping"] == 2500
