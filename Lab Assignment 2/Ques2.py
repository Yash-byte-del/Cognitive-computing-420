scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
high_score=max(scores)
print(high_score)
high_index = scores.index(high_score)
print(high_index)

lowest_score = min(scores)
print(lowest_score)
lowest_count = scores.count(lowest_score)
print(lowest_count)

reversed_scores = list(reversed(scores))
print(f"The reversed tuple as a list is: {reversed_scores}")

user_score=int(input('Enter a score: '))
if user_score in scores:
    first_index = scores.index(user_score)
    print(f"{user_score} found at index {first_index}")
else:
    print(f"{user_score} is not present.")