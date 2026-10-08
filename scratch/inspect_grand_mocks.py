import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section id="grand-mocks".*?</section>', text, re.DOTALL)
if m:
    print("Found grand-mocks section, length:", len(m.group(0)))
    lines = m.group(0).split('\n')
    for line in lines[:50]:
        print(line)
