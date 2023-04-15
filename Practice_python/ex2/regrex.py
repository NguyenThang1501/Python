import re

regex = re.compile(r'<[^>]+>')
def remove_html(data):
    return regex.sub('', data)

def remove_numbers(data):
    return re.sub(r'[~^0-9]', '', data)

with open('C:\\Users\\Thang Laptop\\Desktop\\test.csv','r') as input_file:
    data = input_file.read()
    data = remove_html(remove_numbers(data))
        
with open('C:\\Users\\Thang Laptop\\Desktop\\output.csv', mode='w') as output_file:
    output_file.write(data)
