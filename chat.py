def read_file():
    with open("input.txt", 'r', encoding='etf-8') as f:
        for line in f: 
            lines.append(line)
    return lines
print(lines)w