def save_data(lines):
    if len(lines) == 0:
        return
    with open('measurements_result.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)