# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left <= right:
#         if s[left] != s[right]:
#             return False 
#         left = left + 1
#         right = right - 1

#     return True


# # Driver code
# def main():
#     test_cases = ["RACECAR", "ABBA", "TART"]
#     i = 1
#     for s in test_cases:
#         print("Test Case #", i)
#         print(is_palindrome(s))
#         print("-" * 100, end="\n\n")
#         i = i + 1

# if __name__ == '__main__':
#     main()

# def find_sum_of_three(nums, target):

#     nums.sort()

#     for x in range(len(nums)-2):
#         left = x+1
#         right = len(nums) - 1
#         while left < right:
#             current_sum = nums[right]+nums[x]+nums[left]
#             if current_sum == target:
#                 return True
#             elif current_sum > target:
#                 right = right -1
#             else:
#                 left = left +1
#     return False

# def main():
#     nums_lists = [[3, 7, 1, 2, 8, 4, 5],
#                 [-1, 2, 1, -4, 5, -3],
#                 [2, 3, 4, 1, 7, 9],
#                 [1, -1, 0],
#                 [2, 4, 2, 7, 6, 3, 1]]

#     targets = [10, 7, 20, -1, 8]

#     for i in range(len(nums_lists)):
#         print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
#         if find_sum_of_three(nums_lists[i], targets[i]):
#             print("\tSum for", targets[i], "exists")
#         else:
#             print("\tSum for", targets[i], "does not exist")
#         print("-"*100)

# if __name__ == '__main__':
#     main()

# from linked_list import LinkedList
# from linked_list_node import LinkedListNode

# def remove_nth_last_node(head, n):
#     right = head
#     left = head
    
#     for i in range(n):
#         right = right.next

#     if not right:
#         return head.next

#     while right.next:
#         right = right.next
#         left = left.next
    
#     left.next = left.next.next
    
#     return head

# # Driver code
# def main():
#     lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76], [288, 224, 275, 390, 4, 383, 330, 60, 193],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
#     n = [4, 1, 6, 9, 11]

#     for i in range(len(n)):
#         input_linked_list = LinkedList()
#         input_linked_list.create_linked_list(lists[i])
#         print(i+1, ". Linked List:\t", end='')
#         print()
#         print("n = ", n[i])
#         result = remove_nth_last_node(input_linked_list.head, n[i])
#         print("Updated Linked List:\t", end='')
#         print()
#         print("-"*100)

# if __name__ == '__main__':
#     main()

# def is_palindrome(s):

#   start = 0
#   end = len(s)-1

#   while start<=end:
#     if s[start] == s[end]:
#       start +=1
#       end -=1
#     else:
#       start +=1
#       while start <= end:
#         if s[start] == s[end]:
#           start +=1
#           end -=1
#         else:
#           start -=1
#           end -=1
#           while start <= end:
#             if s[start] == s[end]:
#               start +=1
#               end -=1
#             else:
#               return False

#   return True
# print(is_palindrome("madame"))

# def is_happy_number(n):
#     slow = n
#     fast = sum_of_squared_digits(slow)

#     while fast != 1:
#         slow = sum_of_squared_digits(slow)
#         fast = sum_of_squared_digits(sum_of_squared_digits(fast))
#         if fast == slow:
#             return False
    
#     return True

# def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
#     total_sum = 0
#     while number > 0:
#         digit = number % 10
#         number = number // 10
#         total_sum += digit ** 2
#     return total_sum

# def main():
#     inputs = [1, 5, 19, 25, 7]
#     for i in range(len(inputs)):
#         print(i+1, ".\tInput Number: ", inputs[i], sep="")
#         print("\tIs it a happy number? ", is_happy_number(inputs[i]))
#         print("-" * 100)


# if __name__ == '__main__':
#     main()



# def detect_cycle(head):
#   slow = head
#   fast = head

#   while fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if fast == slow:
#         return True

#   return False


# def get_middle_node(head):
#     slow = head
#     fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     return slow
# def find_duplicate(nums):
#     slow = nums[0]
#     fast = nums[0]

#     while True:
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         if slow == fast:
#             break

#     slow = nums[0]
#     while slow != fast:
#         slow = nums[slow]
#         fast = nums[fast]
  
    
#     return fast
# # Driver code
# def main():
#     nums = [
#         [1, 3, 2, 3, 5, 4], 
#         [2, 4, 5, 4, 1, 3], 
#         [1, 6, 3, 5, 1, 2, 7, 4], 
#         [1, 2, 2, 4, 3], 
#         [3, 1, 3, 5, 6, 4, 2]
#     ]
#     for i in range(len(nums)):
#         print(i + 1, ".\tnums = ", nums[i], sep="")
#         print("\tDuplicate number = ", find_duplicate(nums[i]), sep="")
#         print("-" * 100)
# if __name__ == "__main__":
#     main()

# from linked_list import LinkedList

# def palindrome(head):
#     slow = head
#     fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
    
#     reversed_portion = reverse_linked_list(slow)
#     check = check_for_match(head, reversed_portion)

#     return check

# def check_for_match(first, second):
#     while first and second:
#         if first.data != second.data:
#             return False
#         else:
#             first = first.next
#             second = second.next
    
#     return True
    
