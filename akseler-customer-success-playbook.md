# Akseler Customer Success & Retention Playbook
## Klientų Išlaikymo ir Upsell Žaidimo Vadovas

**Versija:** 1.0  
**Sukurta:** 2026-02-10  
**Tikslas:** Transformuoti vienkartinius pirkėjus į 25-metų partnerius ir referalų šaltinį

---

## 💡 Kodėl Tai Svarbu?

| Metrika | Kaina | Vertė |
|---------|-------|-------|
| Naujo leado įsigijimas | €150-400 | Vienkartinė |
| Eksistuojančio kliento išlaikymas | €10-25 | Metinė |
| Referalas iš patenkinto kliento | €0 | €5,000-50,000 vertės |
| Upsell (baterija/EV/šilumos siurblys) | €50 marketingo | €15,000-40,000 vertės |

**Faktas:** Saulės instaliacijos trunka 25+ metų. Per tą laiką patenkintas klientas gali atnešti 3-5 referalų ir pirkti papildomas paslaugas.

---

## 🎯 4 Fazės Kliento Kelionėje

### FAZĖ 1: Onboarding (0-30 dienų) - "Honeymoon"
**Tikslas:** Pašalinti pirkėjo kaltę, sukurti džiaugsmą

#### Savaitė 1: Instaliacija
- [ ] **Dieną 0:** Sveikinimo SMS + nuotraukų galerija "Jūsų sistema auga"
- [ ] **Dieną 1:** Įdiegimo komandos intro + kontaktai
- [ ] **Dieną 3:** Progreso nuotrauka (jei stogas)
- [ ] **Dieną 7:** Instaliacija baigta - šampano emoji SMS 🍾

#### Savaitė 2-4: Aktyvavimas
- [ ] **Dieną 14:** Pirmas energijos ataskaitos email
  ```
  Subject: Jūs jau sutaupėte €47! ☀️
  
  Labas [Vardas],
  
  Jūsų saulės sistema dirba 14 dienų ir jau:
  ⚡ Pagaminta: 245 kWh
  💰 Sutaupyta: €47
  🌳 CO2 kompensuota: 122 kg
  
  Tai lygu 6 medžiams auginti metus!
  
  [Mygtukas: Peržiūrėti realiu laiku]
  ```
- [ ] **Dieną 21:** Mobilios aplikacijos setup guide (video)
- [ ] **Dieną 30:** Mėnesio santrauka + pirmasis satisfaction check

### FAZĖ 2: Įprasminimas (1-6 mėnesiai) - "Routine Joy"
**Tikslas:** Įpročio sukūrimas, bendruomenės jausmas

#### Mėnesinis Ritualas
- [ ] **Kiekvieno mėnesio 1-oji:** Automatinė ataskaita email
  - Sutaupymas vs prognozė
  - Gamyba vs kaimynai (anonymized ranking)
  - Sezono patarimai
  - Referral CTA (subtelus)

#### Ketvirtinis Ritualas
- [ ] **Kas 3 mėnesius:** "Saulės sveikatos patikrinimas"
  - Sistemos efektyvumo auditas
  - Nemokamas panelių valymas offer (jei reikia)
  - Naujienlaiškis: technologijos, kainos, pokyčiai

### FAZĖ 3: išplėtimo (6-18 mėnesių) - "Expansion Ready"
**Tikslas:** Paruošti upsell, surinkti social proof

#### Upsell Triggers
| Signalas | Timing | Action |
|----------|--------|--------|
| Overproducing (generuoja 120%+) | 6 mėn | Baterijos pasiūlymas |
| EV pirkimas | Real-time | Wallbox integracija |
| Šildymo sezonas | Rugsėjis | Šilumos siurblys |
| Elektros kainų šuolis | News moment | "Apsauga nuo kainų" call |

#### Referal Program Launch (6 mėn)
- [ ] **Laikas:** Po 2-3 mėnesių gerų duomenų
- [ ] **SMS:** 
  ```
  Labas [Vardas]! Jūsų sistema dirba puikiai - jau sutaupėte €312. 
  Ar pažįstate ką nors, kas irgi norėtų mažesnių sąskaitų? 
  Už kiekvieną draugą, kuris įsirengs - €200 jums arba 2 metų garantijos pratęsimas. 
  Pasidalinkite: [Referral Link]
  ```

