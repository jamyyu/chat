
lines = []
with open('3.txt', 'r', encoding ='utf-8-sig') as f: #allen前面有自動存的怪東西編碼加-sig去除
    for line in f:
        lines.append(line.strip())
    


for line in lines:
    s = line.split('')
    time = s[0][:5] #s[0]的前5個 str字串可以當作清單
    name = s[0][5:]
    print(name)

