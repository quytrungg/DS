# question: given 2d matrix of characters and a string, return whether if string is existed in the matrix
def word_search(matrix, word):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0] \
                and j >= len(word) - 1 and (''.join(matrix[i][j-len(word)+1:j+1]))[::-1] == word \
                or i >= len(word) - 1 and (''.join(matrix[temp][j] for temp in range(i-len(word)+1, i+1)))[::-1] == word \
                or len(matrix[i]) - j + 1 >= len(word) and ''.join(matrix[i][j:j+len(word)]) == word \
                or len(matrix) - i + 1 >= len(word) and ''.join(matrix[temp][j] for temp in range(i, i+len(word)-1)) == word:
                    return True
    return False

matrix = [
  ['F', 'O', 'A', 'I'],
  ['A', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAIU'))
# True