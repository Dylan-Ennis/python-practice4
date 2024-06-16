# function 1
def max_num(a,b,c):
    return max([a,b,c])

print(max_num(10,37,25))

# function 2
def mult_list(list):
  if len(list) == 0:
    return 0
 
  prod = list[0]

 
  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i

  return prod

print(mult_list([5,10,2]))
print(mult_list([5,10]))
print(mult_list([5]))
print(mult_list([]))

# function 3
def rev_string(my_str):
  return my_str[::-1]
# not sure why ::-1 works
print(rev_string("abc d"))


# function 4
def num_within(a,b,c):
  return a in range(b,c+1)

print(num_within(1,2,3))
print(num_within(2,1,3))

# function 5

# this was extremely difficult for me without looking at the solution code! not sure if it was supposed to be easy but I was struggling. I just had to use the code in parts and then make sense of it after using the comments.

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)


pascal(0)

pascal(5)
