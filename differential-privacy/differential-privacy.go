package main

import (
	"fmt"
	"log"

	dp "github.com/google/differential-privacy/go"
)

func main() {
	// Original data
	data := []int64{1, 2, 3, 4, 5}

	// Compute the sum in a differentially private manner
	epsilon := 1.0
	delta := 0.05
	budget := dp.NewPrivacyBudget(epsilon, delta)
	sumParams := &dp.SumInt64Params{
		Epsilon:         budget.Epsilon,
		Delta:           budget.Delta,
		MaxPartitionsContributed: 1,
		MaxContributionsPerPartition: 1,
		Lower:           0,
		Upper:           10,
	}

	result, err := dp.SumInt64(data, sumParams)
	if err != nil {
		log.Fatalf("dp.SumInt64 failed: %v", err)
	}

	fmt.Printf("Differentially private sum is %d\n", result)
}
