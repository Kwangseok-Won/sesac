# cart_total 과 is_member 가 주어집니다. 직접 시험해보려면 아래 두 줄의 # 을 지우세요.
cart_total = 25000
is_member = True

if cart_total >= 50000:
    shipping = 0
elif is_member:
    shipping = 2500
else:
    shipping = 3500

###

if cart_total >= 50000:
    shipping = 0
else:
    shipping = 2500 if is_member else 3500
