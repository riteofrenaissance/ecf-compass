# ECF Compass - Technical Architecture

**Version**: 1.0  
**Last Updated**: November 22, 2025  
**Status**: Production Development

---

## 🏗️ System Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  User Interface Layer                    │
│         (React Components + Tailwind CSS)               │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │  Input   │  │ Results  │  │ History  │             │
│  │  Form    │  │ Display  │  │ Timeline │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│              Business Logic Layer                        │
│                (Pure TypeScript)                         │
│                                                          │
│  ┌─────────────────────────────────────────────┐       │
│  │  Scoring Engine (scoring.ts)                │       │
│  │  - calculateSovereigntyScore()              │       │
│  │  - calculateGapAnalysis()                   │       │
│  │  - validateInput()                          │       │
│  └─────────────────────────────────────────────┘       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│            Services & Utilities Layer                    │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ i18n Service │  │  Storage     │  │  Analytics   │ │
│  │ (i18next)    │  │ (localStorage)│  │  (future)    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Component Architecture

### Component Hierarchy

```
App.tsx (Root Container)
│
├── Header
│   ├── Logo
│   ├── Title (i18n)
│   └── LanguageToggle
│       └── Button (AR ⇄ EN)
│
├── Main
│   ├── InputForm
│   │   ├── FormHeader
│   │   ├── DimensionSlider (Awareness)
│   │   │   ├── Label (i18n)
│   │   │   ├── RangeInput (0-100)
│   │   │   └── ValueDisplay
│   │   ├── DimensionSlider (Engagement)
│   │   └── DimensionSlider (Agency)
│   │   └── SubmitButton
│   │
│   ├── Results (conditional render)
│   │   ├── SovereigntyGauge
│   │   │   └── PieChart (Recharts)
│   │   ├── DimensionsChart
│   │   │   └── BarChart (Recharts)
│   │   └── GapAnalysis
│   │       ├── FunctionalGap
│   │       ├── EthicalGap
│   │       └── ExistentialGap
│   │
│   └── ResultsTimeline
│       └── ResultCard[] (last 50)
│
└── Footer
    ├── Copyright
    ├── Links
    └── Version
```

---

## 🔄 Data Flow Architecture

### Complete Assessment Flow

```
┌─────────────────┐
│   User Input    │
│  (3 sliders)    │
└────────┬────────┘
         │
         ↓
┌─────────────────────────────────┐
│   InputForm Component           │
│   - Captures: awareness,        │
│     engagement, agency          │
│   - Validates: 0-100 range      │
└────────┬────────────────────────┘
         │
         ↓ onSubmit
         │
┌─────────────────────────────────┐
│   App.tsx State Update          │
│   setState({                    │
│     awareness,                  │
│     engagement,                 │
│     agency                      │
│   })                            │
└────────┬────────────────────────┘
         │
         ↓ handleSubmit
         │
┌─────────────────────────────────────────┐
│   Scoring Engine                        │
│   calculateSovereigntyScore(input)      │
│                                         │
│   Formula:                              │
│   score = (OA×0.35) + (CE×0.40) +      │
│           (AP×0.25)                     │
│                                         │
│   Returns: ScoringResult {             │
│     sovereigntyScore: number,          │
│     dimensions: {...},                 │
│     gapAnalysis: {...},                │
│     timestamp: Date                    │
│   }                                    │
└────────┬────────────────────────────────┘
         │
         ↓
┌─────────────────────────────────┐
│   Update Application State      │
│   - setCurrentResult()          │
│   - setResults([new, ...old])   │
└────────┬────────────────────────┘
         │
         ├──→ Update UI Components
         │    (Results, Charts, Timeline)
         │
         └──→ Persist to LocalStorage
              localStorage.setItem(
                'ecf_compass_results',
                JSON.stringify(results)
              )
```

---

## 📊 Scoring Algorithm Architecture

### Core Formulas

#### 1. Sovereignty Score Calculation

```typescript
interface ScoringInput {
  awareness: number;   // 0-100
  engagement: number;  // 0-100
  agency: number;      // 0-100
}

function calculateSovereigntyScore(input: ScoringInput): number {
  // Validate and clean inputs
  const OA = clamp(input.awareness, 0, 100);
  const CE = clamp(input.engagement, 0, 100);
  const AP = clamp(input.agency, 0, 100);
  
  // Apply weighted formula
  const score = (OA * 0.35) + (CE * 0.40) + (AP * 0.25);
  
  // Round to 2 decimal places
  return Math.round(score * 100) / 100;
}
```

**Weight Rationale**:
- **Operational Awareness (35%)**: Foundation - understanding systems
- **Critical Engagement (40%)**: Core - active questioning (highest weight)
- **Agency Preservation (25%)**: Outcome - maintaining autonomy

