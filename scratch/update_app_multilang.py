# -*- coding: utf-8 -*-
"""
Add multi-language code transpiler and language selector to js/app.js
"""

path = r"C:\cap\ai\js\app.js"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Define language transpilation engine
lang_engine = """
// ==========================================
// MULTI-LANGUAGE CODE ENGINE (C++, Java, Python, C)
// ==========================================

let currentSelectedLanguage = localStorage.getItem('capprep_preferred_lang') || 'cpp';

function switchQuestionLanguage(lang) {
  currentSelectedLanguage = lang;
  try {
    localStorage.setItem('capprep_preferred_lang', lang);
  } catch(e) {}
  renderQuestion();
  showSecurityToast(`💻 Code syntax switched to ${lang.toUpperCase()}`);
}

function transpileCodeToLang(rawCode, targetLang) {
  if (!rawCode) return '';
  let lines = rawCode.trim().split('\\n');

  if (targetLang === 'python') {
    let pyLines = [];
    for (let rawLine of lines) {
      let line = rawLine.trim();
      if (!line) { pyLines.push(''); continue; }

      if (line.startsWith('#include') || line.startsWith('using namespace') || line.startsWith('package ') || line.startsWith('import java.') || line.includes('class Solution') || line.includes('public class')) {
        continue;
      }
      if (line === '{' || line === '}') continue;

      line = line.replace(/std::cout\\s*<<\\s*(.*?)\\s*<<\\s*std::endl;?/g, 'print($1)');
      line = line.replace(/cout\\s*<<\\s*(.*?)\\s*<<\\s*endl;?/g, 'print($1)');
      line = line.replace(/System\\.out\\.println\\((.*?)\\);?/g, 'print($1)');
      line = line.replace(/System\\.out\\.print\\((.*?)\\);?/g, 'print($1, end="")');
      line = line.replace(/printf\\("([^"]*)",?\\s*(.*?)\\);?/g, 'print($2)');

      line = line.replace(/^(public\\s+|static\\s+|inline\\s+)*(int|void|bool|boolean|string|String|float|double|auto)\\s+(\\w+)\\s*\\((.*?)\\)\\s*\\{?$/g, 'def $3($4):');
      line = line.replace(/(int|bool|boolean|string|String|float|double|auto)\\s+(\\w+)/g, '$2');

      line = line.replace(/^if\\s*\\((.*?)\\)\\s*\\{?$/g, 'if $1:');
      line = line.replace(/^while\\s*\\((.*?)\\)\\s*\\{?$/g, 'while $1:');
      line = line.replace(/^for\\s*\\((\\w+)\\s*=\\s*(\\d+);\\s*\\1\\s*<\\s*(\\w+|\\d+);\\s*\\1\\+\\+\\)\\s*\\{?$/g, 'for $1 in range($2, $3):');
      line = line.replace(/^else\\s*\\{?$/g, 'else:');
      line = line.replace(/^else\\s+if\\s*\\((.*?)\\)\\s*\\{?$/g, 'elif $1:');

      line = line.replace(/nullptr\\b/g, 'None');
      line = line.replace(/NULL\\b/g, 'None');
      line = line.replace(/null\\b/g, 'None');
      line = line.replace(/true\\b/g, 'True');
      line = line.replace(/false\\b/g, 'False');
      line = line.replace(/&&/g, 'and');
      line = line.replace(/\\|\\|/g, 'or');
      line = line.replace(/!(\\w+)/g, 'not $1');

      line = line.replace(/^(int|bool|boolean|string|String|float|double|auto)\\s+(\\w+)\\s*=\\s*/g, '$2 = ');
      line = line.replace(/;\\s*$/g, '');
      line = line.replace(/\\/\\/(.*)/g, '#$1');
      line = line.replace(/[\\{\\}]/g, '').trim();
      if (line) pyLines.push('    ' + line);
    }
    return pyLines.join('\\n') || rawCode;
  }

  if (targetLang === 'java') {
    let javaLines = [];
    for (let rawLine of lines) {
      let line = rawLine;
      if (line.includes('#include') || line.includes('using namespace')) continue;
      line = line.replace(/std::cout\\s*<<\\s*(.*?)\\s*<<\\s*std::endl;/g, 'System.out.println($1);');
      line = line.replace(/cout\\s*<<\\s*(.*?)\\s*<<\\s*endl;/g, 'System.out.println($1);');
      line = line.replace(/nullptr\\b/g, 'null');
      line = line.replace(/NULL\\b/g, 'null');
      line = line.replace(/bool\\b/g, 'boolean');
      line = line.replace(/string\\b/g, 'String');
      line = line.replace(/vector<int>/g, 'ArrayList<Integer>');
      javaLines.push(line);
    }
    return javaLines.join('\\n');
  }

  if (targetLang === 'c') {
    let cLines = [];
    for (let rawLine of lines) {
      let line = rawLine;
      if (line.includes('using namespace') || line.includes('import java.') || line.includes('class Solution')) continue;
      line = line.replace(/std::cout\\s*<<\\s*(.*?)\\s*<<\\s*std::endl;/g, 'printf("%d\\\\n", $1);');
      line = line.replace(/cout\\s*<<\\s*(.*?)\\s*<<\\s*endl;/g, 'printf("%d\\\\n", $1);');
      line = line.replace(/System\\.out\\.println\\((.*?)\\);/g, 'printf("%d\\\\n", $1);');
      line = line.replace(/nullptr\\b/g, 'NULL');
      line = line.replace(/null\\b/g, 'NULL');
      line = line.replace(/None\\b/g, 'NULL');
      line = line.replace(/bool\\b/g, 'int');
      line = line.replace(/boolean\\b/g, 'int');
      line = line.replace(/true\\b/g, '1');
      line = line.replace(/false\\b/g, '0');
      cLines.push(line);
    }
    return cLines.join('\\n');
  }

  // C++ default
  let cppLines = [];
  for (let rawLine of lines) {
    let line = rawLine;
    line = line.replace(/System\\.out\\.println\\((.*?)\\);/g, 'std::cout << $1 << std::endl;');
    line = line.replace(/System\\.out\\.print\\((.*?)\\);/g, 'std::cout << $1;');
    line = line.replace(/boolean\\b/g, 'bool');
    line = line.replace(/null\\b/g, 'nullptr');
    line = line.replace(/None\\b/g, 'nullptr');
    line = line.replace(/True\\b/g, 'true');
    line = line.replace(/False\\b/g, 'false');
    cppLines.push(line);
  }
  return cppLines.join('\\n');
}
"""

