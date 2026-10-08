import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check how MOCK_TESTS is written
# We will modify MOCK_TESTS so:
# Stage 1: vb_1: isPremium: false, vb_2: isPremium: false, others isPremium: true
# Stage 2A: ai_1: false, ai_2: false, others: true
# Stage 2B: dbg_1: false, dbg_2: false, others: true
# Stage 3: aic_1: false, aic_2: false, others: true
# Stage 4: sit_1: false, sit_2: false, others: true
# Stages 5-6: int_1: false, int_2: false, others: true
# Grand Mocks: full_1: false, full_2: false, others: true

# Also check for stage-wise grand mocks in MOCK_TESTS
# Let's inspect where MOCK_TESTS starts and ends
m = re.search(r'const MOCK_TESTS = \[(.*?)\];\s*function', text, re.DOTALL)
if not m:
    print("Could not find MOCK_TESTS")
    sys.exit(1)

print("Found MOCK_TESTS, length:", len(m.group(1)))
