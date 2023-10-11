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