# ____________________________________________________
# Topic 1: String Operations — Split, Sort, Join
# _________________________________________________________



from operator import le


# climate = "Python is a powerful programming language"

# rain=climate.split()
# print(rain)

# sorted_rain=sorted(rain, key=len)
# print(sorted_rain)

# result = " ".join(sorted_rain)
# print(result)



# _________________________________________________________________
# Topic 2: Nested Lists (Matrix) and Loops
# _________________________________________________________________

# data=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# k=0
# for i in data:
#     print(i[k])
#     k+=1
    
# k=2
# for j in data:
#     print(j[k])
#     k-=1

#  _________________________________________________________________
# Topic 3: Function & Algorithm — Diagonal Difference
# _________________________________________________________________

# def diagonal_difference(matrix):
#     n = len(matrix)
#     primary = 0
#     secondary = 0

#     for i in range(n):
#         primary += matrix[i][i]               # ↘ diagonal
#         secondary += matrix[i][n - i - 1]     # ↙ diagonal

#     return abs(primary - secondary)


# # Example Input
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [9, 8, 9]
# ]

# print(diagonal_difference(matrix))  # Output: 2




    