# CapPrep Pro — Progress & State Tracker
**Last Updated**: October 2026 / Capgemini Exceller Batch 2027 (Senior Dev Audit + Security Hardened + Payment Gate Architecture)

This file maintains the exact state of work done so any future session can immediately resume without re-checking from scratch.

---

## ✅ Completed Tasks & Platform Summary

1. **Stage-by-Stage Preparation with 10+ Tests in Every Stage (`index.html` & `app.js`)**:
   - **Stage 1 (English Communication)**: 10 Dedicated Tests (`vb_1` to `vb_10` — Grammar, Comprehension, Para Jumbles, Active/Passive Voice, Vocabulary, Sentence Improvement, Idioms, Subject-Verb Agreement, Spoken AI Fluency, Grand Verbal).
   - **Stage 2A (Technical Assessment)**: 16 Dedicated Tests (`ai_1` to `ai_3`, `ps_1` to `ps_3`, `dsa_1` to `dsa_3`, `db_1` to `db_2`, `oop_1`, `os_1`, `cn_1`, `dv_1`, `apt_1`).
   - **Stage 2B (Debugging Assessment)**: 10 Dedicated Tests (`dbg_1` to `dbg_10` — Tree Recursion, Graph Cycles, 2D DP Bounds, NULL Pointers, Memory Leaks, Loop Errors, Swap By-Value, String Null Term, Linked List Pointer Jumps, Stage 2B Full Mock) + **Live Interactive Debugging Simulator**.
   - **Stage 3 (AI-Assisted Coding Assessment)**: 10 Dedicated Tests (`aic_1` to `aic_10` — Prompt Quality, Review & Adapt, Edge Cases, Complexity Directives, Tree/Graph Prompts, Iterative Refinement, Zero vs Few-Shot, Struct Framing, Capgemini Rubrics, Stage 3 Grand Mock) + **Live Interactive AI Coding Simulator (Lab 27)**.
   - **Stage 4 (Cognitive & ADEPT-15 Assessment)**: 10 Dedicated Tests (`sit_1` to `sit_10` — Motion Logic, Grid Memory, Inductive Rules, Ambition Trait, Team Conflict, Client Delivery, Adaptability, Ethical Choices, High Pressure, Stage 4 Mock).
   - **Stages 5 & 6 (Technical & HR Interview Defense)**: 10 Dedicated Tests (`int_1` to `int_10` — Capgemini 7 Core Values, STAR Framework, DB Architecture, Security & Auth, Project Storytelling, Cultural Fit, DSA Defense, OOPs Systems, Conflict Handling, Grand Interview Mock) + **Stages 4-6 Master Hub**.
   - **Grand Mock Marathon Suite (At End of Page)**: 10 Grand Full-Length Tests (`full_1` to `full_6`, `combo_1` to `combo_4`).

