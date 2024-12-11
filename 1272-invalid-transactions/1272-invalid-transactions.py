from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Parse transactions into a structured format
        parsed = []
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            parsed.append([name, int(time), int(amount), city, i])

        # Sort transactions by name and time
        parsed.sort(key=lambda x: (x[0], x[1]))

        # Group transactions by name
        grouped = defaultdict(list)
        for entry in parsed:
            grouped[entry[0]].append(entry)

        invalids = set()

        # Helper function to mimic bisect_left
        def custom_bisect_left(times, target):
            left, right = 0, len(times)
            while left < right:
                mid = (left + right) // 2
                if times[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for name, records in grouped.items():
            times = [record[1] for record in records]  # Extract times for binary search
            for idx, (name, time, amount, city, i) in enumerate(records):
                # Check if amount exceeds 1000
                if amount > 1000:
                    invalids.add(i)

                # Find the start of the 60-minute range using custom binary search
                start_idx = custom_bisect_left(times, time - 60)
                for j in range(start_idx, idx):  # Only iterate over valid range
                    _, prev_time, _, prev_city, prev_i = records[j]
                    if city != prev_city:  # Different city within 60 minutes
                        invalids.add(i)
                        invalids.add(prev_i)

        # Build results from invalid indexes
        return [transactions[i] for i in sorted(invalids)]
