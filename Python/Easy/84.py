def read_lines(filename):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
      return lines
  except FileNotFoundError:
    print('File not found')
    
result = read_lines('file.txt')