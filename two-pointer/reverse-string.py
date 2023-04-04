def reverse(string):
   stringList = list(string)
   left = 0
   right = len(string) - 1
   newList = stringList.copy()
   while left < right:
       stringList[left] = stringList[right]
       stringList[right] = newList[left]
       left += 1
       right -= 1
   return ''.join(stringList)
print(reverse('hello world'))
