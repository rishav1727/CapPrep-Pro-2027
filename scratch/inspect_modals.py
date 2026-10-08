import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

print("--- Checking Navbar & Buttons in index.html ---")
navbar_match = re.search(r'<nav.*?</nav>', html, re.DOTALL)
if navbar_match:
    print("Navbar HTML:\n", navbar_match.group(0))

print("\n--- Checking Upgrade / Sign In / Pro buttons across index.html ---")
for line in html.split('\n'):
    if any(k in line.lower() for k in ['upgrade', 'sign in', 'signin', 'login', 'pro pass', 'unlock', 'onclick']):
        if 'class=' in line or 'button' in line or 'onclick' in line or 'modal' in line:
            print(line.strip())

print("\n--- Checking Modals in index.html ---")
modal_ids = re.findall(r'id=["\']([^"\']*modal[^"\']*)["\']', html, re.IGNORECASE)
print("Modal IDs in HTML:", modal_ids)

print("\n--- Checking Modal Open/Close Functions in app.js ---")
fn_defs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', app_js)
print("Functions in app.js:", [f for f in fn_defs if 'modal' in f.lower() or 'signin' in f.lower() or 'login' in f.lower() or 'upgrade' in f.lower() or 'pro' in f.lower() or 'pay' in f.lower()])
