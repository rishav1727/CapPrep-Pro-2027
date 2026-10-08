// Multi-Language Code Transpiler for Capgemini Prep Questions
function transpileCodeToLang(rawCode, targetLang) {
  if (!rawCode) return '';
  let lines = rawCode.trim().split('\n');

  if (targetLang === 'python') {
    let pyLines = [];
    let indentLevel = 0;
    for (let rawLine of lines) {
      let line = rawLine.trim();
      if (!line) { pyLines.push(''); continue; }

      // Skip C/C++ includes, using namespace, package, class wrapper
      if (line.startsWith('#include') || line.startsWith('using namespace') || line.startsWith('package ') || line.startsWith('import java.')) {
        continue;
      }
      if (line.includes('class Solution') || line.includes('public class')) {
        continue;
      }
      if (line === '{' || line === '}') {
        continue;
      }

      // Convert print statements
      line = line.replace(/std::cout\s*<<\s*(.*?)\s*<<\s*std::endl;?/g, 'print($1)');
      line = line.replace(/cout\s*<<\s*(.*?)\s*<<\s*endl;?/g, 'print($1)');
      line = line.replace(/System\.out\.println\((.*?)\);?/g, 'print($1)');
      line = line.replace(/System\.out\.print\((.*?)\);?/g, 'print($1, end="")');
      line = line.replace(/printf\("([^"]*)",?\s*(.*?)\);?/g, 'print($2)');

      // Convert function signatures: e.g. int solve(int a, int b) { -> def solve(a, b):
      line = line.replace(/^(public\s+|static\s+|inline\s+)*(int|void|bool|boolean|string|String|float|double|auto)\s+(\w+)\s*\((.*?)\)\s*\{?$/g, 'def $3($4):');
      line = line.replace(/(int|bool|boolean|string|String|float|double|auto)\s+(\w+)/g, '$2');

      // Convert control flow
      line = line.replace(/^if\s*\((.*?)\)\s*\{?$/g, 'if $1:');
      line = line.replace(/^while\s*\((.*?)\)\s*\{?$/g, 'while $1:');
      line = line.replace(/^for\s*\((\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\w+|\d+);\s*\1\+\+\)\s*\{?$/g, 'for $1 in range($2, $3):');
      line = line.replace(/^else\s*\{?$/g, 'else:');
      line = line.replace(/^else\s+if\s*\((.*?)\)\s*\{?$/g, 'elif $1:');

      // Convert literals and operators
      line = line.replace(/nullptr\b/g, 'None');
      line = line.replace(/NULL\b/g, 'None');
      line = line.replace(/null\b/g, 'None');
      line = line.replace(/true\b/g, 'True');
      line = line.replace(/false\b/g, 'False');
      line = line.replace(/&&/g, 'and');
      line = line.replace(/\|\|/g, 'or');
      line = line.replace(/!(\w+)/g, 'not $1');

      // Variable declarations: int x = 10; -> x = 10
      line = line.replace(/^(int|bool|boolean|string|String|float|double|auto)\s+(\w+)\s*=\s*/g, '$2 = ');
      line = line.replace(/;\s*$/g, ''); // strip trailing semicolons
      line = line.replace(/\/\/(.*)/g, '#$1'); // // comment -> # comment

      // Remove closing braces left on lines
      line = line.replace(/[\{\}]/g, '').trim();
      if (line) {
        pyLines.push('    ' + line);
      }
    }
    return pyLines.join('\n') || rawCode;
  }

  if (targetLang === 'java') {
    let javaLines = [];
    for (let rawLine of lines) {
      let line = rawLine;
      if (line.includes('#include') || line.includes('using namespace')) {
        continue;
      }
      line = line.replace(/std::cout\s*<<\s*(.*?)\s*<<\s*std::endl;/g, 'System.out.println($1);');
      line = line.replace(/cout\s*<<\s*(.*?)\s*<<\s*endl;/g, 'System.out.println($1);');
      line = line.replace(/nullptr\b/g, 'null');
      line = line.replace(/NULL\b/g, 'null');
      line = line.replace(/bool\b/g, 'boolean');
      line = line.replace(/string\b/g, 'String');
      line = line.replace(/vector<int>/g, 'ArrayList<Integer>');
      javaLines.push(line);
    }
    return javaLines.join('\n');
  }

  if (targetLang === 'c') {
    let cLines = [];
    for (let rawLine of lines) {
      let line = rawLine;
      if (line.includes('using namespace') || line.includes('import java.') || line.includes('class Solution')) {
        continue;
      }
      line = line.replace(/std::cout\s*<<\s*(.*?)\s*<<\s*std::endl;/g, 'printf("%d\\n", $1);');
      line = line.replace(/cout\s*<<\s*(.*?)\s*<<\s*endl;/g, 'printf("%d\\n", $1);');
      line = line.replace(/System\.out\.println\((.*?)\);/g, 'printf("%d\\n", $1);');
      line = line.replace(/nullptr\b/g, 'NULL');
      line = line.replace(/null\b/g, 'NULL');
      line = line.replace(/bool\b/g, 'int');
      line = line.replace(/boolean\b/g, 'int');
      line = line.replace(/true\b/g, '1');
      line = line.replace(/false\b/g, '0');
      cLines.push(line);
    }
    return cLines.join('\n');
  }

  // C++ default
  let cppLines = [];
  for (let rawLine of lines) {
    let line = rawLine;
    line = line.replace(/System\.out\.println\((.*?)\);/g, 'std::cout << $1 << std::endl;');
    line = line.replace(/System\.out\.print\((.*?)\);/g, 'std::cout << $1;');
    line = line.replace(/boolean\b/g, 'bool');
    line = line.replace(/null\b/g, 'nullptr');
    line = line.replace(/None\b/g, 'nullptr');
    line = line.replace(/True\b/g, 'true');
    line = line.replace(/False\b/g, 'false');
    cppLines.push(line);
  }
  return cppLines.join('\n');
}

// Test sample
const cCode = `int findMax(int arr[], int n) {
    int maxVal = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}`;

console.log("=== C++ ===");
console.log(transpileCodeToLang(cCode, 'cpp'));
console.log("\n=== JAVA ===");
console.log(transpileCodeToLang(cCode, 'java'));
console.log("\n=== PYTHON ===");
console.log(transpileCodeToLang(cCode, 'python'));
console.log("\n=== C ===");
console.log(transpileCodeToLang(cCode, 'c'));