### FAZĖ 4: Ilgalaikė vertė (2-25 metai) - "Partnership"
**Tikslas:** Būti pirmu pasirinkimu visiems energy-related klausimams

#### Metinis Ritualas
- [ ] **Gimtadienio SMS:** "Jūsų saulės sistemai 1 metai! 🎂"
  - Metų santrauka: kWh, €, CO2
  - Nuožmėjimas vs pradinė prognozė
  - Atsinaujinimo pasiūlymai

#### Proaktyvi Priežiūra
- [ ] **5 metai:** Inverter warranty check
- [ ] **10 metai:** Panelių efektyvumo auditas
- [ ] **15 metai:** Atsinaujinimo pasiūlymas (nauja technologija)

---

## 📊 Customer Success Dashboard (GHL)

### Kontaktų Tag'ai
```
Lifecycle:
- onboarding-week-1
- onboarding-month-1  
- active-customer-6m
- active-customer-1y
- active-customer-5y
- expansion-ready
- champion (referral gavęs)
- at-risk (neatsako 60d)

Product:
- solar-only
- solar+battery
- solar+ev
- solar+heatpump
- full-stack

Engagement:
- high-opener (email >50%)
- mobile-app-active
- portal-inactive (nerašo 90d)
- referral-source
- referral-sent
```

### Custom Fields (GHL)
| Field | Type | Purpose |
|-------|------|---------|
| installation_date | Date | Lifecycle triggers |
| system_size_kwp | Number | Upsell scoring |
| monthly_production_kwh | Number | Health monitoring |
| annual_savings_eur | Number | Referral messaging |
| satisfaction_score | 1-10 | Risk flag |
| nps_score | -100 to 100 | Champion identification |
| referral_count | Number | Loyalty tier |
| last_service_date | Date | Proactive maintenance |
| warranty_expiry | Date | Renewal opportunities |

---

## 🔄 GHL Automation Workflows

### Workflow 1: New Customer Onboarding Sequence
**Trigger:** Opportunity status = "Closed Won"

```
Day 0: SMS "Sveikiname! Jūsų saulės kelias prasideda 🌞"
Day 1: Email "Kas nutiks per ateinančias 30 dienų"
Day 3: SMS instaliacijos datos confirmacija
Day 7: SMS "Jūsų komanda dirba! [Nuotrauka]"
Day 14: Email "Jūsų pirmosios 2 savaitės: €X sutaupyta"
Day 21: Email "Kaip skaityti savo energijos duomenis"
Day 30: SMS "1 mėnuo kartu! Jūsų rezultatai: [Link]"
```

### Workflow 2: Monthly Engagement Report
**Trigger:** 1st of month, all active customers

```
Email Subject: [Vardas], jūsų saulės ataskaita 📊

Content Blocks:
1. Hero: €Y sutaupyta šį mėnesį
2. Chart: Gamyba vs suvartojimas
3. Comparison: Jūs vs kaimynai (top 20%?)
4. Seasonal tip: "Vasario patarimas: sniego valymas"
5. Soft CTA: "Pažįstate ką nors, kas irgi norėtų?"
```

### Workflow 3: Expansion Opportunity Scoring
**Trigger:** Monthly, custom logic

```
IF system_age_months >= 6 
   AND avg_monthly_generation > (system_size * 1.2)
   AND battery = false
THEN
   Tag: "battery-upsell-candidate"
   Wait: 7 days
   Email: "Ar žinojote, kad galėtumėte dar daugiau sutaupyti?"
```

### Workflow 4: Referral Program Activation
**Trigger:** satisfaction_score >= 8 OR nps >= 50

```
Day 0: SMS "Džiaugiamės, kad esate patenkinti! Padėkite kitiems atrasti saulę 🌞"
Day 7: Email "Kaip veikia mūsų referral programa"
Day 30: SMS "€200 jums arba garantijos pratęsimas už kiekvieną draugą"
Day 90: Quarterly check-in + soft ask
```

### Workflow 5: At-Risk Re-engagement
**Trigger:** No email open 60 days AND no portal login 90 days

```
Tag: "at-risk"
Day 0: SMS "Viskas gerai su jūsų sistema?"
Day 3: Email "Pastebėjome, kad nesilankote portale"
Day 7: Call task sužadinimas (personal touch)
Day 14: SMS "Nemokamas sistemos patikrinimas - garantuojame"
```

