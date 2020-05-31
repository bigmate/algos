package pow

func Pow(x float64, n int) float64 {
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
