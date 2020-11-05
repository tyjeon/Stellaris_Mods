# 00_focus.txt 다루기

## 1. 모디파이어는 factor 와 조건문 두 개만 적어야 한다.
```
modifier = {
	factor = 3
	is_unemployed = yes # 코드는 여기까지만 읽는다.
	has_job = servant # 이건 적용이 안 된다.
}

modifier = {
	factor = 3
	AND = { # 좋은 예시
		is_unemployed = yes
		has_job = servant
    }
}
```

# 2. (1번과 연결됨) 최초 논리문(OR, AND...) 안에는 직접적인 조건문이 들어가선 안 된다.
```
# 아래처럼 쓰면 안 됨.
modifier = {
	factor = 2
	OR = {
		has_designation = col_capital
		has_designation = col_rural
	}
}

# 아래처럼 적어야 정상작동함.
modifier = {
	factor = 2
	OR = {
		OR = {
			has_designation = col_capital
			has_designation = col_rural
		}
	}
}
```

## 3. is_ai = no 대신 owner = { is_ai = no } 를 써야 한다.
```
modifier = {
	factor = 3
	AND = { # 이러면 이 모디파이어 자체가 기능을 안 한다.
		is_unemployed = yes
		is_ai = no
    }
}

modifier = {
	factor = 3
	AND = {
		is_unemployed = yes
		owner = { is_ai = no } # 이렇게 써야 한다. 망겜수준;
    }
}
```