# Replace renderQuestion in app.js
old_render_q = """  // Handle code blocks in question text
  let qText = q.q || '';
  let codeHTML = '';
  if (qText.includes('```')) {
    const parts = qText.split('```');
    qText = parts[0].trim();
    if (parts[1]) {
      codeHTML = `<div class="question-code">${escHTML(parts[1].trim())}</div>`;
    }
  }

  document.getElementById('q-text').textContent = qText;
  document.getElementById('q-code').innerHTML = codeHTML;"""

new_render_q = """  // Handle code blocks and dynamic multi-language switcher
  let qText = q.q || '';
  let codeHTML = '';
  const langBar = document.getElementById('q-lang-bar');

  const hasCode = qText.includes('```') || (q.code && q.code.length > 0) || ['pseudocode', 'debugging', 'dsa', 'oops', 'ai_coding'].includes(currentTest?.bank);

  if (hasCode) {
    if (langBar) {
      langBar.style.display = 'flex';
      const langs = [
        { id: 'cpp', name: 'C++' },
        { id: 'java', name: 'Java' },
        { id: 'python', name: 'Python' },
        { id: 'c', name: 'C' }
      ];
      langBar.innerHTML = `
        <span class="lang-label">💻 View Code in:</span>
        ${langs.map(l => `
          <button class="lang-pill ${currentSelectedLanguage === l.id ? 'active' : ''}" onclick="switchQuestionLanguage('${l.id}')">
            ${l.name}
          </button>
        `).join('')}
        <span class="lang-badge">⚡ Auto-Adapted (${currentSelectedLanguage.toUpperCase()})</span>
      `;
    }

    let rawCode = '';
    if (qText.includes('```')) {
      const parts = qText.split('```');
      qText = parts[0].trim();
      if (parts[1]) {
        rawCode = parts[1].replace(/^(cpp|c|java|python|js)\\b\\n?/i, '').trim();
      }
    } else if (q.code) {
      rawCode = q.code;
    }

    if (rawCode) {
      const convertedCode = transpileCodeToLang(rawCode, currentSelectedLanguage);
      codeHTML = `<div class="question-code">${escHTML(convertedCode)}</div>`;
    }
  } else {
    if (langBar) langBar.style.display = 'none';
  }

  document.getElementById('q-text').textContent = qText;
  document.getElementById('q-code').innerHTML = codeHTML;"""

if "function transpileCodeToLang" not in code:
    code = lang_engine + "\n" + code

if old_render_q in code:
    code = code.replace(old_render_q, new_render_q)
    print("Replaced renderQuestion code handling with multi-language selector")
else:
    print("Warning: old_render_q not found directly")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated app.js with multi-language code support")
