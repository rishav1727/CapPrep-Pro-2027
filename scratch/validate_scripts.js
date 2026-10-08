const fs = require('fs');

function checkJsInHtml(filename) {
  const html = fs.readFileSync(filename, 'utf-8');
  const scriptRegex = /<script[\s\S]*?>([\s\S]*?)<\/script>/gi;
  let match;
  let idx = 0;
  while ((match = scriptRegex.exec(html)) !== null) {
    idx++;
    if (match[0].includes('src=')) continue;
    const code = match[1];
    try {
      new Function(code);
      console.log('✅ ' + filename + ' inline script #' + idx + ' parsed cleanly.');
    } catch(err) {
      console.error('❌ ' + filename + ' inline script #' + idx + ' syntax error:', err.message);
    }
  }
}

checkJsInHtml('modules/debug_sim.html');
checkJsInHtml('modules/ai_coding_sim.html');
checkJsInHtml('index.html');
console.log('Validation complete.');