---

## 📧 Email Templates Library

### Template 1: Monthly Report
```
Subject: [Vardas], jūsų saulės ataskaita | [Menuo] 2026

Labas [Vardas],

Jūsų saulės sistema [Menuo] mėnesį pagamino [X] kWh energijos.

💰 Sutaupyta: €[Y]
📊 Vidutinis dienos gamyba: [Z] kWh
🏆 Lyginant su kaimynais: Top [20%]

Šio mėnesio patarimas:
[Sezoninis patarimas - pvz. "Vasario sniegas: nusivalykite panes saulėtą dieną"]

Ar pažįstate ką nors, kas irgi norėtų mažesnių sąskaitų?
Pasidalinkite savo patirtimi: [Referral Link]

Į sveikatą,
Akseler Komanda
```

### Template 2: Upsell - Battery
```
Subject: Jūsų sistema gamina daugiau nei naudojate ⚡

Labas [Vardas],

Analizavome jūsų sistemos duomenis ir pastebėjome:

📈 Jūsų saulės sistema generuoja 25% daugiau energijos, 
   nei jūs suvartojate dienos metu
💸 Ši perteklinė energija grįžta į tinklą už mažesnį įkainį
🔋 Su baterija galėtumėte išsaugoti šią energiją vakarui

Skaičiavimas:
- Dabartinė sistema: [X] €/mėn sutaupyta
- Su baterija: [X + 40%] €/mėn sutaupyta
- Investicija atsiperka per 6-8 metus

Ar norėtumėte nemokamos konsultacijos apie baterijos pridėjimą?
[Mygtukas: Suplanuoti pokalbį]

Pagarbiai,
[Account Manager]
```

### Template 3: Referral Ask (Post-NPS)
```
Subject: Jūsų nuomonė mums svarbi (ir gali atnešti €200)

Labas [Vardas],

Dėkojame už pasitikėjimą Akseler! Džiugu, kad esate patenkinti savo sistema.

Jūs jau sutaupėte €[X] ir kompensavote [Y] kg CO2.

Ar pažįstate šeimą ar draugą, kuris irgi svajoja apie mažesnes sąskaitas?

🎁 Jums: €200 arba 2 metų garantijos pratęsimas
🎁 Draugui: €300 nuolaida naujai sistemai

Pasidalinkite savo saulės istorija:
[Referral Link]

Arba tiesiog atsakykite į šį laišką su draugo kontaktais - susisieksime asmeniškai.

Ačiū, kad esate mūsų klientas!

Akseler Komanda
```

### Template 4: 1-Year Anniversary
```
Subject: Jūsų saulės sistemai 1 metai! 🎂

Labas [Vardas],

Prieš lygiai metus įsijungėte savo saulės sistemą.

Metų santrauka:
☀️ Pagaminta energijos: [X] MWh
💰 Sutaupyta: €[Y]
🌳 Kompensuota CO2: [Z] kg (tai [N] medžių metai!)
📊 Efektyvumas: [105]% nuo pradinės prognozės

Jūsų sistema dirba [geriau/blogiau] nei tikėjomės!

Kiti metai atneš dar daugiau saulės. Ar jau galvojote apie:
- Baterijos pridėjimą?
- Elektromobilį?
- Šilumos siurblį?

Šviesių metų,
Akseler Komanda

P.S. Turite draugų, kurie vis dar galvoja? Šiuo metu turime €300 nuolaidą naujiems klientams.
```

---

## 📱 SMS Templates

### Short-form Updates
```
Sutaupymas alert: "Jūs jau sutaupėte €500! ☀️ Šio mėnesio ataskaita: [Link]"

Referral ask: "Patenkinti Akseler? Pasidalinkite su draugu! €200 jums, €300 jam. [Link]"

Seasonal tip: "Žiema ateina! Primename: saulė veikia ir per debesis. Stogo valymas: [Link]"

Service reminder: "Laikas metiniam patikrinimui? Nemokamas auditas laukia. Susisiekime: [Link]"
```

---

## 🎯 Referral Program Structure

### Tiers

| Tier | Requirement | Reward |
|------|-------------|--------|
| Bronze | 1 referral | €200 cash OR 2yr warranty extension |
| Silver | 3 referrals | €250 cash + 3yr extension + premium support |
| Gold | 5+ referrals | €300 cash + lifetime priority + VIP events |

