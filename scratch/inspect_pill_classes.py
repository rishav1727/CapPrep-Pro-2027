import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pill_matches = re.findall(r'<button[^>]*class="[^"]*test-pill-btn[^"]*"[^>]*>(.*?)</button>', text, re.DOTALL)
print(f'Total test-pill-btn buttons: {len(pill_matches)}')
for i, m in enumerate(pill_matches[:5]):
    print(f'Pill {i}: {m}')

card_matches = re.findall(r'<div[^>]*class="[^"]*test-card[^"]*"[^>]*>(.*?)</div>', text, re.DOTALL)
print(f'Total test-card elements: {len(card_matches)}')
for i, m in enumerate(card_matches[:3]):
    print(f'Card {i}: {m[:200]}')
