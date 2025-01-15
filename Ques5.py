#5.1
numbers = [23, 5, 78, 11, 90]
largest = max(numbers)
smallest = min(numbers)
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")


#5.2
name={1:"Yash",2:"Two",3:"Three"}
print(name[1])


#5.3
numbers=[23, 5, 78, 11, 90]
ascending=sorted(numbers)
descending=sorted(numbers, reverse=True)
print(f"Original list:{numbers}")
print(f"Sorted list in ascending order:{ascending}")
print(f"Sorted list in descending order:{descending}")


#5.4
dict1 = {"apple": 120, "banana": 30}
dict2 = {"cherry": 200, "date": 50}
merged_dict = {**dict1,**dict2}
print(f"Merged dictionary: {merged_dict}")