### Mechanics
1. **Unique referral link** per customer (GHL tracking)
2. **Dual-sided incentive:** Referrer gets €200, Referee gets €300 off
3. **Payout timing:** After referee's installation complete
4. **Tracking:** GHL custom field `referral_count`

### Promotion Strategy
- Launch email to all customers 6m+
- Quarterly reminders to high-satisfaction segment
- Physical referral cards with installer (hand-to-hand)
- "Solar Ambassador" program for Gold tier (exclusive perks)

---

## 🔍 Success Metrics (KPIs)

### Monthly Tracking
```
Retention Metrics:
- Customer churn rate (target: <2%/year)
- 1-year retention (target: >95%)
- 5-year retention (target: >90%)

Engagement Metrics:
- Email open rate (target: >40%)
- Portal login frequency (target: 2x/month)
- Support ticket volume (target: <0.5/customer/year)

Growth Metrics:
- Referral rate (target: 15% of customers/year)
- Upsell conversion (target: 20% of candidates)
- NPS score (target: >50)
- Customer lifetime value (target: €2X acquisition cost)
```

### GHL Dashboard Setup
Create custom dashboard with:
1. Active customers by lifecycle stage
2. Revenue from upsells (monthly)
3. Referrals generated (monthly)
4. At-risk customer count
5. NPS trend
6. Support ticket categories

---

## ⚠️ Common Pitfalls & Solutions

| Problema | Sprendimas |
|----------|------------|
| Klientas neina į portalą | SMS su tiesiogine nuoroda į svarbią info |
| Referral nenori prašyti | Daryti tai natūraliai - po gerų naujienų |
| Upsell jaučiasi pushy | Fokusuoti į edukaciją, ne pardavimą |
| Email overload | Leisti pasirinkti dažnumą (monthly vs quarterly) |
| At-risk klientai nesijaučia | Personal touch - skambutis, ne tik automatika |

---

## 🚀 Implementation Checklist

### Week 1: Setup
- [ ] Sukurti GHL custom fields
- [ ] Sukurti contact tags
- [ ] Importuoti existing customers su data
- [ ] Setup basic lifecycle tags

### Week 2: Content
- [ ] Sukurti email templates (5)
- [ ] Sukurti SMS templates (10)
- [ ] Setup monthly report template
- [ ] Paruošti referral landing page

### Week 3: Automation
- [ ] Sukurti onboarding workflow
- [ ] Sukurti monthly report workflow
- [ ] Sukurti upsell scoring workflow
- [ ] Sukurti at-risk workflow
- [ ] Testuoti visas sekas

### Week 4: Launch
- [ ] Soft launch 10 klientams
- [ ] Surinkti feedback
- [ ] Adjustinti
- [ ] Full rollout

---

## 📞 Emergency Escalation

**When to escalate to human:**
- Satisfaction score <= 5
- Support ticket >48h unresolved
- At-risk klientas neatsako į 3 bandymus
- Referral complaint
- Warranty claim

**Escalation path:**
1. Automation tags "urgent-attention"
2. Task assigned to account manager
3. 4h response time commitment
4. Personal call within 24h

---

## 🎓 Best Practices

1. **Under-promise, over-deliver:** Jei prognozuojate 8000 kWh, o gaunate 8500 - klientas džiaugiasi
2. **Celebrate milestones:** 1000 kWh, €100 sutaupyta, 1 metai - visi šventi
3. **Be proactive, not reactive:** Skambinti PRIEŠ nei problema išauga
4. **Make them heroes:** Klientai didžiuojasi savo saulės sistema - duoti dalintis
5. **Human touch matters:** Automatika 80%, asmeninis dėmesys 20%

---

## 📚 Related Documents

- `akseler-daily-operations-playbook.md` - Kasdienės operacijos
- `akseler-sms-marketing-templates.md` - SMS šablonai
- `akseler-email-marketing-strategy.md` - Email strategija
- `akseler-voice-agent-playbook.md` - Voice agentai
- `ghl-solar-automation.py` - Python automatizavimas
- `ghl-workflows.md` - GHL workflow pavyzdžiai

---

**Sukūrė:** Juodčkis 🐾  
**Akseler AI Team**
