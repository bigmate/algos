package atoi

import (
    "strings"
)

func Atoi(str string) int {
    valid, sign, result := validate(str)
    if !valid {
        return 0
    }
    var MAX int = (1 << 31) - 1
    var MIN int = -1 << 31
    var MAX_LEN = 10
    if len(result) > MAX_LEN {
        if sign == -1 {
            return MIN
        }
        return MAX
    }
    var NUM int
    var power int
    var base float64 = 10
    for i:=len(result) - 1; i >= 0; i-- {
        NUM += int(result[i]) * int(pow(base, power))
        power++
        if sign == -1 && NUM * sign < MIN {
            return MIN
        } else if sign == 1 && NUM > MAX {
            return MAX
        } 
    }
    return NUM * sign
}

func validate(str string) (valid bool, sign int, result []uint8) {
    str = strings.Trim(str, " ")
    sign = 1
    if len(str) == 0 {
        return false, sign, result
    }
    switch str[0] {
        case '-':
            str = str[1:]
            sign = -1
        case '+':
            str = str[1:]
    }
    for i:=0; i < len(str) && str[i] >= '0' && str[i] <= '9'; i++ {
        if len(result) == 0 && str[i] == '0' {
            continue
        }
        result = append(result, str[i] - '0')
    }
    
    if len(result) == 0 {
        return false, sign, result 
    }
    
    return true, sign, result
}

func pow(x float64, n int) float64 {
	if n == 0 || x == 1 || (x == -1 && n % 2 == 0) {
		return 1
	}
	if x == -1 {
		return x
	}
	if n < 0 {
		x = 1 / x
        n *= -1
	}
	var product float64 = x
	var result float64 = 1
	cp := 1
	for cp != n {
		cp += cp
		if cp > n {
			n = n - (cp / 2)
			cp = 1
			result *= product
			product = x
			continue
		}
		product *= product
	}
	return result * product
}
