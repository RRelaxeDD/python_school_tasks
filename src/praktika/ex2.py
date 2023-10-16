results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = list(set(results))
print(f"top 3: {sorted_results[-3:]}")
print(f"worst 3: {sorted_results[:3]}")
print(f"start from 10: {results[9:]}")