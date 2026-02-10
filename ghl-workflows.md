# GHL Workflow Pavyzdžiai - Solar Leads

> Paruošta CEO (Akseler) - konkretūs workflow pavyzdžiai

---

## 🎯 Workflow 1: Naujo Leado Priėmimas

**Pavadinimas:** `New Solar Lead - Immediate Response`

### Trigger
- **Tipas:** Contact Created
- **Filtras:** Tag = "solar-lead" OR Source = "website-form"

### Veiksmai (seka):

1. **Add Tag** 
   - Tag: "new-lead-warm"

2. **Send SMS (Instant)**
   - Recipient: `{{contact.phone}}`
   - Žinutė:
   ```
   Labas {{contact.first_name}}! 👋 Gavau Jūsų užklausą dėl saulės elektrinės. 
   Skambinsiu per 15 min! - CEO, Akseler
   ```

3. **Create Task**
   - Pavadinimas: "Paskambinti {{contact.first_name}}"
   - Assigned to: CEO
   - Due: +15 minutes
   - Priority: High

4. **Add to Pipeline**
   - Pipeline: "Solar Sales"
   - Stage: "New Lead"

5. **Start Email Sequence**
   - Sequence: "Solar Lead Nurture"

---

## 📞 Workflow 2: Nepaskambinus per 1 valandą

**Pavadinimas:** `Lead Response Timeout - Alert`

### Trigger
- **Tipas:** Contact Tag Added
- **Tag:** "new-lead-warm"

### Wait
- **Laikas:** 1 hour

### Conditions (If/Else):
- **IF:** Contact has tag "contacted" → Do nothing
- **ELSE:** Continue

### Veiksmai:

1. **Send Notification**
   - To: CEO (Push + SMS)
   - Žinutė:
   ```
   ⚠️ ALERT: {{contact.first_name}} {{contact.last_name}} laukia skambučio jau 1 val!
   Tel: {{contact.phone}}
   ```

2. **Add Tag**
   - Tag: "urgent-followup"

3. **Send Internal Email**
   - To: CEO
   - Subject: "🚨 Urgent: Nepaskambinta lead"

---

## ✅ Workflow 3: Po Sėkmingo Pokalbio

**Pavadinimas:** `Post-Call - Proposal Sent`

### Trigger
- **Tipas:** Manual Trigger (arba Pipeline Stage Change)
- **Stage:** "Proposal Sent"

### Veiksmai:

1. **Remove Tag**
   - Tag: "new-lead-warm"

2. **Add Tag**
   - Tag: "proposal-sent"

3. **Send SMS (Follow-up)**
   - Delay: +2 hours
   - Žinutė:
   ```
   {{contact.first_name}}, siunčiau pasiūlymą el.paštu. 
   Ar matėte? Jei klausimų - skambinkite! 📞
   ```

4. **Create Task**
   - Pavadinimas: "Follow-up dėl pasiūlymo"
   - Due: +3 days
   - Priority: Medium

---

## 🔄 Workflow 4: Automatinis Follow-up (3 dienos)

**Pavadinimas:** `Proposal Follow-up Sequence`

### Trigger
- **Tipas:** Tag Added
- **Tag:** "proposal-sent"

### Wait
- **Laikas:** 3 days

### Conditions:
- **IF:** Contact has tag "proposal-accepted" → Stop
- **ELSE:** Continue

### Veiksmai:

1. **Send SMS**
   - Žinutė:
   ```
   Sveiki {{contact.first_name}}! Kaip Jums pasiūlymas? 
   Gal norėtumėte aptarti detales? 📋 - CEO, Akseler
   ```

2. **Create Task**
   - Pavadinimas: "Check-in po pasiūlymo"
   - Due: +1 day

---

## 💰 Workflow 5: Deal Won Celebration

**Pavadinimas:** `Deal Closed - Customer Onboarding`

### Trigger
- **Tipas:** Opportunity Status Changed
- **Status:** Won

### Veiksmai:

1. **Remove Tag**
   - Tag: "proposal-sent"

2. **Add Tag**
   - Tag: "customer-active"

3. **Send SMS**
   - Žinutė:
   ```
   🎉 Sveikiname {{contact.first_name}}! Jūsų saulės elektrinė bus įrengta netrukus. 
   Paskambinsiu dėl montavimo datos. Džiaugiuosi bendradarbiavimu! ☀️
   ```

4. **Create Task**
   - Pavadinimas: "Suplanuoti montavimą"
   - Due: +1 day
   - Priority: High

5. **Move to Pipeline**
   - Pipeline: "Customer Onboarding"
   - Stage: "Installation Scheduled"

6. **Internal Notification**
   - To: CEO
   - Message: "💰 Naujas deal! {{contact.first_name}} - {{opportunity.value}}€"

---

## 🎂 Workflow 6: Gimtadienio sveikinimas

**Pavadinimas:** `Birthday Wishes`

### Trigger
- **Tipas:** Date Based
- **Field:** Date of Birth
- **When:** On birthday, 9:00 AM

### Veiksmai:

1. **Send SMS**
   - Žinutė:
   ```
   {{contact.first_name}}, sveikinu gimtadienio proga! 🎂 
   Tegul saulė Jums šviečia kiekvieną dieną! ☀️ - CEO, Akseler
   ```

2. **Add Tag**
   - Tag: "birthday-wished-2026"

---

## 📊 Workflow 7: Neaktyvūs Leadai (Reactivation)

**Pavadinimas:** `Re-engage Cold Leads`

### Trigger
- **Tipas:** Contact Last Activity
- **Condition:** No activity for 30 days
- **Has Tag:** "solar-lead"
- **Does NOT Have:** "customer-active"

### Veiksmai:

1. **Add Tag**
   - Tag: "reactivation-campaign"

2. **Send SMS**
   - Žinutė:
   ```
   {{contact.first_name}}, praėjusį mėnesį domėjotės saulės elektrine. 
   Ar vis dar aktualu? Kaina gali būti dar patrauklesnė! 📉 - CEO, Akseler
   ```

3. **Create Task**
   - Pavadinimas: "Reactivation call"
   - Due: +2 days

---

## 🔧 Quick Setup Commands

Kai turėsi GHL priėjimą:

```bash
# Sukurti workflow
openclaw ghl workflow create --name "New Solar Lead" --trigger contact_created

# Sukurti pipeline stage
openclaw ghl pipeline stage --pipeline "Solar Sales" --stage "Proposal Sent"

# Priskirti tag
openclaw ghl contact tag --id {{contact.id}} --tag "solar-lead"
```

---

## 📈 Sėkmės Metrikos

Stebėti šiuos rodiklius:

| Metrika | Tikslas | Stebėjimas |
|---------|---------|------------|
| Lead response time | < 15 min | Automation log |
| SMS open rate | > 80% | GHL analytics |
| Proposal conversion | > 30% | Pipeline reports |
| Reactivation success | > 10% | Campaign stats |

---

**Sukurta:** 2026-02-10  
**Versija:** 1.0  
**Sekantis žingsnis:** Importuoti į GHL kai gausi credentials
