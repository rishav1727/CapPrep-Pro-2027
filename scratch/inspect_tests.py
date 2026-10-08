import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Match objects in MOCK_TESTS
m = re.findall(r'\{\s*id:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*category:\s*"([^"]+)"(.*?)\}', text)
print(f'Total matched: {len(m)}')

categories = {}
for test_id, title, cat, extra in m:
    is_prem = 'isPremium:true' in extra.replace(' ', '')
    categories.setdefault(cat, []).append((test_id, title, is_prem))

for cat, tests in categories.items():
    print(f'\n=== {cat} ({len(tests)} tests) ===')
    for t_id, title, is_prem in tests:
        status = 'LOCKED' if is_prem else 'FREE'
        print(f'  [{status}] {t_id}: {title}')
