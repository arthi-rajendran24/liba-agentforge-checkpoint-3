# AgentForge / Project Monsoon

Run: example-baseline · Team: example-team · 2026-09-03T03:26:19.771525+00:00
Mode: rehearsal · Challenge: baseline · Status: completed

Fictional teaching inputs; unit economics, channels and candidates extend the original workshop scenario. Not market forecasts.

Human review is required before action.

## Scenario snapshot
```json
{
  "name": "Project Monsoon",
  "company": "Aster Foods \u00b7 fictional",
  "brief": "Launch a shelf-stable millet snack in Chennai and Bengaluru within 12 weeks, protecting customer trust and cash runway.",
  "budget": 2400000,
  "units": 30000,
  "price": 120,
  "unit_cost": 65,
  "fixed_cost": 250000,
  "marketing_budget": 180000,
  "margin_target": 38,
  "launch_days": 84,
  "lead_days": 21,
  "production_per_day": 600,
  "team_fte": 8,
  "required_fte": 10,
  "hire_cost": 10000,
  "required_skills": [
    "planning",
    "communication"
  ],
  "candidates": [
    {
      "candidate_id": "C-101",
      "skills": [
        "planning",
        "communication",
        "logistics"
      ],
      "work_sample_score": 82.0
    },
    {
      "candidate_id": "C-102",
      "skills": [
        "planning",
        "data analysis"
      ],
      "work_sample_score": 91.0
    },
    {
      "candidate_id": "C-103",
      "skills": [
        "communication",
        "sales"
      ],
      "work_sample_score": 77.0
    }
  ],
  "signals": [
    {
      "channel": "Retail trials",
      "responses": 120,
      "positive": 92,
      "previous_positive_rate": 0.7
    },
    {
      "channel": "Creator sampling",
      "responses": 90,
      "positive": 71,
      "previous_positive_rate": 0.72
    },
    {
      "channel": "Campus survey",
      "responses": 150,
      "positive": 98,
      "previous_positive_rate": 0.68
    }
  ],
  "labelling_concern": false,
  "evidence_note": "Fictional teaching inputs; unit economics, channels and candidates extend the original workshop scenario. Not market forecasts."
}
```

## PRISM / Analytics

72.5% positive intent across 360 responses

Use channel-level signals to design a small controlled launch. Track conversion, repeat purchase, complaints and contribution margin weekly.

### Calculated metrics
- responses: 360
- positive_pct: 72.5
- trend_pp: 2.83
- interval_low_pct: 67.67
- interval_high_pct: 76.86

### Source evidence
- scenario.signals: 261/360 positive responses; weighted previous rate 0.6967.
- 95% Wilson binomial interval, z=1.96; descriptive only.

### Assumptions
- All source inputs are fictional workshop data.
- Responses are treated as independent for the interval; representativeness is unverified.

### Risks
- Convenience samples can overstate demand; responses are not sales.

### Actions
- **Analytics**: Measure purchases / eligible trial participants by channel — Gate: Weekly review with channel denominators

