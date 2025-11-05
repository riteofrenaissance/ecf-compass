## 🗺️ Application Structure

The Cognitive Compass is a multi-page web application with 5 main sections:

---

### 🏠 Dashboard (`/dashboard`)

**Main control center** showing aggregate metrics across all AI systems.

**Features:**
- 📊 Total systems tracked (10)
- 📈 Overall sovereignty score (75.9%)
- 📉 Average knowledge gaps (30.5%)
- 🎯 Quick system overview
- ➕ Add new AI system button

**Use for:**
- Daily check-in on sovereignty status
- Quick overview of all systems
- Identifying which AIs need attention

**URL:** [app-5c655e46.base44.app/dashboard](https://app-5c655e46.base44.app/dashboard)

---

### 🤖 Systems (`/systems`)

**Individual AI system cards** with detailed per-system information.

**What you see:**
- List of all 10 tracked AIs
- Per-system sovereignty scores
- Gap percentages
- Status badges (نشط, قيد التقييم, غير موصى به)
- Action buttons (محادثة, عرض, حذف)

**AI Cards Include:**
```
┌─────────────────────────────┐
│  🧠 GPT-4                   │
│  OpenAI                     │
│  ─────────────────────────  │
│  الفجوة الإجمالية: 29.4%   │
│  درجة السيادة: 75%          │
│  [نشط] [محادثة] [عرض]      │
└─────────────────────────────┘
```

**Use for:**
- Comparing AI systems side-by-side
- Choosing which AI to use for a task
- Managing your AI portfolio

**URL:** [app-5c655e46.base44.app/systems](https://app-5c655e46.base44.app/systems)

---

### 📋 Assessments (`/assessments`)

**Historical evaluation tracking** with detailed three-dimensional breakdowns.

**Features:**
- ✅ Assessment history timeline
- 📅 Date-stamped evaluations
- 📊 Three-metric breakdown per assessment:
  - 🎯 Operational Awareness (35%)
  - 💭 Critical Engagement (40%)
  - 🛡️ Agency Preservation (25%)
- 📈 Detailed statistics:
  - تفاعلات (Interactions count)
  - أسئلة نقدية (Critical questions asked)
  - تحققات (Verification attempts)
  - قرارات مستقلة (Independent decisions)
- 💬 AI-specific insights and recommendations
- ➕ Add new assessment

**Example Assessment Card:**
```
┌─────────────────────────────────────┐
│  84.3%  DeepL Translator  🧠        │
│  ممتاز                              │
│  تاريخ التقييم: 01-02-2024          │
│  ─────────────────────────────────  │
│  🎯 الوعي التشغيلي      85%        │
│  💭 المشاركة النقدية    80%        │
│  🛡️ الحفاظ على الوكالة  90%        │
│  ─────────────────────────────────  │
│  45 تفاعلات | 5 أسئلة نقدية       │
│  20 تحققات  | 40 قرارات مستقلة     │
│  ─────────────────────────────────  │
│  "استخدام ممتاز - أداة واضحة مع    │
│   حدود محددة. أحتفظ بسيطرة كاملة"  │
└─────────────────────────────────────┘
```

**Tracked Assessments (Examples):**
- GPT-4 (15-01-2024): 65.3% → 69.8% (improvement!)
- Claude 3 (20-01-2024): 75.3%
- DeepL (01-02-2024): 84.3% ⭐

**Use for:**
- Tracking sovereignty evolution over time
- Comparing performance across different AIs
- Identifying improvement areas
- Validating training effectiveness
- Research data collection

**URL:** [app-5c655e46.base44.app/assessments](https://app-5c655e46.base44.app/assessments)

---

### 💬 Chat (`/chat`)

**Interactive conversation interface** (details to be confirmed).

**Likely features:**
- Direct AI interaction within the app
- Real-time sovereignty monitoring during chat
- Live gap detection
- Critical thinking prompts
- Verification suggestions

**URL:** [app-5c655e46.base44.app/chat](https://app-5c655e46.base44.app/chat)

---

### 📚 Resources (`/resources`)

**Educational materials** for improving cognitive sovereignty.

**Likely includes:**
- 📖 Guides on critical AI engagement
- 🎓 Tutorials for each AI system
- 📊 Best practices documentation
- 🔗 External resources
- ❓ FAQs

**URL:** [app-5c655e46.base44.app/resources](https://app-5c655e46.base44.app/resources)

---

## 🔄 User Flow

### Typical Usage Pattern:

```
1. Start → /dashboard
   ↓
   Quick overview of all systems
   
2. Need detail? → /systems
   ↓
   View individual AI cards
   
3. Choose AI → /chat (?)
   ↓
   Interact with AI
   
4. After interaction → /assessments
   ↓
   Log and evaluate
   
5. Learn more → /resources
   ↓
   Improve skills
   
6. Return to → /dashboard
   ↓
   See updated metrics
```

---

## 📊 Assessment Statistics Explained

### Four Key Metrics Per Assessment:

#### 1. **تفاعلات (Interactions)**
Total number of conversations or uses with the AI.
- **Example:** DeepL: 45 interactions

#### 2. **أسئلة نقدية (Critical Questions)**
How many times you questioned or verified the AI's output.
- **Good:** High number = active critical thinking
- **Example:** GPT-4: 12 questions (out of 45 interactions = 27%)

#### 3. **تحققات (Verifications)**
Number of times you fact-checked or confirmed information.
- **Good:** Higher = better verification habits
- **Example:** DeepL: 20 verifications (44%)

#### 4. **قرارات مستقلة (Independent Decisions)**
Decisions made with personal judgment, not just accepting AI output.
- **Good:** Close to interaction count = strong agency
- **Example:** DeepL: 40 independent decisions (89%)

---

## 🎯 Sovereignty Score Calculation

Based on assessment data:

```typescript
sovereignty = (
  operational_awareness * 0.35 +
  critical_engagement * 0.40 +
  agency_preservation * 0.25
)

// Influenced by:
critical_rate = critical_questions / interactions
verification_rate = verifications / interactions  
independence_rate = independent_decisions / interactions
```

---

## 📈 Progress Tracking

### Example: GPT-4 Improvement

```
Assessment 1 (15-01-2024):
  Sovereignty: 65.3%
  Critical Questions: 12/45 = 27%
  
Assessment 2 (Later date):
  Sovereignty: 69.8%
  Critical Questions: Still 12/45
  
→ +4.5% improvement
→ Suggests: Better awareness or agency, 
            but critical engagement stable
```

---

## 🔗 Quick Links

- **Dashboard:** [/dashboard](https://app-5c655e46.base44.app/dashboard)
- **All Systems:** [/systems](https://app-5c655e46.base44.app/systems)
- **Chat Interface:** [/chat](https://app-5c655e46.base44.app/chat)
- **Assessments:** [/assessments](https://app-5c655e46.base44.app/assessments)
- **Resources:** [/resources](https://app-5c655e46.base44.app/resources)

---

<div align="center">

**Navigate the Compass with confidence 🧭**

[Back to Main README](README.md)

</div>