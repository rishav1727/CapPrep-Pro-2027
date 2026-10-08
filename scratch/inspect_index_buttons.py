import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find buttons calling startTest
matches = re.findall(r'onclick="startTest\(\'([^\']+)\'\)"[^>]*>(.*?)</button>', text, re.DOTALL)
print(f'Total startTest buttons in index.html: {len(matches)}')
for tid, content in matches[:20]:
    clean = re.sub(r'<[^>]+>', ' ', content).strip()
    clean = re.sub(r'\s+', ' ', clean)
    print(f'  {tid}: {clean[:60]}')