#### 2. Gap Analysis Calculation

```typescript
interface GapAnalysis {
  functional: number;    // Gap in operational capabilities
  ethical: number;       // Gap in agency maintenance
  existential: number;   // Overall sovereignty gap
}

function calculateGapAnalysis(
  OA: number,
  CE: number, 
  AP: number,
  sovereigntyScore: number
): GapAnalysis {
  return {
    // Functional Gap: Average of OA & CE
    functional: 100 - ((OA + CE) / 2),    // Weight: 45%
    
    // Ethical Gap: Pure agency deficit
    ethical: 100 - AP,                     // Weight: 30%
    
    // Existential Gap: Total sovereignty deficit
    existential: 100 - sovereigntyScore   // Weight: 25%
  };
}
```

**Gap Interpretation**:
| Gap Value | Severity | Meaning |
|-----------|----------|---------|
| 0-25% | Low | Minor improvement needed |
| 25-50% | Moderate | Significant development area |
| 50-75% | High | Critical attention required |
| 75-100% | Critical | Urgent intervention needed |

---

## 💾 Data Architecture

### LocalStorage Schema

```typescript
interface StoredData {
  results: ScoringResult[];
  preferences: UserPreferences;
  metadata: StorageMetadata;
}

interface ScoringResult {
  sovereigntyScore: number;
  dimensions: {
    awareness: number;
    engagement: number;
    agency: number;
  };
  gapAnalysis: {
    functional: number;
    ethical: number;
    existential: number;
  };
  timestamp: Date;
  id: string; // UUID
}

interface UserPreferences {
  language: 'en' | 'ar';
  theme: 'light' | 'dark'; // future
  notifications: boolean;   // future
}

interface StorageMetadata {
  version: string;          // Schema version
  lastUpdate: string;       // ISO timestamp
  totalAssessments: number;
}
```

**Storage Keys**:
- `ecf_compass_results` - Assessment history (max 50)
- `ecf_compass_preferences` - User settings
- `ecf_compass_metadata` - System info

**Storage Limits**:
- Maximum results stored: 50 (FIFO)
- Estimated size per result: ~500 bytes
- Total storage usage: ~25KB

---

## 🌐 Internationalization Architecture

### i18next Configuration

```typescript
// i18n.ts structure
const resources = {
  en: {
    translation: {
      // App metadata
      'app.title': 'ECF Compass',
      'app.subtitle': 'Cognitive Sovereignty Assessment',
      
      // Dimensions
      'dimension.awareness': 'Operational Awareness',
      'dimension.engagement': 'Critical Engagement',
      'dimension.agency': 'Agency Preservation',
      
      // Results
      'result.sovereignty': 'Sovereignty Score',
      'result.gaps': 'Gap Analysis',
      
      // Actions
      'action.calculate': 'Calculate Score',
      'action.reset': 'Reset',
      
      // ... (100+ translation keys)
    }
  },
  ar: {
    translation: {
      // Corresponding Arabic translations
      'app.title': 'البوصلة المعرفية',
      // ...
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });
```

### RTL Support

```typescript
// Dynamic direction based on language
const direction = i18n.language === 'ar' ? 'rtl' : 'ltr';

// Applied at root level
<div dir={direction} className={direction === 'rtl' ? 'rtl' : 'ltr'}>
  {/* All content */}
</div>
```

**RTL Considerations**:
- Text alignment automatically reversed
- Margins/padding swapped (mr ↔ ml)
- Chart orientations maintained (LTR)
- Number formatting: consistent across languages

---

## 🎨 Styling Architecture

### Tailwind CSS Configuration

```javascript
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          // ... full scale
          900: '#0c4a6e'
        },
        sovereignty: {
          low: '#ef4444',      // Red (0-25%)
          moderate: '#f97316', // Orange (25-50%)
          good: '#eab308',     // Yellow (50-75%)
          excellent: '#16a34a' // Green (75-100%)
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        arabic: ['Cairo', 'sans-serif']
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography')
  ]
};
```

### Component Styling Pattern

```typescript
// Consistent className structure
<div className="
  // Layout
  flex flex-col items-center justify-between
  
  // Spacing
  p-4 md:p-6 gap-4
  
  // Sizing
  w-full max-w-4xl min-h-screen
  
  // Colors
  bg-white dark:bg-gray-900
  text-gray-900 dark:text-white
  
  // Effects
  shadow-lg rounded-lg
  transition-all duration-200
  
  // RTL support
  rtl:text-right
">
```

---

## 📈 Performance Architecture

### Optimization Strategies

#### 1. Code Splitting
```typescript
// Lazy loading for heavy components
const DimensionsChart = lazy(() => 
  import('./components/DimensionsChart')
);

// Used with Suspense
<Suspense fallback={<Spinner />}>
  <DimensionsChart data={dimensions} />
</Suspense>
```

