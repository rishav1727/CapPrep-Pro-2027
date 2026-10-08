# CapPrep Pro — Capgemini Exceller 2027 Preparation Platform
**Central Context & Project State Log**

> ⚠️ **AGENT PERSISTENCE NOTICE**: Whenever resuming this task or continuing from a new conversation/session, read this file (`C:\cap\ai\README.md`) and `C:\cap\ai\PROGRESS.md` first. Everything done and current patterns are documented here.

---

## 📌 Project Overview
A complete, self-contained, standalone web-based recruitment preparation platform tailored precisely to the **Capgemini Exceller 2027 hiring pattern (observed across live tests / Tech6Sense pattern)**.

- **Root Directory**: `C:\cap\ai\`
- **Zero External Dependencies**: Pure HTML, CSS, Vanilla JS — runs instantly by opening `index.html` in any browser.

---

## 🗂️ Complete Directory & File Manifest

```
C:\cap\ai\
├── index.html                   ← Main dashboard: 10+ tests in every stage, diagrams, prompt masterclass & grand mocks
├── README.md                    ← Architecture, syllabus map & continuity guidelines (this file)
├── PROGRESS.md                  ← Step-by-step state tracker & session log
├── css\
│   └── style.css                ← Modern dark tech UI styles, responsive grid, quiz & diagram styles
├── js\
│   └── app.js                   ← 76 unique test configurations across 14 question banks, timer & auto-grader
├── data\
│   └── questions.json           ← Complete master question repository
└── modules\
    ├── study_reader.html        ← Protected In-Browser PDF Master Reader (Non-Downloadable, All 6 Stages)
    ├── ai_coding_sim.html       ← Interactive replica of Stage 3 (AI-Assisted Coding Assessment / Lab 27)
    ├── debug_sim.html           ← Interactive replica of Stage 2B (Debugging Assessment in C/C++/Java)
    └── interview_hub.html       ← Stages 4, 5 & 6 Master Hub (Cognitive, Tech Interview, HR 7 Core Values)
```

---

## 🏆 Official 6-Stage Exam Pattern (10+ Tests Per Stage)

| Stage | Round Name | Duration | Study Material & Visuals Included | Dedicated Stage Tests |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1** | **English Communication** | ~30 mins | AI Speech Scoring pipeline, grammar rules, active/passive voice | **10 Tests** (`vb_1` to `vb_10`) |
| **Stage 2A**| **Technical Module** | ~40–50 mins | RAG Vector pipeline, GenAI vs Discriminative, Bitwise shift visualizer, BST diagrams, 7-Layer OSI stack | **16 Tests** (`ai_1-3`, `ps_1-3`, `dsa_1-3`, `db_1-2`, `oop_1`, `os_1`, `cn_1`, `dv_1`, `apt_1`) |
| **Stage 2B**| **Debugging Assessment** | ~20 mins | 4-step debugging workflow, Top 3 bug archetypes (Trees, Graphs, 2D DP) + **Interactive Simulator** | **10 Tests** (`dbg_1` to `dbg_10`) + Live Simulator |
| **Stage 3** | **AI-Assisted Coding** | ~45 mins | 5-part prompt anatomy, **❌ Bad vs ✅ Master 10/10 Prompt comparison**, iterative prompting | **10 Tests** (`aic_1` to `aic_10`) + Live Simulator |
| **Stage 4** | **Cognitive Assessment** | ~20–30 mins | Motion & Grid challenge strategies, ADEPT-15 behavioral profile | **10 Tests** (`sit_1` to `sit_10`) |
| **Stages 5 & 6**| **Technical & HR Interviews** | 20–35 mins | System Architecture defense frameworks, trade-offs, Capgemini 7 Core Values STAR builder | **10 Tests** (`int_1` to `int_10`) + Interview Hub |

> **Grand Mock Marathon Suite (End of Page)**: **10 Grand Full-Length Tests** (`full_1` to `full_6`, `combo_1` to `combo_4`) combining all stages in one sitting.

---

## 💳 Payment Architecture, Free Trial Policy & Pro Pass System

- **Free Trial Policy (2 Free Tests Per Stage)**:
  - Every recruitment stage includes **2 free trial tests** (`vb_1-2`, `ai_1-2`, `dbg_1-2`, `aic_1-2`, `sit_1-2`, `int_1-2`, `full_1-2`) marked with a glowing **`🟢 FREE TRIAL`** badge.
  - All remaining tests (Tests 3 through 10+) are marked with a prominent crimson **`🔒 LOCKED`** badge.
  - Clicking any locked test opens the `#locked-test-modal` prompting enrollment for ₹51 or Sign In with an active account.
- **High-Converting Psychological Pricing Model (₹299 ➔ ₹51)**:
  - List price: <del>₹299</del>. Auto-applied welcome coupon `SUPER51` slashes the price to **₹51** (83% OFF / Save ₹248).
  - Ticking urgency countdown timer (14:59) and live social proof toasts across Indian engineering campuses.
- **Direct Indian UPI Integration (0% Fee / 100% Profit)**:
  - Integrated UPI ID: **`rishavofficials1727-7@okaxis`** (Axis Bank).
  - Direct dynamic QR code generator with fixed amount (₹51) locked and 1-tap mobile payment app intents (Google Pay, PhonePe, Paytm, BHIM).
  - Students enter 12-digit UTR reference upon completion; admin verifies in `admin.html`.
- **Student Accounts & Dedicated Logout Flow**:
  - Enrollment requires Name, Email, Password (min 6 characters), Phone, and UTR.
  - Students can sign back in anytime via the `#signin-modal` to restore Pro access across devices.
  - Top navbar features a dedicated **`🚪 Logout`** button that immediately revokes session access and restores the non-pro visitor view.
- **Show / Hide Password Toggle**:
  - Interactive eye toggles (`👁️` / `🙈`) on all PIN and password fields.

---

## 🎯 Grand Mock Marathons & Live Stage 2 Assessment Drive Selector

- **Stage-Wise Grand Mocks**: Dedicated comprehensive exams for each stage (`gm_s1` to `gm_s56`).
- **Live Assessment Drive Selector**:
  - **`⚡ Mode A (Recommended)`**: Focuses on **Stages 2A + 2B + 3 + 4 + 5/6** (skipping Stage 1 English Communication since Stage 2 is currently live).
  - **`🌐 Mode B`**: Includes **Stage 1 English Communication** + Stages 2A to 6 for the full 6-stage marathon.

---

## 🛡️ Security, Privacy & Admin Protection

- **Zero Public Admin Exposure**: Admin navigation button is dynamically hidden and only revealed when the registered admin (`rishavofficials1727@gmail.com` or `rishav.gupta0527@gmail.com`) signs in. Secret hotkey: `Ctrl + Shift + A`.
- **Admin Portal Security (`admin.html`)**:
  - Access restricted via SHA-256 cryptographic hash (`rishav0527`). No default passwords displayed.
  - Brute-force protection: 3 failed attempts triggers an automated 10-minute lockout.
  - Generic error message: `❌ Access restricted.` without disclosing administrator identity.
- **Anti-Tamper Proctoring**: Tab-switch detection, right-click and text copy prevention, and developer shortcut blocking (`F12`, `Ctrl+Shift+I`, `Ctrl+Shift+J`, `Ctrl+U`).
- **Multi-Language Coding Switcher**: Real-time syntax switcher between **`C++`**, **`Java`**, **`Python`**, and **`C`** on all programming and pseudocode questions.
- **Deployment Ready**: Fully configured for Vercel via `vercel.json` and compatible with Netlify/Cloudflare.

