# Akseler Analytics Dashboard - Specifikacija

**Versija:** 1.0  
**Sukurta:** 2026-02-10  
**Tikslas:** Interaktyvus realaus laiko veiklos dashboard su KPI vizualizacijomis

---

## 🎯 Dashboard Overview

Vieno lango principo valdymo centras, kuris agreguoja duomenis iš GHL, Newo Voice Agent ir išorinių šaltinių. Automatiškai generuoja įžvalgas ir siunčia alertus kritiniais atvejais.

---

## 📊 Pagrindiniai Widget'ai

### 1. Lead Funnel Visualization
```
┌─────────────────────────────────────────┐
│  LEAD FUNNEL - Šiandien                 │
├─────────────────────────────────────────┤
│  New Leads:     ████████░░  24 (+5)    │
│  Qualified:     ██████░░░░  18 (+3)    │
│  Proposals:     ████░░░░░░  12 (+2)    │
│  Negotiations:  ██░░░░░░░░   8 (+1)    │
│  Closed-Won:    █░░░░░░░░░   4 (+1)    │
├─────────────────────────────────────────┤
│  Konversija: 16.7%  │  Target: 20%    │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** GHL Opportunities pipeline stages  
**Atnaujinimas:** Realiu laiku (webhook)  
**Alertai:** Jei konversija < 15% per 7 dienas

---

### 2. Voice Agent Performance
```
┌─────────────────────────────────────────┐
│  VOICE AGENT - Šiandien                 │
├─────────────────────────────────────────┤
│  Calls Made:        47                 │
│  Connected:         28 (59.6%)         │
│  Appointments Set:   6 (21.4%)         │
│  Avg Call Duration: 2:34               │
│  Sentiment Score:   +0.72 🟢           │
├─────────────────────────────────────────┤
│  🏆 Top Script: Kaimynystės metodas    │
│  📉 Worst: Draudimo keitimas (-15%)    │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** Newo call logs + GHL appointments  
**Atnaujinimas:** Kas 15 minučių  
**Alertai:** Jei connected rate < 40%

---

### 3. Revenue Metrics
```
┌─────────────────────────────────────────┐
│  REVENUE - Šis Mėnuo                    │
├─────────────────────────────────────────┤
│                                         │
│  €45,200 ┤                    ╭─╮      │
│  €40,000 ┤         ╭─╮       │ │      │
│  €35,000 ┤    ╭─╮  │ │  ╭─╮  │ │      │
│  €30,000 ┤╭─╮ │ │  │ │  │ │  │ │      │
│  €25,000 ┤│ │ │ │  │ │  │ │  │ │  ╭─╮ │
│          └┴─┴─┴─┴──┴─┴──┴─┴──┴─┴──┴─┴─┘
│          W1   W2   W3   W4   W5        │
├─────────────────────────────────────────┤
│  Target: €50,000 │ Progress: 90.4%     │
│  vs Praeitas mėn: +23% 🟢              │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** GHL Opportunities (won deals)  
**Atnaujinimas:** Kas valandą + manual refresh  
**Alertai:** Jei < 80% target su likusia savaite

---

### 4. Activity Heatmap
```
┌─────────────────────────────────────────┐
│  ACTIVITY HEATMAP - Paskutinės 30 d.    │
├─────────────────────────────────────────┤
│     Pir  Ant  Tre  Ket  Pen  Šeš  Sek   │
│ 09  🟡   🟢   🟢   🟢   🟡   ⚪   ⚪    │
│ 10  🟢   🟢   🟢   🟢   🟢   🟡   ⚪    │
│ 11  🟢   🟢   🔥   🟢   🟢   ⚪   ⚪    │
│ 12  🟡   🟢   🟢   🟢   🟡   ⚪   ⚪    │
│ 13  🟢   🟢   🟢   🟢   🟢   ⚪   ⚪    │
│ 14  🟢   🔥   🟢   🟢   🟢   🟡   ⚪    │
│ 15  🟢   🟢   🟢   🟡   🟢   ⚪   ⚪    │
│ 16  🟡   🟢   🟢   🟢   🟢   ⚪   ⚪    │
│ 17  🟢   🟢   🟢   🟢   🟡   ⚪   ⚪    │
├─────────────────────────────────────────┤
│  🟢 > 5 activities │ 🔥 > 10 activities │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** GHL tasks + calls + emails  
**Atnaujinimas:** Kas valandą  
**Įžvalgos:** Optimalūs skambučių laikai