2. **Senior Developer Audit & Comprehensive Question Bank Expansion**:
   - Expanded question banks across all 14 recruitment domains to include **all probable Capgemini Exceller exam questions**:
     - `ai_literacy`: 30 questions (Transformers, RAG, Self-Attention, HNSW, LoRA, Prompt Injection, RLAIF, Quantization)
     - `pseudocode`: 25 questions (Bitwise XOR/AND/OR, Kernighan bit count, short-circuit, nested loops, recursion traces)
     - `dsa`: 25 questions (Floyd cycle detection, 2-queue stack, AVL height, BFS queue, Topological sort, Dijkstra, DP recurrence)
     - `dbms`: 25 questions (BCNF superkeys, Dirty reads, Serializable isolation, UNION vs UNION ALL, Clustered index, CASCADE, WAL)
     - `oops`: 25 questions (Diamond problem virtual inheritance, Virtual destructors, Deep vs Shallow copy, SOLID principles, Design patterns)
     - `os`: 25 questions (Belady's anomaly, Fork process tree $2^n$, Mutex vs Semaphore, Critical section, Orphan vs Zombie, TLB, SCAN disk)
     - `networks`: 25 questions (Subnetting /27 usable hosts, TCP 4-way termination, Congestion control Slow Start, RFC 1918 Private IPs, TLS crypto, CORS preflight OPTIONS, DHCP DORA)
     - `devops`: 25 questions (Docker CMD vs ENTRYPOINT, Multi-stage builds, K8s Pods/Deployments, Git cherry-pick, Git detached HEAD, Canary releases, Prometheus/Grafana)
     - `aptitude`: 25 questions (Boats & streams, Pipes with leak, Clock angle formula at 3:30, Calendar odd days, Alligation & mixtures, Card probabilities, 2-year CI vs SI difference)
     - `verbal`: 30 questions (Direct/Indirect speech, Prepositions, Correlative conjunctions, Synonyms/Antonyms, Active-Passive with modals, Idioms, Subject-verb agreement)
     - `debugging`: 22 questions (C++ operator precedence `*ptr++`, Floating point equality `x == 0.1`, Binary search mid overflow `low+(high-low)/2`, Arrow `->` vs `.`, Double free, 2D DP array sizing)
     - `ai_coding`: 20 questions (Lab 27 prompt rubric, Plagiarism prevention by requirement restatement, Complexity constraints, Iterative multi-turn prompting, Hallucination correction)
     - `situational`: 20 questions (Friday production outage protocol, Motion & Grid challenge tactics, ADEPT-15 integrity/collaboration traits, Constructive code review feedback)
     - `interview`: 25 questions (Serge Kampf 7 Core Values history, STAR difficult teammate story, CAP Theorem, Cache-aside Redis, Circuit Breaker, 5-year vision, Non-CS transition defense)
   - **Total Question Count: 347 curated high-yield questions** perfectly synchronized across `js/app.js` and `data/questions.json`.
   - Fixed retake bug: Added dynamic `getFreshQuestions()` generator so questions re-randomize fresh on every attempt and retake.
   - Fixed XSS & attribute breakout vulnerability in `escHTML()`: now escapes `&`, `<`, `>`, `"`, and `'`.
   - Fixed CSS `.fade-in` visibility bug: ensured default `opacity: 1` so sections never render as blank when jumping to stage anchors (`#stage1`, etc.).
   - Added null guards and test-result persistence in `localStorage` under `capprep_history`.

3. **Proctored Security & Anti-Tamper Hardening**:
   - **Content-Security-Policy (CSP)** added to HTML `<head>` (`nosniff`, `strict-origin-when-cross-origin`).
   - **Proctored Tab-Switch Detection**: Alerts student on window blur during active tests.
   - **Anti-Copy Protection**: Disables context menu (right-click) and text copy on assessment content.
   - **Anti-DevTools Protection**: Restricts F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U during tests.

4. **Executive Admin Control Center (`admin.html`) & Payment Partner Architecture**:
   - **Primary Master Admin**: Configured exclusively for **`rishavofficials1727@gmail.com`**.
   - **Secure Administrative Gate**: Master PIN access (`admin1727` / `rishav1727`) with cryptographic session persistence.
   - **Executive Dashboard Metrics**: Real-time revenue tally (₹), total paid students, today's sales, conversion rate tracking.
   - **Student Orders & Access Ledger**: Live table recording student names, emails, WhatsApp phones, colleges, payment methods (UPI/Cards), transaction/UTR references, and activation timestamps.
   - **Authority Actions**:
     - Instant access revocation or approval.
     - Manual complimentary access granting (VIP student / campus ambassador passes).
     - Full order export to CSV (compatible with Excel & Google Sheets).
   - **Instant Purchase Notification Hub**:
     - Automated order dispatch directly routed to `rishavofficials1727@gmail.com`.
     - In-dashboard live alert feed logging every single payment.
     - "Test Notification to My Email" button for instant testing.
   - **High-Converting Psychological Pricing Model (₹299 ➔ ₹51)**:
     - Anchor list price: <del>₹299</del>.
     - Auto-applied welcome coupon **`SUPER51`** slashes price to **₹51** (83% OFF / Save ₹248).
     - Live ticking countdown timer (14:59) creates urgent scarcity.
     - Irresistible ₹3,095 value stack breakdown (76+ tests, DRM PDF reader, 2 live simulators, 347 questions).
     - Live social proof floating toasts displaying real-time enrollments across Indian colleges.
   - **Free Indian Payment Partner Integration (100% Direct Profit)**:
     - **Mode 1: Direct Dynamic UPI QR (0% Fee)**: Generates dynamic UPI QR for `rishavofficials1727@okhdfcbank` with one-tap mobile app intents (Google Pay, PhonePe, Paytm). 0% gateway commission = 100% pure profit directly into Rishav's account!
     - **Mode 2: Indian Cards & NetBanking / Razorpay**: Seamless credit/debit card and net banking processing with 0 INR setup fee.

5. **In-Browser Protected PDF Master Reader (`modules/study_reader.html`)**:
   - **DRM Protected & Non-Downloadable**: Cannot be downloaded or printed (`@media print { display: none !important; }`, Ctrl+P/S shortcut interception, watermarked page background).
   - **Interactive Reader UI**: Table of contents index sidebar, stage selector dropdown, zoom controls (+/-), reading themes (Dark Slate, Paper White, Vintage Sepia), fullscreen mode, and section pagination.
   - **Comprehensive Best-of-the-Best Content**:
     - **Stage 1**: AI Speech scoring dimensions (Fluency, Phonemes, Grammar, Lexical), 12 Golden Grammar rules, If-clauses, 50 business idioms & para-jumble frameworks.
     - **Stage 2A**: Discriminative vs Generative ML, 5-Step RAG pipeline, LLM temperature/top-p, Bitwise operator math, DSA Big-O cheatsheets, DBMS Normalization (1NF-3NF) & ACID, Deadlock 4 Coffman conditions, OSI 7 layers.
     - **Stage 2B**: 4-Step diagnostic algorithm, Tree recursion base cases, Graph undirected cycle back-edges, 2D DP array dimensioning.
     - **Stage 3**: 5-part master prompt anatomy, Capgemini prompt scoring scorecard, Side-by-side Bad vs 10/10 Master Prompts for linked lists/trees/DP, Iterative prompt refinement.
     - **Stage 4**: Motion Challenge step-efficiency algorithms, Grid Challenge verbal rehearsal strategies, ADEPT-15 15-trait consistency matrix.
     - **Stages 5 & 6**: Serge Kampf 7 Core Values deep dive, STAR methodology with 6 model answers, 4-step project defense template, Top 25 systems & architecture questions.

6. **Interactive Live Simulators & Hubs**:
   - [`modules/ai_coding_sim.html`](file:///C:/cap/ai/modules/ai_coding_sim.html): Lab 27 AI Assisted Coding interface replica with prompt-grading logic.
   - [`modules/debug_sim.html`](file:///C:/cap/ai/modules/debug_sim.html): 20-minute Stage 2B Debugging workspace with real test case runner (Trees, Graphs, 2D DP).
   - [`modules/interview_hub.html`](file:///C:/cap/ai/modules/interview_hub.html): Stages 4, 5 & 6 Master Hub with Cognitive games guide, resume defense QA, and 7 Core Values STAR templates.
   - [`modules/study_reader.html`](file:///C:/cap/ai/modules/study_reader.html): In-browser protected PDF study guide for all stages.

---

## 📂 Complete File State in `C:\cap\ai\`

6. **Comprehensive Textbook-Grade In-Depth Study Notes (`js/study_docs.js` & `modules/study_reader.html`)**:
   - Expanded from brief summaries to **33 deep, textbook-grade chapters (94.8 KB)** featuring step-by-step intuition, memory layout diagrams, trace tables, formulas, and real Capgemini questions:
     - **Stage 1 (5 Chapters)**: Acoustic ASR Scoring Physics & Spectrograms, 20 Golden Grammar Rules, 4-Step Para-Jumble Decryption Algorithm, 50 Enterprise Words & Idioms, Spoken Test Drills (Repeat Sentences 3-chunking, Story Retelling 3-part blueprint, Extempore 60s PEP framework, Indian English accent fixes).
     - **Stage 2A (7 Chapters)**: Transformers Self-Attention Mathematics ($Q, K, V$), RAG 5-Step Pipeline & Vector DBs, Bitwise Optimization Mathematics & 5 Super-Tricks (Brian Kernighan), Data Structures & Big-O Complexity Encyclopedia, Core CS (DBMS ACID & Isolation levels, OS Deadlock 4 Coffman conditions, TCP 3-Way Handshake vs UDP), Pseudocode Trace Bank (10 real problems with full iteration trace tables), SQL Mastery & Normalization Visualized (1NF to BCNF, Joins Venn diagrams, Window Functions `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`).
     - **Stage 2B (5 Chapters)**: 4-Step Diagnostic Algorithm for 20-min rounds, Top 5 Bug Archetypes (Binary Search midpoint overflow, BFS queue visited timing, Tree NULL checks), Memory & Pointer Bugs in C/C++ (Stack vs Heap layout, dangling pointers, C-string null terminator `\0` overflow), 10 Real Capgemini Algorithmic Debugging Problems with line-by-line fixes (Cycle detection, 2D DP matrix bounds, Vector iterator invalidation), Java & Python Specific Runtime Traps (`==` vs `.equals()`, Integer caching, mutable default arguments).
     - **Stage 3 (5 Chapters)**: Lab 27 Automated Evaluation Rubric (5 scoring pillars), Production-Ready 10/10 Prompts for Core Problems (Trapping Rain Water, Tree LCA), The 7 Fatal Prompting Sins & Exact Fixes, Master Production Prompts for Hard Topics (0/1 Knapsack 1D DP, Dijkstra min-heap, Monotonic Stack Histogram), Test-Case Failure Recovery Workflow (WA, TLE, MLE, SIGSEGV).
     - **Stage 4 (5 Chapters)**: Cognitive Games Mechanics & Step-Minimization Tactics, ADEPT-15 Personality Framework & Capgemini Alignment, Switch Challenge Complete Permutation Matrix & 2-Level Deduction, Digit Challenge Mental Calculation Cheat Sheets (prime factorization, sum/diff balancing), ADEPT-15 15-Trait Alignment & Scenario Bank (10 real situational judgment questions with corporate rationales).
     - **Stages 5 & 6 (6 Chapters)**: Serge Kampf 7 Core Values with fresher STAR examples, Top 25 Technical Architecture Questions & Model Answers (CAP theorem, Cache-Aside, JWT HttpOnly, Circuit Breakers), 4-Step Project Defense & HR Interview Blueprint, System Design & Enterprise Architecture for Freshers (Monolith vs Microservices, Load balancing algorithms, Database sharding vs replication), Top 30 Technical Rapid-Fire Questions & Answers, HR Interview Masterclass: 20 Behavioral Scenarios (Relocation, rotational shifts, team conflict, 5-year vision).

7. **VIP Candidate 100% Free Subscription Authority & WhatsApp Share System**:
   - Master Admin (Rishav) now has full administrative power to grant **100% Free Lifetime VIP Access** to ANY Candidate ID, roll number, or email.
   - **Self-Unlock Button**: 1-click button in `admin.html` to instantly unlock the Pro Pass on Rishav's own device without checkout.
   - **Candidate ID Whitelist**: Admin can enter candidate name, ID/email, phone, and reason. Whitelisted candidates can activate their pass with ₹0 in the modal.
   - **1-Click WhatsApp / Email Invite Link**: Generates unique shareable links (`index.html?vip_unlock=true&user=...`) that automatically activate the Pro Pass when clicked by the student.
   - **Custom 100% Free Coupon Engine**: Admin can create custom promo codes (e.g. `RISHAV100`, `FREEVIP`, `CAMPUS2027`) that reduce payable price to ₹0 and instantly unlock Pro.
   - **Active VIP Roster**: Real-time table in `admin.html` tracking all free candidates with 1-click Link Copy and Revocation controls.

8. **User Account Authentication, Test 1 Free Gate & Payment Architecture (`index.html` & `app.js`)**:
   - **Quiz Engine Fix**: Added missing `#quiz-container` DOM element in `index.html`. Clicking on tests now immediately launches the proctored assessment runner.
   - **Test 1 Free / Tests 2–76 Locked**: Configured `MOCK_TESTS` so only Test 1 (`vb_1`: Diagnostic Verbal Assessment) is free; all other 75 tests are strictly locked behind Pro.
   - **Locked Test Pop-Up Modal (`#locked-test-modal`)**: Clicking any locked test displays an informative modal prompting the student to unlock for ₹51, Sign In if already purchased, or try free Test 1.
   - **Student Account & Sign In Engine**: Added full account registration and login system:
     - Enrollment form requires Name, Email, **Password (min 6 chars)**, Phone, and 12-digit UTR.
     - Student accounts stored in `capprep_users` with password verification.
     - `#signin-modal` allows returning students to log in with Email + Password anytime to restore Pro access across devices.
     - Top navbar features `🔑 Sign In` / `👤 [Name] (Sign Out)`.
   - **UPI ID Integration**: Updated default UPI to **`rishavofficials1727@oksbi`** across QR code generator, 1-tap mobile intents (GPay/PhonePe/Paytm), admin settings, and payment handlers.

9. **Zero Public Admin Exposure, Privacy Hardening, Help & Support, and Multi-Language Coding (`index.html`, `admin.html`, `app.js`)**:
   - **Zero Public Admin Exposure**:
     - Removed all admin links, badges, and admin email mentions from the public navbar, footer, and modals.
     - The Admin navigation link is dynamically hidden (`#nav-admin-link-item`) and strictly renders ONLY when an authorized admin (`rishavofficials1727@gmail.com` or `rishav.gupta0527@gmail.com`) logs into the site.
     - Added a secret emergency hotkey (`Ctrl + Shift + A`) that allows Rishav to launch the Admin Portal from anywhere.
   - **Admin Portal Security Hardening (`admin.html`)**:
     - Removed all default password displays (`(Default: admin1727)` eliminated).
     - Removed hardcoded readonly email address; requires typing the registered admin email + PIN `rishav0527`.
     - Secure authentication using SHA-256 cryptographic hash (`43a0b18f9ea8cfdc6fc3f1066406e32353efec4756e3222982a240bf97bd6b75`). PIN is never stored or visible in plain text.
     - Brute-force protection: 3 failed attempts triggers an automated 10-minute administrative lockout.
   - **Help & Support System**:
     - Added a dedicated Help & Support modal (`#support-modal`) accessible from the navbar, footer, and checkout modal.
     - Direct support email routing to **`rishav.gupta0527@gmail.com`** with a pre-formatted email composition link.
     - Clear student assistance for activation, UTR verification, and technical guidance.
   - **Multi-Language Switcher for Coding & Pseudocode Questions**:
     - Questions featuring programming code, pseudocode, or debugging now display an interactive language selector pill bar: **`C++`**, **`Java`**, **`Python`**, and **`C`**.
     - Dynamic on-the-fly code transpiler adapts syntax constructs, data types, print statements, and function signatures to the candidate's chosen language.
     - Preferred language selection is automatically saved in `localStorage` (`capprep_preferred_lang`) and applied across all test questions.

10. **2 Free Tests Per Stage Policy, Prominent Lock Marking, Stage-Wise Grand Mocks, and Privacy Safeguards**:
   - **2 Free Tests Open in Every Stage for Free Trial**:
     - **Stage 1 (English)**: Tests 1 & 2 (`vb_1`, `vb_2`) are 🟢 Free Trial. Tests 3–10 are 🔒 Locked.
     - **Stage 2A (Technical)**: Tests 1 & 2 (`ai_1`, `ai_2`) are 🟢 Free Trial. Tests 3–16 are 🔒 Locked.
     - **Stage 2B (Debugging)**: Tests 1 & 2 (`dbg_1`, `dbg_2`) are 🟢 Free Trial. Tests 3–10 are 🔒 Locked.
     - **Stage 3 (AI Coding)**: Tests 1 & 2 (`aic_1`, `aic_2`) are 🟢 Free Trial. Tests 3–10 are 🔒 Locked.
     - **Stage 4 (Cognitive & ADEPT-15)**: Tests 1 & 2 (`sit_1`, `sit_2`) are 🟢 Free Trial. Tests 3–10 are 🔒 Locked.
     - **Stages 5 & 6 (Interview)**: Tests 1 & 2 (`int_1`, `int_2`) are 🟢 Free Trial. Tests 3–10 are 🔒 Locked.
     - **Grand Mocks**: Tests 1 & 2 (`full_1`, `full_2`) are 🟢 Free Trial. All other 8 Grand Mocks are 🔒 Locked.
   - **Prominent Visual Lock Marking (`🔒 LOCKED`)**:
     - High-contrast crimson badges (`.test-lock-pill` with `box-shadow`) prominently display `🔒 LOCKED` on every locked test card and pill button.
     - Free trial tests display a glowing green `🟢 FREE TRIAL` badge.
     - Unlocked automatically upon Pro authentication; reverts instantly to `🔒 LOCKED` upon Logout.
   - **Privacy Shield & Generic Error Messages**:
     - Removed all mentions of administrator's name ("Rishav") from the admin login gate.
     - Login error message now strictly displays: `❌ Access restricted.` without disclosing administrator identity.
   - **Show / Hide Password Toggle**:
     - Interactive eye toggle (`👁️` / `🙈`) added to all password and PIN fields across `admin.html`, the Student Sign-In modal, and the Account Creation / UPI payment modal.
   - **Dedicated Logout Flow**:
     - Added an explicit `🚪 Logout` button in the top navbar next to the user name pill.
     - Clicking Logout immediately destroys active session credentials, clears Pro status from `localStorage`, and instantly reverts the entire website to the non-pro visitor state.
   - **Stage-Wise Grand Mocks & Live Stage 2 Assessment Drive Toggle**:
     - Added dedicated Stage-Wise Grand Mocks for each stage (`gm_s1`, `gm_s2a`, `gm_s2b`, `gm_s3`, `gm_s4`, `gm_s56`).
     - Added an interactive candidate mode switcher in `#grand-mocks`:
       - `⚡ Mode A (Recommended)`: Skips Stage 1 English Communication and focuses strictly on Stages 2A, 2B, 3, 4, 5/6 for the currently live assessment drive.
       - `🌐 Mode B`: Includes Stage 1 English Communication for the full 6-stage recruitment marathon.
   - **Vercel Deployment Pipeline**:
     - Configured `vercel.json` with clean URLs, route rewrites, and security headers.
     - Login authentication pipeline active via Vercel CLI OAuth device flow.

```
C:\cap\ai\
├── index.html                   ← Main dashboard with 10+ tests/stage, CSP, Sign In modal, Pro modal, Quiz runner
├── admin.html                   ← Executive Admin Portal with PIN auth, Orders Ledger, VIP Free Pass Manager & UPI Setup
├── README.md                    ← Architecture, syllabus map, payment docs & continuity guidelines
├── PROGRESS.md                  ← Complete session tracker & state log (this file)
├── css\
│   └── style.css                ← Modern UI styles, Pro badges, payment modal, security toasts
├── js\
│   ├── app.js                   ← 76 tests, 14 banks (350+ Qs), dynamic generator, accounts engine, VIP whitelist & payment
│   └── study_docs.js            ← 33 Textbook-Grade In-Depth Chapters across all 6 stages (94.8 KB)
├── data\
│   └── questions.json           ← Complete master question repository
└── modules\
    ├── study_reader.html        ← Protected In-Browser PDF Master Reader (Non-Downloadable)
    ├── ai_coding_sim.html       ← Stage 3 AI-Assisted Coding Simulator (Lab 27 Replica)
    ├── debug_sim.html           ← Stage 2B Debugging Assessment Simulator (Trees, Graphs, 2D DP)
    └── interview_hub.html       ← Stages 4, 5 & 6 Master Hub (Cognitive, Tech Interview, HR 7 Core Values)
```

---

## 🧭 Continuity Guidelines for Future Sessions

- **Always inspect `C:\cap\ai\` first** before making changes.
- **Keep all files within `C:\cap\ai\`**.
- **All code is standalone HTML/CSS/JS** with zero dependencies — runs directly in any browser.
- **Update `README.md` and `PROGRESS.md`** whenever new updates are made.


