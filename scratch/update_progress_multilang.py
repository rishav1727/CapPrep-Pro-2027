import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('PROGRESS.md', 'r', encoding='utf-8') as f:
    text = f.read()

multilang_note = '''
14. **Full Multi-Language Support for Debugging & AI-Assisted Coding (C, C++, Java, Python)**:
    - **Debugging Assessment (`modules/debug_sim.html`)**:
      - Added dynamic real-time language switcher (`C (GCC 11.3)`, `C++ 20`, `Java 17`, `Python 3.10`) for all 10 debugging problems.
      - Each problem includes authentic language-specific buggy code, function signatures, compiler/runtime diagnostics, language-specific hints, and automated multi-testcase validation.
    - **AI-Assisted Coding Assessment (`modules/ai_coding_sim.html`)**:
      - Added dynamic language switcher (`C`, `C++`, `Java`, `Python`) across all 10 scaffolding vibe coding problems.
      - Synchronizes problem signatures, starter code templates, AI generated code snippets, and multi-language testcase validators on the fly.
'''

if "Full Multi-Language Support" not in text:
    text = text.replace("## 🎯 Current Operational Status", multilang_note + "\n## 🎯 Current Operational Status")

with open('PROGRESS.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated PROGRESS.md with Multi-Language support!")
