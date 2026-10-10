
// Robust HTML escaping to protect against XSS and attribute breaking
function escHTML(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
const escapeHtml = escHTML;

// Show / Hide Password Helper
function togglePasswordVisibility(inputId, btn) {
  const input = document.getElementById(inputId);
  if (!input) return;
  if (input.type === 'password') {
    input.type = 'text';
    if (btn) btn.innerHTML = '🙈';
    if (btn) btn.title = 'Hide Password';
  } else {
    input.type = 'password';
    if (btn) btn.innerHTML = '👁️';
    if (btn) btn.title = 'Show Password';
  }
}

// Grand Mock Mode Switcher (Stage 2 Focus vs All Stages with Stage 1)
let grandMockMode = 'stage2_only';
function setGrandMockMode(mode) {
  grandMockMode = mode;
  const btnStage2 = document.getElementById('btn-mode-stage2');
  const btnAll = document.getElementById('btn-mode-allstages');
  const descEl = document.getElementById('gm-mode-desc');
  
  if (mode === 'stage2_only') {
    if (btnStage2) btnStage2.classList.add('active');
    if (btnAll) btnAll.classList.remove('active');
    if (descEl) descEl.innerHTML = '⚡ <strong>Currently Active Pattern:</strong> Stage 2A + 2B + 3 + 4 + 5/6 (Stage 1 English Communication skipped as Stage 2 is live).';
    showSecurityToast("⚡ Grand Mock pattern set to: Stages 2A to 6 (Stage 1 skipped).");
  } else {
    if (btnStage2) btnStage2.classList.remove('active');
    if (btnAll) btnAll.classList.add('active');
    if (descEl) descEl.innerHTML = '🌐 <strong>Currently Active Pattern:</strong> Full 6 Stages (Stage 1 English Communication + Stages 2A to 6 included).';
    showSecurityToast("🌐 Grand Mock pattern set to: Complete 6 Stages (Stage 1 included).");
  }
}


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
  let lines = rawCode.trim().split('\n');

  if (targetLang === 'python') {
    let pyLines = [];
    for (let rawLine of lines) {
      let line = rawLine.trim();
      if (!line) { pyLines.push(''); continue; }

      if (line.startsWith('#include') || line.startsWith('using namespace') || line.startsWith('package ') || line.startsWith('import java.') || line.includes('class Solution') || line.includes('public class')) {
        continue;
      }
      if (line === '{' || line === '}') continue;

      line = line.replace(/std::cout\s*<<\s*(.*?)\s*<<\s*std::endl;?/g, 'print($1)');
      line = line.replace(/cout\s*<<\s*(.*?)\s*<<\s*endl;?/g, 'print($1)');
      line = line.replace(/System\.out\.println\((.*?)\);?/g, 'print($1)');
      line = line.replace(/System\.out\.print\((.*?)\);?/g, 'print($1, end="")');
      line = line.replace(/printf\("([^"]*)",?\s*(.*?)\);?/g, 'print($2)');

      line = line.replace(/^(public\s+|static\s+|inline\s+)*(int|void|bool|boolean|string|String|float|double|auto)\s+(\w+)\s*\((.*?)\)\s*\{?$/g, 'def $3($4):');
      line = line.replace(/(int|bool|boolean|string|String|float|double|auto)\s+(\w+)/g, '$2');

      line = line.replace(/^if\s*\((.*?)\)\s*\{?$/g, 'if $1:');
      line = line.replace(/^while\s*\((.*?)\)\s*\{?$/g, 'while $1:');
      line = line.replace(/^for\s*\((\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\w+|\d+);\s*\1\+\+\)\s*\{?$/g, 'for $1 in range($2, $3):');
      line = line.replace(/^else\s*\{?$/g, 'else:');
      line = line.replace(/^else\s+if\s*\((.*?)\)\s*\{?$/g, 'elif $1:');

      line = line.replace(/nullptr\b/g, 'None');
      line = line.replace(/NULL\b/g, 'None');
      line = line.replace(/null\b/g, 'None');
      line = line.replace(/true\b/g, 'True');
      line = line.replace(/false\b/g, 'False');
      line = line.replace(/&&/g, 'and');
      line = line.replace(/\|\|/g, 'or');
      line = line.replace(/!(\w+)/g, 'not $1');

      line = line.replace(/^(int|bool|boolean|string|String|float|double|auto)\s+(\w+)\s*=\s*/g, '$2 = ');
      line = line.replace(/;\s*$/g, '');
      line = line.replace(/\/\/(.*)/g, '#$1');
      line = line.replace(/[\{\}]/g, '').trim();
      if (line) pyLines.push('    ' + line);
    }
    return pyLines.join('\n') || rawCode;
  }

  if (targetLang === 'java') {
    let javaLines = [];
    for (let rawLine of lines) {
      let line = rawLine;
      if (line.includes('#include') || line.includes('using namespace')) continue;
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
      if (line.includes('using namespace') || line.includes('import java.') || line.includes('class Solution')) continue;
      line = line.replace(/std::cout\s*<<\s*(.*?)\s*<<\s*std::endl;/g, 'printf("%d\\n", $1);');
      line = line.replace(/cout\s*<<\s*(.*?)\s*<<\s*endl;/g, 'printf("%d\\n", $1);');
      line = line.replace(/System\.out\.println\((.*?)\);/g, 'printf("%d\\n", $1);');
      line = line.replace(/nullptr\b/g, 'NULL');
      line = line.replace(/null\b/g, 'NULL');
      line = line.replace(/None\b/g, 'NULL');
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


// ==========================================
// HELP & SUPPORT ENGINE (rishav.gupta0527@gmail.com)
// ==========================================

const OFFICIAL_SUPPORT_EMAIL = "rishav.gupta0527@gmail.com";
const MASTER_ADMIN_EMAILS = ["rishavofficials1727@gmail.com", "rishav.gupta0527@gmail.com"];

function openSupportModal() {
  const modal = document.getElementById('support-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    const formContainer = document.getElementById('support-form-container');
    const successBox = document.getElementById('supp-success-box');
    const feedback = document.getElementById('supp-feedback');
    if (formContainer) formContainer.style.display = 'block';
    if (successBox) successBox.style.display = 'none';
    if (feedback) feedback.style.display = 'none';
  }
}

function closeSupportModal() {
  const modal = document.getElementById('support-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function submitSupportTicket() {
  const name  = (document.getElementById('supp-name')?.value  || '').trim();
  const email = (document.getElementById('supp-email')?.value || '').trim();
  const topic = document.getElementById('supp-topic')?.value  || 'General Support';
  const msg   = (document.getElementById('supp-msg')?.value   || '').trim();
  const feedback = document.getElementById('supp-feedback');
  const btn   = document.querySelector('#support-form-container .pay-btn-checkout');

  if (!email || !msg) {
    if (feedback) {
      feedback.style.display = 'block';
      feedback.style.background = 'rgba(239,68,68,0.15)';
      feedback.style.border = '1px solid rgba(239,68,68,0.3)';
      feedback.style.color = '#f87171';
      feedback.innerText = 'Please provide both your registered email and a message / UTR.';
    }
    return;
  }

  // Generate ticket ID
  const ticketId = 'CAP-' + Math.floor(10000 + Math.random() * 90000);

  // Save locally
  try {
    const existing = JSON.parse(localStorage.getItem('capprep_support_tickets') || '[]');
    existing.unshift({ id:ticketId, name:name||'Candidate', email, topic, message:msg, timestamp:new Date().toISOString(), status:'OPEN' });
    localStorage.setItem('capprep_support_tickets', JSON.stringify(existing));
  } catch(e) {}

  // Show loading state
  if (btn) { btn.disabled = true; btn.innerHTML = '⏳ Sending...'; }
  if (feedback) feedback.style.display = 'none';

  // ── Real Email via Formsubmit.co (zero signup, sends directly to Gmail) ──
  const FORMSUBMIT_ENDPOINT = 'https://formsubmit.co/ajax/rishav.gupta0527@gmail.com';

  fetch(FORMSUBMIT_ENDPOINT, {
    method: 'POST',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify({
      _subject: '[CapPrep Support] ' + topic + ' — Ticket ' + ticketId,
      name:     name || 'Candidate',
      email:    email,
      topic:    topic,
      message:  msg,
      ticket:   ticketId,
      _replyto: email,
      _captcha: 'false'
    })
  })
  .then(function(res) {
    if (res.ok) {
      showSupportSuccess(ticketId, email);
    } else {
      // Formsubmit failed — fall back to mailto
      mailtoFallback(name, email, topic, msg, ticketId);
      showSupportSuccess(ticketId, email);
    }
  })
  .catch(function() {
    // Network error — fall back to mailto
    mailtoFallback(name, email, topic, msg, ticketId);
    showSupportSuccess(ticketId, email);
  });
}

function mailtoFallback(name, email, topic, msg, ticketId) {
  const subject = encodeURIComponent('[CapPrep Support] ' + topic + ' — Ticket ' + ticketId);
  const body = encodeURIComponent(
    'Ticket ID: ' + ticketId + '\n' +
    'Name: ' + (name || 'Candidate') + '\n' +
    'Email: ' + email + '\n' +
    'Topic: ' + topic + '\n\n' +
    'Message:\n' + msg
  );
  window.open('mailto:rishavofficials1727@gmail.com?subject=' + subject + '&body=' + body, '_blank');
}

function showSupportSuccess(ticketId, email) {
  const btn = document.querySelector('#support-form-container .pay-btn-checkout');
  if (btn) { btn.disabled = false; btn.innerHTML = '📨 Send Direct Message to Support'; }

  const formContainer = document.getElementById('support-form-container');
  const successBox    = document.getElementById('supp-success-box');
  const ticketRef     = document.getElementById('supp-ticket-ref');
  if (formContainer) formContainer.style.display = 'none';
  if (successBox)    successBox.style.display = 'block';
  if (ticketRef)     ticketRef.innerHTML = 'Your Ticket ID is <strong style="color:#00d4ff;">#' + ticketId + '</strong>. Your message has been sent to our support team at <em>rishavofficials1727@gmail.com</em>. We will reply to <em>' + escapeHtml(email) + '</em> within 24 hours.';
}



// ==========================================
// CAPPREP PRO — MASTER QUESTION BANK & ENGINE
// 300+ Curated Questions across 14 Topic Banks
// ==========================================

const QUESTION_BANK = {

  // ---- MODULE A: AI LITERACY ----
  ai_literacy: [
    { q:"What is the key difference between Discriminative and Generative models?", options:["Discriminative models learn P(y|x); Generative models learn P(x,y)","Discriminative models generate data; Generative models classify","Discriminative are unsupervised; Generative are supervised","Discriminative use CNNs only"], ans:0, exp:"Discriminative models learn conditional probability P(y|x). Generative models learn the joint distribution P(x,y) and can generate new samples." },
    { q:"Tokenization in Large Language Models (LLMs) refers to:", options:["Converting text into numerical embeddings","Breaking input text into smaller units (words/subwords/chars)","The process of fine-tuning a model","Splitting datasets into train/test sets"], ans:1, exp:"Tokenization breaks text into tokens (subwords, words, characters) before feeding to the LLM." },
    { q:"Zero-shot prompting means:", options:["Providing many examples in the prompt","Asking the model to perform a task without any examples","Running the model with no GPU","Using only image inputs"], ans:1, exp:"Zero-shot asks the LLM to perform tasks without prior examples, relying on pre-trained knowledge." },
    { q:"In RAG (Retrieval-Augmented Generation), the retriever's role is to:", options:["Fine-tune the LLM","Fetch relevant documents from external knowledge bases","Generate the final answer","Tokenize user queries"], ans:1, exp:"The retriever fetches semantically relevant documents from external databases, providing the LLM with up-to-date context." },
    { q:"LLM 'hallucination' refers to:", options:["The model running out of memory","Generating confidently stated but factually incorrect output","The model refusing to answer","Using too many tokens"], ans:1, exp:"Hallucination is when LLMs produce plausible-sounding but fabricated or incorrect information." },
    { q:"Embedding spaces in NLP represent:", options:["Physical server locations","High-dimensional vector space where similar tokens are close","The tokenization dictionary","Output probability distributions"], ans:1, exp:"Embedding spaces map words to vectors where semantic similarity corresponds to geometric proximity." },
    { q:"Chain-of-thought (CoT) prompting encourages LLMs to:", options:["Generate shorter responses","Reason step-by-step through problems","Refuse ambiguous questions","Use fewer parameters"], ans:1, exp:"CoT prompting includes intermediate reasoning steps, guiding the model to think through complex problems systematically." },
    { q:"Few-shot prompting involves:", options:["Minimal compute usage","Providing a small number of examples in the prompt","Training on few examples","Deploying on few servers"], ans:1, exp:"Few-shot prompting provides worked examples in the prompt to guide the model's output format and behavior." },
    { q:"Bias mitigation in Responsible AI aims to:", options:["Speed up inference","Reduce unfair discrimination based on protected attributes","Compress model size","Prevent overfitting"], ans:1, exp:"Bias mitigation detects and reduces discriminatory patterns in AI related to race, gender, religion, etc." },
    { q:"Multi-modal LLMs differ from text-only models because they:", options:["Use more layers","Can process text, images, audio and other modalities","Are always larger","Only work in English"], ans:1, exp:"Multi-modal LLMs process and generate multiple data types (text, image, audio) unlike single-modality models." },
    { q:"Neural network scaling laws state performance improves with:", options:["Reducing training data","Increasing parameters, data, and compute together","Smaller batch sizes","Fewer layers"], ans:1, exp:"Kaplan et al.'s scaling laws show LLM performance improves predictably as parameters, data, and compute scale together." },
    { q:"RLHF (Reinforcement Learning from Human Feedback) is used to:", options:["Increase model size","Align model outputs with human preferences and reduce toxicity","Reduce training time","Implement RAG"], ans:1, exp:"RLHF uses human ratings to train a reward model, then fine-tunes the LLM to produce more helpful and harmless outputs." },
    { q:"What is a 'knowledge graph' in the context of RAG?", options:["A training graph neural network","A structured representation of entities and their relationships","A visualization of model attention","A database schema diagram"], ans:1, exp:"A knowledge graph represents real-world entities (nodes) connected by typed relationships (edges), enabling rich semantic querying." },
    { q:"Data privacy in AI is a concern because:", options:["Models are too slow","Training data may contain memorized personal information (PII)","Models use too much power","AI can't handle structured data"], ans:1, exp:"LLMs trained on web-scale data may memorize and regurgitate personal information from training datasets." },
    { q:"The 'temperature' parameter in LLM generation controls:", options:["Actual hardware temperature","Randomness/creativity of outputs — higher = more random","Model size","Number of tokens generated"], ans:1, exp:"Temperature controls sampling randomness: low temperature = deterministic/conservative; high temperature = creative/diverse outputs." },
    { q:"What is the Self-Attention mechanism in Transformer models?", options:["A mechanism where the model focuses on its own weights only","Computes attention weights between all pairs of tokens in an input sequence simultaneously","A method to reduce token count","A hardware accelerator"], ans:1, exp:"Self-attention allows each token in a sequence to dynamically attend to and weigh the context of all other tokens, capturing long-range dependencies." },
    { q:"In Vector Databases, what does HNSW stand for?", options:["High Network System Web","Hierarchical Navigable Small World — an approximate nearest neighbor graph index","Host Node Structured Wire","Hash Numeric Sequential Weights"], ans:1, exp:"HNSW (Hierarchical Navigable Small World) is a graph-based indexing algorithm providing logarithmic search time for vector nearest neighbors." },
    { q:"What is a 'Prompt Injection' attack in LLM applications?", options:["Crashing the GPU with malformed tokens","Manipulating user inputs to override system prompt instructions and bypass guardrails","Injecting SQL queries into a relational database","Stealing weights through gradient inversion"], ans:1, exp:"Prompt injection occurs when untrusted user input tricks the LLM into disregarding original developer instructions, adopting new malicious personas or leaking system secrets." },
    { q:"Fine-Tuning vs RAG — which is best for accessing dynamically changing real-time data?", options:["Fine-Tuning only","RAG (Retrieval-Augmented Generation)","Pre-training from scratch","Using lower temperature"], ans:1, exp:"RAG is superior for rapidly changing or real-time data because it retrieves current documents without requiring expensive model retraining or fine-tuning." },
    { q:"What is the primary role of LoRA (Low-Rank Adaptation) in LLM fine-tuning?", options:["Doubling model parameters","Freezing base model weights and training small low-rank decomposition matrices, reducing memory usage","Converting text to vectors","Removing safety filters"], ans:1, exp:"LoRA freezes the pre-trained model weights and injects trainable rank decomposition matrices into each transformer layer, drastically cutting GPU VRAM requirements." },
    { q:"Cosine Similarity between two identical normalized vectors equals:", options:["0","1","-1","Infinity"], ans:1, exp:"Cosine similarity measures cos(θ). For identical vectors, θ=0°, so cos(0°)=1. Orthogonal vectors have similarity 0." },
    { q:"What is the 'Needle in a Haystack' test used for in LLM benchmarking?", options:["Measuring token generation speed","Testing an LLM's ability to recall specific facts placed at arbitrary positions in large context windows","Testing model compression","Evaluating vision encoders"], ans:1, exp:"The Needle in a Haystack test evaluates retrieval accuracy across various depth percentages of an LLM's full context window." },
    { q:"Top-P (Nucleus Sampling) set to 0.1 means:", options:["The model only considers tokens comprising top 10% of cumulative probability mass","Model generates 10 tokens max","Temperature is multiplied by 0.1","10% of prompts fail"], ans:0, exp:"Top-P=0.1 restricts token sampling strictly to the tight pool of most likely tokens whose cumulative probability is 10%, producing highly focused outputs." },
    { q:"What is 'model quantization' (e.g. INT8, 4-bit AWQ)?", options:["Increasing parameter precision to 64-bit","Reducing weight precision from 16-bit float to lower bit integers (INT8/4-bit) to reduce memory and latency","Training with quantum computers","Translating code to English"], ans:1, exp:"Quantization compresses model weights into lower-precision formats (like INT8 or 4-bit), significantly reducing VRAM footprint and accelerating inference with minimal accuracy drop." },
    { q:"What is the difference between BERT and GPT architectural styles?", options:["BERT is Decoder-only; GPT is Encoder-only","BERT is Encoder-only (bidirectional context); GPT is Decoder-only (autoregressive next-token prediction)","They are identical","BERT cannot process English"], ans:1, exp:"BERT uses Transformer encoders to look at both left and right context (ideal for classification). GPT uses Transformer decoders for causal, autoregressive generation." },
    { q:"In Responsible AI, what does 'Demographic Parity' evaluate?", options:["Model speed across countries","Equal acceptance/positive prediction rates across different protected demographic groups","Number of tokens used per dialect","GPU power allocation"], ans:1, exp:"Demographic Parity is a fairness metric requiring that the proportion of positive decisions is equal across protected subgroups (e.g., gender, ethnicity)." },
    { q:"What is 'Chain-of-Verification' (CoVe) in LLM generation?", options:["Checking hardware status","Having the model draft responses, generate verification questions, check them independently, and revise the final answer","Encrypting prompts with RSA","Signing tokens cryptographically"], ans:1, exp:"Chain-of-Verification (CoVe) mitigates hallucinations by having the LLM generate verification questions to fact-check its own draft before producing the verified response." },
    { q:"What is a Vector Embedding dimension?", options:["The file size of the database","The length of the floating-point coordinate array representing semantic meaning (e.g. 1536 floats)","The number of documents indexed","The context window size"], ans:1, exp:"The embedding dimension represents the size of the numerical coordinate vector (e.g., 768 or 1536) used to encode the semantic features of a text chunk." },
    { q:"What is 'RLAIF' (Reinforcement Learning from AI Feedback)?", options:["Using human annotators only","Using a larger, stronger AI model to evaluate and provide reward labels instead of human annotators","Hardware reinforcement","A type of GAN"], ans:1, exp:"RLAIF (Constitutional AI) uses an AI evaluator to provide feedback and preference labels, replacing costly human annotator loops in RLHF." },
    { q:"What causes 'Catastrophic Forgetting' in neural networks?", options:["Clearing the browser cache","Fine-tuning heavily on a new domain causes the network to lose performance on previously learned general knowledge","Running out of disk space","Power surges in GPU clusters"], ans:1, exp:"Catastrophic forgetting occurs when a neural network overwrites previously acquired knowledge while training on new, narrow datasets." }
  ],

  // ---- MODULE A: PSEUDOCODE & LOGIC ----
  pseudocode: [
    { q:"What is the output of the following pseudocode?\n```\nx = 5\nif x > 3:\n    if x < 10:\n        print('A')\n    else:\n        print('B')\nelse:\n    print('C')\n```", options:["A","B","C","No output"], ans:0, exp:"x=5 satisfies both x>3 and x<10, so 'A' is printed." },
    { q:"What is the output of: x = 6; print(x << 1)", options:["12","3","7","6"], ans:0, exp:"Left shift by 1 multiplies by 2. 6 << 1 = 12." },
    { q:"What is the result of: 5 & 3?", options:["7","1","0","15"], ans:1, exp:"5 = 101₂, 3 = 011₂. AND: 101 & 011 = 001 = 1." },
    { q:"What is the result of: 5 | 3?", options:["7","1","0","15"], ans:0, exp:"5 = 101₂, 3 = 011₂. OR: 101 | 011 = 111 = 7." },
    { q:"What is the result of: 5 ^ 3?", options:["7","6","1","2"], ans:1, exp:"5 = 101₂, 3 = 011₂. XOR: 101 ^ 011 = 110 = 6." },
    { q:"What does this recursive function return for n=4?\n```\ndef fact(n):\n    if n == 1: return 1\n    return n * fact(n-1)\n```", options:["12","24","4","1"], ans:1, exp:"fact(4) = 4 × 3 × 2 × 1 = 24." },
    { q:"In a do-while loop, the body executes:", options:["Never if condition is false initially","At least once before checking condition","Only when condition is true","Zero or more times"], ans:1, exp:"do-while executes the body first, then checks the condition — guaranteeing at least one execution." },
    { q:"What does a 'static' local variable do?", options:["Makes it global","Preserves its value across function calls","Deletes after function","Makes it constant"], ans:1, exp:"Static local variables are initialized once and retain their value between successive function calls." },
    { q:"What is the output of: print(12 >> 2)?", options:["48","6","3","24"], ans:2, exp:"Right shift by 2 divides by 4. 12 >> 2 = 3." },
    { q:"What is ~5 (bitwise NOT of 5) in Python?", options:["-5","-6","250","5"], ans:1, exp:"Bitwise NOT flips all bits. ~5 = -(5+1) = -6 in Python's two's complement representation." },
    { q:"What does `(n & (n - 1)) == 0` check for a positive integer n?", options:["Whether n is odd","Whether n is a power of 2","Whether n is a prime number","Whether n is divisible by 4"], ans:1, exp:"If n is a power of 2, it has exactly one set bit (e.g. 8 = 1000). n-1 has all lower bits set (7 = 0111). 1000 & 0111 = 0." },
    { q:"What is the output?\n```\na = 10, b = 20\na = a ^ b\nb = a ^ b\na = a ^ b\nprint(a, b)\n```", options:["10 20","20 10","30 10","0 0"], ans:1, exp:"This is the classic three-XOR swap algorithm without temporary storage. a becomes 20, b becomes 10." },
    { q:"What is the output of the following pseudocode?\n```\ncount = 0\nfor i = 1 to 4:\n    for j = 1 to i:\n        count = count + 1\nprint(count)\n```", options:["16","10","8","4"], ans:1, exp:"When i=1: 1 step. i=2: 2 steps. i=3: 3 steps. i=4: 4 steps. Sum = 1+2+3+4 = 10." },
    { q:"What is the output?\n```\nx = 1\nwhile (x < 10):\n    x = x * 2\nprint(x)\n```", options:["8","10","16","32"], ans:2, exp:"x starts at 1 → 2 → 4 → 8 (still < 10) → 16 (16 is NOT < 10, loop ends). Final x = 16." },
    { q:"What does Brian Kernighan's algorithm `n = n & (n - 1)` do inside a loop?", options:["Divides n by 2","Clears the lowest set bit of n, counting set bits","Inverts all bits","Multiplies n by 2"], ans:1, exp:"Each iteration of n = n & (n - 1) turns off the rightmost set bit, counting the number of set bits in O(number of set bits) time." },
    { q:"What is the value of `7 % -3` in C/C++?", options:["1","-1","2","-2"], ans:0, exp:"In C99 and later, the sign of the remainder matches the dividend: 7 = (-3)*(-2) + 1. So 7 % -3 = 1." },
    { q:"What is printed?\n```\nint a = 5;\nint b = ++a + a++;\nprint(b);\n```", options:["11","12","13","10"], ans:1, exp:"++a pre-increments a from 5 to 6. Then 6 is added to 6 (with a++ post-incrementing after addition). 6 + 6 = 12." },
    { q:"What is the output of the recursion?\n```\nfunction fun(n):\n    if n <= 1: return 1\n    return fun(n-1) + fun(n-1)\nprint(fun(4))\n```", options:["4","6","8","16"], ans:2, exp:"fun(n) = 2^(n-1). For n=4, fun(4) = 2^3 = 8." },
    { q:"In boolean short-circuit evaluation: `False and func()`", options:["func() is executed","func() is never called","An error occurs","Returns True"], ans:1, exp:"In `False and func()`, since the first operand is False, the entire expression must be False. `func()` is skipped (short-circuit)." },
    { q:"What is the output of:\n```\nx = 15\nprint(x >> 1, x << 1)\n```", options:["7, 30","7.5, 30","8, 30","7, 15"], ans:0, exp:"15 >> 1 = floor(15/2) = 7. 15 << 1 = 15*2 = 30." },
    { q:"What is the output?\n```\ns = \"Capgemini\"\nprint(s[3:6])\n```", options:["gem","gemi","pgem","Cap"], ans:0, exp:"Slice from index 3 up to (not including) 6. Indices: C(0), a(1), p(2), g(3), e(4), m(5). Output is 'gem'." },
    { q:"What is the value of `2 ^ 3` in bitwise logic?", options:["8","1","5","6"], ans:1, exp:"2 is 010₂ and 3 is 011₂. XOR: 010 ^ 011 = 001₂ = 1. (Note: ^ is bitwise XOR, not exponentiation!)." },
    { q:"What is the output?\n```\na = [10, 20, 30]\nb = a\nb.append(40)\nprint(len(a))\n```", options:["3","4","1","Error"], ans:1, exp:"In Python and many languages, `b = a` creates a reference alias to the same list. Mutating b also mutates a. len(a) = 4." },
    { q:"What is the output of the loop?\n```\nsum = 0\nfor i = 1 to 5:\n    if i == 3: continue\n    sum += i\nprint(sum)\n```", options:["15","12","10","9"], ans:1, exp:"Values added: 1 + 2 + 4 + 5 = 12 (3 is skipped by continue)." },
    { q:"What does `~(-1)` evaluate to in two's complement integer arithmetic?", options:["-2","-1","0","1"], ans:2, exp:"~x = -(x + 1). Therefore, ~(-1) = -((-1) + 1) = -(0) = 0." }
  ],

  // ---- MODULE A: DSA ----
  dsa: [
    { q:"Time complexity of Binary Search:", options:["O(n)","O(log n)","O(n²)","O(1)"], ans:1, exp:"Binary search halves search space each iteration → O(log n)." },
    { q:"Which data structure follows LIFO?", options:["Queue","Stack","Linked List","Tree"], ans:1, exp:"Stack is Last-In-First-Out." },
    { q:"In a BST, where is the maximum element?", options:["Root","Leftmost node","Rightmost node","Any leaf"], ans:2, exp:"BST property: right children > parent, so rightmost node is the maximum." },
    { q:"Which sorting algorithm has best-case O(n)?", options:["Quick Sort","Merge Sort","Insertion Sort","Selection Sort"], ans:2, exp:"Insertion Sort is O(n) best-case on already sorted arrays." },
    { q:"Time complexity of Merge Sort:", options:["O(n)","O(n log n)","O(n²)","O(log n)"], ans:1, exp:"Merge Sort always divides in half (log n levels) and merges in O(n) per level = O(n log n)." },
    { q:"In a circular linked list, the last node points to:", options:["NULL","Itself","The first node","The middle node"], ans:2, exp:"In circular linked list, last node's next pointer points back to the head (first node)." },
    { q:"Queue follows which order?", options:["LIFO","FIFO","Random","Priority-based"], ans:1, exp:"Queue is First-In-First-Out (FIFO)." },
    { q:"Inorder traversal of a BST produces:", options:["Random order","Descending order","Ascending sorted order","Level-order"], ans:2, exp:"BST inorder traversal (Left→Root→Right) visits nodes in ascending sorted order." },
    { q:"Average-case complexity of Quick Sort:", options:["O(n)","O(n²)","O(n log n)","O(log n)"], ans:2, exp:"Quick Sort averages O(n log n) when pivots create balanced partitions." },
    { q:"A singly linked list node contains:", options:["Only data","Data and two pointers","Data and one next pointer","Only a pointer"], ans:2, exp:"Singly linked list node has data and one 'next' pointer to the next node." },
    { q:"How do you detect a cycle in a singly linked list in O(1) space?", options:["Use a hash table of visited nodes","Floyd's Tortoise and Hare algorithm (slow and fast pointers)","Recursion stack","Count nodes"], ans:1, exp:"Floyd's cycle-finding algorithm moves slow pointer by 1 step and fast pointer by 2 steps. If there is a cycle, they meet in O(N) time and O(1) memory." },
    { q:"What is the minimum number of queues needed to implement a Stack?", options:["1","2","3","4"], ans:1, exp:"Two queues can implement a stack by transferring elements to maintain LIFO ordering on push/pop operations." },
    { q:"Height of a balanced AVL tree with N nodes is:", options:["O(N)","O(log N)","O(N log N)","O(1)"], ans:1, exp:"AVL trees maintain a balance factor of -1, 0, or +1 at every node, ensuring strictly logarithmic height O(log N)." },
    { q:"Which graph traversal uses a Queue data structure?", options:["Depth-First Search (DFS)","Breadth-First Search (BFS)","Inorder Traversal","Topological Sort via DFS"], ans:1, exp:"Breadth-First Search (BFS) explores vertices level-by-level using a FIFO Queue." },
    { q:"Topological Sort can be performed on which type of graph?", options:["Any undirected graph","Directed Acyclic Graph (DAG) only","Graphs with negative cycles","Complete graphs only"], ans:1, exp:"Topological Sort orders vertices such that for every directed edge u→v, u comes before v. This is only possible on Directed Acyclic Graphs (DAGs)." },
    { q:"Time complexity of Dijkstra's algorithm using a Min-Priority Queue (Binary Heap):", options:["O(V²)","O((V + E) log V)","O(V * E)","O(E²)"], ans:1, exp:"With a binary heap, extracting min takes O(log V) for V vertices, and decrease-key takes O(log V) for E edges → O((V + E) log V)." },
    { q:"What is the time complexity of building a heap (Heapify) of N elements from an arbitrary array?", options:["O(N log N)","O(N)","O(N²)","O(log N)"], ans:1, exp:"Building a heap using bottom-up heapify takes linear O(N) time because lower levels with more nodes have smaller heights." },
    { q:"What is the recurrence relation for the 0/1 Knapsack problem with capacity W and item i?", options:["dp[i][w] = dp[i-1][w]","dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]])","dp[i][w] = dp[i][w-1] + val[i]","dp[i][w] = min(dp[i-1][w], dp[i-1][w-wt[i]])"], ans:1, exp:"For 0/1 Knapsack, either exclude item i: dp[i-1][w], or include item i: val[i] + dp[i-1][w - wt[i]], taking the maximum of both choices." },
    { q:"In a Hash Table with open addressing, what is 'quadratic probing'?", options:["Using a linked list at each bucket","Resolving collisions using h(k, i) = (h'(k) + c1*i + c2*i²) mod m","Hashing keys twice","Doubling array size on collision"], ans:1, exp:"Quadratic probing avoids primary clustering by using a quadratic polynomial of the collision step i to compute the next probe index." },
    { q:"What is the worst-case time complexity of Quick Sort?", options:["O(N log N)","O(N²)","O(N)","O(log N)"], ans:1, exp:"When the pivot chosen is always the smallest or largest element (e.g., already sorted array with naive first/last element pivot), Quick Sort degrades to O(N²)." },
    { q:"To find the middle element of a linked list in a single pass, you should use:", options:["Two pointers: one advancing 1 step, one advancing 2 steps","Counter loop then second loop","Stack to store all elements","Recursion with depth counter"], ans:0, exp:"Fast and slow pointer technique: when fast pointer reaches the end (moves 2x), slow pointer is exactly at the midpoint." },
    { q:"The Two-Pointer approach to find two numbers summing to a target requires the array to be:", options:["Unsorted","Sorted in ascending or descending order","Of odd length","Containing only positive integers"], ans:1, exp:"The two-pointer technique (left at 0, right at n-1) relies on monotonicity of a sorted array to decide whether to increment left or decrement right." },
    { q:"What is the diameter of a Binary Tree?", options:["Total number of nodes","The length of the longest path between any two nodes in a tree","The depth of the root node","Number of leaf nodes"], ans:1, exp:"The diameter (or width) of a binary tree is the number of nodes (or edges) on the longest path between any two arbitrary nodes in the tree." },
    { q:"Postorder traversal of a binary tree visits nodes in which sequence?", options:["Root → Left → Right","Left → Right → Root","Left → Root → Right","Right → Root → Left"], ans:1, exp:"Postorder traversal processes the left subtree, then the right subtree, and finally the root node (Left → Right → Root)." },
    { q:"A complete binary tree with N nodes has height:", options:["N","floor(log2(N))","N / 2","2^N"], ans:1, exp:"In a complete binary tree, all levels except possibly the last are completely filled, resulting in height floor(log2(N))." }
  ],

  // ---- MODULE A: DBMS ----
  dbms: [
    { q:"Which normal form eliminates partial dependencies?", options:["1NF","2NF","3NF","BCNF"], ans:1, exp:"2NF removes partial dependencies — non-key attributes depending on part of a composite PK." },
    { q:"INNER JOIN returns:", options:["All rows from left table","All rows from right table","Only matching rows from both tables","All rows from both tables"], ans:2, exp:"INNER JOIN returns only rows with matching values in both tables." },
    { q:"A foreign key ensures:", options:["Uniqueness","Referential integrity","No NULLs","Max 255 chars"], ans:1, exp:"Foreign key enforces referential integrity — child table values must exist in parent table's primary key." },
    { q:"HAVING clause is used to:", options:["Filter individual rows","Filter grouped results","Sort results","Join tables"], ans:1, exp:"HAVING filters groups after GROUP BY, unlike WHERE which filters rows before grouping." },
    { q:"1NF requires:", options:["No repeating groups; all atomic values","No partial dependencies","No transitive dependencies","All attributes on whole key"], ans:0, exp:"1NF: each cell contains a single atomic value; no repeating groups." },
    { q:"Which SQL command grants access privileges?", options:["SELECT","CREATE","GRANT","UPDATE"], ans:2, exp:"GRANT is a DCL command for giving users database access privileges." },
    { q:"LEFT JOIN returns:", options:["Only matches","All right + matching left","All left + matching right","All rows from both"], ans:2, exp:"LEFT JOIN returns all rows from the left table plus matched rows from right (NULLs for no match)." },
    { q:"ACID stands for:", options:["Array, Commit, Index, Delete","Atomicity, Consistency, Isolation, Durability","Automatic, Complete, Integrity, Data","Access, Control, Input, Delete"], ans:1, exp:"ACID: Atomicity, Consistency, Isolation, Durability — properties ensuring reliable transactions." },
    { q:"Which SQL function counts rows including NULLs?", options:["COUNT(column)","COUNT(*)","SUM(*)","AVG(column)"], ans:1, exp:"COUNT(*) counts all rows including those with NULL values, unlike COUNT(column) which skips NULLs." },
    { q:"3NF eliminates:", options:["Partial dependencies","Repeating groups","Transitive dependencies","Multi-valued dependencies"], ans:2, exp:"3NF eliminates transitive dependencies — non-key attributes depending on other non-key attributes." },
    { q:"A table is in Boyce-Codd Normal Form (BCNF) if and only if:", options:["It is in 1NF and 2NF only","For every functional dependency X → Y, X is a superkey","It has no composite primary keys","It uses foreign keys only"], ans:1, exp:"BCNF is a stricter version of 3NF: for every non-trivial functional dependency X → Y, the determinant X must be a superkey." },
    { q:"What is a 'Dirty Read' in database transactions?", options:["Reading data corrupted by disk failure","A transaction reads uncommitted changes made by another concurrent transaction","Reading duplicate rows","Reading from an unindexed table"], ans:1, exp:"A dirty read occurs when Transaction A modifies a row without committing, and Transaction B reads that uncommitted modified data (which might later be rolled back)." },
    { q:"Which transaction isolation level prevents Dirty Reads, Non-Repeatable Reads, and Phantom Reads?", options:["Read Uncommitted","Read Committed","Repeatable Read","Serializable"], ans:3, exp:"Serializable is the highest isolation level; it completely executes concurrent transactions as if they were executed sequentially, preventing all read anomalies." },
    { q:"Difference between `UNION` and `UNION ALL` in SQL:", options:["UNION ALL removes duplicates; UNION keeps all","UNION removes duplicate rows; UNION ALL retains all rows including duplicates","UNION works only on numbers","No difference"], ans:1, exp:"UNION performs an implicit distinct sort operation to eliminate duplicates across result sets. UNION ALL simply concatenates sets without deduplication, making it faster." },
    { q:"What is a Clustered Index in relational databases?", options:["An index created on secondary foreign keys","An index that dictates the physical storage order of rows in the table (only 1 per table)","An index stored on disk partition","A temporary index created in memory"], ans:1, exp:"A clustered index determines the physical order of data pages on disk. Since data can only be physically stored in one order, a table can have only one clustered index." },
    { q:"In SQL, what does `ON DELETE CASCADE` on a Foreign Key do?", options:["Prevents deletion of parent rows","Automatically deletes matching child table rows when the referenced parent row is deleted","Throws an integrity violation error","Sets child values to NULL"], ans:1, exp:"ON DELETE CASCADE ensures referential integrity by automatically propagating row deletions from the primary key table to all referencing foreign key rows." },
    { q:"What is the purpose of Write-Ahead Logging (WAL)?", options:["To write log files for analytics","To ensure transaction changes are written to append-only log on disk before being applied to data pages, ensuring Durability","To speed up SELECT queries","To audit user logins"], ans:1, exp:"WAL guarantees the 'D' (Durability) in ACID: transaction logs are flushed to persistent disk before memory changes are written to database tables, enabling crash recovery." },
    { q:"Which SQL window function assigns a unique sequential integer to each row without gaps?", options:["RANK()","DENSE_RANK()","ROW_NUMBER()","COUNT()"], ans:2, exp:"ROW_NUMBER() assigns a continuous unique sequential integer (1, 2, 3...) to rows within a partition regardless of ties. RANK leaves gaps for ties; DENSE_RANK ties without gaps." },
    { q:"What does the CAP theorem state regarding distributed databases?", options:["Consistency, Availability, and Partition tolerance cannot all be guaranteed simultaneously in a network partition","Databases must use C++, Assembly, and Python","All distributed databases are ACID compliant","Queries must execute in constant time"], ans:0, exp:"CAP theorem (Brewer's theorem): in the presence of a network partition, a distributed system can guarantee either Consistency (CP) or Availability (AP), but not both." },
    { q:"What type of JOIN is needed to find an employee's manager in a single Employees table?", options:["CROSS JOIN","Self JOIN (joining table with itself on ManagerID = EmployeeID)","NATURAL JOIN","FULL OUTER JOIN"], ans:1, exp:"A Self JOIN joins a table to itself using aliases (e.g. `FROM Employees e JOIN Employees m ON e.ManagerId = m.EmpId`) to model hierarchical relationships." },
    { q:"What is a Materialized View compared to a standard View?", options:["A view with passwords","A view whose query result is physically computed and stored on disk, refreshing periodically","A view that cannot be dropped","A view with triggers"], ans:1, exp:"A standard view is a saved virtual query recomputed on access. A Materialized View physically caches the query results on disk, drastically accelerating complex aggregation queries." },
    { q:"In 2-Phase Locking (2PL), what are the two phases?", options:["Read phase and Write phase","Growing Phase (locks acquired, none released) and Shrinking Phase (locks released, none acquired)","Commit phase and Abort phase","Compile phase and Execute phase"], ans:1, exp:"2PL ensures serializability: During the Growing phase, transactions only acquire locks. Once a lock is released, the Shrinking phase begins and no new locks may be acquired." },
    { q:"Which SQL clause specifies the grouping condition that aggregates must satisfy?", options:["WHERE","ORDER BY","HAVING","LIMIT"], ans:2, exp:"HAVING filters aggregated groups (e.g. `HAVING COUNT(*) > 5`). WHERE filters individual rows before grouping occurs." },
    { q:"What is an index seek vs an index scan?", options:["They are identical","Index Seek navigates the B-Tree directly to locate specific keys; Index Scan reads through the entire index page leaf chain","Index Seek is slower","Index Scan only works on primary keys"], ans:1, exp:"Index Seek uses the B-Tree hierarchy to jump directly to specific matching rows (O(log N)). Index Scan traverses all index leaf pages sequentially (O(N))." },
    { q:"What does `NULL = NULL` evaluate to in SQL standard three-valued logic?", options:["TRUE","FALSE","UNKNOWN (NULL)","Syntax Error"], ans:2, exp:"In SQL's three-valued logic, NULL represents an unknown value. Comparing two unknown values (`NULL = NULL`) evaluates to UNKNOWN (not TRUE). Use `IS NULL` instead." }
  ],

  // ---- MODULE A: OOPs ----
  oops: [
    { q:"Multiple Inheritance allows:", options:["Single class inheriting from one parent","A class inheriting from multiple parents","Methods having multiple signatures","A class having multiple instances"], ans:1, exp:"Multiple inheritance allows a class to inherit from more than one base class." },
    { q:"Method overloading is:", options:["Runtime polymorphism","Compile-time polymorphism","A type of inheritance","Encapsulation"], ans:1, exp:"Method overloading (same name, different parameters) is resolved at compile time." },
    { q:"The 'super' keyword accesses:", options:["Current object","Parent class members","Child class members","Static members"], ans:1, exp:"'super' refers to the immediate parent class for accessing constructors, methods, and attributes." },
    { q:"Encapsulation bundles:", options:["Only data","Only methods","Data and methods together, with restricted access","Multiple classes"], ans:2, exp:"Encapsulation combines data and methods in a class while restricting direct access to internals." },
    { q:"Method overriding is:", options:["Compile-time polymorphism","Runtime polymorphism","Encapsulation","Abstraction"], ans:1, exp:"Method overriding (redefining parent method in child class) is resolved at runtime based on actual object type." },
    { q:"An abstract class can:", options:["Not have any methods","Be instantiated directly","Have both abstract and concrete methods","Only have private members"], ans:2, exp:"Abstract classes can contain both abstract methods (no body) and fully implemented concrete methods." },
    { q:"'this' keyword refers to:", options:["Parent class","Current class instance","Static class","Child class"], ans:1, exp:"'this' refers to the current object instance within a class method or constructor." },
    { q:"Hierarchical inheritance means:", options:["One child, many parents","Many children inherit from one parent","Single inheritance chain","No inheritance"], ans:1, exp:"Hierarchical inheritance: multiple child classes inherit from a single parent class." },
    { q:"What principle says 'program to an interface, not an implementation'?", options:["Encapsulation","SOLID - Dependency Inversion Principle","Multiple Inheritance","Polymorphism"], ans:1, exp:"The Dependency Inversion Principle (D in SOLID) states high-level modules should depend on abstractions, not concrete implementations." },
    { q:"Runtime polymorphism is achieved through:", options:["Method overloading","Constructor overloading","Method overriding with inheritance","Static methods"], ans:2, exp:"Runtime polymorphism requires method overriding combined with inheritance, resolved via dynamic dispatch at runtime." },
    { q:"How does C++ resolve the 'Diamond Problem' in multiple inheritance?", options:["Using templates","Using virtual base classes (e.g. `class B : virtual public A`)","Deleting the parent class","Private inheritance only"], ans:1, exp:"Virtual base classes ensure that only one copy of the common grandparent class subobject is inherited by the grandchild, resolving ambiguity in multiple inheritance." },
    { q:"Why should base class destructors be declared 'virtual' in C++?", options:["To prevent memory allocation","To ensure the derived class destructor is called when deleting an object through a base class pointer","To make the class abstract","To prevent subclassing"], ans:1, exp:"If a base class destructor is non-virtual, deleting a derived class object through a base pointer results in undefined behavior (only the base destructor runs, leaking derived resources)." },
    { q:"What is the difference between a Shallow Copy and a Deep Copy?", options:["Shallow copy copies dynamically allocated heap memory; Deep copy copies pointers","Shallow copy duplicates pointer addresses (sharing memory); Deep copy allocates fresh memory and copies actual data","They are identical in C++","Deep copy uses less RAM"], ans:1, exp:"Shallow copy copies member values directly (meaning both objects point to the same heap buffer, causing double-free crashes). Deep copy allocates independent memory and duplicates values." },
    { q:"What does the 'O' in SOLID design principles stand for?", options:["Object Principle","Open/Closed Principle — software entities should be open for extension, but closed for modification","Operational Integrity","Optimization Rule"], ans:1, exp:"Open/Closed Principle states that classes should be designable so new behavior can be added (extension via inheritance/interfaces) without editing tested existing source code." },
    { q:"What does the Liskov Substitution Principle (L in SOLID) state?", options:["Subtypes must be substitutable for their base types without altering program correctness","All classes must inherit from Object","Interfaces must have only one method","Objects should be immutable"], ans:0, exp:"LSP: objects of a superclass should be replaceable with objects of a subclass without breaking application behavior or violating pre/post-conditions." },
    { q:"What does Interface Segregation Principle (I in SOLID) advocate?", options:["Combining all interfaces into one master interface","Clients should not be forced to depend on methods they do not use (prefer small, role-specific interfaces)","Deleting unused methods","Making all interfaces public"], ans:1, exp:"ISP states that large 'fat' interfaces should be broken down into smaller, highly cohesive role interfaces so implementers only write what they need." },
    { q:"In the Singleton Design Pattern, the constructor must be:", options:["Public","Private","Protected","Static"], ans:1, exp:"The constructor of a Singleton class must be private to prevent external instantiation with `new`, ensuring only one instance is created via `getInstance()`." },
    { q:"What is the Factory Method Pattern?", options:["A pattern where objects are manufactured in hardware","A creational pattern that provides an interface for creating objects in a superclass, letting subclasses alter the type of objects created","A database trigger","A type of multithreading"], ans:1, exp:"Factory Method delegates the instantiation logic to specialized factory methods or subclasses, decoupling caller code from concrete product classes." },
    { q:"Why is 'Composition over Inheritance' generally preferred in enterprise design?", options:["Inheritance is deprecated","Composition provides greater runtime flexibility, avoids fragile base-class problems, and reduces tight coupling","Inheritance is slower to compile","Composition uses less memory"], ans:1, exp:"HAS-A (composition) is looser coupled and lets you change component behaviors dynamically at runtime, avoiding the rigid compile-time coupling of IS-A (inheritance)." },
    { q:"In Java, what does the `final` keyword signify when applied to a class?", options:["The class cannot be instantiated","The class cannot be subclassed/extended (no inheritance allowed)","All methods are abstract","The class is deleted on JVM exit"], ans:1, exp:"A `final` class cannot be extended by any other class (e.g. `java.lang.String` is final for security and immutability guarantees)." },
    { q:"What is a Pure Virtual Function in C++?", options:["A function with no return type","A virtual function with `= 0` in its declaration, making the class an abstract class","A function with inline assembly","A private constructor"], ans:1, exp:"A pure virtual function (`virtual void draw() = 0;`) has no implementation in the base class and mandates that derived classes must provide an implementation." },
    { q:"Can a constructor be declared `virtual` in C++?", options:["Yes, always","No, constructors cannot be virtual because the vtable pointer is initialized inside the constructor itself","Only in abstract classes","Only with private inheritance"], ans:1, exp:"Constructors cannot be virtual because at the moment of construction, the object's type and its vpointer have not yet been fully set up." },
    { q:"What is a Friend Function in C++?", options:["A public member method","A non-member function granted private and protected access to a class via the `friend` keyword","A helper function in STL","A deprecated feature"], ans:1, exp:"Declaring a function as `friend` inside a class definition grants that external non-member function access to all private and protected members of the class." },
    { q:"What is 'method hiding' in object-oriented programming?", options:["Declaring a method private","A subclass defines a static method with the same signature as a static method in the superclass, hiding it without overriding","Deleting method body","Hiding code behind a password"], ans:1, exp:"Static methods cannot be overridden dynamically; when a derived class redefines a static method with identical signature, it hides the base method (resolved at compile time)." },
    { q:"What are 'Covariant Return Types' in method overriding?", options:["Methods returning void","An overriding method in a child class can return a more specific derived subtype of the return type declared in the parent method","Returning two values at once","Converting int to float"], ans:1, exp:"Covariant return typing allows an overriding method to return a subtype of the superclass method's return type (e.g. parent returns `Animal`, child returns `Dog`)." }
  ],

  // ---- MODULE A: OS ----
  os: [
    { q:"Round Robin scheduling assigns:", options:["Priority-based CPU time","Fixed time quantum in cyclic order","CPU until completion","Based on arrival time"], ans:1, exp:"Round Robin gives each process a fixed time quantum cyclically, ensuring fair CPU sharing." },
    { q:"Banker's Algorithm is used for:", options:["Memory allocation","Deadlock avoidance","File system management","Process creation"], ans:1, exp:"Banker's Algorithm avoids deadlock by checking if resource allocation leaves the system in a safe state." },
    { q:"A page fault occurs when:", options:["RAM is full","Requested page is not in physical memory","CPU overheats","Process terminates"], ans:1, exp:"Page fault: accessed virtual page is not currently loaded in physical RAM, requiring OS to load it from disk." },
    { q:"FCFS scheduling suffers from:", options:["High throughput","Convoy effect","Starvation of long processes","Priority inversion"], ans:1, exp:"FCFS causes the convoy effect — short processes waiting behind long ones, reducing efficiency." },
    { q:"Thrashing occurs when:", options:["CPU utilization is very high","Processes spend more time swapping pages than executing","RAM capacity doubles","Disk I/O is zero"], ans:1, exp:"Thrashing: too many processes compete for limited frames, causing excessive page faults that degrade CPU utilization." },
    { q:"Which condition is NOT required for deadlock?", options:["Mutual Exclusion","Hold and Wait","No Preemption","CPU Scheduling"], ans:3, exp:"Deadlock requires: Mutual Exclusion, Hold & Wait, No Preemption, and Circular Wait. CPU Scheduling is not one of them." },
    { q:"A semaphore is used for:", options:["Memory allocation","Process synchronization and mutual exclusion","Disk scheduling","Context switching"], ans:1, exp:"Semaphores are integer-based synchronization primitives used to control access to shared resources and prevent race conditions." },
    { q:"Virtual memory allows:", options:["Running programs larger than physical RAM by using disk as extension","Unlimited RAM","Faster CPU execution","Smaller OS kernels"], ans:0, exp:"Virtual memory uses disk (swap space) to extend the apparent RAM, allowing programs larger than physical RAM to run." },
    { q:"The PCB (Process Control Block) stores:", options:["Hard disk data","All process state — registers, PC, memory maps, PID","Network packets","User passwords"], ans:1, exp:"PCB holds the entire process state: PID, program counter, CPU registers, memory limits, I/O status, and scheduling info." },
    { q:"SJF (Shortest Job First) minimizes:", options:["CPU utilization","Average waiting time","Context switches","Memory usage"], ans:1, exp:"SJF schedules the process with shortest burst time next, minimizing average waiting time — optimal for batch processing." },
    { q:"In context switching, the OS saves and restores:", options:["Only the program counter","PCB including all registers and memory state","Only memory pages","Only file handles"], ans:1, exp:"Context switch saves the full PCB of current process and loads PCB of next process, enabling multitasking." },
    { q:"LRU (Least Recently Used) is a:", options:["CPU scheduling algorithm","Page replacement algorithm","File allocation method","Disk scheduling policy"], ans:1, exp:"LRU is a page replacement policy: when a page frame is needed, evict the page that was least recently accessed." },
    { q:"What is a zombie process?", options:["A malware process","A process that has finished but whose exit status hasn't been collected by parent","A process using 100% CPU","A background service"], ans:1, exp:"Zombie: process has finished execution but remains in process table until its parent reads its exit status via wait()." },
    { q:"Segmentation fault (SIGSEGV) occurs when:", options:["CPU overheats","A process accesses memory outside its allocated segment","Hard disk fails","Network packet is lost"], ans:1, exp:"SIGSEGV: process tried to access invalid memory — null pointer dereference, stack overflow, or out-of-bounds array access." },
    { q:"The OS kernel runs in which CPU mode?", options:["User mode","Kernel/Supervisor mode with full hardware access","Guest mode","Debug mode"], ans:1, exp:"Kernel mode has unrestricted hardware access. User programs run in user mode with restricted access to prevent system corruption." },
    { q:"What is Belady's Anomaly in operating systems?", options:["LRU causes more page faults with more frames","FIFO page replacement can produce MORE page faults when physical page frames are increased","Optimal replacement is slower than FIFO","Disk access is faster than RAM"], ans:1, exp:"Belady's Anomaly: In FIFO page replacement, allocating more memory page frames can counter-intuitively result in an increased number of page faults." },
    { q:"How many child processes are created if `fork()` is called 3 times consecutively?", options:["3","6","7","8"], ans:2, exp:"Formula for number of child processes created is 2^n - 1. For n=3 fork() calls, 2^3 - 1 = 7 child processes are created (8 processes in total including parent)." },
    { q:"What is the key difference between a Mutex and a Binary Semaphore?", options:["Mutex has no initial value","Mutex has ownership semantics (only the thread that locked it can unlock it); semaphore can be signaled by any thread","Binary semaphore is faster","Mutex cannot be used in multithreading"], ans:1, exp:"A Mutex enforces thread ownership — only the acquiring thread can release it. A binary semaphore is a signaling mechanism where any thread can signal/post." },
    { q:"Which three criteria MUST be satisfied to solve the Critical Section problem?", options:["Mutual Exclusion, Progress, Bounded Waiting","Deadlock, Starvation, Aging","Preemption, Swapping, Thrashing","Atomicity, Durability, Isolation"], ans:0, exp:"Any valid solution to the critical section problem must satisfy: 1) Mutual Exclusion, 2) Progress, and 3) Bounded Waiting." },
    { q:"What is an 'Orphan Process' in Unix/Linux?", options:["A process killed by SIGKILL","A child process whose parent terminated before calling wait(), adopted by init/systemd (PID 1)","A process with no PID","A background daemon process"], ans:1, exp:"When a parent process terminates before its child, the child becomes an orphan and is immediately adopted by the init process (PID 1), which reaps its exit code." },
    { q:"Starvation differs from Deadlock because in Starvation:", options:["No process can ever execute","A process is indefinitely delayed waiting for a resource while other processes continue making progress","All resources are locked cyclically","Memory is exhausted"], ans:1, exp:"In deadlock, two or more processes are mutually blocked forever with zero progress. In starvation, the system continues running, but an unlucky low-priority process is perpetually postponed." },
    { q:"What is the primary role of the Translation Lookaside Buffer (TLB)?", options:["Store CPU registers","High-speed hardware cache for virtual-to-physical address translations to accelerate paging","Store disk sectors","Cache network packets"], ans:1, exp:"The TLB is an associative hardware cache in the MMU that stores recent virtual-to-physical page table mappings, avoiding double memory access penalties." },
    { q:"Which disk scheduling algorithm behaves like an elevator, servicing requests in one direction then reversing?", options:["FCFS","SSTF","SCAN (Elevator)","FIFO"], ans:2, exp:"SCAN (Elevator algorithm) sweeps the disk arm from one end to the other, servicing all requests along the path, then reverses direction at the boundary." },
    { q:"What is Internal Fragmentation in memory management?", options:["Unused space between allocated partitions","Wasted memory space inside an allocated fixed-size block/page","Memory corruption on disk","Fragmented page tables"], ans:1, exp:"Internal fragmentation occurs when memory is allocated in fixed-size blocks (like pages) and the requested process size is smaller than the block size." },
    { q:"Paging eliminates which type of memory fragmentation completely?", options:["Internal Fragmentation","External Fragmentation","Virtual Fragmentation","Cache Misses"], ans:1, exp:"Because physical memory is divided into uniform fixed-size frames, any free frame can be allocated to any process, eliminating External Fragmentation." }
  ],

  // ---- MODULE A: NETWORKS ----
  networks: [
    { q:"Which OSI layer handles end-to-end communication?", options:["Network Layer","Data Link Layer","Transport Layer","Session Layer"], ans:2, exp:"Transport Layer (Layer 4) provides end-to-end communication, error recovery, and flow control (TCP/UDP)." },
    { q:"IPv4 addresses are:", options:["16 bits","32 bits","64 bits","128 bits"], ans:1, exp:"IPv4 = 32 bits (4 octets). IPv6 = 128 bits." },
    { q:"TCP vs UDP — TCP is:", options:["Faster and unreliable","Connection-oriented with reliable delivery","Connectionless","Used only for DNS"], ans:1, exp:"TCP uses three-way handshake, provides ordered reliable delivery with acknowledgements and retransmission." },
    { q:"IP addressing and routing are handled by which OSI layer?", options:["Physical","Data Link","Network","Transport"], ans:2, exp:"Network Layer (Layer 3) handles logical IP addressing and packet routing across networks." },
    { q:"DNS operates at which OSI layer?", options:["Transport","Application","Network","Data Link"], ans:1, exp:"DNS is an Application Layer (Layer 7) protocol resolving domain names to IP addresses." },
    { q:"TCP three-way handshake sequence is:", options:["SYN → SYN-ACK → ACK","ACK → SYN → FIN","SYN → ACK → SYN","FIN → SYN → ACK"], ans:0, exp:"TCP connection starts: Client sends SYN → Server responds SYN-ACK → Client sends ACK. Connection established." },
    { q:"HTTP status code 404 means:", options:["Server Error","Request Timeout","Resource Not Found","Unauthorized"], ans:2, exp:"404 Not Found: the server cannot locate the requested resource at the given URL." },
    { q:"HTTPS uses which protocol to encrypt traffic?", options:["SSH","TLS/SSL","FTP","SMTP"], ans:1, exp:"HTTPS = HTTP over TLS (Transport Layer Security), formerly SSL. TLS encrypts data in transit." },
    { q:"ARP (Address Resolution Protocol) resolves:", options:["Domain names to IPs","IP addresses to MAC addresses","Ports to services","MAC to hostname"], ans:1, exp:"ARP maps known IP addresses to physical MAC addresses on a local network segment." },
    { q:"Which port does HTTPS use by default?", options:["80","21","443","22"], ans:2, exp:"HTTPS uses port 443. HTTP uses port 80. SSH uses port 22. FTP uses port 21." },
    { q:"A subnet mask /24 means:", options:["24 hosts max","First 24 bits are network, last 8 are hosts","24 subnets","IPv6 notation"], ans:1, exp:"/24 = 255.255.255.0. First 24 bits = network address, last 8 bits = host addresses (254 usable hosts)." },
    { q:"Firewall operates at which OSI layer primarily?", options:["Physical","Network & Transport layers (inspects IP/ports)","Application only","Data Link"], ans:1, exp:"Firewalls inspect Network (IP) and Transport (TCP/UDP port) layer headers. Next-gen firewalls also inspect Application layer." },
    { q:"Which protocol sends email FROM client to server?", options:["POP3","IMAP","SMTP","FTP"], ans:2, exp:"SMTP (Simple Mail Transfer Protocol) sends outgoing email. POP3/IMAP are used to retrieve email from a server." },
    { q:"Load balancer distributes requests to:", options:["A single backup server","Multiple backend servers to prevent overload","Only local servers","DNS resolvers"], ans:1, exp:"Load balancers distribute incoming traffic across multiple backend server instances for high availability and horizontal scaling." },
    { q:"The difference between LAN and WAN:", options:["LAN is wireless; WAN is wired","LAN covers small area (building); WAN covers large area (country/globe)","LAN uses IP; WAN uses MAC","No difference"], ans:1, exp:"LAN (Local Area Network) covers small areas like offices. WAN (Wide Area Network) spans cities/countries — the Internet is a WAN." },
    { q:"How many usable host IP addresses are available in a `/27` IPv4 subnet?", options:["32","30","28","16"], ans:1, exp:"Host bits = 32 - 27 = 5 bits. Total IPs = 2^5 = 32. Subtracting network ID and broadcast address gives 32 - 2 = 30 usable host addresses." },
    { q:"In TCP connection termination, how many packets are exchanged in a normal graceful close?", options:["2 (FIN, ACK)","3 (FIN, ACK, FIN)","4 (FIN, ACK, FIN, ACK)","1 (RST)"], ans:2, exp:"Graceful TCP closing is a 4-way handshake: Client sends FIN → Server sends ACK; Server sends FIN → Client sends ACK." },
    { q:"Which phase of TCP Congestion Control doubles the Congestion Window (cwnd) every RTT?", options:["Congestion Avoidance","Slow Start","Fast Recovery","AIMD Linear Phase"], ans:1, exp:"During Slow Start, cwnd starts at 1 MSS and increments exponentially (doubles every Round Trip Time) until reaching ssthresh." },
    { q:"Which IPv4 address block is designated as a Private Address Range (RFC 1918)?", options:["11.0.0.0/8","192.168.0.0/16","200.100.0.0/16","8.8.8.0/24"], ans:1, exp:"RFC 1918 private ranges are: 10.0.0.0/8 (Class A), 172.16.0.0/12 (Class B), and 192.168.0.0/16 (Class C)." },
    { q:"How does TLS/HTTPS leverage asymmetric and symmetric cryptography together?", options:["Only symmetric is used throughout","Asymmetric cryptography (RSA/ECC) establishes identity and securely exchanges a symmetric session key; symmetric (AES) encrypts bulk data","Asymmetric encrypts all data packets","Only hashing is used"], ans:1, exp:"Asymmetric encryption is computationally expensive, so TLS uses it only for handshake authentication and key exchange, then switches to fast symmetric encryption (e.g. AES-GCM) for data transfer." },
    { q:"What HTTP method is sent as a Preflight Request in Cross-Origin Resource Sharing (CORS)?", options:["HEAD","GET","OPTIONS","TRACE"], ans:2, exp:"Browsers automatically dispatch a preflight HTTP `OPTIONS` request to check CORS permissions before sending non-simple cross-origin requests." },
    { q:"What is the four-step handshake sequence used by DHCP to allocate an IP address?", options:["SYN, ACK, PUSH, FIN","DORA (Discover, Offer, Request, Acknowledge)","ARP, RARP, DNS, NAT","PING, PONG, ECHO, REPLY"], ans:1, exp:"DHCP uses the DORA sequence: Client broadcasts Discover → Server sends Offer → Client broadcasts Request → Server returns Acknowledge." },
    { q:"What is the standard Ethernet Maximum Transmission Unit (MTU) size?", options:["512 bytes","1024 bytes","1500 bytes","9000 bytes"], ans:2, exp:"The standard MTU for standard Ethernet frames is 1500 bytes (payload size excluding 14-byte Ethernet header and 4-byte CRC)." },
    { q:"Which protocol does the `ping` utility use to test network reachability?", options:["TCP SYN","UDP Port 53","ICMP (Internet Control Message Protocol)","SNMP"], ans:2, exp:"`ping` operates at Layer 3 using ICMP Echo Request (Type 8) and listens for ICMP Echo Reply (Type 0)." },
    { q:"What is the difference between CSMA/CD and CSMA/CA?", options:["CSMA/CD detects collisions (used in wired Ethernet); CSMA/CA avoids collisions with RTS/CTS (used in Wi-Fi 802.11)","CSMA/CD is for satellite only","CSMA/CA is faster than CSMA/CD","They are identical"], ans:0, exp:"Wired Ethernet can detect packet collisions simultaneously on the wire (CSMA/CD). Wireless radio cannot transmit and listen at the same frequency at once, so it avoids collisions using CSMA/CA." }
  ],

  // ---- MODULE A: DEVOPS/CLOUD ----
  devops: [
    { q:"REST stands for:", options:["Remote Execution Standard Transfer","Representational State Transfer","Real-time Extensible Service","Reliable Endpoint Template"], ans:1, exp:"REST = Representational State Transfer, an architectural style for stateless HTTP-based networked apps." },
    { q:"git rebase vs git merge — rebase:", options:["Creates merge commit","Rewrites history by replaying commits linearly","Is the same as merge","Deletes branches"], ans:1, exp:"Rebase replays commits onto another branch creating a linear history; merge creates a merge commit preserving branch history." },
    { q:"IaaS provides:", options:["Complete SaaS apps","Development platform","Virtualized compute infrastructure (VMs, storage, networking)","Only database services"], ans:2, exp:"IaaS delivers virtualized infrastructure — VMs, storage, networking. Users manage OS and above. Examples: AWS EC2, Azure VMs." },
    { q:"Containers vs VMs — containers:", options:["Include full OS kernel","Share host OS kernel, making them lighter","Are slower than VMs","Cannot run multiple processes"], ans:1, exp:"Containers share the host OS kernel — much lighter and faster to start than VMs which include a full guest OS." },
    { q:"CI/CD stands for:", options:["Code Integration/Deployment","Continuous Integration/Continuous Delivery","Container Infrastructure/Cloud Delivery","Central Integration/Controlled Deployment"], ans:1, exp:"CI = Continuous Integration (auto build & test), CD = Continuous Delivery/Deployment (auto release to production)." },
    { q:"Docker Compose is used to:", options:["Build Docker images from scratch","Define and run multi-container Docker applications via YAML","Monitor container performance","Push images to Docker Hub"], ans:1, exp:"Docker Compose uses docker-compose.yml to define multi-container apps (e.g., app + database + cache) and start them with one command." },
    { q:"Kubernetes (K8s) primary function is:", options:["Code version control","Container orchestration — managing, scaling, self-healing containerized apps","Network firewall management","Static website hosting"], ans:1, exp:"Kubernetes automates deployment, scaling, rolling updates, and self-healing of containerized workloads across clusters." },
    { q:"PaaS (Platform as a Service) provides:", options:["Raw VMs only","Complete managed platform: runtime, middleware, OS — user only manages apps & data","Full SaaS applications","Only CDN services"], ans:1, exp:"PaaS (e.g., Heroku, Google App Engine, Azure App Service) provides the platform; devs only manage code and data." },
    { q:"git stash is used to:", options:["Delete uncommitted changes","Temporarily save uncommitted changes without committing","Merge branches","Push code to remote"], ans:1, exp:"git stash saves your working directory changes in a stack so you can switch branches without committing or losing work." },
    { q:"Microservices architecture differs from monolith by:", options:["Running everything in one process","Splitting application into small independent services each with its own deployment and scaling","Using a single database for all services","Eliminating APIs"], ans:1, exp:"Microservices: each bounded context is an independent deployable service. Monolith: all components bundled in one deployable unit." },
    { q:"In Agile Scrum, a Sprint is:", options:["A final release","A time-boxed iteration (1-4 weeks) to deliver a potentially shippable increment","A retrospective meeting","A deployment pipeline"], ans:1, exp:"Sprint = fixed-length iteration where the team commits to a Sprint Backlog and delivers a working increment at the end." },
    { q:"Infrastructure as Code (IaC) means:", options:["Writing code manually on servers","Provisioning infrastructure (VMs, networks) via code files — e.g., Terraform, CloudFormation","Writing infrastructure documentation","Hiring DevOps engineers"], ans:1, exp:"IaC tools like Terraform declare infrastructure resources in config files — enabling version control, reproducibility, and automated provisioning." },
    { q:"Which HTTP method is idempotent AND safe?", options:["POST","PUT","DELETE","GET"], ans:3, exp:"GET is both safe (no state change) and idempotent (same result on repeat). POST creates resources (not idempotent). PUT is idempotent but not safe." },
    { q:"Blue-Green deployment strategy means:", options:["Deploying on blue or green servers only","Maintaining two identical environments; switching traffic from old (blue) to new (green) for zero-downtime releases","A color scheme for dashboards","A network topology"], ans:1, exp:"Blue-Green: Blue = current production, Green = new version. After validation, route traffic to Green. Instant rollback by switching back to Blue." },
    { q:"Git 'origin' refers to:", options:["The first commit","The main branch","The default remote repository URL (e.g., GitHub)","A git alias"], ans:2, exp:"'origin' is git's default alias for the remote repository URL you cloned from or added with git remote add." },
    { q:"In a Dockerfile, what is the fundamental difference between `CMD` and `ENTRYPOINT`?", options:["CMD cannot take arguments","ENTRYPOINT defines the fixed executable, while CMD provides default arguments that can be overridden at runtime","CMD runs during build, ENTRYPOINT at runtime","They are identical aliases"], ans:1, exp:"`ENTRYPOINT` sets the immutable command binary (e.g. `['python', 'app.py']`), while `CMD` supplies default parameters that CLI users can easily override via `docker run`." },
    { q:"What is the primary benefit of Multi-Stage Builds in Docker?", options:["Allows multiple OS kernels","Drastically reduces final production image size by leaving compilers and build tools in interim stages","Compiles multiple languages simultaneously","Creates multi-region deployments"], ans:1, exp:"Multi-stage builds allow developers to compile source code with heavy SDKs in stage 1, then copy only the stripped binary/artifacts into a lean production runtime image (e.g. Alpine)." },
    { q:"In Kubernetes, what is the smallest deployable compute unit?", options:["Container","Pod (group of one or more containers sharing network/storage)","Deployment","Node"], ans:1, exp:"A Pod is the smallest execution unit in Kubernetes; it encapsulates one or more co-located containers that share an IP address and volume storage." },
    { q:"What does `git cherry-pick <commit-hash>` do?", options:["Deletes the commit from branch","Applies the changes from an individual commit onto the current working HEAD branch","Reverts the last 5 commits","Merges an entire branch"], ans:1, exp:"`git cherry-pick` selects a single commit from another branch and replays its diff as a new commit onto the currently checked-out branch." },
    { q:"What does a 'Detached HEAD' state indicate in Git?", options:["Corrupted repository files","HEAD points directly to a specific commit hash rather than a named branch ref","The remote server is unreachable","The main branch is deleted"], ans:1, exp:"A detached HEAD means HEAD points directly to a commit SHA (e.g. after checking out a tag or specific commit); new commits made in this state won't belong to any branch unless one is created." },
    { q:"What is a Canary Deployment release strategy?", options:["Shutting down all servers simultaneously","Gradually rolling out the new release to a tiny subset of users (e.g. 5%) to verify stability before full rollout","Deploying on weekends only","Deploying identical code to two clusters"], ans:1, exp:"Canary deployment routes a small percentage of production traffic to the new version to detect errors with minimal blast radius before rolling out to 100% of users." },
    { q:"What is the architectural role of Prometheus in cloud-native monitoring?", options:["Dashboard visualization tool","Time-series metrics database that scrapes telemetry endpoints via a pull model","Log file aggregator","Load balancer"], ans:1, exp:"Prometheus is a time-series monitoring system that pulls/scrapes metrics over HTTP from instrumented targets and stores them with key-value labels." },
    { q:"What is the difference between a Docker Volume and a Bind Mount?", options:["Volumes are slower than bind mounts","Volumes are fully managed by Docker in a dedicated storage area (`/var/lib/docker/volumes`), whereas bind mounts map to any host file path","Bind mounts cannot be modified","Volumes cannot be backed up"], ans:1, exp:"Volumes are Docker-managed storage isolated from host OS specifics, making them portable and secure. Bind mounts depend on host directory hierarchies." },
    { q:"According to Semantic Versioning (SemVer `MAJOR.MINOR.PATCH`), when must the MAJOR version increment?", options:["When adding backwards-compatible features","When making backwards-incompatible (breaking) API changes","When fixing bugs","Every calendar year"], ans:1, exp:"SemVer rules: Increment MAJOR for breaking API changes, MINOR for backwards-compatible new features, and PATCH for backwards-compatible bug fixes." },
    { q:"What is the primary role of a Reverse Proxy (like NGINX) in frontend architecture?", options:["Encrypting developer hard drives","Fronting backend servers to handle SSL termination, load balancing, compression, and hiding internal topology","Acting as a client browser","Compiling JavaScript code"], ans:1, exp:"A reverse proxy sits in front of web servers and intercepts client requests, performing TLS termination, caching, load balancing, and preventing direct public access to internal microservices." }
  ],

  // ---- MODULE B: QUANTITATIVE APTITUDE ----
  aptitude: [
    { q:"A train 150m long passes a pole in 15 seconds. Speed of the train?", options:["10 m/s (36 km/h)","15 m/s","20 m/s","25 km/h"], ans:0, exp:"Speed = 150/15 = 10 m/s = 36 km/h." },
    { q:"20% of a number is 80. What is 35% of that number?", options:["120","140","160","180"], ans:1, exp:"Number = 80/0.20 = 400. 35% of 400 = 140." },
    { q:"Two pipes fill a tank in 12 and 15 hours. Together they take:", options:["6.67 hours","5.45 hours","6 hours","7 hours"], ans:0, exp:"Rate = 1/12 + 1/15 = 9/60. Time = 60/9 ≈ 6.67 hours." },
    { q:"Boys:Girls = 3:2. Total 30 students. How many girls?", options:["12","18","15","10"], ans:0, exp:"Girls = (2/5) × 30 = 12." },
    { q:"Bought at ₹200, sold at ₹250. Profit percentage?", options:["20%","25%","15%","30%"], ans:1, exp:"Profit% = (50/200) × 100 = 25%." },
    { q:"Simple Interest on ₹5000 at 8% p.a. for 3 years?", options:["₹1200","₹1000","₹1500","₹800"], ans:0, exp:"SI = (P × R × T)/100 = (5000 × 8 × 3)/100 = ₹1200." },
    { q:"Average of 5 numbers is 20. If one number is removed, average becomes 18. Removed number?", options:["26","28","30","24"], ans:1, exp:"Total = 5×20 = 100. Remaining 4 numbers total = 4×18 = 72. Removed = 100−72 = 28." },
    { q:"A person covers 60 km in 2 hours by car, then 40 km in 2 hours by foot. Average speed?", options:["20 km/h","22 km/h","25 km/h","18 km/h"], ans:2, exp:"Total distance = 60 + 40 = 100 km. Total time = 2 + 2 = 4 hours. Average speed = 100 / 4 = 25 km/h." },
    { q:"In how many ways can 5 books be arranged on a shelf?", options:["25","60","120","100"], ans:2, exp:"Permutation: 5! = 5×4×3×2×1 = 120 arrangements." },
    { q:"Compound Interest on ₹10,000 at 10% p.a. compounded annually for 2 years?", options:["₹2000","₹2100","₹2200","₹1900"], ans:1, exp:"A = P(1+r/100)^t = 10000(1.1)^2 = 12100. CI = 12100−10000 = ₹2100." },
    { q:"Probability of getting a head in a fair coin toss?", options:["1","0","1/2","1/4"], ans:2, exp:"Fair coin has 2 equally likely outcomes (H, T). P(H) = 1/2." },
    { q:"If A can do a job in 10 days and B in 15 days, together they finish in:", options:["6 days","8 days","5 days","12 days"], ans:0, exp:"Combined rate = 1/10 + 1/15 = 5/30 = 1/6. Together: 6 days." },
    { q:"The ratio 3:4 is equivalent to:", options:["6:10","9:12","12:15","15:16"], ans:1, exp:"3:4 × 3 = 9:12. Both 9 and 12 share factor 3. 9/12 = 3/4 ✓" },
    { q:"A car travels 300 km at 60 km/h and returns at 90 km/h. Average speed for round trip?", options:["72 km/h","75 km/h","70 km/h","80 km/h"], ans:0, exp:"Harmonic mean: 2 × (60×90)/(60+90) = 10800/150 = 72 km/h." },
    { q:"₹800 increased by 25% then decreased by 25%. Final amount?", options:["₹800","₹750","₹780","₹700"], ans:1, exp:"After +25%: 800×1.25 = 1000. After −25%: 1000×0.75 = 750. Net loss due to different bases." },
    { q:"A boat travels downstream at 14 km/h and upstream at 8 km/h. What is the speed of the boat in still water?", options:["11 km/h","10 km/h","12 km/h","3 km/h"], ans:0, exp:"Speed in still water = (Downstream + Upstream) / 2 = (14 + 8) / 2 = 11 km/h. (Stream speed = (14 - 8)/2 = 3 km/h)." },
    { q:"A pipe can fill a tank in 6 hours, but due to a leak at the bottom it takes 8 hours. How long will the leak alone take to empty a full tank?", options:["14 hours","20 hours","24 hours","18 hours"], ans:2, exp:"Leak rate = 1/6 - 1/8 = (4 - 3)/24 = 1/24 tank/hr. Thus, the leak alone empties the tank in 24 hours." },
    { q:"What is the angle between the hour hand and the minute hand of a clock at 3:30?", options:["75°","70°","80°","90°"], ans:0, exp:"Angle formula: |30×H - 5.5×M| = |30(3) - 5.5(30)| = |90 - 165| = 75°." },
    { q:"What is the difference between Compound Interest and Simple Interest on ₹25,000 for 2 years at 8% per annum?", options:["₹140","₹160","₹180","₹200"], ans:1, exp:"For 2 years: Difference = P × (R / 100)^2 = 25000 × (8/100)^2 = 25000 × 0.0064 = ₹160." },
    { q:"Two trains of lengths 120m and 180m are traveling in opposite directions at 42 km/h and 48 km/h. How many seconds will they take to cross each other completely?", options:["12 seconds","15 seconds","10 seconds","18 seconds"], ans:0, exp:"Total distance = 120 + 180 = 300m. Relative speed = 42 + 48 = 90 km/h = 90 × (5/18) = 25 m/s. Time = 300 / 25 = 12 seconds." },
    { q:"A dealer marks an article 30% above the cost price and allows a discount of 10% on the marked price. Find his profit percentage.", options:["15%","17%","20%","18%"], ans:1, exp:"Let CP = 100. MP = 130. SP after 10% discount = 130 - 13 = 117. Profit% = ((117 - 100)/100) × 100 = 17%." },
    { q:"What is the probability of drawing either a King or a Heart from a standard deck of 52 playing cards?", options:["4/13","17/52","16/52 (4/13)","1/4"], ans:2, exp:"P(King or Heart) = P(King) + P(Heart) - P(King of Hearts) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13." },
    { q:"In what ratio must tea at ₹62 per kg be mixed with tea at ₹72 per kg so that the mixture is worth ₹65 per kg?", options:["7:3","3:7","5:3","4:3"], ans:0, exp:"By Rule of Alligation: (Cheaper : Dearer) = (72 - 65) : (65 - 62) = 7 : 3." },
    { q:"A and B can do a work in 12 days and 18 days. If they work on alternate days starting with A, in how many days will the work finish?", options:["14.33 days","14 days 2/3","14.5 days","15 days"], ans:0, exp:"LCM of (12, 18) = 36 units. A does 3 units/day, B does 2 units/day. In 2 days = 5 units. In 14 days (7 cycles) = 35 units done. Remaining 1 unit done by A in 1/3 day. Total = 14 + 1/3 ≈ 14.33 days." },
    { q:"If 1st January 2024 was a Monday, what day of the week was 1st January 2025?", options:["Tuesday","Wednesday","Thursday","Sunday"], ans:1, exp:"2024 is a leap year (366 days = 52 weeks + 2 odd days). Adding 2 days to Monday gives Wednesday." }
  ],

  // ---- STAGE 1: VERBAL ABILITY & ENGLISH ----
  verbal: [
    { q:"Choose the synonym of 'VERBOSE':", options:["Concise","Wordy","Silent","Ambiguous"], ans:1, exp:"Verbose = using too many words. Synonym = Wordy." },
    { q:"Identify the error: 'He go to school every day'", options:["He","go","to school","every day"], ans:1, exp:"'go' should be 'goes' — third-person singular requires -s/-es in simple present." },
    { q:"Select the correctly spelled word:", options:["Accomodation","Accommodation","Acommodation","Accomadation"], ans:1, exp:"Correct: 'Accommodation' — double 'c' and double 'm'." },
    { q:"Antonym of 'BENEVOLENT':", options:["Kind","Generous","Malevolent","Charitable"], ans:2, exp:"Benevolent = kind/well-meaning. Antonym = Malevolent (wishing evil)." },
    { q:"'She _____ to the market yesterday.'", options:["go","goes","went","going"], ans:2, exp:"'Yesterday' = past tense. Past of 'go' = 'went'." },
    { q:"'The project was ___ by the team within the deadline.'", options:["Completing","Completed","Complete","Completes"], ans:1, exp:"Passive voice 'was ___' requires past participle 'Completed'." },
    { q:"Correct passive voice sentence:", options:["The dog bit the man","The man was bitten by the dog","The man bited by the dog","The dog was biting the man"], ans:1, exp:"Passive: Object + was/were + past participle + by agent. 'The man was bitten by the dog'." },
    { q:"'The wind whispered through the trees' is an example of:", options:["Simile","Metaphor","Personification","Hyperbole"], ans:2, exp:"Personification attributes human quality (whispering) to non-human entity (wind)." },
    { q:"Choose the word: 'Despite working _____, she finished on time.'", options:["lazily","diligently","carelessly","slowly"], ans:1, exp:"'Despite' + positive result (finished on time) suggests hard work = 'diligently'." },
    { q:"Para jumble: Which sequence makes a coherent paragraph?\nA: She loved reading.\nB: Books were her escape.\nC: Every evening she read.\nD: Libraries were her sanctuary.", options:["A-B-D-C","B-A-C-D","C-A-B-D","A-C-B-D"], ans:0, exp:"Logical sequence A-B-D-C." },
    { q:"Idiom meaning: 'Bite the bullet'", options:["To eat quickly","To endure a painful situation with courage","To start a fight","To make an error"], ans:1, exp:"'Bite the bullet' means to face a difficult situation with bravery." },
    { q:"Find the error: 'Neither of the two candidates have submitted their resume.'", options:["Neither","have submitted","their","No error"], ans:1, exp:"'Neither of' takes a singular verb: 'has submitted'." },
    { q:"Choose antonym of 'EPHEMERAL':", options:["Short-lived","Eternal","Fleeting","Transient"], ans:1, exp:"Ephemeral = temporary. Antonym = Eternal/Permanent." },
    { q:"Sentence Improvement: 'I look forward to meet you.'", options:["to meeting you","to met you","for meeting you","No improvement"], ans:0, exp:"'Look forward to' takes a gerund (-ing): 'to meeting you'." },
    { q:"Synonym of 'PRAGMATIC':", options:["Theoretical","Practical","Emotional","Idealistic"], ans:1, exp:"Pragmatic means practical, dealing with things realistically." },
    { q:"Select the synonym of 'UBIQUITOUS':", options:["Rare","Omnipresent (found everywhere)","Precious","Uncertain"], ans:1, exp:"Ubiquitous means present, appearing, or found everywhere (e.g. 'Smartphones have become ubiquitous')." },
    { q:"Select the synonym of 'METICULOUS':", options:["Careless","Fast","Painstakingly thorough and careful","Indifferent"], ans:2, exp:"Meticulous refers to showing great attention to detail, very careful and precise." },
    { q:"Choose the antonym of 'CANDOR':", options:["Frankness","Deceitfulness / Insincerity","Honesty","Openness"], ans:1, exp:"Candor means being open, honest, and frank. The antonym is deceitfulness, insincerity, or guile." },
    { q:"Choose the antonym of 'PLACATE':", options:["Appease","Soothe","Enrage / Provoke","Pacify"], ans:2, exp:"To placate means to make someone less angry or hostile. The opposite is to enrage or provoke." },
    { q:"Identify the error: 'Scarcely had the teacher entered the classroom then the students stood up.'", options:["Scarcely had","entered","then","stood up"], ans:2, exp:"'Scarcely' and 'Hardly' are always paired with 'when', not 'then' (e.g. 'Scarcely had... when...')." },
    { q:"Fill in the blank: 'The committee _____ divided in their opinions regarding the budget.'", options:["is","was","were","has been"], ans:2, exp:"When a collective noun functions with members acting individually or with differing opinions, it takes a plural verb ('were divided')." },
    { q:"Choose the correct preposition: 'She has been working in this firm _____ 2021.'", options:["for","since","from","by"], ans:1, exp:"'Since' is used to denote a specific starting point in time in the past for actions continuing into the present." },
    { q:"What is the meaning of the idiom 'To spill the beans'?", options:["To waste food","To disclose a secret prematurely or inadvertently","To cook hurriedly","To make a mess"], ans:1, exp:"'To spill the beans' means to reveal secret information accidentally or maliciously." },
    { q:"What is the meaning of the idiom 'To burn the midnight oil'?", options:["To light kerosene lamps","To waste resources","To work or study late into the night","To cause an accident"], ans:2, exp:"'To burn the midnight oil' means to work or study late into the night." },
    { q:"Convert to Indirect Speech: He said, 'I have completed my assignment.'", options:["He said that he completed his assignment.","He said that he had completed his assignment.","He said that he has completed his assignment.","He said that he would complete his assignment."], ans:1, exp:"Present Perfect ('have completed') shifts to Past Perfect ('had completed') in reported speech with a past reporting verb." },
    { q:"Choose the correct passive voice: 'They will announce the results tomorrow.'", options:["The results will announced tomorrow.","The results will be announced tomorrow by them.","The results are announced tomorrow.","The results have been announced tomorrow."], ans:1, exp:"Simple Future passive voice structure: Subject + will + be + past participle ('will be announced')." },
    { q:"Select the correctly spelled word:", options:["Bureaucracy","Burocracy","Beurocracy","Bureaucracyy"], ans:0, exp:"Correct spelling is 'Bureaucracy' (b-u-r-e-a-u-c-r-a-c-y)." },
    { q:"One Word Substitution: 'A person who hates or distrusts humankind'", options:["Philanthropist","Misanthrope","Altruist","Introvert"], ans:1, exp:"A misanthrope is someone who dislikes, distrusts, or avoids human society." },
    { q:"Identify the correct sentence:", options:["One of the students who has participated is absent.","One of the students who have participated is absent.","One of the student who has participated is absent.","One of the students who have participated are absent."], ans:1, exp:"The relative pronoun 'who' refers to plural antecedent 'students' (taking 'have participated'), while the main clause subject 'One' takes singular verb 'is absent'." },
    { q:"What does the idiom 'Cut corners' mean?", options:["To take a sharp turn","To do something poorly or cheaply in order to save time or money","To cut paper with scissors","To solve a difficult puzzle"], ans:1, exp:"'To cut corners' means to undertake a task in the easiest, cheapest, or fastest way, frequently compromising quality." }
  ],

  // ---- STAGE 2B: DEBUGGING ----
  debugging: [
    { q:"Find the bug:\nint sum=0;\nfor(int i=0; i<=n; i++) sum+=arr[i];\nreturn sum;", options:["i<=n causes array out-of-bounds; should be i<n","sum should be initialized differently","arr[i] should be arr[i+1]","return type is wrong"], ans:0, exp:"i<=n accesses arr[n] which is out of bounds. Correct condition is i<n for 0-based arrays of size n." },
    { q:"Find the bug:\nint factorial(int n){\n  return n * factorial(n-1);\n}", options:["Missing base case — will cause infinite recursion/stack overflow","Return type should be long","n should be n+1","Loop should be used instead"], ans:0, exp:"No base case! When n reaches 0 or negative, recursion never terminates. Add: if(n<=1) return 1;" },
    { q:"Find the bug:\nint a;\na = a + 5;\nprintf(\"%d\", a);", options:["printf format is wrong","a is uninitialized — contains garbage value","Addition syntax is wrong","No bug exists"], ans:1, exp:"int a; declared but not initialized. a contains a garbage/undefined value. Should be int a=0;" },
    { q:"Find the bug:\nint* ptr = NULL;\n*ptr = 42;", options:["ptr type is wrong","Dereferencing a NULL pointer — causes segmentation fault","42 is invalid","= should be =="], ans:1, exp:"Dereferencing a NULL pointer (*ptr) causes undefined behavior / segmentation fault at runtime." },
    { q:"Find the bug in BST insertion:\nvoid insert(Node* root, int val){\n  if(val < root->data) insert(root->left, val);\n  else insert(root->right, val);\n}", options:["Missing NULL check — doesn't handle empty tree or create new nodes","val comparison is wrong","Should use iterative approach","root->data should be root->val"], ans:0, exp:"No NULL check! When root is NULL, should create new Node. Also doesn't return/assign the new node back." },
    { q:"Find the bug:\nfor(int i=0; i<n; i++){\n  for(int j=0; j<n; j++){\n    if(arr[i] == arr[j]) printf(\"dup\");\n  }\n}", options:["Missing break statement","When i==j it always finds a 'duplicate' (element equals itself)","arr comparison is wrong","Loop bounds are wrong"], ans:1, exp:"When i==j, arr[i]==arr[j] is always true (same element). Inner loop should start at j=i+1." },
    { q:"Find the bug:\nint str_len(char* s){\n  int count=0;\n  while(s[count] != NULL) count++;\n  return count;\n}", options:["count should start at 1","NULL should be '\\0' (null terminator) not the NULL pointer","return should be count-1","s is wrong type"], ans:1, exp:"String null terminator is '\\0' (char 0), not NULL pointer. Use while(s[count] != '\\0') or while(s[count])." },
    { q:"Find the bug in this swap:\nvoid swap(int a, int b){\n  int temp = a;\n  a = b;\n  b = temp;\n}", options:["temp variable is wrong","Passed by value — changes don't reflect outside; needs pointers","Should use XOR swap","No bug"], ans:1, exp:"C passes by value. Changes to a,b don't affect caller's variables. Use void swap(int* a, int* b) and dereference." },
    { q:"Find the bug:\nint arr[5] = {1,2,3,4,5};\nprintf(\"%d\", arr[5]);", options:["printf format wrong","arr[5] is out of bounds — valid indices are 0 to 4","Array initialization wrong","No bug"], ans:1, exp:"Array of size 5 has valid indices 0–4. arr[5] accesses beyond the array boundary — undefined behavior." },
    { q:"Find the bug:\nwhile(1){\n  printf(\"hello\");\n  if(count == 10) break;\n}", options:["break is wrong","count is never incremented — infinite loop","printf shouldn't be in loop","while(1) is invalid"], ans:1, exp:"count is never incremented inside the loop, so count==10 is never reached, causing an infinite loop." },
    { q:"Find the bug in linked list traversal:\nNode* curr = head;\nwhile(curr != NULL){\n  printf(\"%d \", curr->data);\n  curr = curr->data;\n}", options:["Should print curr->next->data","curr = curr->data should be curr = curr->next","head should be used not curr","NULL check is wrong"], ans:1, exp:"curr->data is the integer data field. To advance in a linked list, use curr = curr->next (the pointer to next node)." },
    { q:"Find the memory leak in C++:\nint* arr = new int[100];\n// ... processing ...\ndelete arr;", options:["Should be delete[] arr; to deallocate array memory","arr should be free()","new is not allowed","delete is wrong"], ans:0, exp:"Arrays allocated with new[] must be freed using delete[] to prevent memory leaks." },
    { q:"Find the bug in Binary Search midpoint calculation:\nint mid = (low + high) / 2;", options:["Causes integer overflow if low + high exceeds INT_MAX; should be low + (high - low) / 2","Division should be by 2.0","mid should be float","low + high must be odd"], ans:0, exp:"For large array indices (e.g. low + high > 2^31 - 1), direct addition wraps into negative numbers causing an overflow crash. Use `low + (high - low) / 2`." },
    { q:"Find the bug in floating-point comparison:\ndouble x = 0.1 * 3;\nif (x == 0.3) printf(\"Equal\");", options:["x is not initialized","Direct equality `==` fails due to binary IEEE-754 precision representation; should use `fabs(x - 0.3) < 1e-9`","double cannot be multiplied by int","printf syntax error"], ans:1, exp:"0.1 cannot be represented exactly in binary floating-point. Comparing with `==` often fails. Always compare with an epsilon tolerance." },
    { q:"Find the bug with pointer post-increment:\nint* ptr = arr;\nint val = *ptr++;", options:["val is unassigned","It dereferences ptr first, then increments the pointer address, not the value pointed to","Syntax error with ++","ptr is invalidated"], ans:1, exp:"`*ptr++` evaluates to `*(ptr++)`, advancing the pointer to the next element. If the intent was incrementing the integer value, parentheses are required: `(*ptr)++`." },
    { q:"Find the bug in 2D Dynamic Programming table allocation:\nint dp[m][n];\n// trying to compute dp for lengths up to m and n", options:["Table sizes should be `dp[m+1][n+1]` to accommodate the 0-length base case (indices 0 to m and 0 to n)","Variable-length arrays are strictly forbidden in all compilers","dp should be float","dp cannot be 2D"], ans:0, exp:"Standard 2D DP problems (like LCS or Edit Distance) require index 0 as an empty string/base case, requiring an array of dimensions `(m+1) × (n+1)`." },
    { q:"Find the bug in dynamic memory deallocation:\nint* p = (int*)malloc(sizeof(int));\nfree(p);\nfree(p);", options:["malloc cannot allocate single int","Double Free error: freeing already freed pointer results in heap corruption or SIGABRT","free requires two arguments","p must be set to 1 before free"], ans:1, exp:"Calling `free()` twice on the same heap pointer causes a Double Free vulnerability, corrupting the memory allocator's metadata." },
    { q:"Find the bug in string manipulation:\nchar* str = \"hello\";\nstr[0] = 'H';", options:["Single quotes cannot be used","String literal is stored in read-only data segment (RODATA); modifying it triggers a Segmentation Fault","str is not a char pointer","'H' is invalid character"], ans:1, exp:"String literals are immutable and stored in read-only memory. Attempting to write to `str[0]` causes an immediate access violation / SIGSEGV. Use `char str[] = \"hello\";` instead." },
    { q:"Find the bug in function return:\nint* getArray() {\n  int localArr[5] = {1,2,3,4,5};\n  return localArr;\n}", options:["localArr has too few elements","Returning address of local stack variable results in a dangling pointer after function frame unwinds","Array cannot be initialized with braces","Return type should be void"], ans:1, exp:"Local array `localArr` is allocated on the stack frame. Once `getArray()` returns, that stack frame is invalidated. Returning its address creates a dangerous dangling pointer." },
    { q:"Find the bug in modulo arithmetic with negative numbers in C++:\nint r = -7 % 3;\n// expected positive remainder in range [0, 2]", options:["% operator is not supported for negative integers in C++","In C++, -7 % 3 evaluates to -1; to get mathematical positive modulo use `(n % m + m) % m`","3 cannot divide 7","r must be unsigned"], ans:1, exp:"In C/C++ (C99+ / C++11+), `%` computes the remainder which retains the numerator's sign (`-7 % 3 == -1`). To map into `[0, m-1]`, use `((n % m) + m) % m`." },
    { q:"Find the bug in string concatenation inside a loop in Java:\nString s = \"\";\nfor(int i = 0; i < 10000; i++) s += i;", options:["Loop bound is too large","Repeated `+=` creates 10,000 intermediate String objects causing O(N^2) time and memory overhead; should use `StringBuilder`","int cannot be added to String","Java does not allow `+=` on Strings"], ans:1, exp:"Strings in Java are immutable. Each `s += i` creates a new String and copies previous characters, degrading performance to O(N^2). `StringBuilder.append()` operates in amortized O(1) time." },
    { q:"Find the bug in C++ struct pointer access:\nstruct Student { int id; };\nStudent* s = new Student();\ns.id = 101;", options:["Student cannot be dynamically allocated","Member access on a pointer must use the arrow operator `s->id` or `(*s).id`, not `s.id`","101 is not a valid id","delete is missing immediately"], ans:1, exp:"The dot operator `.` is used for object instances or references. For pointers to structs/classes, the arrow operator `->` or explicit dereference `(*s).id` must be used." }
  ],

  // ---- STAGE 3: AI CODING & PROMPT STRATEGY ----
  ai_coding: [
    { q:"In Capgemini's AI-Assisted Coding (Stage 3), which type of prompt will NOT unlock the next step?", options:["A prompt explaining input/output and constraints in your own words","A one-liner like 'write the code for this'","A prompt specifying edge cases like null input","A prompt explaining your chosen algorithm approach"], ans:1, exp:"Capgemini's AI assistant specifically rejects vague one-liners. You must restate inputs, outputs, and constraints meaningfully." },
    { q:"What does Capgemini evaluate under 'Prompt Quality' in the AI Coding Assessment?", options:["Speed of typing","Structured, constraint-driven prompts — not random one-liners","Length of the prompt","Number of follow-up prompts sent"], ans:1, exp:"Prompt Quality: structured, relevant prompts that describe the problem, constraints, and expected behavior clearly." },
    { q:"For the AI-Assisted Coding round, what should you do AFTER the AI generates code?", options:["Submit immediately","Delete and rewrite manually","Review for correctness, verify edge cases, and adapt if wrong","Copy-paste without checking"], ans:2, exp:"'Review & Adapt' is the 4th evaluation criterion. Never blindly copy-paste — always verify AI output against test cases." },
    { q:"Which is the BEST prompt to start the AI-Assisted Coding task of 'Reverse a Linked List in-place'?", options:["'Reverse linked list'","'Write me the code'","'Input: head of a singly linked list. Output: new head after reversing all next pointers in-place. Constraint: O(1) memory, no extra arrays. Handle NULL and single-node cases.'","'Use three pointers'"], ans:2, exp:"A great framing prompt includes: input, output, constraints, and edge cases in your own words — not just task name." },
    { q:"Capgemini's AI Coding Assessment measures 'AI Literacy' as:", options:["Your knowledge of Python","Understanding & interpreting the problem, then responding meaningfully to the AI","How fast you type","How many tokens you use"], ans:1, exp:"AI Literacy criterion: understanding the problem fully and framing your AI interactions meaningfully." },
    { q:"'Problem-Solving' criterion in the AI Coding Assessment means:", options:["Getting the exact answer","Brute-forcing the solution","Choosing the right algorithmic approach and guiding the AI step-by-step","Submitting fastest"], ans:2, exp:"Problem-Solving: selecting the correct approach (e.g., 3-pointer technique for linked list reversal) and systematically guiding the AI." },
    { q:"What is 'iterative prompting' in the AI Coding context?", options:["Running code multiple times","Refining and narrowing your prompt across multiple messages to fix issues","Using loops in code","Typing prompts faster"], ans:1, exp:"Iterative prompting: starting broad, then drilling into specifics across follow-up prompts as the AI's response is refined." },
    { q:"The Debugging Assessment (Stage 2B) specifically tests on:", options:["Web development bugs","UI/UX errors","Trees, Graphs, and 2D Dynamic Programming in C/C++/Java","Python runtime errors only"], ans:2, exp:"Official Capgemini syllabus: Debugging Assessment covers Trees, Graphs, and 2D DP in C, C++, or Java." },
    { q:"In the 4-step Debugging process, what happens in the 'Validate' step?", options:["Rewrite entire code","Submit","Check logic, test approach, and handle edge cases like null/empty inputs","Just compile the code"], ans:2, exp:"Validate: After fixing, check correctness — test edge cases like null input, single node, empty arrays, duplicates." },
    { q:"What should you prompt the AI when its generated code exceeds the time limit (TLE)?", options:["'Make it faster'","'The current O(N^2) brute-force approach causes TLE on N=10^5. Please optimize to an O(N log N) or O(N) approach using a Hash Map or Two Pointers.'","'Error'","'Retry'"], ans:1, exp:"Explicit algorithmic direction identifying the asymptotic bottleneck and suggesting the target data structure gets immediate correct results." },
    { q:"Under Capgemini's Lab 27 prompt rubric, why is verbatim copying of the problem statement penalized?", options:["Because the platform does not allow clipboard paste","Because the AI evaluates your ability to decompose and synthesize requirements in your own words, proving genuine comprehension","Because the prompt will exceed maximum token limits","Because LLMs cannot read long text"], ans:1, exp:"The evaluation framework specifically tests comprehension and articulation. Rephrasing the problem in your own terms demonstrates algorithmic understanding." },
    { q:"When the AI generates code that hallucinates a non-existent standard library method, what is the best follow-up prompt?", options:["'This does not work, write something else'","'Method X does not exist in standard Java/C++ libraries. Please replace it using standard collections/primitives and verify standard library compatibility.'","'Change programming language'","'Restart session'"], ans:1, exp:"Pointing out the exact hallucinated API and specifying the replacement constraint (standard collections/primitives) yields targeted corrections." },
    { q:"What is 'Few-Shot Prompting' and how does it help when generating competitive programming logic?", options:["Sending only few prompts per day","Providing 1 or 2 concrete examples of inputs and desired outputs with step-by-step traces before requesting the code","Writing short code snippets","Prompting without examples"], ans:1, exp:"Few-shot prompting provides concrete demonstration pairs of inputs and expected outputs, which grounds the model's inductive reasoning on complex edge cases." },
    { q:"How should you guide an AI to optimize a 2D DP solution from O(M × N) space to O(min(M, N)) auxiliary space?", options:["'Reduce memory'","'Since the recurrence relation dp[i][j] only depends on row i-1 and current row i, optimize space by using two 1D rolling arrays of size N.'","'Use bit manipulation'","'Remove the array entirely'"], ans:1, exp:"Explicitly stating the recurrence dependency structure (only needing the prior row) instructs the LLM to implement rolling array space optimization." },
    { q:"What should be included when pasting compiler errors back to the AI assistant?", options:["Only the word 'Compilation Error'","The exact compiler error message, the specific line number, and the corresponding code snippet","A screenshot of the screen","Nothing, just ask it to regenerate"], ans:1, exp:"Feeding the exact error message and line number allows the LLM to isolate the syntax or type mismatch without having to guess context." },
    { q:"When prompting the AI for a graph traversal algorithm (BFS/DFS), what critical edge case should you explicitly mandate?", options:["The graph having 1,000,000 edges","Handling disconnected graph components using an outer loop over all vertices, and detecting cycles via visited states","Using only while loops","Ignoring visited nodes"], ans:1, exp:"Graphs frequently feature multiple disconnected subgraphs or cycles. Explicitly requiring an outer loop over unvisited vertices prevents incomplete traversals." },
    { q:"What is 'Chain-of-Thought' prompting in coding tasks?", options:["Writing code with chained method calls","Instructing the model to write out the algorithmic logic, invariants, and step-by-step reasoning in plain English BEFORE generating the code","Running multiple chained LLMs","Writing multiple recursive functions"], ans:1, exp:"Chain-of-Thought (CoT) prompting prompts the AI to think aloud step-by-step, drastically reducing logic flaws and edge-case omissions in generated code." },
    { q:"How should you instruct the AI when writing code that handles 64-bit integer calculations?", options:["'Use big numbers'","'Ensure all intermediate product computations use 64-bit integers (`long long` in C++ / `long` in Java) to prevent 32-bit integer overflow before modulo.'","'Use floating point double'","'Ignore large inputs'"], ans:1, exp:"Intermediate products (e.g. `(a * b) % MOD`) can overflow a standard 32-bit signed int even if both operands are smaller than MOD. Explicit 64-bit casting is critical." },
    { q:"What is the safest way to prompt the AI to implement defensive programming against null inputs in Tree algorithms?", options:["'Check if root is NULL at the entry of the function and return 0 / NULL before accessing root->left or root->right.'","'Assume root is always non-null'","'Use try-catch blocks everywhere'","'Trees never have null pointers'"], ans:0, exp:"Explicitly specifying base-case guard clauses for NULL/empty trees prevents runtime segmentation faults and null pointer exceptions." },
    { q:"If the AI gives you a recursive solution that will hit a Recursion Depth / Stack Overflow error on N=10^5, how do you prompt it?", options:["'Make recursion faster'","'Recursion depth of N=10^5 exceeds call stack limits. Please rewrite the solution iteratively using an explicit Stack / Two Pointers.'","'Increase stack memory'","'Change return type'"], ans:1, exp:"Specifying the stack overflow constraint and instructing an iterative refactor using an explicit data structure resolves call stack exhaustion." }
  ],

  // ---- STAGE 4: COGNITIVE & ADEPT-15 SITUATIONAL ----
  situational: [
    { q:"You finish a task 2 hours early. What do you do?", options:["Leave for the day","Start learning or help teammates / ask for more work","Browse social media","Wait for the day to end"], ans:1, exp:"Capgemini values initiative and teamwork. Proactively adding value by helping others or upskilling demonstrates the right attitude." },
    { q:"A teammate submits code with a critical bug before a deadline. You notice it. What do you do?", options:["Say nothing — not your problem","Tell your manager only","Inform your teammate immediately and help fix it, then notify the manager if needed","Rewrite their entire module yourself"], ans:2, exp:"Collaborative problem-solving. Respectfully alert the teammate first, offer to help, then escalate if time requires." },
    { q:"You disagree with your tech lead's technical decision. What do you do?", options:["Ignore it and do your own thing","Raise your concern privately with data and reasoning, then accept the final decision","Complain to other team members","File a formal complaint"], ans:1, exp:"Professional disagreement: raise concerns with evidence in a respectful channel, then respect the hierarchy's decision." },
    { q:"You are assigned a task using a technology you've never used. What do you do?", options:["Refuse the task","Inform your manager immediately that you can't do it","Research independently, ask targeted questions when stuck, deliver within timeline","Do nothing and wait for training"], ans:2, exp:"Continuous learning is core to Capgemini's culture. Self-directed learning with smart escalation is the expected approach." },
    { q:"During a client presentation, your live demo crashes. You should:", options:["Panic and apologize repeatedly","Remain calm, explain what the demo shows conceptually, offer to share screenshots/recording later","Blame a teammate","Cancel the meeting"], ans:1, exp:"Professional composure under pressure. Pivot smoothly — clients appreciate calm problem-solving over panic." },
    { q:"Your project deadline is tomorrow and you realize you need 3 more days. What do you do?", options:["Submit incomplete work without telling anyone","Work all night without telling your manager","Proactively inform your manager TODAY with a revised timeline and mitigation plan","Ask a teammate to cover you without telling management"], ans:2, exp:"Early, transparent communication with a solution plan is critical. Surprises at the deadline are far worse than early escalation." },
    { q:"In the Motion Challenge cognitive game, what is the best strategy?", options:["Random clicking to see what moves","Planning 3-4 moves in advance to minimize total step count","Moving the largest obstacle first always","Restarting repeatedly"], ans:1, exp:"Motion Challenge penalizes excessive trial-and-error moves. Planning paths mentally before executing produces higher scores." },
    { q:"In the Grid Challenge (working memory game), how should you manage dual tasks?", options:["Ignore the symmetry question and only memorize dots","Use verbal rehearsal (e.g. repeating 'top-left, center') while evaluating symmetry","Guess all dots at the end","Click as fast as possible"], ans:1, exp:"Verbal chunking and mental rehearsal keeps spatial coordinates active in working memory during distraction tasks." },
    { q:"Under the ADEPT-15 behavioral framework, what does 'Consistency' measure?", options:["Answering in the same time per question","Maintaining coherent trait responses across re-phrased situational questions without contradiction","Always picking the first option","Selecting extreme answers"], ans:1, exp:"ADEPT-15 assesses authenticity by re-phrasing underlying workplace traits across multiple questions to detect random guessing or fake personas." },
    { q:"A client requests a feature that wasn't in the original scope. You should:", options:["Build it immediately without telling anyone","Refuse outright","Discuss with your team lead, assess impact, document scope change, then communicate timeline adjustment","Promise it verbally"], ans:2, exp:"Scope changes need structured impact assessment, team alignment, and formal change management." },
    { q:"A critical production bug occurs on a Friday evening right after release. What is your immediate course of action?", options:["Wait until Monday morning since work hours are over","Follow incident protocol: alert on-call lead, check error logs, prepare a hotfix or rollback, and verify resolution","Restart the production database without telling anyone","Delete the release branch"], ans:1, exp:"Production incidents require following incident response protocols: immediate escalation to on-call leads, root-cause log inspection, mitigation/rollback, and post-mortem analysis." },
    { q:"You notice a subtle security vulnerability in an internal tool that isn't part of your assigned deliverables. What should you do?", options:["Ignore it because it is outside your sprint commitment","Privately report the vulnerability to the tech lead or security team with reproduction steps","Exploit it to demonstrate it to peers","Post about it on public social media"], ans:1, exp:"Demonstrating proactive integrity and organizational stewardship: quietly report security issues through proper channels with reproducible evidence." },
    { q:"During a sprint code review, a senior peer leaves very critical feedback on your pull request. How should you react?", options:["Take it personally and reject their comments","View it objectively as a learning opportunity, discuss architectural improvements professionally, and implement constructive fixes","Complain to HR","Ignore the review and merge directly"], ans:1, exp:"Receptiveness to feedback is a core engineering competency. Separate your ego from your code, seek clarification respectfully, and adopt best practices." },
    { q:"In the Switch Challenge (Capgemini cognitive test), what is the optimal deduction tactic?", options:["Guessing based on visual patterns","Tracking the change in position of one unique symbol across the operators to determine the switch rule","Selecting options randomly to beat the countdown timer","Focusing only on color"], ans:1, exp:"In Switch Challenge, isolating a single symbol and tracking how each numbered operator alters its position allows you to systematically deduce the correct transformation sequence." },
    { q:"In the Digit Challenge (mental arithmetic cognitive game), what balance produces the highest score?", options:["Guessing every question instantly","Maintaining high speed while ensuring strict accuracy, skipping only excessively lengthy equations","Attempting only 2 questions perfectly","Using a physical calculator"], ans:1, exp:"Capgemini cognitive games evaluate both speed and accuracy. Reckless guessing drastically lowers efficiency ratings, while calculated speed with high accuracy maximizes percentile rank." },
    { q:"Under ADEPT-15, which trait reflects an employee's willingness to help peers without seeking personal credit?", options:["Ambition","Cooperation / Altruism","Assertiveness","Autonomy"], ans:1, exp:"Cooperation and Altruism evaluate a candidate's readiness to support team members, share knowledge, and prioritize collective team success over individual ego." },
    { q:"Under ADEPT-15, which behavior best demonstrates 'Emotional Composure'?", options:["Expressing frustration openly when deadlines compress","Remaining calm, measured, and solution-focused during unexpected escalations or setbacks","Avoiding all difficult conversations","Never speaking in meetings"], ans:1, exp:"Emotional Composure assesses resilience: keeping a level head under stressful project milestones and focusing energy on mitigation rather than panic." },
    { q:"You are dependent on an API from another team, but their engineer has not responded to messages for 2 days. What should you do?", options:["Stop working and wait indefinitely","Escalate to your lead with the timeline impact while working on mock data/stubs to prevent your own sprint blocker","Send 20 urgent emails to their manager","Abandon the feature"], ans:1, exp:"Unblocking yourself using mock interfaces while professionally informing leadership of the cross-team dependency minimizes project downtime." },
    { q:"A client asks for an unrealistic deadline that you know cannot be met without severe code degradation. What is the best approach?", options:["Agree to the date and ship untested, buggy code","Provide data-backed estimates, explain the trade-offs, and propose a phased MVP delivery schedule","Blame the development team","Refuse to communicate"], ans:1, exp:"Professional consulting involves managing expectations: offering a prioritized MVP (Minimum Viable Product) and demonstrating realistic effort-hour estimates." },
    { q:"What is the Capgemini value demonstrated when an employee takes ownership of an honest mistake in production?", options:["Boldness and Honesty","Modesty only","Fun","Freedom without accountability"], ans:0, exp:"Honesty (owning the mistake with transparency) combined with Boldness (stepping forward to address it decisively) directly embodies Capgemini's founding values." }
  ],

  // ---- STAGES 5 & 6: INTERVIEW & CORE VALUES ----
  interview: [
    { q:"What are Capgemini's 7 Core Values?", options:["Speed, Power, Profit, Quality, Tech, Global, Code","Honesty, Boldness, Trust, Freedom, Fun, Modesty, Team Spirit","Integrity, Discipline, Fast Delivery, Sales, AI, Cloud, Java","Respect, Punctuality, Leadership, Vision, Cost, Innovation, Design"], ans:1, exp:"Founded in 1967 by Serge Kampf, Capgemini's 7 Core Values are Honesty, Boldness, Trust, Freedom, Fun, Modesty, Team Spirit." },
    { q:"In the STAR framework, what does 'A' stand for?", options:["Answer","Action — the specific steps you personally took","Analysis","Agreement"], ans:1, exp:"STAR = Situation, Task, Action (your personal contribution & actions), Result (quantifiable outcome)." },
    { q:"When asked 'Why Capgemini?', which response is strongest?", options:["'I need a job immediately'","'Capgemini is a global leader in AI, digital transformation, and people-first culture where I can grow in Cloud and enterprise engineering'","'Because my friend works here'","'For high package'"], ans:1, exp:"Connecting your personal tech aspirations with Capgemini's industry leadership (AI, Cloud, Digital Transformation) shows genuine interest." },
    { q:"Why do we use JWT (JSON Web Tokens) with HttpOnly cookies?", options:["To make web pages load faster","To prevent Cross-Site Scripting (XSS) attacks from accessing auth tokens via JavaScript","Because it is required by HTML5","To compress images"], ans:1, exp:"HttpOnly cookies cannot be accessed via document.cookie by client-side JS, mitigating token theft via XSS." },
    { q:"When explaining project architecture, what is the best sequence?", options:["Show code line by line","Problem Statement → High-level architecture & DB choice → Key Challenges & Trade-offs → Quantifiable Impact/Result","Complain about team members","Only talk about UI"], ans:1, exp:"Senior interviewers look for structured systems thinking: Problem → Tech Stack Rationale → Challenges/Trade-offs → Results." },
    { q:"'Tell me about yourself' — the ideal structure in an interview is:", options:["List your hobbies first","Background → Technical skills → Key project highlight → Why this role aligns with your goals","Only mention academic marks","Start with your salary expectation"], ans:1, exp:"Elevator pitch structure: brief background, core tech skills, one strong project highlight, and tie it to why you want this specific role." },
    { q:"What does 'S' in SOLID stand for?", options:["Synchronization Principle","Single Responsibility Principle — each class has one reason to change","Speed Optimization","Static Declaration"], ans:1, exp:"S = Single Responsibility Principle: a class should have only ONE reason to change, meaning only one job/responsibility." },
    { q:"In system design interviews, what is 'horizontal scaling'?", options:["Making one server more powerful","Adding more servers to distribute load (scale out)","Increasing RAM in a single server","Vertical partitioning of databases"], ans:1, exp:"Horizontal scaling (scale-out): add more machines. Vertical scaling (scale-up): make one machine more powerful. Horizontal is preferred for fault tolerance." },
    { q:"Database indexing improves:", options:["Write performance at cost of storage","Read query performance, especially for large datasets","Only JOIN operations","Primary key uniqueness"], ans:1, exp:"Indexes (B-tree, Hash) dramatically speed up SELECT/WHERE lookups at the cost of extra storage and slower INSERTs/UPDATEs." },
    { q:"What is 'Dependency Injection' in OOP?", options:["Injecting bugs into code","Providing dependencies (objects a class needs) from outside rather than creating them inside","A runtime error","A database pattern"], ans:1, exp:"Dependency Injection: pass required dependencies (collaborators) into a class via constructor/method rather than having the class create them — improves testability and decoupling." },
    { q:"How would you answer 'Tell me about a time you failed'?", options:["Deny ever failing","STAR format: real failure, personal responsibility, concrete lessons, how you applied them subsequently","Blame teammates","Say it was the manager's fault"], ans:1, exp:"Interviewers want growth mindset. Use STAR: real failure, own it, specific lessons learned, and evidence you applied them in later work." },
    { q:"REST API vs GraphQL — GraphQL's key advantage is:", options:["Faster servers","Client requests only the exact fields it needs — no over-fetching or under-fetching","Better security","Simpler authentication"], ans:1, exp:"GraphQL lets clients specify exactly what data they need in one query, eliminating REST's over-fetching (too much data) and under-fetching (multiple requests)." },
    { q:"What is 'technical debt'?", options:["Money owed for software licenses","Shortcuts or suboptimal code written now that will require refactoring later — trades short-term speed for long-term maintenance cost","A type of database error","Server downtime cost"], ans:1, exp:"Technical debt is the implied cost of future rework caused by choosing an easy/fast solution now instead of a better approach that would take longer." },
    { q:"Capgemini's global headquarters is in:", options:["London, UK","Paris, France","New York, USA","Bangalore, India"], ans:1, exp:"Capgemini SE is headquartered in Paris, France. Founded 1967 by Serge Kampf. Listed on Euronext Paris (CAC 40 index)." },
    { q:"During HR negotiation, when asked 'What is your expected salary?', best response:", options:["Say the highest number possible","Research market rates, give a justified range based on the role, skills, and market data, while expressing flexibility","Refuse to answer","Quote your friend's package"] , ans:1, exp:"Come prepared with market research (Glassdoor, Ambitionbox). Give a reasoned range, express enthusiasm for the role, and show willingness to discuss the full package." },
    { q:"What does the Spade symbol in Capgemini's logo represent historically?", options:["Playing cards only","Serge Kampf chose the ace of spades representing highest value and strength in bridge/poker, and precision in engineering","A gardening tool","French royalty crest"], ans:1, exp:"In 1967, founder Serge Kampf selected the ace of spades because in card games (bridge) it is the highest card, signifying top-tier excellence and strength." },
    { q:"What does the CAP Theorem state for distributed data stores?", options:["Consistency, Availability, and Partition Tolerance cannot all three be guaranteed simultaneously in network partitions","Compute, Access, and Performance are equal","Cloud Always Protects data","Continuous API Polling is required"], ans:0, exp:"CAP theorem proves that in any distributed data system across an unreliable network, you can guarantee at most two of: Consistency, Availability, and Partition Tolerance (CP or AP)." },
    { q:"What is the Cache-Aside (Lazy Loading) caching pattern?", options:["The application writes to cache first and async writes to DB","The application queries cache; on a miss, reads from database, writes result into cache, and returns it to the client","Cache automatically polls the database every second","Database directly invalidates browser memory"], ans:1, exp:"Cache-Aside: app queries cache first. On cache miss, it reads from the DB, stores the result in cache for future reads, and returns data." },
    { q:"What is the Circuit Breaker pattern in microservices architecture?", options:["A physical switch on the server rack","A software design pattern that detects downstream service failures and immediately returns fallback responses without overloading failing dependencies","A Docker restart policy","A method to terminate deadlocks"], ans:1, exp:"Circuit Breaker (e.g. Resilience4j) wraps network calls to downstream services. If error rates exceed a threshold, it trips open, preventing cascading failures across the system." },
    { q:"When should you choose a NoSQL Document Store (like MongoDB) over a Relational SQL DB (like PostgreSQL)?", options:["When ACID multi-table transactions and strict schema guarantees are paramount","When dealing with rapidly evolving, hierarchical, unstructured/semi-structured JSON-like data with high horizontal write scale","When using foreign keys heavily","Only for small toy apps"], ans:1, exp:"Document stores excel when data is non-relational, schemas change frequently, and data models fit into nested JSON documents with horizontal sharding." },
    { q:"What is the difference between PUT and PATCH HTTP methods?", options:["PUT is for deletion; PATCH is for creation","PUT replaces the entire resource representation idempotently; PATCH applies partial modifications to the resource","PUT is unencrypted; PATCH is encrypted","They are identical"], ans:1, exp:"PUT replaces the entire entity with the provided payload (idempotent). PATCH applies partial field-level updates to an existing resource." },
    { q:"How should a candidate answer 'What is your greatest weakness?' in Capgemini HR interview?", options:["'I am a perfectionist and work too hard'","State a genuine, non-critical technical or soft skill weakness, along with the proactive steps you are actively taking to improve it","'I have no weaknesses'","'I am always late for work'"], ans:1, exp:"Interviewers test self-awareness and continuous improvement. Mention an authentic skill gap (e.g. public speaking or a specific framework) and show concrete actions you are taking." },
    { q:"At the end of an interview, what is the best question to ask the interviewer?", options:["'How many days of leave do I get?'","'What does success look like for a graduate engineer in their first 6 months on your team, and what tech stack initiatives is the team focusing on?'","'Did I pass the interview?'","'Nothing, I am ready to leave'"], ans:1, exp:"Asking about team goals, 6-month performance expectations, and technical roadmap shows enthusiasm, maturity, and forward-thinking professionalism." },
    { q:"How do you explain a gap in education or non-CS background during the technical round?", options:["Hide it and hope they don't notice","Acknowledge it transparently, highlight self-driven learning, certifications, hands-on projects, and how your unique perspective adds value","Blame college professors","Make up false work experience"], ans:1, exp:"Honesty and resilience impress interviewers. Connect your transition with self-discipline, projects built, and how problem-solving carries across domains." },
    { q:"In Capgemini enterprise architectures, what is the advantage of asynchronous messaging (Kafka / RabbitMQ)?", options:["Decouples microservices, absorbs traffic spikes (buffer), and provides eventual consistency without blocking client threads","Replaces all databases","Makes networks 100% immune to failures","Allows writing frontend code in Java"], ans:0, exp:"Message queues decouple producers and consumers, smooth out sudden traffic spikes via buffering, and enable event-driven architectures with high throughput." }
  ]
};

// Helper: pick N items from an array (shuffled)
function pick(arr, n) {
  if (!arr || arr.length === 0) return [];
  const shuffled = [...arr].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(n, arr.length));
}

// ==========================================
// ALL 75+ MOCK TESTS CONFIGURATION
// (10+ Tests in Every Stage + Grand Mocks)
// ==========================================

const MOCK_TESTS = [
  // ==========================================
  // STAGE 1: ENGLISH COMMUNICATION (10 TESTS)
  // ==========================================
  { id:"vb_1", title:"Verbal Test 1 — Grammar & Error Spotting", category:"Stage 1 English", bank:"verbal", icon:"📝", difficulty:"easy", questions:10, duration:12 , isPremium:false },
  { id:"vb_2", title:"Verbal Test 2 — Reading Comprehension", category:"Stage 1 English", bank:"verbal", icon:"📖", difficulty:"medium", questions:10, duration:12, isPremium:false },
  { id:"vb_3", title:"Verbal Test 3 — Para Jumbles & Ordering", category:"Stage 1 English", bank:"verbal", icon:"✏️", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"vb_4", title:"Verbal Test 4 — Active & Passive Voice", category:"Stage 1 English", bank:"verbal", icon:"🗣️", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"vb_5", title:"Verbal Test 5 — Vocabulary & Synonyms", category:"Stage 1 English", bank:"verbal", icon:"📚", difficulty:"easy", questions:10, duration:12, isPremium:true },
  { id:"vb_6", title:"Verbal Test 6 — Sentence Improvement", category:"Stage 1 English", bank:"verbal", icon:"🔍", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"vb_7", title:"Verbal Test 7 — Idioms & Phrases", category:"Stage 1 English", bank:"verbal", icon:"💡", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"vb_8", title:"Verbal Test 8 — Subject-Verb Agreement", category:"Stage 1 English", bank:"verbal", icon:"🎯", difficulty:"easy", questions:10, duration:12, isPremium:true },
  { id:"vb_9", title:"Verbal Test 9 — Spoken AI Fluency Replica", category:"Stage 1 English", bank:"verbal", icon:"🎙️", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"vb_10", title:"Verbal Test 10 — Stage 1 Grand Assessment", category:"Stage 1 English", bank:"verbal", icon:"🏆", difficulty:"hard", questions:15, duration:18, isPremium:true },

  // ==========================================
  // STAGE 2A: TECHNICAL ASSESSMENT (16 TESTS)
  // ==========================================
  { id:"ai_1", title:"AI Literacy Test 1 — GenAI & RAG Basics", category:"Stage 2A Tech", bank:"ai_literacy", icon:"🤖", difficulty:"medium", questions:12, duration:15, isPremium:false },
  { id:"ai_2", title:"AI Literacy Test 2 — LLMs & Prompting", category:"Stage 2A Tech", bank:"ai_literacy", icon:"🧠", difficulty:"medium", questions:12, duration:15, isPremium:false },
  { id:"ai_3", title:"AI Literacy Test 3 — Responsible AI & Safety", category:"Stage 2A Tech", bank:"ai_literacy", icon:"🛡️", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"ps_1", title:"Pseudocode Test 1 — Bitwise & Logic", category:"Stage 2A Tech", bank:"pseudocode", icon:"⚙️", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"ps_2", title:"Pseudocode Test 2 — Recursion & Scope", category:"Stage 2A Tech", bank:"pseudocode", icon:"🔄", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"ps_3", title:"Pseudocode Test 3 — Control Flow & Loops", category:"Stage 2A Tech", bank:"pseudocode", icon:"🧮", difficulty:"medium", questions:10, duration:15, isPremium:true },
  { id:"dsa_1", title:"DSA Test 1 — Linear Structures", category:"Stage 2A Tech", bank:"dsa", icon:"📊", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"dsa_2", title:"DSA Test 2 — Trees & Sorting", category:"Stage 2A Tech", bank:"dsa", icon:"🌳", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"dsa_3", title:"DSA Test 3 — Algorithms & Big O", category:"Stage 2A Tech", bank:"dsa", icon:"⚡", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"db_1", title:"DBMS Test 1 — SQL & Normalization", category:"Stage 2A Tech", bank:"dbms", icon:"🗄️", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"db_2", title:"DBMS Test 2 — Joins & ACID", category:"Stage 2A Tech", bank:"dbms", icon:"🔗", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"oop_1", title:"OOPs Test 1 — 4 Pillars", category:"Stage 2A Tech", bank:"oops", icon:"🧩", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"os_1", title:"OS Test 1 — CPU & Deadlock", category:"Stage 2A Tech", bank:"os", icon:"💻", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"cn_1", title:"Networks Test 1 — OSI & TCP/IP", category:"Stage 2A Tech", bank:"networks", icon:"🌐", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"dv_1", title:"DevOps Test 1 — Cloud & REST", category:"Stage 2A Tech", bank:"devops", icon:"☁️", difficulty:"easy", questions:10, duration:12, isPremium:true },
  { id:"apt_1", title:"Aptitude Test 1 — Quant Fundamentals", category:"Stage 2A Tech", bank:"aptitude", icon:"📐", difficulty:"medium", questions:10, duration:15, isPremium:true },

  // ==========================================
  // STAGE 2B: DEBUGGING ASSESSMENT (10 HANDS-ON TESTS — NO MCQS)
  // ==========================================
  { id:"dbg_1", title:"Debugging Challenge 1 — 01. Knapsack-C (Aon Replica)", category:"Stage 2B Debugging", icon:"🐛", difficulty:"hard", questions:1, duration:20, isPremium:false },
  { id:"dbg_2", title:"Debugging Challenge 2 — 02. Binary Tree Max Path Sum", category:"Stage 2B Debugging", icon:"🌳", difficulty:"hard", questions:1, duration:20, isPremium:false },
  { id:"dbg_3", title:"Debugging Challenge 3 — 03. Graph Cycle in DAG (Java)", category:"Stage 2B Debugging", icon:"🕸️", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_4", title:"Debugging Challenge 4 — 04. 2D DP Grid Obstacles (C)", category:"Stage 2B Debugging", icon:"🧮", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_5", title:"Debugging Challenge 5 — 05. List Cycle Traps (C++)", category:"Stage 2B Debugging", icon:"🔗", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_6", title:"Debugging Challenge 6 — 06. Binary Search Overflow", category:"Stage 2B Debugging", icon:"🔍", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_7", title:"Debugging Challenge 7 — 07. String Palindrome & '\0'", category:"Stage 2B Debugging", icon:"🔤", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_8", title:"Debugging Challenge 8 — 08. Pass-by-Reference & Swaps", category:"Stage 2B Debugging", icon:"🧩", difficulty:"medium", questions:1, duration:20, isPremium:true },
  { id:"dbg_9", title:"Debugging Challenge 9 — 09. Double Free & Dangling Pointer", category:"Stage 2B Debugging", icon:"💾", difficulty:"hard", questions:1, duration:20, isPremium:true },
  { id:"dbg_10", title:"Debugging Challenge 10 — 10. Longest Increasing Subsequence DP", category:"Stage 2B Debugging", icon:"🎖️", difficulty:"hard", questions:1, duration:20, isPremium:true },

  // ==========================================
  // STAGE 3: AI-ASSISTED CODING (10 HANDS-ON CHALLENGES — NO MCQS)
  // ==========================================
  { id:"aic_1", title:"AI Coding Challenge 1 — 01. LCM of Two Trees (Official Capgemini)", category:"Stage 3 AI Coding", icon:"💡", difficulty:"medium", questions:1, duration:45, isPremium:false },
  { id:"aic_2", title:"AI Coding Challenge 2 — 02. In-Place Reversal of Linked List", category:"Stage 3 AI Coding", icon:"🔄", difficulty:"medium", questions:1, duration:45, isPremium:false },
  { id:"aic_3", title:"AI Coding Challenge 3 — 03. Longest Substring Without Repeating", category:"Stage 3 AI Coding", icon:"🛡️", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_4", title:"AI Coding Challenge 4 — 04. Lowest Common Ancestor (LCA)", category:"Stage 3 AI Coding", icon:"⚡", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_5", title:"AI Coding Challenge 5 — 05. Course Schedule / DAG Cycle", category:"Stage 3 AI Coding", icon:"🌳", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_6", title:"AI Coding Challenge 6 — 06. Merge K Sorted Linked Lists", category:"Stage 3 AI Coding", icon:"🎯", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_7", title:"AI Coding Challenge 7 — 07. Subarray Sum Equals K", category:"Stage 3 AI Coding", icon:"🧠", difficulty:"medium", questions:1, duration:45, isPremium:true },
  { id:"aic_8", title:"AI Coding Challenge 8 — 08. Coin Change (Minimum Coins DP)", category:"Stage 3 AI Coding", icon:"📐", difficulty:"hard", questions:1, duration:45, isPremium:true },
  { id:"aic_9", title:"AI Coding Challenge 9 — 09. Valid Parentheses with Wildcards", category:"Stage 3 AI Coding", icon:"📋", difficulty:"medium", questions:1, duration:45, isPremium:true },
  { id:"aic_10", title:"AI Coding Challenge 10 — 10. Word Search on 2D Matrix", category:"Stage 3 AI Coding", icon:"🌟", difficulty:"hard", questions:1, duration:45, isPremium:true },

  // ==========================================
  // STAGE 4: COGNITIVE & SITUATIONAL (10 TESTS)
  // ==========================================
  { id:"sit_1", title:"Cognitive Test 1 — Motion Challenge Logic", category:"Stage 4 Cognitive", bank:"situational", icon:"🎮", difficulty:"medium", questions:10, duration:15, isPremium:false },
  { id:"sit_2", title:"Cognitive Test 2 — Grid Working Memory", category:"Stage 4 Cognitive", bank:"situational", icon:"🧩", difficulty:"medium", questions:10, duration:15, isPremium:false },
  { id:"sit_3", title:"Cognitive Test 3 — Inductive Pattern Rules", category:"Stage 4 Cognitive", bank:"situational", icon:"🔍", difficulty:"hard", questions:10, duration:15, isPremium:true },
  { id:"sit_4", title:"Cognitive Test 4 — ADEPT-15 Drive & Ambition", category:"Stage 4 Cognitive", bank:"situational", icon:"🚀", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"sit_5", title:"Cognitive Test 5 — Teamwork & Conflict", category:"Stage 4 Cognitive", bank:"situational", icon:"🤝", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"sit_6", title:"Cognitive Test 6 — Client Delivery Scenarios", category:"Stage 4 Cognitive", bank:"situational", icon:"💼", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"sit_7", title:"Cognitive Test 7 — Adaptability & Growth", category:"Stage 4 Cognitive", bank:"situational", icon:"🌱", difficulty:"easy", questions:10, duration:12, isPremium:true },
  { id:"sit_8", title:"Cognitive Test 8 — Ethical Decision Making", category:"Stage 4 Cognitive", bank:"situational", icon:"⚖️", difficulty:"medium", questions:10, duration:12, isPremium:true },
  { id:"sit_9", title:"Cognitive Test 9 — High-Pressure Scenarios", category:"Stage 4 Cognitive", bank:"situational", icon:"⏱️", difficulty:"hard", questions:10, duration:12, isPremium:true },
  { id:"sit_10", title:"Cognitive Test 10 — Stage 4 Grand Mock", category:"Stage 4 Cognitive", bank:"situational", icon:"🎭", difficulty:"hard", questions:10, duration:15, isPremium:true },

  // ==========================================
  // STAGES 5 & 6: INTERVIEW & CORE VALUES (10 TESTS)
  // ==========================================
  { id:"int_1", title:"Interview Test 1 — Capgemini 7 Core Values", category:"Stages 5-6 Interview", bank:"interview", icon:"🏛️", difficulty:"medium", questions:5, duration:8, isPremium:false },
  { id:"int_2", title:"Interview Test 2 — STAR Method Scenarios", category:"Stages 5-6 Interview", bank:"interview", icon:"⭐", difficulty:"medium", questions:5, duration:8, isPremium:false },
  { id:"int_3", title:"Interview Test 3 — Architecture & DB Defense", category:"Stages 5-6 Interview", bank:"interview", icon:"🛡️", difficulty:"hard", questions:5, duration:8, isPremium:true },
  { id:"int_4", title:"Interview Test 4 — Security & Auth Mechanics", category:"Stages 5-6 Interview", bank:"interview", icon:"🔐", difficulty:"hard", questions:5, duration:8, isPremium:true },
  { id:"int_5", title:"Interview Test 5 — Project Storytelling", category:"Stages 5-6 Interview", bank:"interview", icon:"💬", difficulty:"medium", questions:5, duration:8, isPremium:true },
  { id:"int_6", title:"Interview Test 6 — Cultural Fit & Integrity", category:"Stages 5-6 Interview", bank:"interview", icon:"🤝", difficulty:"medium", questions:5, duration:8, isPremium:true },
  { id:"int_7", title:"Interview Test 7 — DSA Complexity Defense", category:"Stages 5-6 Interview", bank:"interview", icon:"⚡", difficulty:"hard", questions:5, duration:8, isPremium:true },
  { id:"int_8", title:"Interview Test 8 — OOPs Real-World Systems", category:"Stages 5-6 Interview", bank:"interview", icon:"🧩", difficulty:"medium", questions:5, duration:8, isPremium:true },
  { id:"int_9", title:"Interview Test 9 — Behavioral Conflict Handling", category:"Stages 5-6 Interview", bank:"interview", icon:"🎭", difficulty:"medium", questions:5, duration:8, isPremium:true },
  { id:"int_10", title:"Interview Test 10 — Grand Interview Defense Mock", category:"Stages 5-6 Interview", bank:"interview", icon:"🎓", difficulty:"hard", questions:8, duration:12, isPremium:true },

  // ==========================================
  
  // ==========================================
  // STAGE-WISE GRAND MOCKS
  // ==========================================
  { id:"gm_s1", title:"Stage 1 Grand Mock — English Communication", category:"Stage-Wise Grand Mocks", bank:"verbal", icon:"🎙️", difficulty:"medium", questions:25, duration:25, isPremium:true },
  { id:"gm_s2a", title:"Stage 2A Grand Mock — Technical Assessment", category:"Stage-Wise Grand Mocks", icon:"💻", difficulty:"hard", questions:30, duration:35, isPremium:true, spec:[{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"os",n:4},{bank:"networks",n:3}] },
  { id:"gm_s2b", title:"Stage 2B Grand Mock — Debugging Marathon", category:"Stage-Wise Grand Mocks", bank:"debugging", icon:"🐛", difficulty:"hard", questions:15, duration:25, isPremium:true },
  { id:"gm_s3", title:"Stage 3 Grand Mock — AI-Assisted Coding Assessment", category:"Stage-Wise Grand Mocks", bank:"ai_coding", icon:"🤖", difficulty:"hard", questions:15, duration:20, isPremium:true },
  { id:"gm_s4", title:"Stage 4 Grand Mock — Cognitive Games & ADEPT-15", category:"Stage-Wise Grand Mocks", bank:"situational", icon:"🧠", difficulty:"medium", questions:20, duration:25, isPremium:true },
  { id:"gm_s56", title:"Stages 5 & 6 Grand Mock — Tech Defense & HR Values", category:"Stage-Wise Grand Mocks", bank:"interview", icon:"🏆", difficulty:"hard", questions:15, duration:20, isPremium:true },

  // GRAND MOCK MARATHON SUITE (10 FULL TESTS)
  { id:"full_1", title:"Full Mock Test 1 — Main Assessment Drive (Stages 2A to 6)", category:"Grand Mocks", icon:"🎯", difficulty:"medium", questions:42, duration:45, isPremium:true, spec:[{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"os",n:4},{bank:"debugging",n:5},{bank:"ai_coding",n:5},{bank:"situational",n:5}] },
  { id:"full_2", title:"Full Mock Test 2 — All Stages Complete Marathon (Stage 1 Included)", category:"Grand Mocks", icon:"🚀", difficulty:"hard", questions:50, duration:55, isPremium:true, spec:[{bank:"verbal",n:8},{bank:"ai_literacy",n:5},{bank:"pseudocode",n:5},{bank:"dsa",n:5},{bank:"dbms",n:4},{bank:"oops",n:4},{bank:"debugging",n:5},{bank:"ai_coding",n:5},{bank:"situational",n:5},{bank:"interview",n:4}] },
  { id:"full_3", title:"Full Mock Test 3 — Tech + Verbal Combo", category:"Grand Mocks", icon:"📋", difficulty:"medium", questions:35, duration:45, isPremium:true, spec:[{bank:"verbal",n:10},{bank:"ai_literacy",n:5},{bank:"dsa",n:6},{bank:"dbms",n:5},{bank:"aptitude",n:9}] },
  { id:"full_4", title:"Full Mock Test 4 — Debugging + AI Coding Focus", category:"Grand Mocks", icon:"🔬", difficulty:"hard", questions:30, duration:40, isPremium:true, spec:[{bank:"debugging",n:10},{bank:"ai_coding",n:10},{bank:"pseudocode",n:5},{bank:"ai_literacy",n:5}] },
  { id:"full_5", title:"Full Mock Test 5 — Situational + Technical", category:"Grand Mocks", icon:"🎭", difficulty:"medium", questions:30, duration:35, isPremium:true, spec:[{bank:"situational",n:10},{bank:"ai_literacy",n:6},{bank:"dsa",n:7},{bank:"dbms",n:7}] },
  { id:"full_6", title:"Full Mock Test 6 — 50Q Stage 2 Endurance", category:"Grand Mocks", icon:"🏋️", difficulty:"hard", questions:40, duration:50, isPremium:true, spec:[{bank:"ai_literacy",n:8},{bank:"pseudocode",n:6},{bank:"dsa",n:8},{bank:"dbms",n:6},{bank:"oops",n:6},{bank:"networks",n:6}] },
  { id:"combo_1", title:"⚡ Speed Challenge — 20Q in 20 Mins", category:"Grand Mocks", icon:"⏱️", difficulty:"hard", questions:20, duration:20, isPremium:true, spec:[{bank:"ai_literacy",n:4},{bank:"dsa",n:4},{bank:"dbms",n:4},{bank:"aptitude",n:4},{bank:"verbal",n:4}] },
  { id:"combo_2", title:"Core CS Marathon — 30 Questions", category:"Grand Mocks", icon:"🏃", difficulty:"hard", questions:30, duration:35, isPremium:true, spec:[{bank:"os",n:8},{bank:"networks",n:8},{bank:"dbms",n:7},{bank:"oops",n:7}] },
  { id:"combo_3", title:"AI + DevOps Future-Ready Test", category:"Grand Mocks", icon:"🌟", difficulty:"medium", questions:20, duration:25, isPremium:true, spec:[{bank:"ai_literacy",n:10},{bank:"devops",n:5},{bank:"networks",n:5}] },
  { id:"combo_4", title:"Beginner Warm-Up Test", category:"Grand Mocks", icon:"🌱", difficulty:"easy", questions:15, duration:20, isPremium:true, spec:[{bank:"dsa",n:5},{bank:"oops",n:5},{bank:"aptitude",n:5}] }
];

// Dynamic Question Generator: fresh shuffle every single time
function getFreshQuestions(test) {
  if (!test) return [];

  // Multi-bank combo test
  if (test.spec && Array.isArray(test.spec)) {
    let pool = [];
    test.spec.forEach(item => {
      const bankItems = QUESTION_BANK[item.bank] || [];
      pool.push(...pick(bankItems, item.n));
    });
    // Shuffle the assembled multi-bank set
    return pool.sort(() => Math.random() - 0.5);
  }

  // Single bank test
  if (test.bank && QUESTION_BANK[test.bank]) {
    return pick(QUESTION_BANK[test.bank], test.questions || 10);
  }

  // Fallback if legacy questionKeys exist
  if (test.questionKeys && Array.isArray(test.questionKeys)) {
    return pick(test.questionKeys, test.questions || 10);
  }

  return [];
}


// ==========================================
// PRO PASS & PAYMENT MODULE SYSTEM
// ==========================================
const ADMIN_NOTIFICATION_EMAIL = "rishavofficials1727@gmail.com";
let currentPayablePrice = 51;
let flashTimerInterval = null;
let socialProofInterval = null;

// ==========================================
// USER ACCOUNTS & AUTHENTICATION ENGINE
// ==========================================

function getStoredUsers() {
  try {
    return JSON.parse(localStorage.getItem('capprep_users') || '[]');
  } catch(e) {
    return [];
  }
}

function saveStoredUsers(users) {
  try {
    localStorage.setItem('capprep_users', JSON.stringify(users));
  } catch(e) {}
}

function getCurrentUser() {
  try {
    return JSON.parse(localStorage.getItem('capprep_current_user') || 'null');
  } catch(e) {
    return null;
  }
}

function setCurrentUser(user) {
  if (user) {
    try {
      localStorage.setItem('capprep_current_user', JSON.stringify(user));
      if (user.isPro) {
        localStorage.setItem('capprep_pro_unlocked', 'true');
      } else {
        localStorage.removeItem('capprep_pro_unlocked');
      }
    } catch(e) {}
  } else {
    try {
      localStorage.removeItem('capprep_current_user');
      localStorage.removeItem('capprep_pro_unlocked');
    } catch(e) {}
  }
  updateProUI();
}

const OFFICIAL_TEST_ACCOUNTS = [
  {
    id: "test1@capprep.com",
    name: "CapPrep Tester Alpha",
    password: "pass_test1_2027",
    role: "Full Pro Access (Tester Alpha)",
    isTestAccount: true
  },
  {
    id: "test2@capprep.com",
    name: "CapPrep Tester Beta",
    password: "pass_test2_2027",
    role: "Full Pro Access (Tester Beta)",
    isTestAccount: true
  },
  {
    id: "test3@capprep.com",
    name: "CapPrep Tester Gamma",
    password: "pass_test3_2027",
    role: "Full Pro Access (Tester Gamma)",
    isTestAccount: true
  }
];

// Global Verified VIP Students (Granted by Master Admin - Accessible across all devices)
const GLOBAL_VERIFIED_VIP_ACCOUNTS = [
  {
    name: "Rajneesh Chaubey",
    email: "rajneeshchaubey360@gmail.com",
    password: "HpbFpxwD",
    phone: "+91 98000 00000",
    role: "Verified Pro Student (VIP Pass)",
    isPro: true
  },
  {
    name: "Enrolled Pro Student",
    email: "pinea8888@gmail.com",
    password: "cap2027",
    phone: "+91 98000 00000",
    role: "Verified Paid Candidate (CapPrep Pro)",
    isPro: true
  }
];

function validateActiveSession() {
  const cur = getCurrentUser();
  if (!cur || !cur.isTestAccount) return true;

  try {
    const activeSessions = JSON.parse(localStorage.getItem('capprep_active_sessions') || '{}');
    const expectedToken = activeSessions[cur.email.toLowerCase()];
    const myToken = (typeof sessionStorage !== 'undefined' ? sessionStorage.getItem('capprep_session_token') : null) || cur.sessionToken;

    if (expectedToken && myToken && expectedToken !== myToken) {
      userSignOut();
      alert(`⚠️ CONCURRENT LOGIN BLOCKED!\n\nThis Test ID (${cur.email}) was just logged into from another browser or device.\n\nOnly 1 active session is allowed per Test ID.\nYour session on this device has been automatically signed out.`);
      showSecurityToast("🔒 Session expired: Test ID active on another device.");
      return false;
    }
  } catch(e) {}
  return true;
}

// ==========================================
// MASTER ACCESS SWITCH:
// Set to true = 100% UNLOCKED FOR EVERYONE (FREE OPEN ACCESS)
// Set to false = RESTORE PRO PAYWALL (PAID / LOGIN REQUIRED)
// ==========================================
const GLOBAL_FREE_ACCESS_MODE = true;

function isProUser() {
  if (GLOBAL_FREE_ACCESS_MODE) return true;
  if (!validateActiveSession()) return false;
  const cur = getCurrentUser();
  if (!cur) return false;  // Must be logged in — no user = no Pro
  if (cur.isPro) return true;
  // Double-check the localStorage flag only when user IS logged in
  return localStorage.getItem('capprep_pro_unlocked') === 'true';
}

function openSignInModal() {
  closeLockedTestModal();
  closePaymentModal();
  const modal = document.getElementById('signin-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    const err = document.getElementById('signin-error-msg');
    if (err) err.style.display = 'none';
    setTimeout(() => document.getElementById('signin-email-input')?.focus(), 100);
  }
}

function closeSignInModal() {
  const modal = document.getElementById('signin-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function handleNavAuthClick() {
  const cur = getCurrentUser();
  if (cur) {
    if (confirm(`Logged in as ${cur.name} (${cur.email}).\nDo you want to sign out?`)) {
      userSignOut();
    }
  } else {
    openSignInModal();
  }
}

function handleNavProClick() {
  openPaymentModal();
}

function userSignOut() {
  setCurrentUser(null);
  try {
    localStorage.removeItem('capprep_pro_unlocked');
    localStorage.removeItem('capprep_txn_id');
    if (typeof sessionStorage !== 'undefined') {
      sessionStorage.removeItem('capprep_session_token');
    }
  } catch(e) {}
  updateProUI();
  showSecurityToast("👋 Signed out successfully. Reverted to Free Tier (2 Free Trials per Stage).");
}

async function processUserSignIn() {
  const email = (document.getElementById('signin-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('signin-password-input')?.value || '').trim();
  const errorEl = document.getElementById('signin-error-msg');

  if (!email || !password) {
    if (errorEl) {
      errorEl.style.display = 'block';
      errorEl.textContent = '⚠️ Please enter both email and password.';
    }
    return;
  }

  // 1. Check Official Test Accounts (Single Active Session Protected)
  const testAcc = OFFICIAL_TEST_ACCOUNTS.find(t => t.id.toLowerCase() === email && t.password === password);
  if (testAcc) {
    const sessionToken = "SESS_" + Date.now() + "_" + Math.floor(100000 + Math.random() * 900000);
    try {
      const activeSessions = JSON.parse(localStorage.getItem('capprep_active_sessions') || '{}');
      activeSessions[testAcc.id.toLowerCase()] = sessionToken;
      localStorage.setItem('capprep_active_sessions', JSON.stringify(activeSessions));
      if (typeof sessionStorage !== 'undefined') {
        sessionStorage.setItem('capprep_session_token', sessionToken);
      }
    } catch(e) {}

    const testUser = {
      name: testAcc.name,
      email: testAcc.id,
      password: testAcc.password,
      phone: "+91 98000 00000",
      college: testAcc.role,
      isPro: true,
      isTestAccount: true,
      sessionToken: sessionToken,
      joinedAt: new Date().toLocaleString()
    };
    setCurrentUser(testUser);
    closeSignInModal();
    showSecurityToast(`🧪 Welcome ${testUser.name}! Full Pro Access Active.`);
    alert(`🎉 WELCOME ${testUser.name.toUpperCase()}!\n\nFull Pro Access is ACTIVE for this session.\n\n🛡️ NOTE: Single Active Session is strictly enforced. If this Test ID logs in on another device/browser, your current session will be automatically disconnected.`);
    return;
  }

  // 1b. Check Global Verified VIP Accounts (Cross-Device Admin Grants)
  const vipAccountMatch = GLOBAL_VERIFIED_VIP_ACCOUNTS.find(v => 
    v.email.toLowerCase() === email && (v.password === password || password === 'cap2027')
  );
  if (vipAccountMatch) {
    const vipUser = {
      name: vipAccountMatch.name,
      email: vipAccountMatch.email,
      password: vipAccountMatch.password,
      phone: vipAccountMatch.phone || "+91 98000 00000",
      college: vipAccountMatch.role || "Capgemini Candidate (VIP Pass)",
      isPro: true,
      isVip: true,
      joinedAt: new Date().toLocaleString()
    };
    const storedUsers = getStoredUsers();
    const existingIdx = storedUsers.findIndex(u => u.email && u.email.toLowerCase() === email);
    if (existingIdx >= 0) {
      storedUsers[existingIdx] = Object.assign({}, storedUsers[existingIdx], vipUser);
    } else {
      storedUsers.unshift(vipUser);
    }
    saveStoredUsers(storedUsers);
    setCurrentUser(vipUser);
    closeSignInModal();
    showSecurityToast(`⭐ Welcome ${vipUser.name}! CapPrep Pro Pass Active.`);
    alert(`🎉 WELCOME ${vipUser.name.toUpperCase()}!\n\nYour CapPrep Pro Lifetime Pass is ACTIVE.\nAll 76+ Mock Tests, Lab 27 AI Simulator, and Study Notes are unlocked!`);
    return;
  }

  // 1c. Check Live Supabase Cloud Database (Centralized Across All Devices)
  if (typeof dbAuthenticate === 'function') {
    try {
      const cloudUser = await dbAuthenticate(email, password);
      if (cloudUser) {
        setCurrentUser(cloudUser);
        closeSignInModal();
        showSecurityToast(`⭐ Welcome ${cloudUser.name}! CapPrep Pro Pass Active.`);
        alert(`🎉 WELCOME ${cloudUser.name.toUpperCase()}!\n\nYour CapPrep Pro Lifetime Pass is ACTIVE via Live Cloud Database.\nAll 76+ Mock Tests, Simulators, and Study Notes are unlocked!`);
        return;
      }
    } catch(err) {
      console.warn("Supabase auth check fallback:", err);
    }
  }

  // 2. Check Master Admin Credentials
  if (MASTER_ADMIN_EMAILS.includes(email) && (password === '1727' || password === 'cap2027' || password === 'rishav')) {
    const adminUser = {
      name: "Rishav Kumar Gupta",
      email: email,
      password: password,
      phone: "+91 98000 00000",
      college: "Master Administrator",
      isPro: true,
      isAdmin: true,
      joinedAt: new Date().toLocaleString()
    };
    setCurrentUser(adminUser);
    closeSignInModal();
    showSecurityToast("👑 Master Administrator Signed In Successfully!");
    alert("👑 WELCOME MASTER ADMIN RISHAV!\n\nYou are signed in with Full Administrator Privileges.\nAll 76+ Mock Tests, Simulators, and Admin Control Center are active.");
    return;
  }


  // 3. Check Stored User Database
  const users = getStoredUsers();
  const user = users.find(u => u.email && u.email.toLowerCase() === email && u.password === password);

  if (user) {
    setCurrentUser(user);
    closeSignInModal();
    if (user.isPro) {
      showSecurityToast(`⭐ Welcome back, ${user.name}! Your CapPrep Pro Pass is active.`);
      alert(`🎉 WELCOME BACK ${user.name.toUpperCase()}!\n\nYour CapPrep Pro Lifetime Pass is ACTIVE.\nAll 76+ Mock Tests, Simulators, and Study Notes are unlocked!`);
    } else {
      showSecurityToast(`👤 Logged in as ${user.name} (Free Tier).`);
    }
    return;
  }

  // 4. Check Orders Ledger (capprep_orders)
  try {
    const orders = JSON.parse(localStorage.getItem('capprep_orders') || '[]');
    const orderMatch = orders.find(o => o.email && o.email.toLowerCase() === email);
    if (orderMatch && orderMatch.password && password === orderMatch.password) {
      const ordUser = {
        name: orderMatch.name || "Enrolled Student",
        email: email,
        password: password,
        phone: orderMatch.phone || "+91 98000 00000",
        college: orderMatch.college || "Capgemini Candidate",
        isPro: true,
        joinedAt: orderMatch.timestamp || new Date().toLocaleString()
      };
      users.unshift(ordUser);
      saveStoredUsers(users);
      setCurrentUser(ordUser);
      closeSignInModal();
      showSecurityToast(`⭐ Welcome ${ordUser.name}! Verified Pro Pass Active.`);
      alert(`🎉 WELCOME ${ordUser.name.toUpperCase()}!\n\nYour CapPrep Pro Pass is ACTIVE.\nAll 76+ Mock Tests & Simulators are unlocked!`);
      return;
    }
  } catch(e) {}

  // 5. Check VIP Whitelist
  try {
    const vipList = JSON.parse(localStorage.getItem('capprep_vip_whitelist') || '[]');
    const vipMatch = vipList.find(v => v.id && v.id.toLowerCase() === email);
    if (vipMatch && password && password.length >= 4 && (password === vipMatch.password || password === 'cap2027')) {
      const vipUser = {
        name: vipMatch.name || "VIP Candidate",
        email: email,
        password: password,
        phone: vipMatch.phone || "+91 98000 00000",
        college: vipMatch.reason || "VIP Candidate",
        isPro: true,
        joinedAt: new Date().toLocaleString()
      };
      users.unshift(vipUser);
      saveStoredUsers(users);
      setCurrentUser(vipUser);
      closeSignInModal();
      showSecurityToast(`👑 Welcome VIP Candidate ${vipUser.name}! Pro Access Unlocked.`);
      alert(`🎉 WELCOME ${vipUser.name.toUpperCase()}!\n\nYour VIP CapPrep Pro Lifetime Pass has been ACTIVATED.\nAll 76+ Mock Tests & Simulators are unlocked!`);
      return;
    }
  } catch(e) {}

  // Failed Authentication
  if (errorEl) {
    errorEl.style.display = 'block';
    errorEl.innerHTML = `❌ Invalid credentials for <strong>${escHTML(email)}</strong>.<br><br>• Forgot password? <a href="javascript:void(0)" onclick="openForgotPasswordModal()" style="color:#38bdf8; font-weight:700;">Recover Password →</a><br>• Haven't enrolled yet? <a href="javascript:void(0)" onclick="closeSignInModal(); openPaymentModal();" style="color:var(--accent); font-weight:700;">Enroll for ₹51 →</a>`;
  }
}

let currentLockedTest = null;

function openLockedTestModal(test) {
  currentLockedTest = test;
  const modal = document.getElementById('locked-test-modal');
  if (!modal) {
    openPaymentModal(test);
    return;
  }
  const titleEl = document.getElementById('locked-modal-test-title');
  const metaEl = document.getElementById('locked-modal-test-meta');
  const freeBtn = document.getElementById('locked-modal-free-btn');

  if (titleEl && test) titleEl.textContent = `🔒 ${test.title} is Locked`;
  if (metaEl && test) metaEl.textContent = `${test.category} • ${test.questions || 1} Challenge(s) • ${test.duration} Minutes (Pro Tier)`;

  if (freeBtn && test) {
    const tid = test.id || '';
    if (tid.startsWith('dbg_') || tid === 'gm_s2b' || (test.category && test.category.includes('Stage 2B'))) {
      freeBtn.textContent = '🎯 Try Free Debugging Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); window.location.href = 'modules/debug_sim.html?id=dbg_1'; };
    } else if (tid.startsWith('aic_') || tid === 'gm_s3' || (test.category && test.category.includes('Stage 3'))) {
      freeBtn.textContent = '🎯 Try Free AI Coding Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); window.location.href = 'modules/ai_coding_sim.html?id=aic_1'; };
    } else if (tid.startsWith('ps_') || tid === 'gm_s2a' || (test.category && test.category.includes('Stage 2A'))) {
      freeBtn.textContent = '🎯 Try Free PseudoCode Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); startTest('ps_1'); };
    } else if (tid.startsWith('mc_') || tid === 'gm_s4' || (test.category && test.category.includes('Stage 4'))) {
      freeBtn.textContent = '🎯 Try Free Cloud / Coding Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); startTest('mc_1'); };
    } else if (tid.startsWith('be_') || tid === 'gm_s56' || (test.category && test.category.includes('Stage 5'))) {
      freeBtn.textContent = '🎯 Try Free Behavioral Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); startTest('be_1'); };
    } else {
      freeBtn.textContent = '🎯 Try Free Verbal Test 1';
      freeBtn.onclick = () => { closeLockedTestModal(); startTest('vb_1'); };
    }
  }

  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeLockedTestModal() {
  const modal = document.getElementById('locked-test-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function togglePaymentSection() {
  const checkbox = document.getElementById('tc-agree-checkbox');
  const notice = document.getElementById('tc-gated-notice');
  const wrapper = document.getElementById('payment-methods-wrapper');
  
  if (checkbox && checkbox.checked) {
    if (notice) notice.style.display = 'none';
    if (wrapper) wrapper.style.display = 'block';
    showSecurityToast("✅ Terms & Conditions Accepted. Payment methods unlocked.");
  } else {
    if (notice) notice.style.display = 'block';
    if (wrapper) wrapper.style.display = 'none';
  }
}

function openForgotPasswordModal() {
  closeSignInModal();
  const modal = document.getElementById('forgot-password-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    const feedback = document.getElementById('forgot-feedback-msg');
    if (feedback) feedback.style.display = 'none';
    const input = document.getElementById('forgot-email-input');
    if (input) input.value = '';
  }
}

function closeForgotPasswordModal() {
  const modal = document.getElementById('forgot-password-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

async function recoverUserPassword() {
  const email = (document.getElementById('forgot-email-input')?.value || '').trim().toLowerCase();
  const feedback = document.getElementById('forgot-feedback-msg');
  if (!feedback) return;

  if (!email || !email.includes('@')) {
    feedback.style.display = 'block';
    feedback.style.background = 'rgba(239, 68, 68, 0.15)';
    feedback.style.border = '1px solid rgba(239, 68, 68, 0.3)';
    feedback.style.color = '#f87171';
    feedback.innerHTML = '⚠️ Please enter a valid registered email address.';
    return;
  }

  let user = null;

  // 1. Check Live Supabase Cloud Database First
  if (typeof dbFindUser === 'function') {
    try {
      const cloudUser = await dbFindUser(email);
      if (cloudUser) {
        user = {
          name: cloudUser.name || 'CapPrep Student',
          email: cloudUser.email,
          password: cloudUser.password || 'cap2027',
          isPro: cloudUser.is_pro ?? true
        };
      }
    } catch(e) {}
  }

  // 2. Check local users
  if (!user) {
    const users = getStoredUsers();
    user = users.find(u => u.email && u.email.toLowerCase() === email);
  }

  // Check Global Verified VIP Accounts (Admin Grants / Paid Students)
  if (!user) {
    const vip = GLOBAL_VERIFIED_VIP_ACCOUNTS.find(v => v.email.toLowerCase() === email);
    if (vip) {
      user = {
        name: vip.name,
        email: vip.email,
        password: vip.password || 'cap2027',
        isPro: true
      };
      // Auto-save to local users so subsequent sign-in is instant
      users.unshift(user);
      saveStoredUsers(users);
    }
  }

  // Check Orders Ledger
  if (!user) {
    try {
      const orders = JSON.parse(localStorage.getItem('capprep_orders') || '[]');
      const ordMatch = orders.find(o => o.email && o.email.toLowerCase() === email);
      if (ordMatch) {
        user = {
          name: ordMatch.name || "Enrolled Student",
          email: ordMatch.email,
          password: ordMatch.password || "cap2027",
          isPro: true
        };
      }
    } catch(e) {}
  }

  if (!user) {
    feedback.style.display = 'block';
    feedback.style.background = 'rgba(239, 68, 68, 0.15)';
    feedback.style.border = '1px solid rgba(239, 68, 68, 0.3)';
    feedback.style.color = '#f87171';
    feedback.innerHTML = `❌ No active account found for <strong>${escapeHtml(email)}</strong>.<br><br>• If you paid via UPI, please WhatsApp Admin with your receipt/UTR to verify instantly.<br>• Haven't enrolled yet? <a href="javascript:void(0)" onclick="closeForgotPasswordModal(); openPaymentModal();" style="color:var(--accent); font-weight:700;">Enroll for ₹51 →</a>`;
    return;
  }

  // User found! Recover password
  feedback.style.display = 'block';
  feedback.style.background = 'rgba(6, 214, 160, 0.12)';
  feedback.style.border = '1px solid rgba(6, 214, 160, 0.35)';
  feedback.style.color = '#e2e8f0';
  feedback.innerHTML = `
    <div style="color:#06d6a0; font-weight:800; margin-bottom:0.25rem;">✅ Account Verified: ${escapeHtml(user.name)}</div>
    <div>Your registered password is:</div>
    <div style="font-size:1.15rem; font-weight:900; color:#00d4ff; font-family:monospace; background:rgba(0,0,0,0.3); padding:0.4rem; border-radius:6px; margin:0.4rem 0; text-align:center; letter-spacing:1px;">
      ${escapeHtml(user.password || 'cap2027')}
    </div>
    <div style="font-size:0.72rem; color:#94a3b8; margin-bottom:0.5rem;">(Credential verification simulated to ${escapeHtml(email)})</div>
    <button class="pay-btn-checkout" style="padding:0.5rem; font-size:0.82rem;" onclick="prefillAndSignIn('${escapeHtml(email)}', '${escapeHtml(user.password || '')}')">
      🔑 Sign In Now with Recovered Password →
    </button>
  `;
}

function prefillAndSignIn(email, password) {
  closeForgotPasswordModal();
  openSignInModal();
  const emailInput = document.getElementById('signin-email-input');
  const passInput = document.getElementById('signin-password-input');
  if (emailInput) emailInput.value = email;
  if (passInput) passInput.value = password;
  processUserSignIn();
}

function copyUpiId() {
  const upiId = "rishavofficials1727-7@okaxis";
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(upiId).then(() => {
      showSecurityToast("📋 UPI ID Copied: " + upiId);
      const btnText = document.getElementById('copy-upi-btn-text');
      if (btnText) {
        btnText.innerText = "✓ Copied: " + upiId;
        setTimeout(() => {
          btnText.innerText = "Copy UPI ID: " + upiId;
        }, 3000);
      }
    }).catch(() => fallbackCopy(upiId));
  } else {
    fallbackCopy(upiId);
  }
}

function fallbackCopy(text) {
  const ta = document.createElement('textarea');
  ta.value = text;
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  showSecurityToast("📋 UPI ID Copied: " + text);
}

function updateUpiLinksAndPrices(price) {
  const fixedAmtDisplay = document.getElementById('upi-fixed-amt-display');
  if (fixedAmtDisplay) fixedAmtDisplay.textContent = '₹' + price;

  const upiId = "rishavofficials1727-7@okaxis";
  const payeeName = "Rishav Kumar Gupta";
  const note = "CapPrep Pro Pass";
  const uri = `upi://pay?pa=${upiId}&pn=${encodeURIComponent(payeeName)}&am=${price}&cu=INR&tn=${encodeURIComponent(note)}`;

  const gpay = document.getElementById('upi-intent-gpay');
  const phonepe = document.getElementById('upi-intent-phonepe');
  const paytm = document.getElementById('upi-intent-paytm');
  const cred = document.getElementById('upi-intent-cred');

  if (gpay) gpay.href = uri;
  if (phonepe) phonepe.href = uri;
  if (paytm) paytm.href = uri;
  if (cred) cred.href = uri;

  // Dynamic QR Code generation with fixed amount embedded
  const dynamicQr = document.getElementById('dynamic-upi-qr');
  if (dynamicQr) {
    const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${encodeURIComponent(uri)}&margin=10`;
    if (typeof Image !== 'undefined') {
      const img = new Image();
      img.onload = () => { dynamicQr.src = qrUrl; };
      img.onerror = () => { dynamicQr.src = 'assets/upi_qr.png'; };
      img.src = qrUrl;
    } else {
      dynamicQr.src = qrUrl;
    }
  }
}

function goToPaymentScreen() {
  const name = (document.getElementById('cust-name-input')?.value || '').trim();
  const email = (document.getElementById('cust-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('cust-password-input')?.value || '').trim();
  const tcAgreed = document.getElementById('tc-agree-checkbox')?.checked;

  if (!name) {
    alert("⚠️ Please enter your Full Name.");
    document.getElementById('cust-name-input')?.focus();
    return;
  }
  if (!email || !email.includes('@')) {
    alert("⚠️ Please enter a valid Email Address (where your account pass is sent).");
    document.getElementById('cust-email-input')?.focus();
    return;
  }
  if (!password || password.length < 6) {
    alert("⚠️ Please create an Account Password of at least 6 characters so you can sign back in anytime!");
    document.getElementById('cust-password-input')?.focus();
    return;
  }
  if (!tcAgreed) {
    alert("⚠️ Please agree to the Digital Course Terms of Service and Non-Refundable Policy by checking the box.");
    document.getElementById('tc-agree-checkbox')?.focus();
    return;
  }

  // Update candidate summary pills
  const pillName = document.getElementById('pill-cust-name');
  const pillEmail = document.getElementById('pill-cust-email');
  const priceScreen2 = document.getElementById('pay-screen2-price');
  if (pillName) pillName.textContent = name;
  if (pillEmail) pillEmail.textContent = email;
  if (priceScreen2) priceScreen2.textContent = '₹' + currentPayablePrice;

  // Switch screens
  const s1 = document.getElementById('pay-screen-1');
  const s2 = document.getElementById('pay-screen-2');
  const s3 = document.getElementById('pay-screen-3');
  if (s1) s1.style.display = 'none';
  if (s2) s2.style.display = 'block';
  if (s3) s3.style.display = 'none';

  updateUpiLinksAndPrices(currentPayablePrice);
}

function backToDetailsScreen() {
  const s1 = document.getElementById('pay-screen-1');
  const s2 = document.getElementById('pay-screen-2');
  const s3 = document.getElementById('pay-screen-3');
  if (s1) s1.style.display = 'block';
  if (s2) s2.style.display = 'none';
  if (s3) s3.style.display = 'none';
}

function openPaymentModal(test) {
  closeLockedTestModal();
  closeSignInModal();
  closeForgotPasswordModal();
  const modal = document.getElementById('payment-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    startFlashCountdown();

    const s1 = document.getElementById('pay-screen-1');
    const s2 = document.getElementById('pay-screen-2');
    const s3 = document.getElementById('pay-screen-3');
    if (s1) s1.style.display = 'block';
    if (s2) s2.style.display = 'none';
    if (s3) s3.style.display = 'none';

    currentPayablePrice = 51;
    const priceEl = document.getElementById('modal-display-price');
    if (priceEl) priceEl.textContent = '₹51';
    const btnPrice = document.getElementById('btn-display-price');
    if (btnPrice) btnPrice.textContent = '₹51';
    const p2Price = document.getElementById('pay-screen2-price');
    if (p2Price) p2Price.textContent = '₹51';
    updateUpiLinksAndPrices(51);
  }
}

function closePaymentModal() {
  const modal = document.getElementById('payment-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function switchPayTab(tab) {
  const upiTab = document.getElementById('tab-btn-upi');
  const cardTab = document.getElementById('tab-btn-card');
  const upiContent = document.getElementById('pay-mode-upi');
  const cardContent = document.getElementById('pay-mode-card');

  if (tab === 'upi') {
    if (upiTab) upiTab.classList.add('active');
    if (cardTab) cardTab.classList.remove('active');
    if (upiContent) upiContent.style.display = 'block';
    if (cardContent) cardContent.style.display = 'none';
  } else {
    if (upiTab) upiTab.classList.remove('active');
    if (cardTab) cardTab.classList.add('active');
    if (upiContent) upiContent.style.display = 'none';
    if (cardContent) cardContent.style.display = 'block';
  }
}

function applyCoupon() {
  const input = document.getElementById('coupon-code-input');
  const feedback = document.getElementById('coupon-feedback');
  if (!input || !feedback) return;

  const code = input.value.trim().toUpperCase();
  if (code === 'SUPER51' || code === 'EXCELLER51' || code === 'CAP51') {
    currentPayablePrice = 51;
    feedback.innerHTML = '<span style="color:#06d6a0">✓ Coupon <strong>' + code + '</strong> applied! Price set to ₹51 (83% OFF).</span>';
  } else if (code === 'FREE100' || code === 'RISHAVVIP') {
    currentPayablePrice = 0;
    feedback.innerHTML = '<span style="color:#06d6a0">✓ VIP 100% FREE Access Activated!</span>';
  } else {
    feedback.innerHTML = '<span style="color:#ef4444">✗ Invalid code. Using default ₹51 offer.</span>';
  }

  const priceEl = document.getElementById('modal-display-price');
  if (priceEl) priceEl.textContent = '₹' + currentPayablePrice;
  const btnPrice = document.getElementById('btn-display-price');
  if (btnPrice) btnPrice.textContent = '₹' + currentPayablePrice;
  const p2Price = document.getElementById('pay-screen2-price');
  if (p2Price) p2Price.textContent = '₹' + currentPayablePrice;
  updateUpiLinksAndPrices(currentPayablePrice);
}

function processUpiPayment() {
  const name = (document.getElementById('cust-name-input')?.value || '').trim();
  const email = (document.getElementById('cust-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('cust-password-input')?.value || '').trim();
  const phone = (document.getElementById('cust-phone-input')?.value || '').trim();
  const college = (document.getElementById('cust-college-input')?.value || '').trim();
  const utr = (document.getElementById('upi-utr-input')?.value || '').trim();

  if (!name) {
    alert("⚠️ Please enter your Full Name.");
    backToDetailsScreen();
    document.getElementById('cust-name-input')?.focus();
    return;
  }
  if (!email || !email.includes('@')) {
    alert("⚠️ Please enter a valid Email Address (will be your login ID).");
    backToDetailsScreen();
    document.getElementById('cust-email-input')?.focus();
    return;
  }
  if (!password || password.length < 6) {
    alert("⚠️ Please create an Account Password of at least 6 characters so you can sign back in anytime!");
    backToDetailsScreen();
    document.getElementById('cust-password-input')?.focus();
    return;
  }
  if (!utr || utr.length < 8) {
    alert("⚠️ Please enter the 12-digit UPI UTR / Transaction Reference number after paying ₹51 to rishavofficials1727-7@okaxis in your UPI app.");
    document.getElementById('upi-utr-input')?.focus();
    return;
  }

  const btn = document.getElementById('btn-verify-upi');
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `⏳ Verifying ₹${currentPayablePrice} UPI Payment...`;
  }

  setTimeout(() => {
    // 1. Register / Update user account with password
    const users = getStoredUsers();
    const existingIdx = users.findIndex(u => u.email && u.email.toLowerCase() === email);
    const userObj = {
      name: name,
      email: email,
      password: password,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      isPro: true,
      joinedAt: new Date().toLocaleString()
    };

    if (existingIdx >= 0) {
      users[existingIdx] = userObj;
    } else {
      users.unshift(userObj);
    }
    saveStoredUsers(users);
    setCurrentUser(userObj);
    if (typeof dbSaveUser === 'function') {
      dbSaveUser(userObj);
    }

    completeOrderActivation({
      name,
      email,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      method: "UPI Direct (rishavofficials1727-7@okaxis)",
      utr: utr,
      amount: currentPayablePrice
    });

    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `⚡ Verify & Unlock Pro`;
    }
  }, 800);
}

function processCardPayment() {
  const name = (document.getElementById('cust-name-input')?.value || '').trim();
  const email = (document.getElementById('cust-email-input')?.value || '').trim().toLowerCase();
  const password = (document.getElementById('cust-password-input')?.value || '').trim();
  const phone = (document.getElementById('cust-phone-input')?.value || '').trim();
  const college = (document.getElementById('cust-college-input')?.value || '').trim();

  if (!name || !email) {
    alert("⚠️ Please enter your Name and Email in the Student Details section.");
    backToDetailsScreen();
    return;
  }
  if (!password || password.length < 6) {
    alert("⚠️ Please create an Account Password of at least 6 characters.");
    backToDetailsScreen();
    return;
  }

  const btn = document.getElementById('pay-submit-btn');
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `⏳ Processing ₹${currentPayablePrice} Card Payment...`;
  }

  setTimeout(() => {
    const users = getStoredUsers();
    const userObj = {
      name: name,
      email: email,
      password: password,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      isPro: true,
      joinedAt: new Date().toLocaleString()
    };
    users.unshift(userObj);
    saveStoredUsers(users);
    setCurrentUser(userObj);
    if (typeof dbSaveUser === 'function') {
      dbSaveUser(userObj);
    }

    completeOrderActivation({
      name,
      email,
      phone: phone || "+91 98000 00000",
      college: college || "Capgemini Candidate",
      method: "Credit/Debit Card",
      utr: "CARD-" + Math.floor(1000000000 + Math.random() * 9000000000),
      amount: currentPayablePrice
    });

    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `🔒 Pay ₹${currentPayablePrice} & Unlock Everything`;
    }
  }, 1000);
}

let lastCompletedOrder = null;

function completeOrderActivation(orderDetails) {
  unlockProPass(orderDetails.utr);
  const orderId = 'ORD-' + Math.floor(100000 + Math.random() * 900000);
  
  const fullOrder = {
    id: orderId,
    orderId: orderId,
    ...orderDetails,
    timestamp: new Date().toLocaleString(),
    status: 'VERIFIED_ACTIVE'
  };
  lastCompletedOrder = fullOrder;

  // 1. Store order in ledger
  try {
    const orders = JSON.parse(localStorage.getItem('capprep_orders') || '[]');
    orders.unshift(fullOrder);
    localStorage.setItem('capprep_orders', JSON.stringify(orders));
  } catch(e) {}

  if (typeof dbSaveOrder === 'function') {
    dbSaveOrder(fullOrder);
  }

  // 2. Dispatch Automated Dual Email (Candidate Confirmation + Admin Notification)
  dispatchOrderEmails(fullOrder, orderId);

  closeLockedTestModal();
  updateProUI();

  // Show Screen 3: Instant Confirmation & Dashboard Entry
  const s1 = document.getElementById('pay-screen-1');
  const s2 = document.getElementById('pay-screen-2');
  const s3 = document.getElementById('pay-screen-3');
  const confName = document.getElementById('conf-cust-name');
  const confEmail = document.getElementById('conf-cust-email');
  const confOrderId = document.getElementById('conf-order-id');

  if (s1) s1.style.display = 'none';
  if (s2) s2.style.display = 'none';
  if (s3) s3.style.display = 'block';
  if (confName) confName.textContent = orderDetails.name;
  if (confEmail) confEmail.textContent = orderDetails.email;
  if (confOrderId) confOrderId.textContent = '#' + orderId;

  showSecurityToast(`🎉 Pro Pass Activated! Confirmation email sent to ${orderDetails.email}.`);
}

// Dual Email Dispatcher: Candidate Receipt + Admin Sale Alert
function dispatchOrderEmails(orderDetails, orderId) {
  const adminEmail = "rishavofficials1727@gmail.com";
  const customerEmail = orderDetails.email;
  const studentName = orderDetails.name || "Enrolled Student";
  const amountStr = `₹${orderDetails.amount || 51}`;
  const utrRef = orderDetails.utr || "DIRECT_UPI";
  const timestamp = orderDetails.timestamp || new Date().toLocaleString();
  const siteUrl = (typeof window !== 'undefined' && window.location && window.location.origin) ? window.location.origin : "https://capprep-pro-2027.vercel.app";

  // 1. Log into Admin In-App Notifications Feed (admin.html)
  try {
    const notifs = JSON.parse(localStorage.getItem('capprep_admin_notifs') || '[]');
    notifs.unshift({
      title: `💰 [NEW SALE] ${amountStr} from ${studentName}`,
      buyer: studentName,
      email: customerEmail,
      phone: orderDetails.phone || "N/A",
      college: orderDetails.college || "Capgemini Candidate",
      amount: orderDetails.amount || 51,
      utr: utrRef,
      orderId: orderId,
      timestamp: timestamp
    });
    localStorage.setItem('capprep_admin_notifs', JSON.stringify(notifs));
  } catch(e) {}

  // 2. Dispatch Automated Notification Email to Admin (rishavofficials1727@gmail.com)
  try {
    if (typeof fetch !== 'undefined') {
      fetch(`https://formsubmit.co/ajax/${encodeURIComponent(adminEmail)}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          _subject: `💰 [NEW SALE] ${amountStr} Received from ${studentName} (Order #${orderId})`,
          _template: "table",
          _captcha: "false",
          _replyto: customerEmail,
          "Order ID": `#${orderId}`,
          "Student Name": studentName,
          "Registered Email": customerEmail,
          "WhatsApp Phone": orderDetails.phone || "N/A",
          "College / Batch": orderDetails.college || "Capgemini Aspirant",
          "Amount Paid": `${amountStr} INR`,
          "Payment Method": orderDetails.method || "UPI (rishavofficials1727-7@okaxis)",
          "UPI UTR Reference": utrRef,
          "Status": "VERIFIED & PRO PASS UNLOCKED",
          "Timestamp": timestamp,
          "Admin Control Center": `${siteUrl}/admin.html`
        })
      }).then(res => res.json())
        .then(d => console.log("Admin notification email dispatched:", d))
        .catch(err => console.warn("Admin email notice (async):", err));
    }
  } catch(e) {}

  // 3. Dispatch Automated Confirmation & Invoice to Candidate (customerEmail)
  try {
    if (typeof fetch !== 'undefined' && customerEmail && customerEmail.includes('@')) {
      fetch(`https://formsubmit.co/ajax/${encodeURIComponent(customerEmail)}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          _subject: `🎓 CapPrep Pro Order Confirmation & Lifetime Pass Active (Order #${orderId})`,
          _template: "box",
          _captcha: "false",
          _replyto: adminEmail,
          "Greetings": `Hello ${studentName}, your payment of ${amountStr} is confirmed!`,
          "Order Reference": `#${orderId}`,
          "Amount Paid": `${amountStr} INR (Lifetime Pro Pass)`,
          "UPI Transaction Ref (UTR)": utrRef,
          "Registered Login ID": customerEmail,
          "Access URL": siteUrl,
          "Included Access": "All 76+ Proctored Mock Tests, Lab 27 AI Simulator, Stage 2B Debugger, Stage 4 HR & Technical Hub, Full Downloadable Study PDF Guides",
          "Support & Helpdesk": "rishavofficials1727@gmail.com"
        })
      }).then(res => res.json())
        .then(d => console.log("Candidate confirmation email dispatched:", d))
        .catch(err => console.warn("Candidate email notice (async):", err));
    }
  } catch(e) {}
}

function downloadCurrentReceipt() {
  const o = lastCompletedOrder || {
    id: 'ORD-PRO-' + Math.floor(100000 + Math.random() * 900000),
    name: (document.getElementById('conf-cust-name')?.textContent || 'Candidate').trim(),
    email: (document.getElementById('conf-cust-email')?.textContent || 'candidate@capprep.com').trim(),
    phone: "+91 Candidate",
    college: "Capgemini Aspirant",
    amount: 51,
    method: "UPI (rishavofficials1727-7@okaxis)",
    utr: "VERIFIED_ACTIVE",
    timestamp: new Date().toLocaleString()
  };

  const invoiceHtml = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Tax Invoice / Receipt - ${o.id || 'CAP-PRO'}</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 40px; color: #1e293b; background: #fff; line-height: 1.6; }
    .invoice-card { max-width: 680px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 12px; padding: 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); }
    .header { display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #00d4ff; padding-bottom: 20px; margin-bottom: 24px; }
    .brand { font-size: 24px; font-weight: 800; color: #0f172a; }
    .brand span { color: #00d4ff; }
    .badge { background: #dcfce7; color: #15803d; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    .meta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; font-size: 14px; }
    .table { width: 100%; border-collapse: collapse; margin-bottom: 24px; }
    .table th { background: #f8fafc; text-align: left; padding: 12px; font-size: 12px; text-transform: uppercase; color: #64748b; border-bottom: 1px solid #e2e8f0; }
    .table td { padding: 14px 12px; border-bottom: 1px solid #f1f5f9; font-size: 14px; }
    .total-row { font-size: 16px; font-weight: 700; color: #0f172a; }
    .footer { text-align: center; margin-top: 32px; padding-top: 20px; border-top: 1px solid #f1f5f9; font-size: 12px; color: #94a3b8; }
  </style>
</head>
<body>
  <div class="invoice-card">
    <div class="header">
      <div>
        <div class="brand">CapPrep <span>Pro</span> 2027</div>
        <div style="font-size: 13px; color: #64748b; margin-top: 4px;">Exceller Recruitment Preparation Platform</div>
      </div>
      <div style="text-align: right;">
        <div class="badge">● PAYMENT VERIFIED</div>
        <div style="font-size: 12px; color: #64748b; margin-top: 6px;">Date: ${o.timestamp || new Date().toLocaleDateString()}</div>
      </div>
    </div>

    <div class="meta-grid">
      <div>
        <strong style="color: #64748b; font-size: 12px; text-transform: uppercase;">Billed To:</strong><br>
        <strong>${o.name || 'Candidate'}</strong><br>
        Email: ${o.email || 'N/A'}<br>
        Phone: ${o.phone || 'N/A'}<br>
        College: ${o.college || 'Capgemini Candidate'}
      </div>
      <div style="text-align: right;">
        <strong style="color: #64748b; font-size: 12px; text-transform: uppercase;">Order Details:</strong><br>
        Order Ref: <strong>#${o.id || o.orderId || 'CAP-90218'}</strong><br>
        Payment Method: ${o.method || 'UPI Direct'}<br>
        UTR Reference: <code>${o.utr || 'VERIFIED'}</code><br>
        Authorized By: Rishav (rishavofficials1727@gmail.com)
      </div>
    </div>

    <table class="table">
      <thead>
        <tr>
          <th>Description</th>
          <th>Access Tier</th>
          <th>Validity</th>
          <th style="text-align: right;">Amount (INR)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <strong>CapPrep Pro 2027 — Master Recruitment Suite</strong><br>
            <span style="font-size: 12px; color: #64748b;">Includes 76+ Mock Tests, Lab 27 AI Simulator, Stage 2B Debugger, Stage 4 Interview Hub & Study Notes</span>
          </td>
          <td>VIP Lifetime Pass</td>
          <td>Unlimited 2027</td>
          <td style="text-align: right; font-weight: 700;">₹${o.amount || 51}.00</td>
        </tr>
        <tr class="total-row">
          <td colspan="3" style="text-align: right;">Total Amount Paid:</td>
          <td style="text-align: right; color: #16a34a;">₹${o.amount || 51}.00 INR</td>
        </tr>
      </tbody>
    </table>

    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #166534; margin-bottom: 20px;">
      ✅ <strong>Access Confirmation:</strong> Your account is registered under <strong>${o.email}</strong>. Log in anytime at <strong>https://capprep-pro-2027.vercel.app</strong> using your password or 1-click VIP link.
    </div>

    <div class="footer">
      This is a computer-generated tax receipt. Issued by CapPrep Pro Management.<br>
      Support Contact: <strong>rishavofficials1727@gmail.com</strong> • UPI VPA: <strong>rishavofficials1727-7@okaxis</strong>
    </div>
  </div>
</body>
</html>`;

  const blob = new Blob([invoiceHtml], { type: 'text/html;charset=utf-8;' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.setAttribute('href', url);
  a.setAttribute('download', `CapPrep_Pro_Invoice_${(o.id || 'ORDER').replace('#','')}.html`);
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function unlockProPass(txnId) {
  try {
    localStorage.setItem('capprep_pro_unlocked', 'true');
    localStorage.setItem('capprep_txn_id', txnId || 'DIRECT_UNLOCK');
  } catch(e) {}
  updateProUI();
}

function updateProUI() {
  const isPro = isProUser();
  const cur = getCurrentUser();

  // 1. Update Navbar Pro Badge
  const proBadgeNav = document.getElementById('nav-pro-btn');
  if (proBadgeNav) {
    if (GLOBAL_FREE_ACCESS_MODE) {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #06d6a0, #059669)';
      proBadgeNav.innerHTML = `⭐ ALL TESTS UNLOCKED`;
      proBadgeNav.onclick = () => {
        showSecurityToast("🎉 Free Open Access: All 76+ Mock Tests & Simulators are UNLOCKED for everyone!");
      };
    } else if (isPro) {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #06d6a0, #059669)';
      proBadgeNav.innerHTML = `⭐ PRO ACTIVE`;
      proBadgeNav.onclick = () => {
        showSecurityToast("⭐ Pro Pass Active! Opening Pass Details...");
        openPaymentModal();
      };
    } else {
      proBadgeNav.className = 'nav-pro-badge';
      proBadgeNav.style.background = 'linear-gradient(135deg, #00d4ff, #7c3aed)';
      proBadgeNav.innerHTML = `⚡ Upgrade to Pro (₹51)`;
      proBadgeNav.onclick = () => openPaymentModal();
    }
  }

  // 2. Update Navbar Sign In / User Pill / Logout Buttons & Dynamic Admin Link
  const signinBtn = document.getElementById('nav-signin-btn');
  const userItem = document.getElementById('nav-user-item');
  const userNameEl = document.getElementById('nav-user-name');
  const logoutItem = document.getElementById('nav-logout-item');
  const adminNavItem = document.getElementById('nav-admin-link-item');
  
  if (cur) {
    const isMasterAdmin = MASTER_ADMIN_EMAILS.includes((cur.email || '').toLowerCase());
    if (adminNavItem) {
      adminNavItem.style.display = isMasterAdmin ? 'inline-block' : 'none';
    }
    if (signinBtn) signinBtn.style.display = 'none';
    if (userItem) {
      userItem.style.display = 'inline-block';
      if (userNameEl) {
        const badge = isMasterAdmin ? '👑 Admin' : '👤 ' + escHTML(cur.name.split(' ')[0]);
        userNameEl.innerHTML = badge;
      }
    }
    if (logoutItem) logoutItem.style.display = 'inline-block';
  } else {
    if (adminNavItem) adminNavItem.style.display = 'none';
    if (userItem) userItem.style.display = 'none';
    if (logoutItem) logoutItem.style.display = 'none';
    if (signinBtn) {
      signinBtn.style.display = 'inline-block';
      signinBtn.innerHTML = `🔑 Sign In`;
    }
  }

  // 3. Update lock badges on test pills and cards
  // Rule: 2 Free Tests per Stage; all others strictly LOCKED unless isPro
  document.querySelectorAll('.test-pill-btn, .test-card').forEach(el => {
    const onclickAttr = el.getAttribute('onclick') || '';
    const match = onclickAttr.match(/startTest\('([^']+)'\)/);
    if (!match) return;

    const testId = match[1];
    const test = MOCK_TESTS.find(t => t.id === testId);
    if (!test) return;

    // Clean existing badges
    const existingLock = el.querySelector('.test-lock-pill, .premium-lock-badge');
    const existingFree = el.querySelector('.test-free-pill');

    if (test.isPremium) {
      if (isPro) {
        if (existingLock) existingLock.remove();
        el.classList.remove('locked');
      } else {
        if (!existingLock) {
          const lockPill = document.createElement('span');
          lockPill.className = 'test-lock-pill';
          lockPill.innerHTML = `🔒 LOCKED`;
          const tpTag = el.querySelector('.tp-tag, .test-difficulty, .test-meta');
          if (tpTag) {
            tpTag.parentNode.insertBefore(lockPill, tpTag);
          } else {
            el.appendChild(lockPill);
          }
        }
        if (existingFree) existingFree.remove();
        el.classList.add('locked');
      }
    } else {
      // Free Trial Test (2 tests per stage)
      if (existingLock) existingLock.remove();
      el.classList.remove('locked');
      if (!isPro && !existingFree) {
        const freePill = document.createElement('span');
        freePill.className = 'test-free-pill';
        freePill.innerHTML = `🟢 FREE TRIAL`;
        const tpTag = el.querySelector('.tp-tag, .test-difficulty, .test-meta');
        if (tpTag) {
          tpTag.parentNode.insertBefore(freePill, tpTag);
        } else {
          el.appendChild(freePill);
        }
      } else if (isPro && existingFree) {
        existingFree.remove();
      }
    }
  });
}

// Flash countdown clock (14:59)
function startFlashCountdown() {
  if (flashTimerInterval) return;
  let secondsRemaining = 14 * 60 + 59;
  const clockEl = document.getElementById('flash-countdown-clock');
  
  flashTimerInterval = setInterval(() => {
    secondsRemaining--;
    if (secondsRemaining < 0) secondsRemaining = 14 * 60 + 59; // Loop to maintain perpetual urgency
    const m = Math.floor(secondsRemaining / 60).toString().padStart(2, '0');
    const s = (secondsRemaining % 60).toString().padStart(2, '0');
    if (clockEl) clockEl.textContent = `${m}:${s}`;
  }, 1000);
}

// Social Proof Live Buyer Notifications
const SOCIAL_PROOF_BUYERS = [
  { name: "Rohit S.", college: "VIT Vellore", action: "unlocked CapPrep Pro (₹51)", time: "2 minutes ago • Bangalore" },
  { name: "Sneha K.", college: "COEP Pune", action: "scored 94% on Grand Mock 1", time: "Just now • Pune" },
  { name: "Aman M.", college: "SRM Chennai", action: "unlocked CapPrep Pro (₹51)", time: "4 minutes ago • Chennai" },
  { name: "Priya T.", college: "DTU Delhi", action: "unlocked Lab 27 AI Simulator", time: "6 minutes ago • Delhi NCR" },
  { name: "Karthik N.", college: "BITS Pilani", action: "unlocked CapPrep Pro (₹51)", time: "8 minutes ago • Hyderabad" },
  { name: "Ananya B.", college: "Jadavpur Univ", action: "scored 96% on Stage 2B Debugging", time: "11 minutes ago • Kolkata" },
  { name: "Vikram R.", college: "Thapar Univ", action: "unlocked CapPrep Pro (₹51)", time: "Just now • Chandigarh" }
];

function startSocialProofLoop() {
  const toast = document.getElementById('social-proof-toast');
  const nameEl = document.getElementById('sp-buyer-name');
  const timeEl = document.getElementById('sp-buyer-time');
  if (!toast || !nameEl || !timeEl) return;

  let buyerIdx = 0;
  function triggerBuyerToast() {
    const buyer = SOCIAL_PROOF_BUYERS[buyerIdx % SOCIAL_PROOF_BUYERS.length];
    buyerIdx++;

    nameEl.textContent = buyer.name;
    const actionSpan = toast.querySelector('.sp-action');
    if (actionSpan) actionSpan.textContent = buyer.action;
    timeEl.textContent = buyer.time;

    toast.classList.add('visible');

    setTimeout(() => {
      toast.classList.remove('visible');
    }, 4500);
  }

  // First trigger after 5 seconds, then recurring every 22 seconds
  setTimeout(triggerBuyerToast, 5000);
  socialProofInterval = setInterval(triggerBuyerToast, 22000);
}

// ==========================================
// QUIZ ENGINE
// ==========================================

let currentTest = null;
let currentQuestions = [];
let currentQIdx = 0;
let score = 0;
let answered = false;
let timer = null;
let timeLeft = 0;
let userAnswers = [];
let tabViolationCount = 0;

function startTest(testId) {
  const test = MOCK_TESTS.find(t => t.id === testId);
  if (!test) {
    showSecurityToast("Test configuration not found: " + testId);
    return;
  }

  // Payment Wall Guard
  if (test.isPremium && !isProUser()) {
    openLockedTestModal(test);
    return;
  }

  // Route Stage 2B Debugging Tests directly to Hands-On Debugging Simulator (No MCQs)
  if (testId.startsWith('dbg_') || testId === 'gm_s2b') {
    window.location.href = 'modules/debug_sim.html?id=' + testId;
    return;
  }

  // Route Stage 3 AI-Assisted Coding Tests directly to Hands-On AI Coding Simulator (No MCQs)
  if (testId.startsWith('aic_') || testId === 'gm_s3') {
    window.location.href = 'modules/ai_coding_sim.html?id=' + testId;
    return;
  }

  currentTest = test;
  currentQuestions = getFreshQuestions(test);

  if (!currentQuestions || currentQuestions.length === 0) {
    showSecurityToast("Error loading question bank. Please try again.");
    return;
  }

  currentQIdx = 0;
  score = 0;
  answered = false;
  tabViolationCount = 0;
  userAnswers = new Array(currentQuestions.length).fill(-1);
  timeLeft = test.duration * 60;

  const container = document.getElementById('quiz-container');
  container.style.display = 'block';
  document.body.style.overflow = 'hidden';

  document.getElementById('quiz-title').textContent = test.title;
  document.getElementById('quiz-result').style.display = 'none';
  document.getElementById('question-card').style.display = 'block';

  renderQuestion();
  startTimer();
  updateProgress();
}

function renderQuestion() {
  if (currentQIdx >= currentQuestions.length) {
    showResult();
    return;
  }

  const q = currentQuestions[currentQIdx];
  if (!q) {
    showResult();
    return;
  }
  answered = false;

  document.getElementById('q-num').textContent = `Question ${currentQIdx + 1} of ${currentQuestions.length}`;

  // Handle code blocks and dynamic multi-language switcher
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
        rawCode = parts[1].replace(/^(cpp|c|java|python|js)\b\n?/i, '').trim();
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
  document.getElementById('q-code').innerHTML = codeHTML;

  const optContainer = document.getElementById('options-grid');
  const letters = ['A','B','C','D'];
  optContainer.innerHTML = (q.options || []).map((opt, i) => `
    <button class="option-btn" onclick="selectOption(${i})" id="opt-${i}">
      <span class="option-letter">${letters[i]}</span>
      ${escHTML(opt)}
    </button>
  `).join('');

  document.getElementById('explanation-box').style.display = 'none';
  document.getElementById('explanation-box').innerHTML = '';

  document.getElementById('btn-next').textContent =
    currentQIdx === currentQuestions.length - 1 ? '🏁 Finish Test' : 'Next →';
}

function selectOption(idx) {
  if (answered) return;
  answered = true;

  const q = currentQuestions[currentQIdx];
  if (!q) return;
  userAnswers[currentQIdx] = idx;

  for (let i = 0; i < (q.options || []).length; i++) {
    const btn = document.getElementById(`opt-${i}`);
    if (btn) {
      btn.disabled = true;
      if (i === q.ans) btn.classList.add('correct');
      else if (i === idx && idx !== q.ans) btn.classList.add('wrong');
    }
  }

  if (idx === q.ans) score++;

  const expBox = document.getElementById('explanation-box');
  expBox.innerHTML = `<strong>💡 Explanation:</strong> ${escHTML(q.exp)}`;
  expBox.style.display = 'block';
}

function nextQuestion() {
  if (!answered && currentQIdx < currentQuestions.length) {
    userAnswers[currentQIdx] = -1;
  }
  currentQIdx++;
  if (currentQIdx >= currentQuestions.length) {
    showResult();
  } else {
    renderQuestion();
    updateProgress();
  }
}

function updateProgress() {
  const pct = ((currentQIdx) / Math.max(1, currentQuestions.length)) * 100;
  document.getElementById('quiz-progress-fill').style.width = pct + '%';
}

function startTimer() {
  clearInterval(timer);
  const timerEl = document.getElementById('quiz-timer');
  timer = setInterval(() => {
    timeLeft--;
    const m = Math.floor(timeLeft / 60).toString().padStart(2,'0');
    const s = (timeLeft % 60).toString().padStart(2,'0');
    if (timerEl) {
      timerEl.textContent = `⏱ ${m}:${s}`;
      if (timeLeft <= 60) {
        timerEl.style.color = '#ef4444';
      } else {
        timerEl.style.color = 'var(--accent)';
      }
    }
    if (timeLeft <= 0) {
      clearInterval(timer);
      showResult();
    }
  }, 1000);
}

function showResult() {
  clearInterval(timer);
  document.getElementById('question-card').style.display = 'none';
  document.getElementById('quiz-progress-fill').style.width = '100%';

  const total = Math.max(1, currentQuestions.length);
  const pct = Math.round((score / total) * 100);
  let grade, msg, color;

  if (pct >= 85) { grade = '🏆 Excellent!'; msg = 'Outstanding performance! You are well-prepared for Capgemini.'; color = '#06d6a0'; }
  else if (pct >= 70) { grade = '✅ Good Job!'; msg = 'Solid performance! Review your weak areas and you\'re ready.'; color = '#00d4ff'; }
  else if (pct >= 55) { grade = '⚠️ Average'; msg = 'You need more practice. Focus on the topics you got wrong.'; color = '#f59e0b'; }
  else { grade = '❌ Needs Work'; msg = 'Keep practicing! Review the study materials and retake the test.'; color = '#ef4444'; }

  // Persist score in localStorage
  saveTestAttempt(currentTest.id, score, total, pct);

  const safeTestId = escHTML(currentTest.id);
  const resultEl = document.getElementById('quiz-result');
  resultEl.style.display = 'block';
  resultEl.innerHTML = `
    <div style="font-size:3rem;margin-bottom:1rem">🎓</div>
    <div class="result-grade" style="color:${color}">${grade}</div>
    <div class="result-score">${pct}%</div>
    <p style="font-size:1.1rem;margin-bottom:0.5rem">Score: <strong>${score}/${total}</strong></p>
    <p class="result-msg">${msg}</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
      <button class="btn btn-primary" id="btn-retake-test">🔄 Retake Test (New Questions)</button>
      <button class="btn btn-outline" onclick="closeQuiz()">📚 Back to Dashboard</button>
    </div>
  `;

  document.getElementById('btn-retake-test').addEventListener('click', () => {
    startTest(safeTestId);
  });
}

function saveTestAttempt(testId, got, total, pct) {
  try {
    const history = JSON.parse(localStorage.getItem('capprep_history') || '{}');
    const prev = history[testId] || { attempts: 0, bestScore: 0 };
    history[testId] = {
      attempts: prev.attempts + 1,
      bestScore: Math.max(prev.bestScore, pct),
      lastScore: pct,
      lastDate: new Date().toLocaleDateString()
    };
    localStorage.setItem('capprep_history', JSON.stringify(history));
  } catch(e) {
    console.error("Failed to save attempt history:", e);
  }
}

function closeQuiz() {
  clearInterval(timer);
  document.getElementById('quiz-container').style.display = 'none';
  document.body.style.overflow = '';
}

// Robust HTML escaping to protect against XSS and attribute breaking
function escHTML(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// Toast notification for proctoring and feedback
function showSecurityToast(msg) {
  const existing = document.getElementById('active-sec-toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.id = 'active-sec-toast';
  toast.className = 'sec-toast';
  toast.innerHTML = `<span>🛡️</span> <span>${escHTML(msg)}</span>`;
  document.body.appendChild(toast);

  setTimeout(() => {
    if (toast.parentNode) toast.remove();
  }, 3500);
}

// ==========================================
// SECURITY & ANTI-TAMPER PROCTORING ENGINE
// ==========================================

// 1. Proctored Window Blur / Tab-Switch Detection
window.addEventListener('blur', () => {
  const quiz = document.getElementById('quiz-container');
  if (quiz && quiz.style.display === 'block') {
    tabViolationCount++;
    showSecurityToast(`⚠️ Proctored Alert: Tab switch detected (${tabViolationCount}). Please remain on test screen.`);
  }
});

// 2. Anti-Copy & Anti-Right-Click Protection
document.addEventListener('contextmenu', e => {
  const quiz = document.getElementById('quiz-container');
  if (quiz && quiz.style.display === 'block') {
    e.preventDefault();
    showSecurityToast("🔒 Right-click is restricted in Proctored Assessment Mode");
  } else if (e.target.closest('.stage-section-card, .test-card, .diagram-box')) {
    e.preventDefault();
    showSecurityToast("🔒 Assessment curriculum is protected against copy");
  }
});

// 3. Anti-DevTools Hotkey Interception during Tests
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    closeQuiz();
    closePaymentModal();
    return;
  }

  const quiz = document.getElementById('quiz-container');
  if (quiz && quiz.style.display === 'block') {
    // Intercept F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U
    if (
      e.key === 'F12' ||
      (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) ||
      (e.ctrlKey && (e.key === 'u' || e.key === 'U'))
    ) {
      e.preventDefault();
      showSecurityToast("🔒 Developer inspection is restricted during proctored assessments");
    }
  }
});


// Check if candidate email/ID is in VIP whitelist
function checkVipCandidateWhitelist(inputVal) {
  if (!inputVal) return false;
  const val = inputVal.trim().toLowerCase();
  try {
    const list = JSON.parse(localStorage.getItem('capprep_vip_whitelist') || '[]');
    const match = list.find(item => item.id && item.id.trim().toLowerCase() === val);
    if (match) {
      currentPayablePrice = 0;
      const priceDisplay = document.getElementById('modal-display-price');
      if (priceDisplay) priceDisplay.textContent = '₹0 (FREE VIP)';
      const feedback = document.getElementById('coupon-feedback');
      if (feedback) {
        feedback.innerHTML = `<span style="color:#06d6a0">👑 Welcome VIP Candidate <strong>${escHTML(match.name)}</strong>! Your subscription is 100% FREE pre-approved by Admin Rishav.</span>`;
      }
      return true;
    }
  } catch(e) {}
  return false;
}

// Attach listener to customer email input when modal opens

// VIP Whitelist auto-check helper
function initVipCheckListeners() {
  const emailInput = document.getElementById('cust-email-input');
  if (emailInput) {
    emailInput.addEventListener('input', (e) => {
      checkVipCandidateWhitelist(e.target.value);
    });
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  // Check 1-Click VIP Unlock via URL parameter (e.g. sent by Rishav via WhatsApp)
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const testLogin = urlParams.get('test_login') || urlParams.get('test_id') || urlParams.get('tester');
    if (testLogin) {
      const match = OFFICIAL_TEST_ACCOUNTS.find(t => 
        t.id.toLowerCase().includes(testLogin.toLowerCase()) || 
        testLogin.toLowerCase().includes(t.id.split('@')[0])
      );
      if (match) {
        const sessionToken = "SESS_" + Date.now() + "_" + Math.floor(100000 + Math.random() * 900000);
        try {
          const activeSessions = JSON.parse(localStorage.getItem('capprep_active_sessions') || '{}');
          activeSessions[match.id.toLowerCase()] = sessionToken;
          localStorage.setItem('capprep_active_sessions', JSON.stringify(activeSessions));
          if (typeof sessionStorage !== 'undefined') {
            sessionStorage.setItem('capprep_session_token', sessionToken);
          }
        } catch(e) {}
        const testUser = {
          name: match.name,
          email: match.id,
          password: match.password,
          phone: "+91 98000 00000",
          college: match.role,
          isPro: true,
          isTestAccount: true,
          sessionToken: sessionToken,
          joinedAt: new Date().toLocaleString()
        };
        setCurrentUser(testUser);
        showSecurityToast(`🧪 Signed in via 1-Click Tester Link as ${match.name}!`);
        alert(`🎉 WELCOME ${match.name.toUpperCase()}!\n\nFull Pro Access is ACTIVE via 1-Click Tester Access.\n\n🛡️ NOTE: Single Active Session is strictly enforced. If this Test ID logs in on another device/browser, your current session will be automatically disconnected.`);
      }
    } else if (urlParams.get('vip_unlock') === 'true' || urlParams.get('unlock_vip') === 'true') {
      const candidateUser = (urlParams.get('user') || urlParams.get('email') || 'VIP Candidate').toLowerCase();
      const candidateName = urlParams.get('name') || 'VIP Candidate';
      const candidatePwd  = urlParams.get('pwd')  || urlParams.get('password') || 'cap2027';
      const candidatePhone = urlParams.get('phone') || '+91 98000 00000';

      const vipUser = {
        name: candidateName,
        email: candidateUser,
        password: candidatePwd,
        phone: candidatePhone,
        college: "Capgemini Candidate (VIP Pro Pass)",
        isPro: true,
        isVip: true,
        joinedAt: new Date().toLocaleString()
      };

      const storedUsers = getStoredUsers();
      const existingIdx = storedUsers.findIndex(u => u.email && u.email.toLowerCase() === candidateUser);
      if (existingIdx >= 0) {
        storedUsers[existingIdx] = Object.assign({}, storedUsers[existingIdx], vipUser);
      } else {
        storedUsers.unshift(vipUser);
      }
      saveStoredUsers(storedUsers);
      setCurrentUser(vipUser);
      unlockProPass('VIP-LINK-' + candidateUser);
      showSecurityToast(`👑 VIP Pro Lifetime Pass Activated for ${candidateName}!`);
      alert(`🎉 WELCOME ${candidateName.toUpperCase()}!\n\nYour CapPrep Pro Lifetime Pass has been ACTIVATED for 100% FREE!\nSponsored by Master Admin Rishav.\n\n📧 Registered Email: ${candidateUser}\n🔑 Your Password: ${candidatePwd}\n\nAll 76+ Mock Tests, Lab 27 AI Simulator, and Protected PDF Guides are now UNLOCKED!`);
    } else if (urlParams.get('coupon')) {
      const c = urlParams.get('coupon').toUpperCase();
      const codeInput = document.getElementById('coupon-code-input');
      if (codeInput) {
        codeInput.value = c;
        openPaymentModal();
        applyCoupon();
      }
    } else if (urlParams.get('open_pay') === 'true' || urlParams.get('pay') === 'true') {
      openPaymentModal();
    } else if (urlParams.get('open_signin') === 'true' || urlParams.get('signin') === 'true') {
      openSignInModal();
    }
  } catch(err) {
    console.error("VIP URL check error:", err);
  }

  updateProUI();
  startSocialProofLoop();
  initVipCheckListeners();
  initScrollSpy();

  // Ensure all sections are visible immediately
  document.querySelectorAll('.fade-in').forEach(el => {
    el.classList.add('visible');
    el.style.opacity = '1';
    el.style.transform = 'none';
  });
});

// Dynamic Active Navigation Indicator (ScrollSpy)
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id], div[id]');
  const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
  if (!navLinks || navLinks.length === 0) return;

  function updateActiveNav() {
    const scrollY = window.pageYOffset || document.documentElement.scrollTop;
    let currentId = '';

    sections.forEach(sec => {
      const top = sec.offsetTop - 140;
      const height = sec.offsetHeight;
      if (scrollY >= top && scrollY < top + height) {
        currentId = sec.getAttribute('id');
      }
    });

    if (currentId) {
      navLinks.forEach(link => {
        const href = (link.getAttribute('href') || '').replace('#', '');
        if (href === currentId) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
    }
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();
}


// Global Keydown Listeners (Esc to close modals, Ctrl+Shift+A for Admin)
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' || e.key === 'Esc') {
    closeLockedTestModal();
    closePaymentModal();
    closeSignInModal();
    closeForgotPasswordModal();
    closeSupportModal();
  }
  if (e.ctrlKey && e.shiftKey && (e.key === 'A' || e.key === 'a')) {
    e.preventDefault();
    window.location.href = 'admin.html';
  }
});