#### 2. Memoization
```typescript
// Expensive calculations
const sovereigntyScore = useMemo(
  () => calculateSovereigntyScore(input),
  [input]
);

// Component optimization
const ResultsDisplay = memo(({ result }) => {
  // Only re-renders when result changes
});
```

#### 3. Virtual Scrolling
```typescript
// For history timeline (50+ items)
import { FixedSizeList } from 'react-window';

<FixedSizeList
  height={600}
  itemCount={results.length}
  itemSize={80}
>
  {ResultRow}
</FixedSizeList>
```

### Performance Metrics

| Metric | Target | Achieved (Prototype) |
|--------|--------|---------------------|
| First Contentful Paint | < 1.5s | ~1.2s |
| Time to Interactive | < 2.5s | ~2.0s |
| Largest Contentful Paint | < 2.5s | ~1.8s |
| Cumulative Layout Shift | < 0.1 | ~0.05 |
| Bundle Size (gzipped) | < 200KB | ~180KB |

---

## 🔐 Security Architecture

### Client-Side Security

#### 1. Input Validation
```typescript
function validateInput(value: number): number {
  // Type checking
  if (typeof value !== 'number') {
    throw new Error('Invalid input type');
  }
  
  // Range validation
  if (value < 0 || value > 100) {
    throw new Error('Input out of range');
  }
  
  // NaN protection
  if (isNaN(value)) {
    return 0;
  }
  
  return value;
}
```

#### 2. XSS Prevention
```typescript
// React automatically escapes by default
// Manual sanitization when needed
import DOMPurify from 'dompurify';

const clean = DOMPurify.sanitize(userInput);
```

#### 3. LocalStorage Security
```typescript
// No sensitive data stored
// Results are non-identifiable
// User can delete anytime

// Clear storage function
function clearAllData() {
  localStorage.removeItem('ecf_compass_results');
  localStorage.removeItem('ecf_compass_preferences');
}
```

### Privacy Principles
- ✅ No user authentication
- ✅ No server communication
- ✅ No tracking/analytics (in prototype)
- ✅ No cookies
- ✅ Data stays on device
- ✅ User controls deletion

---

## 🧪 Testing Architecture

### Testing Strategy

```
src/
├── utils/
│   ├── scoring.ts
│   └── scoring.test.ts       # Unit tests
├── components/
│   ├── InputForm.tsx
│   ├── InputForm.test.tsx    # Component tests
│   ├── SovereigntyGauge.tsx
│   └── SovereigntyGauge.test.tsx
└── App.test.tsx              # Integration tests
```

### Test Coverage Targets

| Layer | Target | Priority |
|-------|--------|----------|
| Scoring logic | 100% | Critical |
| Components | 80% | High |
| Integration | 70% | Medium |
| E2E | 50% | Medium |

---

## 🚀 Build & Deployment Architecture

### Development
```bash
npm run dev
# Vite dev server
# - Hot Module Replacement
# - Fast refresh
# - Source maps
# Port: 5000
```

### Production Build
```bash
npm run build
# Output: dist/
# - Minified JS/CSS
# - Code splitting
# - Asset optimization
# - Tree shaking
```

### Deployment Targets

#### Current (Prototype)
- **Platform**: Replit
- **URL**: Dynamic (Replit subdomain)
- **SSL**: Automatic
- **Updates**: Manual push

#### Planned (Production)
- **Platform**: base44.app
- **URL**: Custom domain
- **SSL**: Managed
- **CI/CD**: Automated

---

## 🔗 Integration Architecture

### Current Integrations
- None (fully client-side)

### Planned Integrations

#### 1. Research Data Export
```typescript
interface ExportFormat {
  format: 'json' | 'csv' | 'xlsx';
  results: ScoringResult[];
  metadata: ExportMetadata;
}
```

#### 2. Analytics (Optional)
```typescript
// Privacy-preserving analytics
interface AnalyticsEvent {
  event: string;
  anonymousId: string; // No PII
  timestamp: Date;
  properties: Record<string, any>;
}
```

---

## 📚 Related Documentation

- [Project Lifecycle](PROJECT_LIFECYCLE.md) - Development stages
- [README](../README.md) - Project overview
- [Contributing](../CONTRIBUTING.md) - Development guidelines

---

## 🔄 Architecture Evolution

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2025-11 | Initial prototype architecture |
| 1.0 | 2025-11 | Documentation of validated architecture |

### Future Considerations
- Microservices for analytics (optional)
- GraphQL API for data queries
- WebSocket for real-time features
- Service Worker for offline support

---

**Last Updated**: November 22, 2025  
**Maintained by**: Rite of Renaissance Research Foundation  
**Technical Lead**: Samir Baladi