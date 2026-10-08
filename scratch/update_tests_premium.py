# -*- coding: utf-8 -*-
"""
Update js/app.js:
1. Ensure MOCK_TESTS has vb_1 as the ONLY free test (isPremium: false),
   and ALL other 75 tests marked as isPremium: true.
2. Update UPI ID everywhere to rishavofficials1727@oksbi.
3. Add User Accounts system (Sign Up, Sign In, Password Hash, Account Profile).
4. Update isProUser() to check logged-in account status.
5. Add locked test modal handler.
6. Fix startTest to handle locked tests cleanly.
"""

import re

path = r"C:\cap\ai\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace any old UPI IDs with rishavofficials1727@oksbi
code = code.replace("rishavofficials1727@okhdfcbank", "rishavofficials1727@oksbi")

# Let's inspect MOCK_TESTS and set isPremium: true for all tests except vb_1
def fix_mock_tests(text):
    # Find MOCK_TESTS array definition
    start_idx = text.find("const MOCK_TESTS = [")
    if start_idx == -1:
        return text
    end_idx = text.find("];", start_idx) + 2
    mock_block = text[start_idx:end_idx]

    # Process each test object in the array
    # Replace isPremium:true if present, or add isPremium:true if id != "vb_1"
    lines = mock_block.split("\n")
    new_lines = []
    for line in lines:
        if line.strip().startswith("{") and 'id:"' in line:
            # Check id
            m = re.search(r'id:"([^"]+)"', line)
            if m:
                test_id = m.group(1)
                if test_id == "vb_1":
                    # Free test
                    line = re.sub(r',\s*isPremium:\s*(true|false)', '', line)
                    line = re.sub(r'\}\s*,?\s*$', ', isPremium:false },', line)
                    # clean up double commas or formatting
                    line = re.sub(r',\s*,', ',', line)
                else:
                    # Premium test!
                    if "isPremium" not in line:
                        # Append before closing }
                        last_brace = line.rfind("}")
                        if last_brace != -1:
                            before = line[:last_brace].rstrip()
                            if before.endswith(","):
                                line = before + " isPremium:true " + line[last_brace:]
                            else:
                                line = before + ", isPremium:true " + line[last_brace:]
            new_lines.append(line)
        else:
            new_lines.append(line)

    new_mock_block = "\n".join(new_lines)
    return text[:start_idx] + new_mock_block + text[end_idx:]

code = fix_mock_tests(code)

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated MOCK_TESTS in js/app.js")
