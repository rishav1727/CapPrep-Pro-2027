# -*- coding: utf-8 -*-
"""
Builder script to generate C:\cap\ai\js\study_docs.js
Contains complete, comprehensive, textbook-grade study notes across all stages:
- Stage 1: English & AI Spoken Communication Guide (5 Chapters)
- Stage 2A: Technical Assessment & CS Compendium (7 Chapters)
- Stage 2B: Algorithmic Debugging Master Handbook (5 Chapters)
- Stage 3: Lab 27 AI Coding & Prompt Engineering Manual (5 Chapters)
- Stage 4: Cognitive Games & ADEPT-15 Behavioral Dossier (5 Chapters)
- Stages 5-6: Tech & HR Interview Defense Playbook (6 Chapters)
Total: 33 Deep, In-Depth Chapters with diagrams, step-by-step walkthroughs, trace tables, formulas, and real Capgemini questions.
"""

import json

def build_docs():
    # We will build dictionary in Python, then write as valid JavaScript export
    docs = {}

    # =========================================================================
    # STAGE 1: ENGLISH COMMUNICATION & AI SPOKEN SUITE (5 Chapters)
    # =========================================================================
    docs["stage1"] = {
        "title": "Stage 1: English & AI Spoken Communication Guide",
        "sections": [
            {
                "id": "s1_ai_speech_deep",
                "title": "Chapter 1: The AI Speech Scoring Engine & Acoustic Assessment",
                "content": """
<h1>🎙️ Chapter 1: The AI Speech Scoring Engine & Acoustic Assessment</h1>
<p>Stage 1 of the Capgemini recruitment assessment uses an automated, neural-network-driven Automated Speech Recognition (ASR) engine (powered by CoCubes/Versant frameworks). Understanding how acoustic signals are analyzed is critical to maximizing your score.</p>

<div class="pdf-callout tip">
  <strong>Key Realization:</strong> The scoring engine does <strong>NOT</strong> favor fake British or American accents. It evaluates <strong>Phonetic Alignment</strong> (crisp articulation of consonants and vowels) and <strong>Acoustic Rhythm</strong> (steady word pacing without unnatural mid-sentence pauses).
</div>

<h2>1.1 The 4 Computational Scoring Dimensions</h2>
<table class="pdf-table">
  <tr>
    <th>Dimension</th>
    <th>Weight</th>
    <th>Algorithmic Measurement Metrics</th>
    <th>High-Score Target</th>
  </tr>
  <tr>
    <td><strong>Fluency & Cadence</strong></td>
    <td>35%</td>
    <td>Words Per Minute (WPM), inter-word silence distribution, hesitation frequency, syllable duration variance.</td>
    <td><strong>110 – 140 WPM</strong> with zero pauses exceeding 2.5 seconds.</td>
  </tr>
  <tr>
    <td><strong>Acoustic Pronunciation</strong></td>
    <td>25%</td>
    <td>Phoneme-level acoustic model matching against standard International Phonetic Alphabet (IPA) benchmarks.</td>
    <td>&gt;85% phoneme accuracy; crisp delivery of plosives (/p/, /b/, /t/, /d/) and fricatives (/s/, /z/, /th/).</td>
  </tr>
  <tr>
    <td><strong>Grammatical Integrity</strong></td>
    <td>25%</td>
    <td>Syntactic parsing of transcribed text, subject-verb agreement, tense consistency, auxiliary verbs.</td>
    <td>Zero structural subject-verb or past-tense sequence violations.</td>
  </tr>
  <tr>
    <td><strong>Vocabulary & Semantics</strong></td>
    <td>15%</td>
    <td>Lexical diversity index (Type-Token Ratio), contextual relevance, avoiding filler crutches.</td>
    <td>Zero filler words ("umm", "uhh", "you know", "like") and high contextual relevance.</td>
  </tr>
</table>

<h2>1.2 The Acoustic Spectrogram: How Pauses are Scored</h2>
<p>The ASR engine converts your microphone input into an acoustic spectrogram. Pauses are categorized as follows:</p>
<div class="code-block">
[Spoken Word Chunk 1] ─── (0.3s Natural Breath) ─── [Spoken Word Chunk 2]  --> PASS (Natural Fluency)
[Spoken Word Chunk 1] ─── (2.8s Dead Silence) ───── [Spoken Word Chunk 2]  --> PENALTY (Fluency Drop -20%)
[Spoken Word Chunk 1] ─── ("Ummm... Ahhh...") ─────── [Spoken Word Chunk 2]  --> SEVERE PENALTY (Acoustic Noise)
</div>

<h2>1.3 Microphone Placement & Room Calibration</h2>
<ul>
  <li><strong>Collar/Headset Distance:</strong> Position the mic <strong>2 fingers (approx 3 cm)</strong> to the side of your mouth. Never speak directly into the capsule to avoid plosive breath pops ("pop" on 'p' and 'b').</li>
  <li><strong>Input Gain Level:</strong> Set your OS microphone volume to <strong>75% – 80%</strong>. Setting it to 100% causes digital clipping/distortion that confuses the acoustic model.</li>
  <li><strong>Background Noise Gate:</strong> Ensure a room with &lt;40dB ambient noise. Fan noise or keyboard tapping creates high-frequency noise floor spikes.</li>
</ul>
"""
            },
            {
                "id": "s1_grammar_mastery",
                "title": "Chapter 2: The 20 Golden Grammar Rules Tested in Capgemini",
                "content": """
<h1>📐 Chapter 2: The 20 Golden Grammar Rules Tested in Capgemini</h1>
<p>Capgemini's written English section focuses heavily on error spotting, sentence correction, and fill-in-the-blanks. Master these 20 non-negotiable rules.</p>

<h2>Rule 1: Subject-Verb Agreement with Prepositional Distractors</h2>
<div class="pdf-callout info">
  The verb agrees with the true subject, <strong>never</strong> with the intervening prepositional phrase.
</div>
<div class="code-block">
❌ Incorrect: The quality of these mangoes are exceptional.
✔️ Correct:   The quality [of these mangoes] IS exceptional. (Subject is singular 'quality')

❌ Incorrect: A bouquet of yellow roses were presented to the CEO.
✔️ Correct:   A bouquet [of yellow roses] WAS presented to the CEO.
</div>

<h2>Rule 2: Correlative Conjunction Parallelism</h2>
<p>Structures linked by <em>Either... or</em>, <em>Neither... nor</em>, and <em>Not only... but also</em> must balance identical grammatical parts of speech.</p>
<div class="code-block">
❌ Incorrect: He not only lost his ticket, but also his wallet.
✔️ Correct:   He lost NOT ONLY his ticket, BUT ALSO his wallet. (Balanced noun phrases)

Rule for Verb Agreement:
When subjects differ in number or person, the verb agrees with the CLOSER subject:
✔️ Correct: Neither the manager nor the ENGINEERS WERE present.
✔️ Correct: Neither the engineers nor the MANAGER WAS present.
</div>

<h2>Rule 3: Conditional Clauses (If-Condition Sequence of Tenses)</h2>
<table class="pdf-table">
  <tr>
    <th>Conditional Type</th>
    <th>'If' Clause Tense</th>
    <th>Main Clause Verb</th>
    <th>Example</th>
  </tr>
  <tr>
    <td><strong>Type 0 (Universal Truth)</strong></td>
    <td>Simple Present</td>
    <td>Simple Present</td>
    <td>If water <em>reaches</em> 100°C, it <em>boils</em>.</td>
  </tr>
  <tr>
    <td><strong>Type 1 (Real Future)</strong></td>
    <td>Simple Present</td>
    <td>Will / Can + Base Verb</td>
    <td>If she <em>studies</em> diligently, she <em>will clear</em> the exam.</td>
  </tr>
  <tr>
    <td><strong>Type 2 (Hypothetical Present)</strong></td>
    <td>Simple Past (were)</td>
    <td>Would / Could + Base Verb</td>
    <td>If I <em>were</em> the CEO, I <em>would invest</em> in cloud R&D.</td>
  </tr>
  <tr>
    <td><strong>Type 3 (Unreal Past)</strong></td>
    <td>Past Perfect (had + V3)</td>
    <td>Would have + V3</td>
    <td>If they <em>had deployed</em> the patch, the server <em>would not have crashed</em>.</td>
  </tr>
</table>

<h2>Rule 4: Negative Adverb Inversion</h2>
<p>When a sentence begins with negative or restrictive adverbs (<em>Hardly, Scarcely, Seldom, Rarely, Barely, No sooner</em>), the auxiliary verb precedes the subject.</p>
<div class="code-block">
❌ Incorrect: Hardly I had reached the station when the train left.
✔️ Correct:   Hardly HAD I REACHED the station WHEN the train left.

Note on Pairings:
- Hardly / Scarcely / Barely  ────► Paired with: WHEN
- No sooner                   ────► Paired with: THAN
✔️ Correct: No sooner HAD the bell RUNG THAN the students entered.
</div>

<h2>Rule 5: Subjunctive Mood for Demands & Recommendations</h2>
<p>Verbs such as <em>demand, insist, recommend, propose, suggest</em> require the subjunctive mood (base form of verb without 's' or 'es' or 'should').</p>
<div class="code-block">
❌ Incorrect: The architect recommended that the database runs on SSDs.
✔️ Correct:   The architect recommended that the database RUN on SSDs.

❌ Incorrect: The manager insisted that he is present.
✔️ Correct:   The manager insisted that he BE present.
</div>

<h2>Rule 6: Dangling and Misplaced Modifiers</h2>
<p>A participial phrase at the start of a sentence must describe the subject immediately following the comma.</p>
<div class="code-block">
❌ Incorrect: Walking through the server room, the cold air chilled Rahul.
             (Was the cold air walking through the room? No!)
✔️ Correct:   Walking through the server room, RAHUL was chilled by the cold air.
</div>

<h2>Rule 7: One of the [Plural Noun] Who [Plural Verb]</h2>
<div class="code-block">
Case A (Relative Pronoun 'who/which/that'):
✔️ Correct: He is ONE OF THOSE ENGINEERS who ARE constantly innovating.
            ('who' refers to plural 'engineers', hence plural verb 'are')

Case B (Preceded by 'Only'):
✔️ Correct: He is THE ONLY ONE of those engineers who IS certified in Kubernetes.
            ('the only one' isolates singular subject, hence singular verb 'is')
</div>
"""
            },
            {
                "id": "s1_parajumbles_framework",
                "title": "Chapter 3: The 4-Step Para-Jumble Decryption Algorithm",
                "content": """
<h1>🧩 Chapter 3: The 4-Step Para-Jumble Decryption Algorithm</h1>
<p>Para-Jumbles (Sentence Rearrangement) are among the highest-weighted verbal reasoning questions in Capgemini. Use this systematic elimination algorithm rather than trying to read all possible permutations.</p>

<h2>3.1 The 4-Step Algorithmic Process</h2>
<div class="code-block">
Step 1: Identify the Standalone Opening Sentence (Independent Subject)
        ├── Rule: Cannot begin with pronouns (he, she, they, it), transitions (however, therefore), or acronyms without prior expansion.
        └── Must introduce the overarching theme or core noun.

Step 2: Detect Invariable Mandatory Pairs (2-Sentence Atomic Links)
        ├── Chronological sequence (Dates, Past -> Present -> Future).
        ├── Noun -> Pronoun relationship (e.g. "Capgemini SE" -> "The enterprise").
        ├── Cause -> Effect link (e.g. "Network failure occurred" -> "Consequently, transactions stalled").
        └── Acronym definition -> Abbreviation (e.g. "Artificial Intelligence (AI)" -> "AI algorithms").

Step 3: Leverage Transition Signals
        ├── Contrast pairs: Although, However, On the contrary, Yet, Conversely.
        ├── Additive pairs: Furthermore, In addition, Moreover, Besides.
        └── Conclusive pairs: Therefore, Hence, Thus, In summary, Ultimately.

Step 4: Cross-Reference Option Pairs to Eliminate 75% of Choices
        └── If [B-D] is a mandatory pair, eliminate any option where B is not immediately followed by D.
</div>

<h2>3.2 Fully Worked Exam Example with Step-by-Step Deduction</h2>
<p><strong>Sentences:</strong></p>
<ul>
  <li><strong>A:</strong> This exponential surge in data generation necessitates distributed computing clusters.</li>
  <li><strong>B:</strong> Today, IoT sensors and edge devices record billions of telemetry data points every second.</li>
  <li><strong>C:</strong> Consequently, enterprise architectures are migrating from monolithic servers to cloud-native microservices.</li>
  <li><strong>D:</strong> Without such distributed infrastructures, analytics pipelines suffer catastrophic latency bottlenecks.</li>
</ul>

<p><strong>Step-by-Step Deduction:</strong></p>
<ol>
  <li><strong>Find the Opener:</strong>
    <ul>
      <li>Sentence A begins with demonstrative pronoun <em>"This exponential surge"</em> (needs prior antecedent).</li>
      <li>Sentence C begins with transition <em>"Consequently"</em> (needs prior cause).</li>
      <li>Sentence D begins with <em>"Without such distributed infrastructures"</em> (needs prior mention of infrastructure).</li>
      <li>Sentence B introduces the independent subject: <em>"IoT sensors and edge devices record billions..."</em>. <strong>Opener = B.</strong></li>
    </ul>
  </li>
  <li><strong>Form Mandatory Pair 1:</strong>
    <ul>
      <li>Sentence B mentions <em>"billions of telemetry data points"</em>. Sentence A refers to <em>"This exponential surge in data generation"</em>. Therefore, <strong>B ➔ A is an unbreakable pair</strong>.</li>
    </ul>
  </li>
  <li><strong>Form Mandatory Pair 2:</strong>
    <ul>
      <li>Sentence A introduces <em>"distributed computing clusters"</em>. Sentence D explains what happens <em>"Without such distributed infrastructures"</em>. Therefore, <strong>A ➔ D is an unbreakable pair</strong>.</li>
    </ul>
  </li>
  <li><strong>Verify Conclusion:</strong>
    <ul>
      <li>Sentence C provides the ultimate strategic consequence: <em>"Consequently, enterprise architectures are migrating..."</em>. <strong>Final sequence = B ➔ A ➔ D ➔ C.</strong></li>
    </ul>
  </li>
</ol>
"""
            },
            {
                "id": "s1_vocabulary_idioms",
                "title": "Chapter 4: 50 High-Frequency Enterprise Words & Idioms",
                "content": """
<h1>📚 Chapter 4: 50 High-Frequency Enterprise Words & Idioms</h1>
<p>Master these 50 curated high-frequency corporate, technical, and analytical vocabulary words and business idioms frequently encountered in Capgemini tests and reading passages.</p>

<h2>4.1 Core Corporate & Analytical Vocabulary</h2>
<table class="pdf-table">
  <tr>
    <th>Word</th>
    <th>Part of Speech</th>
    <th>Precise Definition</th>
    <th>Exam Context / Usage</th>
  </tr>
  <tr>
    <td><strong>Pragmatic</strong></td>
    <td>Adjective</td>
    <td>Dealing with problems in a sensible, practical way rather than following theoretical ideals.</td>
    <td>"The team took a <em>pragmatic</em> approach by refactoring legacy modules incrementally."</td>
  </tr>
  <tr>
    <td><strong>Ubiquitous</strong></td>
    <td>Adjective</td>
    <td>Present, appearing, or found everywhere simultaneously.</td>
    <td>"Smartphones and cloud APIs have become <em>ubiquitous</em> in modern commerce."</td>
  </tr>
  <tr>
    <td><strong>Ephemeral</strong></td>
    <td>Adjective</td>
    <td>Lasting for a very short duration; transitory.</td>
    <td>"Serverless container instances are <em>ephemeral</em>, spinning down after execution."</td>
  </tr>
  <tr>
    <td><strong>Cognizant</strong></td>
    <td>Adjective</td>
    <td>Having conscious awareness, knowledge, or mindfulness of something.</td>
    <td>"Engineers must remain <em>cognizant</em> of memory leak hazards when working with pointers."</td>
  </tr>
  <tr>
    <td><strong>Mitigate</strong></td>
    <td>Verb</td>
    <td>To make something bad or dangerous less severe, serious, or painful.</td>
    <td>"Database sharding was implemented to <em>mitigate</em> query latency during flash sales."</td>
  </tr>
  <tr>
    <td><strong>Disparate</strong></td>
    <td>Adjective</td>
    <td>Essentially different in kind; not allowing comparison; distinct.</td>
    <td>"The ETL pipeline harmonized data from five <em>disparate</em> legacy systems."</td>
  </tr>
  <tr>
    <td><strong>Redundant</strong></td>
    <td>Adjective</td>
    <td>Not needed or useful; superfluous; exceeding what is natural or necessary.</td>
    <td>"Automated CI/CD pipelines eliminated <em>redundant</em> manual deployment checklists."</td>
  </tr>
  <tr>
    <td><strong>Scrutinize</strong></td>
    <td>Verb</td>
    <td>To examine or inspect something closely and thoroughly.</td>
    <td>"Security architects rigorously <em>scrutinized</em> the third-party dependencies."</td>
  </tr>
  <tr>
    <td><strong>Paradigm</strong></td>
    <td>Noun</td>
    <td>A typical example, pattern, or model of something.</td>
    <td>"Object-Oriented Programming represented a major shift from the procedural <em>paradigm</em>."</td>
  </tr>
  <tr>
    <td><strong>Concurrently</strong></td>
    <td>Adverb</td>
    <td>Occurring or operating simultaneously at the exact same time.</td>
    <td>"The distributed broker processes multiple consumer topics <em>concurrently</em>."</td>
  </tr>
</table>

<h2>4.2 High-Scoring Business Idioms for Speaking & Verbal</h2>
<table class="pdf-table">
  <tr>
    <th>Business Idiom</th>
    <th>Meaning</th>
    <th>Professional Example</th>
  </tr>
  <tr>
    <td><strong>Touch base</strong></td>
    <td>Briefly make contact or reconnect to review progress.</td>
    <td>"Let's <em>touch base</em> on Friday to verify sprint milestones."</td>
  </tr>
  <tr>
    <td><strong>Hit the ground running</strong></td>
    <td>Start a new endeavor immediately with full energy and competence.</td>
    <td>"With prior Docker training, the fresher <em>hit the ground running</em> in DevOps."</td>
  </tr>
  <tr>
    <td><strong>Ballpark figure</strong></td>
    <td>A rough, approximate estimate.</td>
    <td>"The architect gave a <em>ballpark figure</em> of 200 milliseconds for endpoint response."</td>
  </tr>
  <tr>
    <td><strong>Think outside the box</strong></td>
    <td>Approach a problem with unconventional, innovative thinking.</td>
    <td>"Rather than adding more hardware, the team <em>thought outside the box</em> and optimized SQL indexes."</td>
  </tr>
  <tr>
    <td><strong>On the same page</strong></td>
    <td>Having a shared understanding and agreement.</td>
    <td>"The standup meeting ensured developers and QA were <em>on the same page</em>."</td>
  </tr>
</table>
"""
            },
            {
                "id": "s1_spoken_survival_drills",
                "title": "Chapter 5: Spoken Test Drills: Repeat Sentences, Retellings & Extempore",
                "content": """
<h1>🗣️ Chapter 5: Spoken Test Mastery & Drills: Repeat Sentences, Retellings & Extempore</h1>
<p>The AI Spoken Assessment measures real-time acoustic delivery. Here is how to conquer every section with proven templates and short-term memory techniques.</p>

<h2>5.1 Section A: Repeat Sentences (16 Items)</h2>
<p><strong>The Challenge:</strong> You hear an audio sentence once (8–14 words) and must repeat it immediately upon the beep. Human short-term memory degrades after 7 items unless organized into chunks.</p>

<div class="pdf-callout tip">
  <strong>The 3-Chunk Auditory Memorization Technique:</strong>
  Divide the sentence into 3 mental buckets as you hear it:
  <ol>
    <li><strong>Subject Chunk:</strong> Who or what is acting? (<em>"The senior software engineer"</em>)</li>
    <li><strong>Action Chunk:</strong> What did they do? (<em>"deployed the microservices patch"</em>)</li>
    <li><strong>Context Chunk:</strong> When, where, or why? (<em>"before the scheduled downtime."</em>)</li>
  </ol>
</div>

<div class="code-block">
GOLDEN RULE FOR REPEAT SENTENCES:
If you forget 1 or 2 words, NEVER stop speaking! NEVER say "sorry" or "umm"!
The AI scores FLUENCY (35%) higher than vocabulary.
Maintain an uninterrupted, confident cadence:
Heard:  "All candidates must submit their project files before five PM on Friday."
Spoken: "All candidates must submit their files before five PM on Friday."  --> 92% Score!
Silence: "All candidates... umm... wait... submit..."                   --> 30% Score!
</div>

<h2>5.2 Section B: Story Retelling (3 Items)</h2>
<p>You hear a short narrative (approx 45 seconds). After a 10-second chime, you have 30 seconds to summarize the story. Use this foolproof 3-Sentence Retelling Architecture:</p>

<div class="code-block">
THE 3-SENTENCE RETELLING ARCHITECTURE:
Sentence 1 (Character & Setting):
"The story revolves around [Character Name/Role] who was trying to [Primary Goal]."

Sentence 2 (Conflict / Obstacle):
"However, a sudden challenge arose when [Unexpected Problem/Complication occurred]."

Sentence 3 (Resolution & Outcome):
"Ultimately, [Character] overcame this obstacle by [Action taken], leading to [Positive Resolution]."
</div>

<h3>Worked Practice Story:</h3>
<p><strong>Audio Story:</strong> <em>"Anita was leading a software demonstration for a major healthcare client. Ten minutes before the presentation, the cloud server lost connection due to a datacenter outage. Instead of canceling, Anita switched to an offline cached demo environment she had prepared the night before. The client was thoroughly impressed by her preparedness and signed the contract."</em></p>
<p><strong>Your 30-Second Spoken Response:</strong></p>
<div class="code-block">
"The story describes Anita, who was preparing an important software demonstration for a healthcare client.
However, an unexpected datacenter outage caused the cloud connection to drop just before the meeting.
Anita resolved the crisis by switching to her pre-configured offline backup environment, which thoroughly impressed the client and secured the deal."
</div>

<h2>5.3 Section C: Spoken Extempore / Topic Speaking (1 Minute)</h2>
<p>You are given a topic (e.g. <em>"Should companies allow permanent remote work?"</em>) and 30 seconds to prepare, followed by 60 seconds to speak. Use the <strong>PEP (Point - Explanation - Proof) Blueprint</strong>.</p>

<div class="code-block">
THE PEP BLUEPRINT (60-SECOND PACING):
00s - 15s | POINT (P):
"I firmly believe that [State your clear stance], as it provides significant advantages for both [Entity A] and [Entity B]."

15s - 40s | EXPLANATION (E):
"The primary reason is that [Explain Reason 1, e.g. productivity, cost, flexibility]. Furthermore, [Explain Reason 2, e.g. access to global talent pools, work-life balance]."

40s - 55s | PROOF / PERSPECTIVE (P):
"For instance, leading technology firms like Capgemini have demonstrated that hybrid collaborative models improve employee retention while sustaining enterprise delivery quality."

55s - 60s | CONCLUSION:
"Therefore, adopting balanced remote work frameworks represents the future of sustainable enterprise operations."
</div>

<h2>5.4 The Indian English Phonetic Correction Checklist</h2>
<ul>
  <li><strong>V vs W:</strong> Avoid pronouncing 'V' and 'W' identically. For <strong>/v/</strong> (<em>vector, verify</em>), your upper teeth must touch your lower lip. For <strong>/w/</strong> (<em>window, work</em>), your lips form a round circle without teeth contact.</li>
  <li><strong>S-Clusters:</strong> Do not insert an initial vowel before 's' (e.g., say <em>"school"</em>, NOT <em>"is-school"</em>; say <em>"special"</em>, NOT <em>"is-peshal"</em>).</li>
  <li><strong>Past-Tense '-ed' endings:</strong> Do not drop past-tense consonants. Say <em>"develop-t"</em> (developed), <em>"connect-id"</em> (connected), <em>"concur-d"</em> (concurred).</li>
</ul>
"""
            }
        ]
    }

    # =========================================================================
    # STAGE 2A: TECHNICAL ASSESSMENT & CS COMPENDIUM (7 Chapters)
    # =========================================================================
    docs["stage2a"] = {
        "title": "Stage 2A: Technical Assessment & CS Compendium",
        "sections": [
            {
                "id": "s2a_transformers_rag",
                "title": "Chapter 1: AI Literacy, Transformers & Generative Architecture",
                "content": """
<h1>🤖 Chapter 1: AI Literacy, Transformers & Generative Architecture</h1>
<p>In the Exceller 2026-2027 recruitment pattern, Capgemini evaluates AI Literacy. You must understand how modern Large Language Models (LLMs), Transformers, and Retrieval-Augmented Generation (RAG) work under the hood.</p>

<h2>1.1 The Transformer Architecture: Self-Attention Mechanics</h2>
<p>Prior to the 2017 paper <em>"Attention Is All You Need"</em>, recurrent networks (RNNs/LSTMs) processed text sequentially, leading to vanishing gradients and inability to parallelize training. The Transformer replaces recurrence entirely with <strong>Scaled Dot-Product Self-Attention</strong>.</p>

<div class="code-block">
Attention Formula:
Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V

Where:
- Q (Query):  What the current token is seeking (Matrix of dimensions N x d_k)
- K (Key):    What the other tokens advertise/represent (Matrix of dimensions N x d_k)
- V (Value):  The semantic information content of tokens (Matrix of dimensions N x d_v)
- sqrt(d_k):  Scaling factor preventing extreme dot products from driving softmax into regions with near-zero gradients.
</div>

<h2>1.2 Multi-Head Attention</h2>
<div class="code-block">
Input Token Embeddings
         │
    ┌────┴────────────────────────┬────────────────────────┐
    ▼                             ▼                        ▼
Head 1: (Q1, K1, V1)         Head 2: (Q2, K2, V2)     Head h: (Qh, Kh, Vh)
(Syntax / Grammar)           (Factual Associations)   (Long-Range Context)
    │                             │                        │
    └────┬────────────────────────┴────────────────────────┘
         ▼
Concatenate Heads ──► Linear Projection (W_o) ──► Output Representation
</div>

<h2>1.3 Retrieval-Augmented Generation (RAG) 5-Step Pipeline</h2>
<p>LLMs suffer from hallucinations and outdated training cutoff dates. RAG connects the LLM dynamically to enterprise knowledge stores:</p>
<ol>
  <li><strong>Document Ingestion & Chunking:</strong> PDF/Text documents are split into semantic chunks (e.g. 500 tokens with 50-token overlap).</li>
  <li><strong>Embedding Generation:</strong> Chunks are converted to dense floating-point vector arrays (e.g. 1536 dimensions using text-embedding-3-small).</li>
  <li><strong>Vector Database Storage:</strong> Vectors are indexed in vector databases (Pinecone, Milvus, Qdrant) using HNSW (Hierarchical Navigable Small World) graphs for rapid cosine similarity search.</li>
  <li><strong>Contextual Retrieval:</strong> When a user queries, the query is embedded, top-$k$ nearest chunks are retrieved.</li>
  <li><strong>Augmented Generation:</strong> The original user query + retrieved context chunks are combined into a system prompt for the LLM to generate grounded, cited answers.</li>
</ol>
"""
            },
            {
                "id": "s2a_pseudocode_math",
                "title": "Chapter 2: Pseudocode Traps & Bitwise Optimization Mathematics",
                "content": """
<h1>⚡ Chapter 2: Pseudocode Traps & Bitwise Optimization Mathematics</h1>
<p>Capgemini pseudocode questions test your ability to trace bit manipulation, short-circuit logic, and pointer operations under timed pressure.</p>

<h2>2.1 The Essential Bitwise Truth Table</h2>
<table class="pdf-table">
  <tr>
    <th>A</th>
    <th>B</th>
    <th>AND (A & B)</th>
    <th>OR (A | B)</th>
    <th>XOR (A ^ B)</th>
    <th>NOT (~A) [Assuming 8-bit Signed]</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>-1 (Inverts all bits, two's complement)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>-2</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>-1</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>-2</td>
  </tr>
</table>

<h2>2.2 The 5 Bitwise Mathematical Super-Tricks</h2>
<div class="code-block">
1. Check if a number N is a Power of 2:
   Formula: (N > 0) && ((N & (N - 1)) == 0)
   Why: Powers of 2 have exactly one set bit (e.g., 8 is 1000). (8 - 1) is 7 (0111).
        1000 & 0111 = 0000.

2. Clear the Lowest Set Bit (Brian Kernighan's Algorithm):
   Formula: N = N & (N - 1)
   Application: Counts total number of set bits in O(set bits) time rather than O(total bits).

3. Isolate the Lowest Set Bit:
   Formula: lowest_bit = N & (-N)
   Why: In two's complement, -N = (~N) + 1. All bits to the left invert, isolating the rightmost 1.

4. Fast In-Place Swap Without Temporary Variables:
   a = a ^ b;
   b = a ^ b;  // (a ^ b) ^ b = a
   a = a ^ b;  // (a ^ b) ^ a = b

5. Find the Only Non-Repeating Element in an Array (Where every other element appears twice):
   Formula: XOR all elements together. Identical numbers cancel out to 0 (x ^ x = 0), leaving only the unique value.
</div>

<h2>2.3 Shift Operators: Arithmetic vs Logical</h2>
<ul>
  <li><strong>Left Shift (<code>x &lt;&lt; k</code>):</strong> Multiplies $x$ by $2^k$. Zeros are shifted in from the right.</li>
  <li><strong>Arithmetic Right Shift (<code>x &gt;&gt; k</code>):</strong> Divides $x$ by $2^k$. Preserves the sign bit (copies the MSB).</li>
  <li><strong>Logical Right Shift (<code>x &gt;&gt;&gt; k</code> in Java):</strong> Shifts bits right and always fills left with 0, treating the number as unsigned.</li>
</ul>
"""
            },
            {
                "id": "s2a_dsa_compendium",
                "title": "Chapter 3: Data Structures & Algorithms Encyclopedia",
                "content": """
<h1>🌳 Chapter 3: Data Structures & Algorithms Encyclopedia</h1>
<p>Review asymptotic Big-O complexities and internal operations of all standard data structures tested in the Technical Assessment.</p>

<h2>3.1 Asymptotic Complexity Reference Matrix</h2>
<table class="pdf-table">
  <tr>
    <th>Data Structure</th>
    <th>Access (Avg / Worst)</th>
    <th>Search (Avg / Worst)</th>
    <th>Insertion (Avg / Worst)</th>
    <th>Deletion (Avg / Worst)</th>
    <th>Space Complexity</th>
  </tr>
  <tr>
    <td><strong>Array</strong></td>
    <td>O(1) / O(1)</td>
    <td>O(N) / O(N)</td>
    <td>O(N) / O(N)</td>
    <td>O(N) / O(N)</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Singly Linked List</strong></td>
    <td>O(N) / O(N)</td>
    <td>O(N) / O(N)</td>
    <td>O(1) / O(1)*</td>
    <td>O(1) / O(1)*</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Stack / Queue</strong></td>
    <td>O(N) / O(N)</td>
    <td>O(N) / O(N)</td>
    <td>O(1) / O(1)</td>
    <td>O(1) / O(1)</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Binary Search Tree (BST)</strong></td>
    <td>O(log N) / O(N)</td>
    <td>O(log N) / O(N)</td>
    <td>O(log N) / O(N)</td>
    <td>O(log N) / O(N)</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Red-Black / AVL Tree</strong></td>
    <td>O(log N) / O(log N)</td>
    <td>O(log N) / O(log N)</td>
    <td>O(log N) / O(log N)</td>
    <td>O(log N) / O(log N)</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Hash Table</strong></td>
    <td>N/A</td>
    <td>O(1) / O(N)</td>
    <td>O(1) / O(N)</td>
    <td>O(1) / O(N)</td>
    <td>O(N)</td>
  </tr>
  <tr>
    <td><strong>Binary Heap (Min/Max)</strong></td>
    <td>O(1) (peek)</td>
    <td>O(N)</td>
    <td>O(log N)</td>
    <td>O(log N)</td>
    <td>O(N)</td>
  </tr>
</table>
<p><small>* Linked List insertion/deletion is O(1) assuming the pointer to the target node is already held.</small></p>

<h2>3.2 Binary Tree Traversal Orders Visualized</h2>
<div class="code-block">
        1
       / \\
      2   3
     / \\
    4   5

1. In-order (Left, Root, Right):    4 -> 2 -> 5 -> 1 -> 3  (Yields sorted order in a BST!)
2. Pre-order (Root, Left, Right):   1 -> 2 -> 4 -> 5 -> 3  (Used for serializing trees)
3. Post-order (Left, Right, Root):  4 -> 5 -> 2 -> 3 -> 1  (Used for deleting trees, evaluating postfix math)
4. Level-order (BFS Queue):         1 -> 2 -> 3 -> 4 -> 5  (Shortest path in unweighted graphs)
</div>
"""
            },
            {
                "id": "s2a_dbms_os_cn",
                "title": "Chapter 4: Core CS Systems: DBMS, OS & Computer Networks",
                "content": """
<h1>💻 Chapter 4: Core CS Systems: DBMS, OS & Computer Networks</h1>
<p>The technical assessment includes multiple questions spanning database transactions, operating system memory/process management, and network protocols.</p>

<h2>4.1 DBMS: ACID Properties & Transaction States</h2>
<ul>
  <li><strong>Atomicity:</strong> "All-or-Nothing". Either all statements in a transaction execute successfully, or the entire transaction is rolled back. Implemented using Undo Logs (Write-Ahead Logging).</li>
  <li><strong>Consistency:</strong> The database transitions from one valid state satisfying all schema constraints, foreign keys, and triggers to another valid state.</li>
  <li><strong>Isolation:</strong> Concurrent transactions execute without interfering with one another. Controlled via Isolation Levels:
    <ul>
      <li><em>Read Uncommitted:</em> Suffers from Dirty Reads.</li>
      <li><em>Read Committed:</em> Eliminates Dirty Reads; suffers from Non-Repeatable Reads.</li>
      <li><em>Repeatable Read:</em> Eliminates Non-Repeatable Reads; can suffer from Phantom Reads.</li>
      <li><em>Serializable:</em> Highest isolation; total elimination of anomalies via two-phase locking (2PL) or multi-version concurrency control (MVCC).</li>
    </ul>
  </li>
  <li><strong>Durability:</strong> Once committed, transaction results survive power failures, system reboots, and crashes. Implemented using Redo Logs synced to disk.</li>
</ul>

<h2>4.2 Operating Systems: The 4 Coffman Conditions for Deadlock</h2>
<div class="pdf-callout warn">
  A deadlock occurs if and only if all four of these conditions hold simultaneously in the OS:
</div>
<ol>
  <li><strong>Mutual Exclusion:</strong> At least one resource must be non-shareable (only one process holds it at a time).</li>
  <li><strong>Hold and Wait:</strong> A process holds at least one resource and is waiting to acquire additional resources held by other processes.</li>
  <li><strong>No Preemption:</strong> Resources cannot be forcibly seized from a holding process; they can only be released voluntarily.</li>
  <li><strong>Circular Wait:</strong> A closed chain of processes exists: P0 waits for resource held by P1, P1 waits for P2, ..., Pn waits for P0.</li>
</ol>
<p><strong>Deadlock Prevention:</strong> Invalidate at least one condition (e.g., impose strict global linear ordering on all resource acquisitions to eliminate Circular Wait).</p>

<h2>4.3 Computer Networks: The TCP 3-Way Handshake</h2>
<div class="code-block">
Client                                           Server
  │                                                │
  ├─────── [SYN (seq = x)] ───────────────────────►│  (Client initiates connection)
  │                                                │
  │◄────── [SYN-ACK (seq = y, ack = x + 1)] ───────┤  (Server acknowledges & replies)
  │                                                │
  ├─────── [ACK (seq = x + 1, ack = y + 1)] ──────►│  (Connection ESTABLISHED!)
  │                                                │
</div>
<p><strong>TCP vs UDP Comparison:</strong></p>
<ul>
  <li><strong>TCP (Transmission Control Protocol):</strong> Connection-oriented, guarantees packet delivery and ordering, flow control (sliding window), congestion control. Used for HTTP/HTTPS, SSH, FTP, Email.</li>
  <li><strong>UDP (User Datagram Protocol):</strong> Connectionless, unreliable, low-overhead, no acknowledgments. Used for live video streaming (VoIP), online gaming, DNS queries, DHCP.</li>
</ul>
"""
            },
            {
                "id": "s2a_aptitude_cheatsheets",
                "title": "Chapter 5: Quantitative Aptitude Shortcuts & Formulas",
                "content": """
<h1>🧮 Chapter 5: Quantitative Aptitude Shortcuts & Formulas</h1>
<p>Capgemini quant tests speed and mental math tricks. Memorize these proven shortcuts to solve questions in under 45 seconds.</p>

<h2>5.1 Time & Work: The LCM Unit Method</h2>
<div class="pdf-callout tip">
  Never use fractions like 1/A + 1/B. Always calculate Total Work as the <strong>LCM of the given days</strong>.
</div>
<div class="code-block">
Problem:
A can finish a task in 12 days. B can finish it in 18 days.
Together, how long will they take?

Step 1: Find Total Work Units = LCM(12, 18) = 36 Units.
Step 2: Calculate Daily Work Rate:
        A's rate = 36 / 12 = 3 Units/day
        B's rate = 36 / 18 = 2 Units/day
Step 3: Combined rate = 3 + 2 = 5 Units/day.
Step 4: Total Time = 36 / 5 = 7.2 Days (7 days and 4.8 hours).
</div>

<h2>5.2 Time, Speed, and Distance Shortcuts</h2>
<ul>
  <li><strong>Average Speed (Equal Distances at speeds $u$ and $v$):</strong>
    $$\text{Average Speed} = \frac{2 \cdot u \cdot v}{u + v}$$
    <em>Caution: Do NOT take the simple arithmetic mean $(u + v)/2$!</em></li>
  <li><strong>Relative Speed:</strong>
    <ul>
      <li>Moving in <strong>Opposite Directions:</strong> Relative Speed $= S_1 + S_2$.</li>
      <li>Moving in <strong>Same Direction:</strong> Relative Speed $= |S_1 - S_2|$.</li>
    </ul>
  </li>
  <li><strong>Unit Conversion:</strong>
    $$\text{km/h to m/s: Multiply by } \frac{5}{18}$$
    $$\text{m/s to km/h: Multiply by } \frac{18}{5}$$
  </li>
</ul>

<h2>5.3 Profit, Loss, and Discount Formulas</h2>
<ul>
  <li>Cost Price (CP), Selling Price (SP), Marked Price (MP).</li>
  <li>$\text{Profit \%} = \frac{SP - CP}{CP} \times 100$</li>
  <li>$\text{Loss \%} = \frac{CP - SP}{CP} \times 100$</li>
  <li><strong>Successive Discounts ($d_1\%$ and $d_2\%$):</strong>
    $$\text{Net Discount} = \left( d_1 + d_2 - \frac{d_1 \cdot d_2}{100} \right)\%$$
  </li>
</ul>
"""
            },
            {
                "id": "s2a_pseudocode_trace_bank",
                "title": "Chapter 6: Pseudocode Trace Bank: 10 Real Problems Solved Step-by-Step",
                "content": """
<h1>🔍 Chapter 6: Pseudocode Trace Bank: 10 Real Problems Solved Step-by-Step</h1>
<p>Here are 10 authentic Capgemini pseudocode problems with full variable execution trace tables.</p>

<h2>Problem 1: Bitwise XOR and Shift in Nested Loop</h2>
<div class="code-block">
Integer a = 3, b = 6, c = 2
if ((a & b) < (b ^ c))
    b = (a << 1) + c
    c = b >> 1
end if
print a + b + c
</div>
<p><strong>Step-by-Step Trace:</strong></p>
<ol>
  <li>Evaluate Condition:
    <ul>
      <li>$a = 3$ (0011 in binary), $b = 6$ (0110 in binary).</li>
      <li>$a \ \& \ b = 0011 \ \& \ 0110 = 0010_2 = 2$.</li>
      <li>$c = 2$ (0010 in binary).</li>
      <li>$b \text{ \textasciicircum } c = 0110 \text{ \textasciicircum } 0010 = 0100_2 = 4$.</li>
      <li>Is $2 < 4$? <strong>TRUE</strong>. Execute if block.</li>
    </ul>
  </li>
  <li>Compute new $b$:
    <ul>
      <li>$a \ll 1 = 3 \times 2 = 6$.</li>
      <li>$b = 6 + c = 6 + 2 = 8$.</li>
    </ul>
  </li>
  <li>Compute new $c$:
    <ul>
      <li>$c = b \gg 1 = 8 / 2 = 4$.</li>
    </ul>
  </li>
  <li>Final print: $a + b + c = 3 + 8 + 4 = \mathbf{15}$.</li>
</ol>

<h2>Problem 2: Recursive Static Variable Trace</h2>
<div class="code-block">
Integer fun(Integer n)
    static Integer x = 0
    if (n <= 0)
        return 1
    end if
    x = x + 1
    return fun(n - 1) + x
end function
// Main calls fun(4)
</div>
<p><strong>Step-by-Step Trace:</strong></p>
<table class="pdf-table">
  <tr>
    <th>Call Stack Depth</th>
    <th>n</th>
    <th>Static x value (persists across calls)</th>
    <th>Return Expression</th>
  </tr>
  <tr>
    <td>Call 1</td>
    <td>4</td>
    <td>$x = 0 + 1 = 1$</td>
    <td>fun(3) + x</td>
  </tr>
  <tr>
    <td>Call 2</td>
    <td>3</td>
    <td>$x = 1 + 1 = 2$</td>
    <td>fun(2) + x</td>
  </tr>
  <tr>
    <td>Call 3</td>
    <td>2</td>
    <td>$x = 2 + 1 = 3$</td>
    <td>fun(1) + x</td>
  </tr>
  <tr>
    <td>Call 4</td>
    <td>1</td>
    <td>$x = 3 + 1 = 4$</td>
    <td>fun(0) + x</td>
  </tr>
  <tr>
    <td>Call 5 (Base Case)</td>
    <td>0</td>
    <td>$x = 4$ (not incremented)</td>
    <td>returns 1</td>
  </tr>
</table>
<p><strong>Unwinding the Stack:</strong> At the time of unwinding, the static variable $x$ retains its final value of <strong>4</strong>!</p>
<ul>
  <li>fun(1) = fun(0) + x = 1 + 4 = 5</li>
  <li>fun(2) = fun(1) + x = 5 + 4 = 9</li>
  <li>fun(3) = fun(2) + x = 9 + 4 = 13</li>
  <li>fun(4) = fun(3) + x = 13 + 4 = <strong>17</strong>.</li>
</ul>

<h2>Problem 3: Modulo Arithmetic & Jumping Index While Loop</h2>
<div class="code-block">
Integer p = 15, q = 4, count = 0
while (p > 0)
    p = p - q
    if (p mod 2 != 0)
        count = count + p
    end if
end while
print count
</div>
<p><strong>Trace Table:</strong></p>
<table class="pdf-table">
  <tr>
    <th>Iteration</th>
    <th>Initial p</th>
    <th>p = p - 4</th>
    <th>p mod 2 != 0 ?</th>
    <th>count update</th>
  </tr>
  <tr>
    <td>1</td>
    <td>15</td>
    <td>11</td>
    <td>11 % 2 = 1 (TRUE)</td>
    <td>count = 0 + 11 = 11</td>
  </tr>
  <tr>
    <td>2</td>
    <td>11</td>
    <td>7</td>
    <td>7 % 2 = 1 (TRUE)</td>
    <td>count = 11 + 7 = 18</td>
  </tr>
  <tr>
    <td>3</td>
    <td>7</td>
    <td>3</td>
    <td>3 % 2 = 1 (TRUE)</td>
    <td>count = 18 + 3 = 21</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>-1</td>
    <td>-1 % 2 = -1 != 0 (TRUE)</td>
    <td>count = 21 + (-1) = 20</td>
  </tr>
  <tr>
    <td>5</td>
    <td>-1</td>
    <td>Loop terminates (p > 0 is FALSE)</td>
    <td>-</td>
    <td>Final Output = <strong>20</strong></td>
  </tr>
</table>
"""
            },
            {
                "id": "s2a_dbms_sql_mastery",
                "title": "Chapter 7: SQL Mastery & Normalization Visualized",
                "content": """
<h1>🗄️ Chapter 7: SQL Mastery & Normalization Visualized</h1>
<p>Deep dive into relational database concepts frequently questioned in Capgemini tests and technical interviews.</p>

<h2>7.1 Normalization Forms Visualized (1NF to BCNF)</h2>
<div class="code-block">
Unnormalized (Multi-valued attributes)
       │
       ▼  [Rule: Atomic values only. No arrays or comma-separated lists in columns]
First Normal Form (1NF)
       │
       ▼  [Rule: 1NF + No Partial Functional Dependencies (All non-key attrs depend on WHOLE primary key)]
Second Normal Form (2NF)
       │
       ▼  [Rule: 2NF + No Transitive Dependencies (Non-key attrs must not depend on other non-key attrs)]
Third Normal Form (3NF)
       │
       ▼  [Rule: For every functional dependency X -> Y, X must be a SUPER KEY]
Boyce-Codd Normal Form (BCNF)
</div>

<h3>Concrete Example: 2NF to 3NF Decomposition</h3>
<p>Consider table <code>Employee_Project (EmpID, ProjectID, EmpName, DeptID, DeptName)</code>:</p>
<ul>
  <li>Primary Key: <code>(EmpID, ProjectID)</code></li>
  <li><code>EmpID -> EmpName</code> violates 2NF because <code>EmpName</code> depends only on part of the composite key (Partial Dependency). Solution: Move <code>(EmpID, EmpName)</code> to a separate <code>Employee</code> table.</li>
  <li>In <code>Employee (EmpID, DeptID, DeptName)</code>: <code>DeptID -> DeptName</code> is a Transitive Dependency (Non-key depends on Non-key). Solution: Separate into <code>Employee (EmpID, DeptID)</code> and <code>Department (DeptID, DeptName)</code> for 3NF!</li>
</ul>

<h2>7.2 SQL Joins Visualized</h2>
<table class="pdf-table">
  <tr>
    <th>Join Type</th>
    <th>Visual Venn Analogy</th>
    <th>SQL Syntax</th>
    <th>Result Rows</th>
  </tr>
  <tr>
    <td><strong>INNER JOIN</strong></td>
    <td>Intersection (A ∩ B)</td>
    <td><code>SELECT * FROM A INNER JOIN B ON A.id = B.id</code></td>
    <td>Only records where there is a match in BOTH tables.</td>
  </tr>
  <tr>
    <td><strong>LEFT JOIN</strong></td>
    <td>All A + matching B</td>
    <td><code>SELECT * FROM A LEFT JOIN B ON A.id = B.id</code></td>
    <td>All records from left table; unmatched right table columns are NULL.</td>
  </tr>
  <tr>
    <td><strong>RIGHT JOIN</strong></td>
    <td>All B + matching A</td>
    <td><code>SELECT * FROM A RIGHT JOIN B ON A.id = B.id</code></td>
    <td>All records from right table; unmatched left table columns are NULL.</td>
  </tr>
  <tr>
    <td><strong>FULL OUTER JOIN</strong></td>
    <td>Union (A ∪ B)</td>
    <td><code>SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id</code></td>
    <td>All records from both tables; NULL where no match exists.</td>
  </tr>
  <tr>
    <td><strong>CROSS JOIN</strong></td>
    <td>Cartesian Product (A × B)</td>
    <td><code>SELECT * FROM A CROSS JOIN B</code></td>
    <td>Every row in A paired with every row in B ($N \times M$ rows).</td>
  </tr>
</table>

<h2>7.3 Window Functions: Salary Ranking Example</h2>
<div class="code-block">
SELECT emp_name, department, salary,
       ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) as row_num,
       RANK()       OVER(PARTITION BY department ORDER BY salary DESC) as rnk,
       DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as dense_rnk
FROM Employees;

Difference between Ranking Functions (if salaries are: 100k, 100k, 90k):
- ROW_NUMBER(): 1, 2, 3 (Strict sequential, no ties)
- RANK():       1, 1, 3 (Ties share rank; skips subsequent rank!)
- DENSE_RANK(): 1, 1, 2 (Ties share rank; DOES NOT skip subsequent rank!)
</div>
"""
            }
        ]
    }

    # =========================================================================
    # STAGE 2B: ALGORITHMIC DEBUGGING MASTER HANDBOOK (5 Chapters)
    # =========================================================================
    docs["stage2b"] = {
        "title": "Stage 2B: Algorithmic Debugging Master Handbook",
        "sections": [
            {
                "id": "s2b_methodology_deep",
                "title": "Chapter 1: The 4-Step Diagnostic Algorithm for 20-Min Rounds",
                "content": """
<h1>🩺 Chapter 1: The 4-Step Diagnostic Algorithm for 20-Min Rounds</h1>
<p>In Stage 2B, you are given 7 to 10 pre-written code snippets containing subtle algorithmic, logical, or boundary bugs. You must diagnose and fix each bug in under 2 minutes. Follow this systematic 4-step diagnostic algorithm.</p>

<h2>The 4-Step Diagnostic Algorithm</h2>
<div class="code-block">
Step 1: Check Loop Terminations & Indices (50% of all bugs)
        ├── Are loop bounds 0-indexed or 1-indexed?
        ├── Is it 'i < n' or 'i <= n'? (Off-by-one errors)
        ├── In decrementing loops, is it 'i >= 0' or 'i > 0'?
        └── Are pointer increments inside while loops advancing correctly?

Step 2: Check Edge Case Initialization & Neutral Elements
        ├── Is minimum initialized to 0 instead of INT_MAX?
        ├── Is product initialized to 0 instead of 1?
        ├── Is array size allocated with N instead of N + 1 for 1-based indexing?
        └── In recursion, is the base case reachable when N = 0 or N = 1?

Step 3: Check Pointer & NULL References (C/C++ & Java)
        ├── Is 'ptr->next' accessed without first checking 'if (ptr != NULL)'?
        ├── In binary trees, does the recursive call handle 'root == NULL'?
        └── In linked list deletions, is the head pointer reassignment preserved?

Step 4: Check Operator Precedence & Type Overflows
        ├── Is arithmetic multiplication overflowing 32-bit signed int? (10^5 * 10^5 = 10^10 > 2^31 - 1)
        ├── Is bitwise operator precedence respected? ('a & b == 0' evaluates as 'a & (b == 0)')
        └── Is floating point equality tested directly with '=='?
</div>
"""
            },
            {
                "id": "s2b_tree_graph_dp_bugs",
                "title": "Chapter 2: Deep Dive: The 5 Most Frequent Bug Archetypes",
                "content": """
<h1>🐛 Chapter 2: Deep Dive: The 5 Most Frequent Bug Archetypes</h1>
<p>These 5 specific bug patterns account for over 70% of questions in the Capgemini debugging round.</p>

<h2>Archetype 1: Binary Search Midpoint Overflow & Infinite Loop</h2>
<div class="code-block">
// ❌ BUGGY IMPLEMENTATION
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n; // Bug 1: high should be n - 1
    while (low <= high) {
        int mid = (low + high) / 2; // Bug 2: (low + high) can overflow 32-bit int!
        if (arr[mid] == target) return mid;
        if (arr[mid] < target)
            low = mid; // Bug 3: Infinite loop! Must be mid + 1
        else
            high = mid; // Bug 4: Infinite loop! Must be mid - 1
    }
    return -1;
}

// ✔️ CORRECTED IMPLEMENTATION
int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2; // Safe against integer overflow
        if (arr[mid] == target) return mid;
        if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
</div>

<h2>Archetype 2: BFS Queue Visited Marking Timing</h2>
<div class="code-block">
// ❌ BUGGY IMPLEMENTATION: Marking node as visited upon DEQUEUE
void bfs(int start, vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        visited[u] = true; // BUG! Node is marked visited too late!
        for (int v : adj[u]) {
            if (!visited[v]) {
                q.push(v); // Duplicate copies of v are pushed into the queue, causing TLE/MLE!
            }
        }
    }
}

// ✔️ CORRECTED: Mark visited immediately upon ENQUEUE
void bfs(int start, vector<vector<int>>& adj, int V) {
    vector<bool> visited(V, false);
    queue<int> q;
    visited[start] = true;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true; // Mark visited right before pushing!
                q.push(v);
            }
        }
    }
}
</div>
"""
            },
            {
                "id": "s2b_memory_pointer_bugs",
                "title": "Chapter 3: Memory & Pointer Bugs in C/C++: Stack, Heap & Overflows",
                "content": """
<h1>💾 Chapter 3: Memory & Pointer Bugs in C/C++: Stack, Heap & Overflows</h1>
<p>Memory errors are the leading cause of segmentation faults and undefined behavior. Here is how memory operates under the hood.</p>

<h2>3.1 Process Memory Segmentation Layout</h2>
<div class="code-block">
High Memory  ┌──────────────────────────────────────────────┐
             │ Kernel Space (Operating System)              │
             ├──────────────────────────────────────────────┤
             │ Stack (Local variables, function call frames)│ ▼ Grows downward
             ├──────────────────────────────────────────────┤
             │               [ Free Memory ]                │
             ├──────────────────────────────────────────────┤
             │ Heap (Dynamically allocated: malloc / new)   │ ▲ Grows upward
             ├──────────────────────────────────────────────┤
             │ BSS Segment (Uninitialized static/globals)   │
             ├──────────────────────────────────────────────┤
             │ Data Segment (Initialized static/globals)    │
Low Memory   ├──────────────────────────────────────────────┤
             │ Text Segment (Compiled binary code / machine)│
             └──────────────────────────────────────────────┘
</div>

<h2>3.2 Dangling Pointer & Use-After-Free</h2>
<div class="code-block">
// ❌ DANGEROUS BUG
int* createArray() {
    int localArr[5] = {1, 2, 3, 4, 5};
    return localArr; // BUG! localArr is allocated on the STACK!
                     // When function returns, its stack frame is popped.
                     // The returned pointer points to invalid/garbage memory!
}

// ✔️ CORRECT ALLOCATION (On the HEAP)
int* createArray() {
    int* heapArr = (int*)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) heapArr[i] = i + 1;
    return heapArr; // Caller must free() this memory!
}
</div>

<h2>3.3 C-String Null Terminator Bug</h2>
<div class="code-block">
// ❌ OFF-BY-ONE STRING OVERFLOW
char str[5];
strcpy(str, "HELLO"); // BUG! "HELLO" has 5 characters + 1 null terminator ('\\0') = 6 bytes!
                      // str[5] overflows by 1 byte, overwriting adjacent memory!

// ✔️ FIX: Always allocate Length + 1 bytes for C-strings
char str[6];
strcpy(str, "HELLO"); // Correct: str[0]='H', ..., str[4]='O', str[5]='\\0'
</div>
"""
            },
            {
                "id": "s2b_10_real_problems",
                "title": "Chapter 4: 10 Real Capgemini Algorithmic Debugging Problems Solved",
                "content": """
<h1>🛠️ Chapter 4: 10 Real Capgemini Algorithmic Debugging Problems Solved</h1>
<p>Line-by-line solutions to 10 authentic debugging questions from past Capgemini tests.</p>

<h2>Problem 1: Linked List Cycle Detection Pointer Jump</h2>
<div class="code-block">
// ❌ BUGGY CODE:
bool hasCycle(ListNode *head) {
    ListNode *slow = head;
    ListNode *fast = head;
    while (fast != NULL) { // BUG! Does not check if fast->next is NULL!
        slow = slow->next;
        fast = fast->next->next; // Segfault if fast is the last node!
        if (slow == fast) return true;
    }
    return false;
}

// ✔️ FIX:
while (fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) return true;
}
</div>

<h2>Problem 2: 2D Matrix DP Boundary Initialization Error</h2>
<div class="code-block">
// Problem: Find unique paths in an M x N grid from (0,0) to (M-1, N-1)
// ❌ BUGGY CODE:
int uniquePaths(int m, int n) {
    int dp[m][n];
    for (int i = 0; i < m; i++) dp[i][0] = i; // BUG! Should be 1, only 1 path along edge!
    for (int j = 0; j < n; j++) dp[0][j] = j; // BUG! Should be 1!
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
    return dp[m-1][n-1];
}

// ✔️ FIX:
for (int i = 0; i < m; i++) dp[i][0] = 1;
for (int j = 0; j < n; j++) dp[0][j] = 1;
</div>

<h2>Problem 3: Palindrome String Non-Alphanumeric Skip Bug</h2>
<div class="code-block">
// ❌ BUGGY: Does not bound check inner while loops
bool isPalindrome(string s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        while (!isalnum(s[left])) left++;   // BUG: Can increment beyond 'right' or string bounds!
        while (!isalnum(s[right])) right--; // BUG: Can decrement below 0!
        if (tolower(s[left]) != tolower(s[right])) return false;
        left++; right--;
    }
    return true;
}

// ✔️ FIX: Guard inner loops with 'left < right'
while (left < right && !isalnum(s[left])) left++;
while (left < right && !isalnum(s[right])) right--;
</div>

<h2>Problem 4: C++ Vector Iterator Invalidation in Erase Loop</h2>
<div class="code-block">
// ❌ BUGGY:
for (auto it = vec.begin(); it != vec.end(); it++) {
    if (*it % 2 == 0) {
        vec.erase(it); // BUG: erase() invalidates 'it'. Incrementing it++ causes undefined behavior!
    }
}

// ✔️ FIX: Use the returned iterator from erase()
for (auto it = vec.begin(); it != vec.end(); ) {
    if (*it % 2 == 0) {
        it = vec.erase(it); // Returns iterator to the next element
    } else {
        it++;
    }
}
</div>
"""
            },
            {
                "id": "s2b_java_python_traps",
                "title": "Chapter 5: Java & Python Specific Runtime Traps & Exceptions",
                "content": """
<h1>☕ Chapter 5: Java & Python Specific Runtime Traps & Exceptions</h1>
<p>Many students prepare in Java or Python. Learn the language-specific gotchas that Capgemini tests.</p>

<h2>5.1 Java Traps</h2>
<h3>Trap 1: String Equality (<code>==</code> vs <code>.equals()</code>)</h3>
<div class="code-block">
String s1 = new String("Capgemini");
String s2 = new String("Capgemini");

System.out.println(s1 == s2);      // FALSE! '==' compares object memory references!
System.out.println(s1.equals(s2));  // TRUE! '.equals()' compares character contents!
</div>

<h3>Trap 2: Integer Caching (-128 to 127)</h3>
<div class="code-block">
Integer a = 100, b = 100;
System.out.println(a == b); // TRUE (Cached in JVM Integer Pool)

Integer c = 200, d = 200;
System.out.println(c == d); // FALSE! Beyond 127, JVM creates new heap objects!
// Always use: c.intValue() == d.intValue() or c.equals(d)
</div>

<h2>5.2 Python Traps</h2>
<h3>Trap 1: Mutable Default Arguments</h3>
<div class="code-block">
# ❌ DANGEROUS PYTHON TRAP
def append_item(item, target_list=[]): # Default list created ONCE at function definition time!
    target_list.append(item)
    return target_list

print(append_item(1)) # [1]
print(append_item(2)) # [1, 2] -- NOT [2]! The same list is mutated across calls!

# ✔️ SAFE IDIOM
def append_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
</div>

<h3>Trap 2: Division Operators (<code>/</code> vs <code>//</code>)</h3>
<p>In Python 3, <code>5 / 2 = 2.5</code> (float). To get integer floor division, always use <code>5 // 2 = 2</code>.</p>
"""
            }
        ]
    }

    # =========================================================================
    # STAGE 3: LAB 27 AI CODING & PROMPT ENGINEERING MANUAL (5 Chapters)
    # =========================================================================
    docs["stage3"] = {
        "title": "Stage 3: Lab 27 AI Coding & Prompt Engineering Manual",
        "sections": [
            {
                "id": "s3_rubric_deep",
                "title": "Chapter 1: The Lab 27 Automated Evaluation Rubric",
                "content": """
<h1>🧪 Chapter 1: The Lab 27 Automated Evaluation Rubric</h1>
<p>Stage 3 is Capgemini's revolutionary <strong>Lab 27 AI Coding Assessment</strong>. Instead of typing every line of code from scratch, you interact with an enterprise AI coding assistant. The platform grades both your <strong>Prompting Precision</strong> and the <strong>Code's Benchmark Performance</strong>.</p>

<h2>1.1 The 5 Pillars of the Lab 27 Scoring Rubric</h2>
<table class="pdf-table">
  <tr>
    <th>Scoring Dimension</th>
    <th>Weight</th>
    <th>What the Automated Grader Tests</th>
    <th>How to Score 10/10</th>
  </tr>
  <tr>
    <td><strong>Functional Correctness</strong></td>
    <td>35%</td>
    <td>Passes 100% of hidden test cases (boundary limits, empty inputs, negative numbers, duplicates).</td>
    <td>Explicitly instruct the AI to handle zero-length inputs, single elements, and extreme boundaries in your prompt.</td>
  </tr>
  <tr>
    <td><strong>Time Complexity (TLE Prevention)</strong></td>
    <td>25%</td>
    <td>Algorithm runtime must be within strict execution limits (usually 1.0 to 2.0 seconds).</td>
    <td>State the required Big-O complexity directly in the prompt (e.g. <em>"Must run in O(N log N) time; O(N^2) approaches will fail"</em>).</td>
  </tr>
  <tr>
    <td><strong>Space Complexity & Memory Bounds</strong></td>
    <td>15%</td>
    <td>Auxiliary heap and stack memory usage within 256MB limit.</td>
    <td>Instruct the AI to use $O(1)$ auxiliary space or in-place transformations where applicable.</td>
  </tr>
  <tr>
    <td><strong>Prompt Specificity & Structure</strong></td>
    <td>15%</td>
    <td>Whether your prompt followed the 5-Part Master Prompt Anatomy vs vague conversational queries.</td>
    <td>Use structured role, language, constraint, and edge-case framing.</td>
  </tr>
  <tr>
    <td><strong>Code Cleanliness & Production Hygiene</strong></td>
    <td>10%</td>
    <td>Clean variable naming, absence of debug print statements, proper modular decomposition.</td>
    <td>Instruct the AI to avoid conversational filler and output pure production-ready code with Fast I/O.</td>
  </tr>
</table>
"""
            },
            {
                "id": "s3_master_prompts_bank",
                "title": "Chapter 2: Production-Ready 10/10 Prompts for Core Problems",
                "content": """
<h1>📐 Chapter 2: Production-Ready 10/10 Prompts for Core Problems</h1>
<p>Examine the anatomy of a perfect 10/10 prompt and study production-ready examples for core algorithmic challenges.</p>

<h2>The 5-Part Master Prompt Anatomy</h2>
<div class="code-block">
[PART 1: ROLE & OBJECTIVE]
"Act as a Principal Software Engineer. Write a complete, optimal, bug-free solution in [C++17 / Java 17 / Python 3] for the following problem: [Problem Title]."

[PART 2: FORMAL PROBLEM STATEMENT & I/O FORMAT]
"Given [Input description and formats]. Return [Exact output specification]."

[PART 3: STRICT ASYMPTOTIC CONSTRAINTS]
"- Time Complexity: Must be strictly O([Required Time])
 - Auxiliary Space Complexity: Must be O([Required Space])
 - Input constraints: N <= [Max value, e.g. 2 * 10^5]. Sub-optimal O(N^2) algorithms will result in Time Limit Exceeded."

[PART 4: MANDATORY EDGE CASES TO HANDLE]
"- Empty or NULL input
 - Arrays with all identical elements
 - Negative numbers and large 64-bit integer values (use long long in C++ / long in Java)
 - Single-element inputs"

[PART 5: OUTPUT SPECIFICATION]
"Provide only pure, self-contained, compilable code without markdown explanations or debug print statements. Include Fast I/O."
</div>

<h2>Example 1: Trapping Rain Water ($O(N)$ Time, $O(1)$ Space)</h2>
<div class="code-block">
Prompt to Submit to Lab 27 AI:
"Act as a Principal Competitive Programmer. Write a complete C++17 solution for the Trapping Rain Water problem.
Input: An array of non-negative integers representing an elevation map where the width of each bar is 1.
Output: Total units of water trapped after raining.
Strict Constraints:
- Time Complexity: O(N) single-pass using Two Pointers technique.
- Auxiliary Space: O(1) strictly. Do NOT allocate prefix/suffix max arrays.
- Constraints: N <= 2 * 10^5, height[i] <= 10^5. Use 64-bit long long for total water sum to prevent integer overflow.
Edge Cases to Guard:
- Array length < 3 (returns 0).
- Monotonically increasing or decreasing heights (returns 0).
Output only the compilable class Solution with trap(vector<int>& height) method."
</div>
"""
            },
            {
                "id": "s3_7_fatal_sins",
                "title": "Chapter 3: The 7 Fatal Prompting Sins in Lab 27 & Exact Fixes",
                "content": """
<h1>⚠️ Chapter 3: The 7 Fatal Prompting Sins in Lab 27 & Exact Fixes</h1>
<p>Avoid these 7 common mistakes that cause candidates to lose points in Lab 27.</p>

<table class="pdf-table">
  <tr>
    <th>Fatal Sin</th>
    <th>Symptom / Consequence</th>
    <th>The Exact Prompting Remedy</th>
  </tr>
  <tr>
    <td><strong>1. Implicit Constraints</strong></td>
    <td>AI generates a naive $O(N^2)$ brute-force loop, causing Time Limit Exceeded (TLE) on test cases with $N = 10^5$.</td>
    <td><em>"Target Time Complexity: Strictly O(N log N) or O(N). Brute force will exceed execution limits."</em></td>
  </tr>
  <tr>
    <td><strong>2. 32-Bit Integer Overflow</strong></td>
    <td>Fails hidden test cases involving large sums or factorials due to signed 32-bit integer wraparound (-2,147,483,648).</td>
    <td><em>"Accumulate all intermediate products and sums using 64-bit integers ('long long' in C++, 'long' in Java)."</em></td>
  </tr>
  <tr>
    <td><strong>3. Omitting Fast I/O</strong></td>
    <td>Code times out purely because standard console streaming (<code>cin</code> / <code>System.out</code>) is too slow for $10^6$ lines.</td>
    <td><em>"Include Fast I/O directives: ios_base::sync_with_stdio(false); cin.tie(NULL);"</em></td>
  </tr>
  <tr>
    <td><strong>4. Conversational LLM Verbosity</strong></td>
    <td>The AI outputs introductory text ("Sure! Here is the code:"), which triggers compiler syntax errors in the auto-grader.</td>
    <td><em>"Output ONLY valid compilable source code inside code blocks. Zero markdown prose, greetings, or explanations."</em></td>
  </tr>
  <tr>
    <td><strong>5. Deep Recursion Stack Overflow</strong></td>
    <td>Python scripts crash with <code>RecursionError: maximum recursion depth exceeded</code> on trees of depth &gt; 1000.</td>
    <td><em>"Use an iterative stack/queue approach, or include 'import sys; sys.setrecursionlimit(200000)'."</em></td>
  </tr>
  <tr>
    <td><strong>6. Unchecked Memory Allocation</strong></td>
    <td>Algorithm allocates 2D DP matrix for $N = 10^5$, exceeding 256MB memory limit (MLE).</td>
    <td><em>"Space Optimization: Optimize DP transitions using two 1D rows or rolling variables to ensure O(N) or O(1) space."</em></td>
  </tr>
  <tr>
    <td><strong>7. Ignoring Zero & Empty Edge Cases</strong></td>
    <td>Crashes on hidden test case 1 (empty array) with IndexOutOfBounds or NullPointerException.</td>
    <td><em>"Defensive checks: If input container is empty or length is 0, return default identity immediately."</em></td>
  </tr>
</table>
"""
            },
            {
                "id": "s3_hard_topics_prompts",
                "title": "Chapter 4: Master Production Prompts for Hard Algorithmic Topics",
                "content": """
<h1>🏆 Chapter 4: Master Production Prompts for Hard Algorithmic Topics</h1>
<p>Ready-to-use prompts for the most challenging topics tested in Lab 27.</p>

<h2>1. Dynamic Programming: 0/1 Knapsack & Coin Change ($O(W)$ Space)</h2>
<div class="code-block">
"Act as a Principal Algorithmic Engineer. Provide a complete, production-grade Java solution for the Coin Change problem:
Input: int[] coins, int amount.
Output: Minimum number of coins needed to make up that amount, or -1 if impossible.
Strict Directives:
- Dynamic Programming Approach: Bottom-up 1D array DP of size (amount + 1).
- Time Complexity: O(coins.length * amount).
- Space Complexity: O(amount) strictly.
- Edge cases: amount == 0 (returns 0), coins with values greater than amount, impossible amounts.
- Initialize DP array with (amount + 1) as sentinel infinity. Do NOT use Integer.MAX_VALUE to prevent addition overflow.
Provide only the compilable class Solution."
</div>

<h2>2. Graph Algorithms: Dijkstra's Shortest Path ($O((V+E) \log V)$)</h2>
<div class="code-block">
"Write an optimal C++17 implementation of Dijkstra's Single-Source Shortest Path algorithm on a directed weighted graph.
Input: int V, vector<vector<pair<int, int>>> adj (where pair is {neighbor, weight}), int source.
Output: vector<long long> dist representing minimum distance from source to all vertices. Return -1 for unreachable nodes.
Strict Directives:
- Use std::priority_queue with greater comparator (min-heap) storing {distance, vertex}.
- Maintain a visited or distance-check guard: if current popped distance > dist[u], continue immediately.
- Use 64-bit 'long long' for all path accumulations to prevent overflow.
- Time Complexity: O((V + E) log V). Space: O(V + E).
Provide pure runnable code."
</div>

<h2>3. Monotonic Stack: Next Greater Element & Histogram</h2>
<div class="code-block">
"Write an optimal Python 3 solution for the Largest Rectangle in Histogram problem.
Input: heights: List[int]
Output: Maximum rectangular area possible.
Strict Directives:
- Implement the Monotonic Increasing Stack algorithm running in strictly O(N) time and O(N) auxiliary space.
- Handle trailing bar calculation by appending a sentinel height of 0 at the end of the array.
- Edge cases: empty list (return 0), all identical heights, strictly increasing heights.
Provide self-contained, clean Python code."
</div>
"""
            },
            {
                "id": "s3_failure_recovery_workflow",
                "title": "Chapter 5: The Test-Case Failure Diagnostic Workflow",
                "content": """
<h1>🩺 Chapter 5: The Test-Case Failure Diagnostic Workflow</h1>
<p>What should you do when your first prompt passes 10 out of 15 test cases, but fails the remaining 5? Use this systematic troubleshooting workflow.</p>

<div class="code-block">
SITUATION A: "Wrong Answer (WA) on Test Case 11 of 15"
Diagnosis: Boundary condition, 64-bit overflow, or duplicate values.
Prompt Adjustment:
"The previous solution failed on edge test cases. Refactor the code with these explicit safeguards:
1. Ensure all intermediate accumulators use 64-bit integer types ('long long' / 'long').
2. Handle cases where the array contains duplicate elements.
3. Verify behavior when N = 1 and when all values in the array are negative."

SITUATION B: "Time Limit Exceeded (TLE) on Test Case 14 of 15"
Diagnosis: Algorithmic complexity is too high ($O(N^2)$ instead of $O(N \log N)$), or slow I/O.
Prompt Adjustment:
"The previous code timed out on large inputs (N = 2 * 10^5).
Refactor to strictly O(N) or O(N log N) using:
- Replace nested loops with Two Pointers / Hash Map / Monotonic Stack.
- Disable stream synchronization with Fast I/O.
- Eliminate repeated string concatenations by using StringBuilder / string::reserve."

SITUATION C: "Memory Limit Exceeded (MLE)"
Diagnosis: Unnecessary 2D DP matrix or deep recursive call stack.
Prompt Adjustment:
"The previous solution exceeded the 256MB memory limit.
- Compress the 2D DP state into two 1D vectors (rolling array technique).
- Convert recursive DFS into an iterative BFS or iterative stack to eliminate call stack frames."
</div>
"""
            }
        ]
    }

    # =========================================================================
    # STAGE 4: COGNITIVE GAMES & ADEPT-15 BEHAVIORAL DOSSIER (5 Chapters)
    # =========================================================================
    docs["stage4"] = {
        "title": "Stage 4: Cognitive Games & ADEPT-15 Behavioral Dossier",
        "sections": [
            {
                "id": "s4_cognitive_deep",
                "title": "Chapter 1: Cognitive Game Mechanics & Step-Minimization Tactics",
                "content": """
<h1>🎮 Chapter 1: Cognitive Game Mechanics & Step-Minimization Tactics</h1>
<p>Stage 4 evaluates candidates using interactive cognitive mini-games and the ADEPT-15 psychometric framework. These games test problem-solving speed, spatial awareness, and working memory.</p>

<h2>1.1 The 4 Core Cognitive Games</h2>
<table class="pdf-table">
  <tr>
    <th>Game Name</th>
    <th>Cognitive Faculty Tested</th>
    <th>Time Per Level</th>
    <th>Target Strategy</th>
  </tr>
  <tr>
    <td><strong>Motion Challenge</strong></td>
    <td>Spatial planning & trajectory optimization.</td>
    <td>60 – 90 seconds</td>
    <td>Solve puzzles in the <em>absolute minimum number of moves</em>. Quality of moves is scored higher than pure speed.</td>
  </tr>
  <tr>
    <td><strong>Grid Challenge</strong></td>
    <td>Working memory & dual-task cognitive load.</td>
    <td>90 seconds</td>
    <td>Remember dot sequence locations while simultaneously evaluating spatial symmetry of intervening shapes.</td>
  </tr>
  <tr>
    <td><strong>Switch Challenge</strong></td>
    <td>Deductive reasoning & symbol mapping.</td>
    <td>60 seconds</td>
    <td>Determine which operator rule modifies an initial 4-digit sequence to produce the target output.</td>
  </tr>
  <tr>
    <td><strong>Digit Challenge</strong></td>
    <td>Numerical fluency & mental calculation under pressure.</td>
    <td>90 seconds</td>
    <td>Construct a target number using available digit cards and arithmetic operators (+, -, ×, /).</td>
  </tr>
</table>

<h2>1.2 Motion Challenge: Shortest-Path Planning</h2>
<div class="pdf-callout tip">
  <strong>The 10-Second Pause Rule:</strong> Do not touch the mouse or move blocks for the first 10 seconds of each round. Work backward from the target slot:
  <ol>
    <li>Identify which obstacle blocks directly block the target path.</li>
    <li>Identify which auxiliary blocks must move to free those obstacle blocks.</li>
    <li>Execute only the required moves in sequence. Superfluous back-and-forth moves heavily penalize your score.</li>
  </ol>
</div>
"""
            },
            {
                "id": "s4_adept15_matrix",
                "title": "Chapter 2: The ADEPT-15 Personality Framework & Culture Fit",
                "content": """
<h1>🧠 Chapter 2: The ADEPT-15 Personality Framework & Culture Fit</h1>
<p>The ADEPT-15 is an adaptive psychometric questionnaire measuring 15 distinct workplace personality traits. It is <strong>NOT</strong> an exam with right or wrong answers, but Capgemini matches candidates against enterprise consulting profiles.</p>

<h2>2.1 The 15 Personality Dimensions & Capgemini Alignment</h2>
<table class="pdf-table">
  <tr>
    <th>Dimension</th>
    <th>Trait Definition</th>
    <th>Capgemini Consulting Preference</th>
  </tr>
  <tr>
    <td><strong>Adaptability</strong></td>
    <td>Comfort with shifting priorities and technology stacks.</td>
    <td><strong>HIGH:</strong> Essential for client projects and shifting requirements.</td>
  </tr>
  <tr>
    <td><strong>Collaboration</strong></td>
    <td>Willingness to share credit and support team members.</td>
    <td><strong>VERY HIGH:</strong> Core value (Team Spirit).</td>
  </tr>
  <tr>
    <td><strong>Achievement Drive</strong></td>
    <td>Pursuit of excellence and challenging project goals.</td>
    <td><strong>HIGH:</strong> Self-starter orientation.</td>
  </tr>
  <tr>
    <td><strong>Emotional Resilience</strong></td>
    <td>Maintaining calm during production outages or tight deadlines.</td>
    <td><strong>VERY HIGH:</strong> Poised and constructive under pressure.</td>
  </tr>
  <tr>
    <td><strong>Integrity & Ethics</strong></td>
    <td>Adherence to compliance, honesty, and client confidentiality.</td>
    <td><strong>MAXIMUM:</strong> Serge Kampf's #1 founding value (Honesty).</td>
  </tr>
</table>

<h2>2.2 The 3 Golden Rules of ADEPT-15 Response</h2>
<ol>
  <li><strong>Consistency Cross-Checks:</strong> The test asks the same core trait in 3 different phrasings across 80 questions. If you claim to love teamwork in Question 5, do not claim you prefer working completely alone in Question 42.</li>
  <li><strong>Avoid Extreme Polarization:</strong> Do not select "Strongly Agree" or "Strongly Disagree" for every question. Reserve extremes for core ethical principles (e.g. honesty, integrity). Use moderate ratings for preferences.</li>
  <li><strong>Always Embody Accountability:</strong> When asked about project failures, always choose answers reflecting personal ownership, root-cause analysis, and preventative fixes rather than blaming external circumstances.</li>
</ol>
"""
            },
            {
                "id": "s4_switch_challenge_math",
                "title": "Chapter 3: Switch Challenge Complete Permutation Matrix",
                "content": """
<h1>🔄 Chapter 3: Switch Challenge Complete Permutation Matrix</h1>
<p>The Switch Challenge tests deductive logic by applying permutation switches to a sequence of 4 geometric shapes or digits.</p>

<h2>3.1 How the Switch Operators Work</h2>
<div class="code-block">
Initial Sequence:   [ Circle,  Triangle,  Square,  Diamond ]
Position Indices:      1          2         3         4

Example Switch Rule: [ 3, 1, 4, 2 ]
Meaning:
- New Position 1 gets what was in Old Position 3 (Square)
- New Position 2 gets what was in Old Position 1 (Circle)
- New Position 3 gets what was in Old Position 4 (Diamond)
- New Position 4 gets what was in Old Position 2 (Triangle)

Transformed Output: [ Square,  Circle,  Diamond,  Triangle ]
</div>

<h2>3.2 The 2-Level Deduction Strategy</h2>
<p>In advanced levels, you are shown two alternative switch boxes in series, with one unknown. Follow this rapid elimination strategy:</p>
<ol>
  <li><strong>Track the Outlier Symbol:</strong> Pick the single rarest shape or digit in the starting sequence.</li>
  <li><strong>Trace Its Destination:</strong> Look at where that single symbol ended up in the final output.</li>
  <li><strong>Eliminate Non-Matching Switch Options:</strong> This single tracking step immediately eliminates 2 of the 4 candidate switch operators, saving precious seconds.</li>
</ol>
"""
            },
            {
                "id": "s4_digit_challenge_shortcuts",
                "title": "Chapter 4: Digit Challenge Mental Calculation Cheat Sheets",
                "content": """
<h1>🔢 Chapter 4: Digit Challenge Mental Calculation Cheat Sheets</h1>
<p>In the Digit Challenge, you must combine 3 to 5 given numbers using basic arithmetic (+, -, ×, /) to reach a target number in under 15 seconds.</p>

<h2>4.1 The Prime Factorization Strategy</h2>
<div class="pdf-callout tip">
  Whenever the target number is large (&gt;30), instantly check if it divides cleanly by one of your available cards.
</div>
<div class="code-block">
Available Cards: [ 4, 7, 3, 2 ]
Target Number:   56

Step 1: Does 56 divide by any available card?
        56 / 7 = 8!
Step 2: Can we create 8 using the remaining cards [ 4, 3, 2 ]?
        4 * 2 = 8 (or 4 + 3 + 2 - 1)
Step 3: Solution: 7 * (4 * 2) = 56! Solved in 4 seconds!
</div>

<h2>4.2 The Sum & Difference Balancing Strategy</h2>
<div class="code-block">
Available Cards: [ 9, 6, 4, 2 ]
Target Number:   50

Step 1: Find a product close to 50:
        9 * 6 = 54
Step 2: We need: 54 - 4 = 50!
Step 3: Solution: (9 * 6) - 4 = 50. Card [2] is unused! Solved in 3 seconds!
</div>
"""
            },
            {
                "id": "s4_adept15_scenarios_bank",
                "title": "Chapter 5: ADEPT-15 15-Trait Alignment & Scenario Bank",
                "content": """
<h1>📋 Chapter 5: ADEPT-15 15-Trait Alignment & Scenario Bank</h1>
<p>Study these 10 real situational judgment questions with Capgemini's preferred responses and corporate rationale.</p>

<h2>Scenario 1: Handling Ambiguous Project Requirements</h2>
<div class="code-block">
Question:
"You are assigned a critical software module, but the client requirements provided are vague and contradictory. What do you do?"

A. Wait for the project manager to provide clear documentation before starting work.
B. Make your own assumptions, build the feature, and present it at the end of the sprint.
C. Draft a list of clarifying questions, propose a sensible default architecture, and schedule a 15-minute alignment call with the tech lead. [PREFERRED]
D. Complain to HR that the client is unorganized.

Capgemini Rationale: Option C demonstrates Boldness, Autonomy, and Team Spirit without reckless assumptions.
</div>

<h2>Scenario 2: Dealing with a Teammate's Performance Lag</h2>
<div class="code-block">
Question:
"A teammate working on the same sprint is missing daily deadlines, jeopardizing the release date. What is your response?"

A. Report their lack of delivery immediately to the delivery manager.
B. Privately reach out to the colleague, offer peer programming assistance on their blocking task, and help re-estimate remaining story points. [PREFERRED]
C. Ignore the issue since your own tasks are completed on time.
D. Take over all their tasks without telling them.

Capgemini Rationale: Option B embodies the core value of Team Spirit and People-First problem-solving.
</div>
"""
            }
        ]
    }

    # =========================================================================
    # STAGES 5 & 6: TECH & HR INTERVIEW DEFENSE PLAYBOOK (6 Chapters)
    # =========================================================================
    docs["stage56"] = {
        "title": "Stages 5-6: Tech & HR Interview Defense Playbook",
        "sections": [
            {
                "id": "s5_7values_deep",
                "title": "Chapter 1: Serge Kampf's Legacy & The 7 Core Values",
                "content": """
<h1>🏛️ Chapter 1: Serge Kampf's Legacy & The 7 Core Values</h1>
<p>Capgemini was founded in 1967 in Grenoble, France, by the visionary entrepreneur <strong>Serge Kampf</strong>. Unlike companies driven solely by process, Capgemini's entire culture is anchored in <strong>7 Core Values</strong>. Demonstrating these values in your interviews is mandatory to clear the behavioral round.</p>

<h2>The 7 Core Values & How to Prove Them (STAR Method)</h2>
<table class="pdf-table">
  <tr>
    <th>Core Value</th>
    <th>What It Means to Capgemini</th>
    <th>Fresher Interview Evidence (STAR Example)</th>
  </tr>
  <tr>
    <td><strong>1. Honesty (L'Honnêteté)</strong></td>
    <td>Saying what is true, admitting errors openly, client transparency.</td>
    <td>"When our capstone demo encountered a bug, I openly informed our professor of the root cause rather than hiding it."</td>
  </tr>
  <tr>
    <td><strong>2. Boldness (L'Audace)</strong></td>
    <td>Taking calculated risks, innovating, challenging outdated ways of working.</td>
    <td>"I took the initiative to learn Docker and containerize our application when the rest of the team was deploying manually."</td>
  </tr>
  <tr>
    <td><strong>3. Trust (La Confiance)</strong></td>
    <td>Believing in team capabilities, delegating without micromanagement.</td>
    <td>"I trusted my junior teammate with the database migration scripts after thorough code review."</td>
  </tr>
  <tr>
    <td><strong>4. Freedom (La Liberté)</strong></td>
    <td>Creative autonomy balanced with accountability for deliverables.</td>
    <td>"We had freedom to pick our frontend stack, and we justified React with measurable render metrics."</td>
  </tr>
  <tr>
    <td><strong>5. Team Spirit (L'Esprit d'Équipe)</strong></td>
    <td>Solidarity, sharing praise, supporting struggling teammates.</td>
    <td>"During semester exams, I organized peer code sessions to help non-CS batchmates clear data structures."</td>
  </tr>
  <tr>
    <td><strong>6. Modesty (La Modestie)</strong></td>
    <td>Humility, active listening, learning continuously from everyone.</td>
    <td>"Despite winning the hackathon, I sought constructive code review feedback from senior judges to improve."</td>
  </tr>
  <tr>
    <td><strong>7. Fun (Le Plaisir)</strong></td>
    <td>Finding joy and passion in engineering excellence and collaboration.</td>
    <td>"We celebrated sprint milestones with pizza and hack nights, making hard coding marathons enjoyable."</td>
  </tr>
</table>
"""
            },
            {
                "id": "s5_tech_questions_25",
                "title": "Chapter 2: Top 25 Technical Interview Questions & Model Answers",
                "content": """
<h1>💼 Chapter 2: Top 25 Technical Interview Questions & Model Answers</h1>
<p>High-scoring model answers to the most frequent technical interview questions asked in Capgemini final rounds.</p>

<h2>Q1: Explain the CAP Theorem and its real-world engineering trade-offs.</h2>
<div class="code-block">
Answer:
1. Definition: In any distributed data store, you can simultaneously guarantee at most TWO out of three properties:
   - Consistency (C): Every read receives the most recent write or an error.
   - Availability (A): Every non-failing node returns a non-error response, but without guarantee it contains the latest write.
   - Partition Tolerance (P): The system continues operating despite arbitrary network dropped messages or network splits.

2. Real-World Engineering Trade-Off:
   Because physical networks can drop packets or experience latency partitions, Partition Tolerance (P) is MANDATORY in real-world distributed systems.
   Therefore, the real choice is between CP and AP:
   - CP Systems (Consistency + Partition Tolerance): e.g. MongoDB, HBase, Google Spanner. If network splits occur, nodes reject writes until sync is restored.
   - AP Systems (Availability + Partition Tolerance): e.g. Apache Cassandra, Amazon DynamoDB, CouchDB. Nodes accept reads/writes and rely on Eventual Consistency.
</div>

<h2>Q2: What is the Cache-Aside Pattern and how do you prevent Cache Stampede?</h2>
<div class="code-block">
Answer:
1. Cache-Aside Workflow:
   - Step 1: Application checks Redis/Memcached. If Cache HIT -> return data directly.
   - Step 2: If Cache MISS -> query primary relational database.
   - Step 3: Write retrieved data into Redis with an explicit TTL (Time To Live).
   - Step 4: Return data to client.

2. Cache Stampede (Thundering Herd Problem):
   Occurs when a high-traffic cache key expires simultaneously, causing thousands of concurrent requests to hit the database at once, crashing it.
   Mitigation Strategies:
   - Mutex / Distributed Locks: The first thread that encounters a miss acquires a Redis lock to query the DB; other threads wait.
   - Probabilistic Early Expiration (XFetch Algorithm): Refresh the cache key slightly before its official TTL expires.
   - Background Worker Warm-up: Scheduled jobs refresh popular keys asynchronously.
</div>

<h2>Q3: Why use JWT with HttpOnly cookies instead of LocalStorage?</h2>
<div class="code-block">
Answer:
- LocalStorage Flaw: Data stored in localStorage is directly accessible via JavaScript (window.localStorage). If your web app has a Cross-Site Scripting (XSS) vulnerability, injected scripts can steal the JWT token instantly.
- HttpOnly Cookie Protection: The browser enforces that JavaScript CANNOT read the cookie via document.cookie. The browser automatically attaches the cookie to same-origin HTTP requests.
- Pair HttpOnly cookies with 'SameSite=Strict' and CSRF token verification headers to prevent Cross-Site Request Forgery (CSRF).
</div>
"""
            },
            {
                "id": "s5_hr_defense_blueprint",
                "title": "Chapter 3: The 4-Step Project Defense & HR Interview Blueprint",
                "content": """
<h1>🎯 Chapter 3: The 4-Step Project Defense & HR Interview Blueprint</h1>
<p>How to present your academic capstone project with confidence and answer common HR behavioral questions.</p>

<h2>3.1 The 4-Step Project Defense Formula (90 Seconds)</h2>
<ol>
  <li><strong>Step 1: The Business Problem (20 Seconds):</strong>
    "In our capstone project, university students faced 25-minute wait times during lunch hours at campus cafeterias. We designed a real-time order forecasting and queuing system."</li>
  <li><strong>Step 2: Architecture & Stack Justification (30 Seconds):</strong>
    "We built a React frontend with a Node.js microservices backend and PostgreSQL database. We chose PostgreSQL over MongoDB because order processing requires strict ACID transaction guarantees for inventory and payment reconciliation."</li>
  <li><strong>Step 3: The Hardest Technical Bottleneck Solved (30 Seconds):</strong>
    "Under peak load simulation, concurrent order placements triggered race conditions that allowed double-booking inventory. I resolved this by implementing optimistic concurrency control with row versioning and Redis distributed locks."</li>
  <li><strong>Step 4: Quantifiable Impact (10 Seconds):</strong>
    "The system sustained 2,500 simulated concurrent orders with sub-120ms response latency."</li>
</ol>

<h2>3.2 High-Scoring Answers to Tricky HR Questions</h2>
<h3>"Where do you see yourself in 3 to 5 years at Capgemini?"</h3>
<div class="code-block">
Model Answer:
"In my first 1 to 2 years, my priority is mastering Capgemini's enterprise delivery standards, earning advanced cloud certifications in AWS or Azure, and contributing high-quality code to client deliverables.
By year 3 to 5, I see myself growing into a Senior Software Engineer or Module Lead role, taking architectural ownership of scalable distributed services and mentoring incoming graduate engineers, embodying Capgemini's culture of People First and Team Spirit."
</div>

<h3>"What questions do you have for us?" (Always ask 2 strategic questions)</h3>
<ul>
  <li><em>"What does success look like for a graduate engineer joining your team in their first 6 months?"</em></li>
  <li><em>"How is Capgemini currently integrating Generative AI tools and internal LLMs into your daily software development lifecycle?"</em></li>
</ul>
"""
            },
            {
                "id": "s5_system_design_freshers",
                "title": "Chapter 4: System Design & Enterprise Architecture for Freshers",
                "content": """
<h1>🏗️ Chapter 4: System Design & Enterprise Architecture for Freshers</h1>
<p>Senior interviewers frequently test whether freshers understand real-world enterprise architectures beyond simple college CRUD apps.</p>

<h2>4.1 Monolith vs Microservices Architecture</h2>
<table class="pdf-table">
  <tr>
    <th>Architecture</th>
    <th>Key Advantages</th>
    <th>Key Challenges</th>
    <th>When to Choose</th>
  </tr>
  <tr>
    <td><strong>Monolithic Architecture</strong></td>
    <td>Simple deployment (single artifact), easy local debugging, zero network serialization latency between modules.</td>
    <td>Tight coupling, entire system redeployed on minor changes, scaling bottlenecks.</td>
    <td>Early-stage MVPs, small development teams (&lt;10 engineers), tightly coupled domain logic.</td>
  </tr>
  <tr>
    <td><strong>Microservices Architecture</strong></td>
    <td>Independent deployability, language/stack polyglotism, isolated fault domains, horizontal autoscaling per service.</td>
    <td>Distributed data consistency (Saga pattern), network latency, complex observability (distributed tracing).</td>
    <td>Large enterprise platforms, multiple autonomous engineering teams, services with differing compute profiles.</td>
  </tr>
</table>

<h2>4.2 Load Balancing Strategies Visualized</h2>
<div class="code-block">
Client Traffic ──► [ Load Balancer / Reverse Proxy (Nginx) ]
                          ├── Round Robin ────────► [ App Server Node 1 ]
                          ├── Least Connections ──► [ App Server Node 2 ]
                          └── IP Hash (Affinity) ─► [ App Server Node 3 ]
</div>
<ul>
  <li><strong>Round Robin:</strong> Requests distributed sequentially across servers. Best when servers have identical hardware and tasks have equal duration.</li>
  <li><strong>Least Connections:</strong> Sends new requests to the node currently handling the fewest active connections. Best for long-lived sessions (WebSockets).</li>
  <li><strong>IP Hash:</strong> Computes hash of client IP to ensure the same client always reaches the same server (session stickiness).</li>
</ul>

<h2>4.3 Database Scaling: Replication vs Sharding</h2>
<ul>
  <li><strong>Master-Slave Replication:</strong>
    <ul>
      <li>All writes (INSERT, UPDATE, DELETE) go to the <strong>Master Database</strong>.</li>
      <li>Changes are asynchronously replicated to <strong>Read Replicas (Slaves)</strong>.</li>
      <li>All read queries (SELECT) hit the replicas, scaling read throughput 10x.</li>
    </ul>
  </li>
  <li><strong>Database Sharding (Horizontal Partitioning):</strong>
    <ul>
      <li>Splits a massive table into smaller physical partitions across separate database servers based on a <strong>Shard Key</strong> (e.g. <code>user_id % 4</code>).</li>
    </ul>
  </li>
</ul>
"""
            },
            {
                "id": "s5_rapid_fire_tech_30",
                "title": "Chapter 5: Top 30 Technical Rapid-Fire Questions & Answers",
                "content": """
<h1>⚡ Chapter 5: Top 30 Technical Rapid-Fire Questions & Answers</h1>
<p>Master these 30 rapid-fire questions covering OOP, DSA, DBMS, OS, and CN frequently asked during final interviews.</p>

<table class="pdf-table">
  <tr>
    <th>Subject</th>
    <th>Question</th>
    <th>Crisp, High-Scoring Answer</th>
  </tr>
  <tr>
    <td><strong>OOP</strong></td>
    <td>Difference between Method Overloading and Method Overriding?</td>
    <td>Overloading is Compile-Time Polymorphism (same method name, different parameter signature in the same class). Overriding is Run-Time Polymorphism (subclass provides specific implementation of a superclass method).</td>
  </tr>
  <tr>
    <td><strong>OOP</strong></td>
    <td>Can you instantiate an Abstract Class or an Interface?</td>
    <td>No, neither can be instantiated directly. An abstract class can have constructors and instance variables; an interface only defines contract methods and public static final constants.</td>
  </tr>
  <tr>
    <td><strong>DSA</strong></td>
    <td>Why is QuickSort preferred over MergeSort for arrays?</td>
    <td>QuickSort sorts in-place with O(1) auxiliary space and exhibits superior cache locality, whereas MergeSort requires O(N) auxiliary buffer space.</td>
  </tr>
  <tr>
    <td><strong>DSA</strong></td>
    <td>What is Hash Collision and how is it resolved?</td>
    <td>Occurs when two distinct keys produce the same hash index. Resolved via Chaining (linked lists or balanced trees at index) or Open Addressing (Linear/Quadratic Probing).</td>
  </tr>
  <tr>
    <td><strong>DBMS</strong></td>
    <td>What is the difference between Clustered and Non-Clustered Index?</td>
    <td>A Clustered Index alters the actual physical order of table rows on disk (only 1 per table, typically the Primary Key). A Non-Clustered Index is a separate pointer structure pointing back to table rows.</td>
  </tr>
  <tr>
    <td><strong>OS</strong></td>
    <td>Difference between Process and Thread?</td>
    <td>A process is an isolated executing program with its own memory address space. A thread is a lightweight execution unit within a process that shares code, data, and heap memory.</td>
  </tr>
  <tr>
    <td><strong>CN</strong></td>
    <td>What happens when you type 'google.com' in a browser?</td>
    <td>1. Browser checks cache / DNS lookup. 2. Resolves IP. 3. Initiates TCP 3-Way Handshake. 4. Performs TLS handshake. 5. Sends HTTP GET request. 6. Server responds with HTML/CSS/JS. 7. Browser DOM parser renders page.</td>
  </tr>
</table>
"""
            },
            {
                "id": "s5_hr_behavioral_masterclass",
                "title": "Chapter 6: HR Interview Masterclass: 20 Behavioral Scenarios",
                "content": """
<h1>🌟 Chapter 6: HR Interview Masterclass: 20 Behavioral Scenarios</h1>
<p>Capgemini HR rounds evaluate cultural fit, teamwork, adaptability, and integrity. Use these structured responses.</p>

<h2>Scenario 1: "Are you willing to relocate to any Capgemini delivery location?"</h2>
<div class="code-block">
Model Response:
"Yes, absolutely. I understand that Capgemini serves global Fortune 500 clients from strategic centers across India, including Bangalore, Pune, Hyderabad, Chennai, Mumbai, and Noida.
As a fresher starting my professional career, I see relocation as an incredible opportunity to experience new engineering hubs, collaborate with diverse teams, and adapt to high-impact client engagements."
</div>

<h2>Scenario 2: "Are you comfortable working in rotational shifts or supporting client timezones?"</h2>
<div class="code-block">
Model Response:
"Yes, completely comfortable. In modern IT consulting, enterprise systems operate 24/7 across US, European, and APAC client timezones.
During college hackathons and project submissions, I regularly worked late hours and managed tight turnarounds. As long as team communication is clear, I am flexible with shift rotations."
</div>

<h2>Scenario 3: "Tell me about a time you had a serious disagreement with a team member."</h2>
<div class="code-block">
Model Response (STAR Framework):
- Situation: During our third-year database project, our frontend lead wanted to use Firebase for quick setup, while I advocated for PostgreSQL.
- Task: We needed to decide on our architecture without delaying sprint deadlines or causing interpersonal friction.
- Action: Rather than arguing subjectively, I benchmarked both options: I showed our schema required complex relational joins and ACID constraints that Firebase would make cumbersome. I scheduled a polite discussion where we weighed trade-offs objectively.
- Result: The team agreed on PostgreSQL, and our final project delivered seamless transaction handling with zero data inconsistencies, earning an 'A' grade.
</div>

<h2>Scenario 4: "Why should Capgemini hire you over other candidates today?"</h2>
<div class="code-block">
Model Response:
"While many candidates bring strong academic credentials, I bring three distinct assets:
1. Strong fundamentals in Data Structures, AI literacy, and system design, proven through rigorous practical preparation.
2. A demonstrated ability to quickly learn new frameworks and adapt, as evidenced by my hands-on full-stack projects.
3. Complete alignment with Capgemini's core values of Honesty, Boldness, and Team Spirit, ensuring I hit the ground running as a collaborative, dependable software engineer."
</div>
"""
            }
        ]
    }

    # Write out as JavaScript file
    js_content = "// =======================================================================\n"
    js_content += "// CAPPREP PRO — OFFICIAL COMPREHENSIVE TEXTBOOK-GRADE STUDY COMPENDIUM\n"
    js_content += "// Capgemini Exceller Recruitment Exam Curriculum (Batch 2026 - 2027)\n"
    js_content += "// Fully detailed, step-by-step explanatory notes across all 6 stages.\n"
    js_content += "// Generated with 33 Deep Chapters: Diagrams, Trace Tables, Real Questions.\n"
    js_content += "// =======================================================================\n\n"
    js_content += "const STAGE_DOCS = " + json.dumps(docs, indent=2, ensure_ascii=False) + ";\n\n"
    js_content += "if (typeof module !== 'undefined' && module.exports) {\n"
    js_content += "  module.exports = { STAGE_DOCS };\n"
    js_content += "}\n"

    target_path = r"C:\cap\ai\js\study_docs.js"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully generated {target_path} ({len(js_content)} bytes)")

if __name__ == "__main__":
    build_docs()