### Detail worksheet
```json
[
  {
    "channel": "Retail trials",
    "responses": 120,
    "positive_pct": 76.67,
    "change_pp": 6.67
  },
  {
    "channel": "Creator sampling",
    "responses": 90,
    "positive_pct": 78.89,
    "change_pp": 6.89
  },
  {
    "channel": "Campus survey",
    "responses": 150,
    "positive_pct": 65.33,
    "change_pp": -2.67
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
72.5% positive intent across 360 responses

Use channel-level signals to design a small controlled launch. Track conversion, repeat purchase, complaints and contribution margin weekly.

scenario.signals: 261/360 positive responses; weighted previous rate 0.6967.
95% Wilson binomial interval, z=1.96; descriptive only.

## PULSE / Marketing

Start with creator sampling

Run a measured sampling pilot with the strongest observed channel; review conversion before expanding spend.

### Calculated metrics
- campaign_budget_inr: 180000
- allocated_inr: 180000.0
- channels: 3
- trust_gate: review

### Source evidence
- scenario.signals and scenario.marketing_budget; allocation proportional to positive counts.
- analytics hand-off: 72.5% positive intent across 360 responses

### Assumptions
- All source inputs are fictional workshop data.
- Budget allocation is a teaching heuristic; no ROI is established.

### Risks
- Survey intent is not causal evidence of channel performance.

### Actions
- **Marketing**: Approve labelled draft copy and run a controlled pilot — Gate: Customer trust and claim review before publication

### Detail worksheet
```json
[
  {
    "channel": "Creator sampling",
    "budget_inr": 48965.52,
    "positive_pct": 78.89,
    "draft_message": "A millet snack for your workday. Explore ingredients before you try."
  },
  {
    "channel": "Retail trials",
    "budget_inr": 63448.28,
    "positive_pct": 76.67,
    "draft_message": "A millet snack for your workday. Explore ingredients before you try."
  },
  {
    "channel": "Campus survey",
    "budget_inr": 67586.2,
    "positive_pct": 65.33,
    "draft_message": "A millet snack for your workday. Explore ingredients before you try."
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
Start with creator sampling

Run a measured sampling pilot with the strongest observed channel; review conversion before expanding spend.

scenario.signals and scenario.marketing_budget; allocation proportional to positive counts.
analytics hand-off: 72.5% positive intent across 360 responses

## NOVA / Human Resources

Close a 2 FTE capacity gap

Review the anonymous skills worksheet, calibrate work samples and assign training or temporary staffing. The worksheet does not make hiring decisions.

### Calculated metrics
- available_fte: 8
- required_fte: 10
- gap_fte: 2
- staffing_cost_inr: 20000
- candidates: 3

### Source evidence
- scenario.team_fte=8; required_fte=10.
- Review score = 60% required-skill coverage + 40% work-sample score; only allowlisted candidate fields are accepted.

### Assumptions
- All source inputs are fictional workshop data.
- Staffing cost is a one-time workshop planning allowance per additional FTE, not a salary estimate.

### Risks
- Skills and sample scores may still contain bias; protected-attribute exclusion does not establish fairness.
- No demographic parity claim can be made from this anonymous dataset.

### Actions
- **HR**: Calibrate the rubric with a human reviewer and check accessibility — Gate: No candidate rejection or offer from this score
- **HR**: Plan capacity for 2 additional FTE — Gate: Finance approval of staffing allowance

### Detail worksheet
```json
[
  {
    "candidate_id": "C-101",
    "skill_coverage_pct": 100.0,
    "work_sample_score": 82.0,
    "review_score": 92.8,
    "missing_skills": "None",
    "decision": "Human review required"
  },
  {
    "candidate_id": "C-102",
    "skill_coverage_pct": 50.0,
    "work_sample_score": 91.0,
    "review_score": 66.4,
    "missing_skills": "communication",
    "decision": "Human review required"
  },
  {
    "candidate_id": "C-103",
    "skill_coverage_pct": 50.0,
    "work_sample_score": 77.0,
    "review_score": 60.8,
    "missing_skills": "planning",
    "decision": "Human review required"
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
Close a 2 FTE capacity gap

Review the anonymous skills worksheet, calibrate work samples and assign training or temporary staffing. The worksheet does not make hiring decisions.

scenario.team_fte=8; required_fte=10.
Review score = 60% required-skill coverage + 40% work-sample score; only allowlisted candidate fields are accepted.

## ATLAS / Operations

Production fits the launch window

Stage an initial release of at most 30,000 units. Reserve production capacity and validate supplier readiness before commitments.

### Calculated metrics
- production_days: 50
- completion_day: 71
- buffer_days: 13
- deliverable_units: 30000
- capacity_units: 37800
- shortfall_units: 0

### Source evidence
- Completion = 21 lead days + ceil(30000/600) = 71 days.
- Capacity = max(0, 84-21) × 600 = 37800 units.

### Assumptions
- All source inputs are fictional workshop data.
- The lead-time and production phases are sequential; lead time includes delivery to production.

### Risks
- Daily capacity is assumed constant; downtime, transit and quality failures are not modelled.

### Actions
- **Operations**: Confirm supplier milestone and alternate capacity — Gate: Supplier confirmation before production release

### Detail worksheet
```json
[
  {
    "phase": "Supply lead time",
    "days": 21
  },
  {
    "phase": "Production",
    "days": 50
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
Production fits the launch window

Stage an initial release of at most 30,000 units. Reserve production capacity and validate supplier readiness before commitments.

Completion = 21 lead days + ceil(30000/600) = 71 days.
Capacity = max(0, 84-21) × 600 = 37800 units.

## LEDGER / Finance

INR 0 cash headroom

The planned production fits the cash budget. Authorize spend only after staffing, supply and customer-trust reviews.

### Calculated metrics
- budget_inr: 2400000
- cash_required_inr: 2400000.0
- funding_gap_inr: 0
- headroom_inr: 0.0
- gross_margin_pct: 45.83
- margin_target_pct: 38
- break_even_units: 8182
- fixed_and_launch_cost_inr: 450000.0

### Source evidence
- Cash required = 30,000 × INR 65 + INR 250,000 fixed + INR 180,000 marketing + INR 20,000 staffing = INR 2,400,000.
- Gross margin = (120-65)/120 × 100.
- Revenue is constrained to 30000 deliverable units by Operations.

### Assumptions
- All source inputs are fictional workshop data.
- All units are financed upfront, unsold inventory retains its cost, and sold units collect cash immediately.
- Scenario contribution less fixed costs is not accounting net profit.

### Risks
- Taxes, financing, returns and payment collection delays are excluded.

### Actions
- **Finance**: Approve a cash plan and test downside sell-through — Gate: No spend approval until the funding and margin gates pass

### Detail worksheet
```json
[
  {
    "case": "Downside",
    "demand_units": 18000,
    "sold_units": 18000,
    "revenue_inr": 2160000,
    "contribution_less_fixed_inr": 540000.0,
    "cash_after_launch_inr": 2160000.0
  },
  {
    "case": "Base",
    "demand_units": 30000,
    "sold_units": 30000,
    "revenue_inr": 3600000,
    "contribution_less_fixed_inr": 1200000.0,
    "cash_after_launch_inr": 3600000.0
  },
  {
    "case": "Upside",
    "demand_units": 42000,
    "sold_units": 30000,
    "revenue_inr": 3600000,
    "contribution_less_fixed_inr": 1200000.0,
    "cash_after_launch_inr": 3600000.0
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
INR 0 cash headroom

The planned production fits the cash budget. Authorize spend only after staffing, supply and customer-trust reviews.

Cash required = 30,000 × INR 65 + INR 250,000 fixed + INR 180,000 marketing + INR 20,000 staffing = INR 2,400,000.
Gross margin = (120-65)/120 × 100.
Revenue is constrained to 30000 deliverable units by Operations.

## JARVIS / General Management

CONDITIONAL GO · executive launch recommendation

Proceed to a limited, human-approved pilot with weekly KPI review and explicit stop conditions.

### Calculated metrics
- decision: CONDITIONAL GO
- reports_received: 5
- blocked_gates: 0

### Source evidence
- analytics hand-off: 72.5% positive intent across 360 responses
- marketing hand-off: Start with creator sampling
- hr hand-off: Close a 2 FTE capacity gap
- operations hand-off: Production fits the launch window
- finance hand-off: INR 0 cash headroom

### Assumptions
- All source inputs are fictional workshop data.
- No specialist hold can be overridden by the synthesis agent.

### Risks
- All agent outputs remain decision support; an accountable human owns the launch.

### Actions
- **General Management**: Review every specialist gate and sign the executive package — Gate: Human approval required
- **Analytics**: Review launch KPIs with the team after the pilot — Gate: Pause if trust, cash or delivery assumptions fail

### Detail worksheet
```json
[
  {
    "agent": "analytics",
    "gate": "review",
    "finding": "72.5% positive intent across 360 responses"
  },
  {
    "agent": "marketing",
    "gate": "review",
    "finding": "Start with creator sampling"
  },
  {
    "agent": "hr",
    "gate": "review",
    "finding": "Close a 2 FTE capacity gap"
  },
  {
    "agent": "operations",
    "gate": "review",
    "finding": "Production fits the launch window"
  },
  {
    "agent": "finance",
    "gate": "review",
    "finding": "INR 0 cash headroom"
  }
]
```

### Agent commentary
[Rehearsal · computed evidence]
CONDITIONAL GO · executive launch recommendation

Proceed to a limited, human-approved pilot with weekly KPI review and explicit stop conditions.

analytics hand-off: 72.5% positive intent across 360 responses
marketing hand-off: Start with creator sampling
hr hand-off: Close a 2 FTE capacity gap
operations hand-off: Production fits the launch window
finance hand-off: INR 0 cash headroom
