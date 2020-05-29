package primeNumberGenerator

const (
	prime = iota + 1
	composite
)

type Generator struct {
	sieve []int
	last  int
}

func New(n int) *Generator {
	return &Generator{sieve: make([]int, n), last: 1}
}

func (g *Generator) Next() int {
	g.last++
	for g.last < len(g.sieve) && g.sieve[g.last] != 0 {
		g.last++
	}
	if g.last >= len(g.sieve) {
		return -1
	}
	g.sieve[g.last] = prime
	for i := g.last * 2; i < len(g.sieve); i+=g.last {
		g.sieve[i] = composite
	}
	return g.last
}

func (g *Generator) Count() int {
	count := 0
	for i := 1; i < len(g.sieve); i++ {
		if g.sieve[i] == prime {
			count++
		}
	}
	return count
}
