package addBigNums

func addInt(short, long string) string {
	result := ""
	diff := len(long) - len(short)
	var carry uint8 = 0
	var sum uint8 = 0
	for i := len(long) - 1; i >= 0; i-- {
		if i-diff >= 0 {
			sum = carry + long[i] + short[i-diff] - 2*'0'
		} else {
			sum = carry + long[i] - '0'
		}
		if sum > 9 {
			carry = sum / 10
		} else {
			carry = 0
		}
		result = string(sum%10+'0') + result
	}
	if carry > 0 {
		result = string(carry+'0') + result
	}
	return result
}

func addFraction(short, long string) (string, string) {
	result := addInt(short, long[:len(short)]) + long[len(short):]
	if len(result) > len(long) {
		return result[0:1], result[1:]
	}
	return "0", result
}

func add(a, b string) string {
	compoundA := strings.Split(a, ".")
	compoundB := strings.Split(b, ".")
	if len(compoundA) < 2 {
		compoundA = append(compoundA, "0")
	}
	if len(compoundB) < 2 {
		compoundB = append(compoundB, "0")
	}
	sum := ""
	wholePart, fraction := "", ""
	if len(compoundA[0]) < len(compoundB[0]) {
		sum = addInt(compoundA[0], compoundB[0])
	} else {
		sum = addInt(compoundB[0], compoundA[0])
	}
	if len(compoundA[1]) < len(compoundB[1]) {
		wholePart, fraction = addFraction(compoundA[1], compoundB[1])
	} else {
		wholePart, fraction = addFraction(compoundB[1], compoundA[1])
	}
	i:=len(fraction)-1
	for  i >= 0 && fraction[i] == '0' {
		i--
	}
	fraction = fraction[:i+1]
	sum = addInt(wholePart, sum)
	j := 0
	for j < len(sum) - 1 && sum[j] == '0' {
		j++
	}
	sum = sum[j:]
	if len(fraction) > 0 {
		sum = sum + "." + fraction
	}
	return sum
}
