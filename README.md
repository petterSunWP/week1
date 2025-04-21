# Create a NumPy array of the first 10 positive integers
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the array
print("Array:", arr)

# Print the shape and data type of the array
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

# Multiply each element by 2 and print the result
doubled = arr * 2
print("Doubled array:", doubled)

# Given scores
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1. Average score for each student (row-wise mean)
student_averages = np.mean(scores, axis=1)
print("Average score for each student:", student_averages)

# 2. Average score for each subject (column-wise mean)
subject_averages = np.mean(scores, axis=0)
print("Average score for each subject:", subject_averages)

# 3. Identify the student (row index) with the highest total score
total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)
print("Student with the highest total score (row index):", top_student_index)

# 4. Add 5 bonus points to the third subject (column index 2) for all students
scores[:, 2] += 5
print("Updated scores after adding 5 bonus points to third subject:\n", scores)