---

### 5. Lead Source Breakdown
```
┌─────────────────────────────────────────┐
│  LEAD SOURCES - Šis Mėnuo               │
├─────────────────────────────────────────┤
│                                         │
│  Facebook Ads   ████████████████████ 35%│
│  Referrals      ██████████████ 28%      │
│  Google Ads     ██████████ 22%          │
│  Cold Calling   ██████ 12%              │
│  Website        ██ 3%                   │
│                                         │
├─────────────────────────────────────────┤
│  💰 Best ROI: Referrals (€0 cost)      │
│  📈 Growing: Google Ads (+15% MoM)     │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** GHL contact source field  
**Atnaujinimas:** Kasdien  
**Alertai:** Jei vienas šaltinis > 60% (priklausomybės rizika)

---

### 6. Follow-up Queue
```
┌─────────────────────────────────────────┐
│  FOLLOW-UP QUEUE                        │
├─────────────────────────────────────────┤
│  🔴 CRITICAL (24h)          3 leads     │
│     └─ J. Petraitis - laukia pasiūlymo  │
│     └─ A. Jonaitienė - reikalingas call │
│     └─ M. Kazlauskas - callback pažadėta│
│                                         │
│  🟡 NORMAL (> 48h)         12 leads     │
│  🟢 SCHEDULED               8 leads     │
├─────────────────────────────────────────┤
│  [Peržiūrėti visus]  [Auto-prioritize]  │
└─────────────────────────────────────────┘
```

**Duomenų šaltinis:** GHL tasks + last activity timestamp  
**Atnaujinimas:** Realiu laiku  
**Alertai:** Push notification kai atsiranda CRITICAL

---

## 🔔 Alert Sistema

### Critical Alerts (Instant SMS + Email)
- Lead neatsakytas > 24h
- Didelis deal (€10k+) pereina į Closed-Lost
- Voice agent down > 30 min
- Revenue target < 50% su likusia puse mėnesio

### Warning Alerts (Email summary kas 4h)
- Follow-up queue > 20 leads
- Konversija žemiau targeto 3 dienas iš eilės
- Specific ad campaign ROI < 1.5
- Unusual activity drop (pvz., 0 calls per 2h)

### Daily Digest (8:00 AM)
- Yesterday's summary
- Today's priorities
- Week-over-week trends
- Upcoming appointments

---

## 🛠️ Techninė Implementacija

### Stack Rekomendacija
```
Frontend:  React + Recharts (grafikai)
Backend:   Python FastAPI + WebSocket (real-time)
Database:  PostgreSQL (time-series: TimescaleDB)
Cache:     Redis (real-time widget'ams)
Hosting:   VPS (DigitalOcean/Vultr) arba Vercel + Railway
```

### GHL Integracija
```python
# Webhook handler pseudocode
@app.post("/webhook/ghl")
async def ghl_webhook(payload):
    event_type = payload["type"]
    
    if event_type == "OpportunityStatusUpdate":
        await update_funnel_widget(payload)
        await check_conversion_alerts()
    
    elif event_type == "TaskCreate":
        await update_followup_queue()
    
    elif event_type == "ContactCreate":
        await update_lead_sources()
        await increment_daily_counter()
```

### Newo Integracija
```python
# Voice agent metrics polling
async def poll_newo_metrics():
    calls = await newo_api.get_calls(since="15m")
    
    metrics = {
        "total_calls": len(calls),
        "connected": sum(1 for c in calls if c.duration > 30),
        "appointments": sum(1 for c in calls if c.outcome == "appointment_set"),
        "avg_duration": mean(c.duration for c in calls),
        "sentiment": analyze_sentiment(calls)
    }
    
    await redis.publish("voice_widget", metrics)
```

---

## 📱 Mobile App (Optional Phase 2)

### Key Features
- Push notifications for CRITICAL alerts
- Quick actions (call lead, mark as done)
- Voice-to-notes (užrašai po pokalbio)
- Offline mode with sync

### Tech Stack
- React Native arba Flutter
- Shared backend su web dashboard

---

## 🚀 Implementation Roadmap

### Phase 1: MVP (2 savaitės)
- [ ] Basic funnel widget
- [ ] Revenue metrics
- [ ] Follow-up queue
- [ ] Daily email digest

### Phase 2: Real-time (1 savaitė)
- [ ] WebSocket integration
- [ ] Live activity heatmap
- [ ] Push notifications

### Phase 3: Advanced (2 savaitės)
- [ ] AI-powered insights (trend prediction)
- [ ] Custom report builder
- [ ] Mobile app

### Phase 4: Automation (1 savaitė)
- [ ] Auto-prioritize follow-ups
- [ ] Smart scheduling suggestions
- [ ] ROI optimization recommendations

---

## 💡 Unikalūs Features (Differentiators)

### 1. ADHD-Optimized UI
- Dideli skaičiai, aiškios spalvos
- Vienas pagrindinis metric per ekraną
- "Focus mode" - viskas paslėpta, tik vienas widget
- Quick actions (vienas click = veiksmas)

### 2. Voice Command Support
- "Kiek leadų šiandien?"
- "Rodyk critical follow-ups"
- "Koks šio mėnesio target?"
- Integracija su Newo voice agent

### 3. Predictive Alerts
- "Šiandien nepaskambinsi pakankamai - reikia +5 skambučių"
- "Ši savaitė silpna - fokusuokis ant referrals"
- "3 leadai šiandien nebus pasiekiami (pattern from history)"

### 4. Gamification
- Daily streaks (kiekvieną dieną X activities)
- Weekly challenges (pvz., „+10% konversija")
- Badges (Cold Call King, Follow-up Master)
- Leaderboard (jei ateityje komanda didėja)

---

## 📈 Expected Impact

| Metrika | Before | After 30d | After 90d |
|---------|--------|-----------|-----------|
| Lead response time | 4h | 1h | 30min |
| Follow-up completion | 60% | 85% | 95% |
| Revenue visibility | Manual | Real-time | Predictive |
| Decision speed | Days | Hours | Minutes |
| Admin time/day | 45min | 20min | 10min |

---

## 🔐 Security & Privacy

- HTTPS everywhere
- API key rotation every 90 days
- Rate limiting (prevent abuse)
- Audit log (kas matė ką)
- GDPR-compliant data retention

---

## 💰 Cost Estimate

### Development
- Phase 1 MVP: €3,000-5,000 (freelancer) arba 40h (DIY)
- Phase 2-4: €2,000-4,000 papildomai

### Monthly Operations
- VPS hosting: €20-50/mėn
- Database: €15-30/mėn
- Monitoring: €10/mėn
- **Total: ~€50-90/mėn**

### ROI
- Admin time saved: 30min/day × €50/h = €25/diena = €625/mėn
- Faster follow-ups → +10% conversion = €5,000+/mėn
- **Payback: < 1 mėnuo**

---

## 📝 Next Steps

1. **Patvirtinti prioritetus** - kurie widget'ai svarbiausi
2. **Pasirinkti tech stack** - DIY vs freelancer vs agency
3. **GHL webhook setup** - technical foundation
4. **Start Phase 1** - MVP kūrimas

---

**Sukurta autonomiškai pagal HEARTBEAT.md instrukcijas**  
**Kauliukas: 70 → 📈 Badaujantis tikslas → 🎁 Staigmena CEO**