# def reverse_linked_list(slow_ptr):
#     prev = None
#     next = None
#     curr = slow_ptr
#     while curr is not None:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev

# # Driver code
# def main():
#     input = (
#                 [2, 4, 6, 4, 2],
#                 [0, 3, 5, 5, 0],
#                 [9, 7, 4, 4, 7, 9],
#                 [5, 4, 7, 9, 4, 5],
#                 [5, 9, 8, 3, 8, 9, 5],
#             )
#     j = 1

#     for i in range(len(input)):
#         input_linked_list = LinkedList()
#         input_linked_list.create_linked_list(input[i])
#         print(j, ".\tLinked List:", end=" ", sep="")
#         head = input_linked_list.head
#         print("\n\tIs it a palindrome?", "Yes" if palindrome(head) else "No")
#         j += 1
#         print("-"*100, "\n")


# if __name__ == "__main__":
#     main()

# def merge_intervals(intervals):
#     output = []
#     output.append([intervals[0][0], intervals[0][1]])

#     for i in range(1, len(intervals)):
#         last_added = output[len(output)-1]
#         cur_begin = intervals[i][0]
#         cur_end = intervals[i][1]
#         last_added_end = last_added[1]

#         if cur_begin <= last_added_end:
#             output[-1][1] = max(cur_end, last_added_end)
#         else:
#             output.append([cur_begin, cur_end])


#     return output


# # Driver code
# def main():
    
#     all_intervals = [
#     [[1, 5], [3, 7], [4, 6]],
#     [[1, 5], [4, 6], [6, 8], [11, 15]],
#     [[3, 7], [6, 8], [10, 12], [11, 15]],
#     [[1, 5]],
#     [[1, 9], [3, 8], [4, 4]],
#     [[1, 2], [3, 4], [8, 8]],
#     [[1, 5], [1, 3]],
#     [[1, 5], [6, 9]],
#     [[0, 0], [1, 18], [1, 3]]
#     ]

#     for i in range(len(all_intervals)):
#         print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
#         result = merge_intervals(all_intervals[i])
#         print("   Merged intervals:\t", result)
#         print("-"*100)

# if __name__ == '__main__':
#     main()

# def insert_interval(existing_intervals, new_interval):
#     new_interval_start = new_interval[0]
#     new_interval_end = new_interval[1]

#     output = []
#     i=0
    
#     existing_length = len(existing_intervals)

#     while i < existing_length and existing_intervals[i][0] < new_interval_start:
#         output.append(existing_intervals[i])
#         i+=1

#     if not output or output[-1][1] < new_interval_start:
#         output.append(new_interval)
#     else:
#         output[-1][1] = new_interval_end

#     for i in range(len(existing_intervals)):
#         last_added = output[len(output)-1]
#         cur_begin = existing_intervals[i][0]
#         cur_end = existing_intervals[i][1]
#         last_added_end = last_added[1]

#         if cur_begin <= last_added_end:
#             output[-1][1] = max(cur_end, last_added_end)
#             i +=1
#         else:
#             output.append([cur_begin, cur_end])
#             i+=1

#     return output

# # Driver code
# def main():
#     new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
#     existing_intervals = [
#         [[1, 2], [3, 5], [6, 8]],
#         [[1, 3], [5, 7], [10, 12]],
#         [[8, 10], [12, 15]],
#         [[5, 7], [8, 9]],
#         [[3, 5]]
#     ]
    
#     for i in range(len(new_interval)):
#         print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
#         print("\tNew interval: ", new_interval[i], sep="")
#         output = insert_interval(existing_intervals[i], new_interval[i])
#         print("\tUpdated intervals: ", output, sep = "")
#         print("-"*100)


# if __name__ == "__main__":
#     main()

def intervals_intersection(interval_list_a, interval_list_b):
    results = []
    i = 0
    j = 0

    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])

        if start <= end:
            results.append([start, end])

        if interval_list_a[i][1] < interval_list_b[j][1]:
            i +=1
        else:
            j+=1


    return results

# Driver code
def main():
    input_interval_list_a = [
        [[1, 2]],
        [[1, 4], [5, 6], [9, 15]],
        [[3, 6], [8, 16], [17, 25]],
        [
            [4, 7],
            [9, 16],
            [17, 28],
            [39, 50],
            [55, 66],
            [70, 89],
        ],
        [
            [1, 3],
            [5, 6],
            [7, 8],
            [12, 15],
        ],
    ]
    input_interval_list_b = [
        [[1, 2]],
        [[2, 4], [5, 7], [9, 15]],
        [[2, 3], [10, 15], [18, 23]],
        [
            [3, 6],
            [7, 8],
            [9, 10],
            [14, 19],
            [23, 33],
            [35, 40],
            [45, 59],
            [60, 64],
            [68, 76],
        ],
        [[2, 4], [7, 10]],
    ]

    for i in range(len(input_interval_list_a)):
        print(i + 1, '.\t Interval List A: ', input_interval_list_a[i], sep="")
        print('\t Interval List B: ', input_interval_list_b[i], sep="")
        print("\t Intersecting intervals in 'A' and 'B' are: ", intervals_intersection(input_interval_list_a[i], input_interval_list_b[i]), sep="")

        print('-' * 100)


if __name__ == "__main__":
    main()
