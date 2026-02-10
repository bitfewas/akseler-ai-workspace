# Ginklu Klubas + Newo Backend - Jungties Analizė

**Data:** 2026-02-10  
**Scope:** Kaip Ginklu Klubas duomenys jungiasi su Newo CAMainFlow  
**Status:** Quick integration overview

---

## 🔄 PAGRINDINĖ JUNGČIŲ SCHEMA

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           VARTOTOJO SKAMBUTIS                                │
│                     (Phone / Chat / SMS / Telegram)                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NEWO VOICE INTEGRATION                               │
│  • V2V (Voice-to-Voice) mode: ON                                            │
│  • Voice: Erinome                                                            │
│  • STT: Deepgram (nova-3, multi-language)                                   │
│  • TTS: ElevenLabs (eleven_flash_v2_5, voice: m2sZ6cyg8CYkgA7WLQRSH)        │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CAMAINFLOW ORKESTRATOR                               │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ EVENT HANDLER                                                        │   │
│  │ • conversation_started → Scenario 0 (Introduction)                   │   │
│  │ • user_message → Intent Classification                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      INTENT CLASSIFICATION (AI)                              │
│  Analizuoja vartotojo žinutę ir nustato ketinimą iš:                         │
│  • project_attributes_private_dynamic_itm_compiled                          │
│  • 11 intent types (Large Group, Regular, Voucher, etc.)                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SCENARIO SELECTION                                   │
│  Pagal intentą pasirenkamas scenarijus:                                      │
│  • Scenario 0: Introduction                                                  │
│  • Scenario 1: Regular Reservation (< 7)                                     │
│  • Scenario 2: Large Group (≥ 7)                                             │
│  • Scenario 3: Relay to Manager                                              │
│  • Scenario 4: Answering Questions                                           │
│  • Scenario 12: Voucher Technical Support                                    │
│  • Scenario 20: Finish Conversation                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GINKLŲ KLUBAS DATA INJECTION                              │
│                                                                              │
│  Dinamiškai injektuojama iš attributes.yaml:                                 │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ BUSINESS CONTEXT (project_attributes_private_dynamic_business_context)│   │
│  │ • Verslo pavadinimas: Ginklų klubas                                  │   │
│  │ • Adresas: Islandijos pl. 209, Kaunas                                │   │
│  │ • Telefonas: +37064069242                                            │   │
│  │ • Darbo laikas: II-VI 10-18, VI 10-17                                │   │
│  │ • Produktai: 6 paslaugų aprašymai su kainomis                        │
│  │ • FAQ: 10 klausimų atsakymų                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ AGENT PERSONA (project_attributes_private_dynamic_agent_persona)      │   │
│  │ • Vardas: Tomas                                                      │   │
│  │ • Pareigos: AI Representative                                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ AMI - AGENT MAIN INSTRUCTION                                          │   │
│  │ (project_attributes_private_dynamic_ami_compiled)                     │   │
│  │ • 9 procedūrų aprašymai                                              │   │
│  │ • 7 scenarijų aprašymai                                              │   │
│  │ • Lietuviškos frazės                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ RESERVATION SETTINGS                                                  │   │
│  │ • Large group threshold: 7 žmonės                                    │   │
│  │ • Regular reservation URL: https://ginkluklubas.lt/rezervacija/      │   │
│  │ • Check-in notes: "Nepamirškite atsivešti dovanų kupono..."          │   │
│  │ • Regular questions: 2 klausimai (nepilnamečiai, savo ginklai)       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ INTENTS (project_attributes_private_dynamic_itm_compiled)             │   │
│  │ • 11 intent types su aprašymais                                      │   │
│  │ • Mapping į scenarijus                                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PROCEDURE EXECUTION                                     │
│                                                                              │
│  Scenarijaus metu kviečiamos procedūros:                                     │
│                                                                              │
│  1. Gathering Preferred Date and Time                                        │
│     → Naudoja <ConvoAgentCalendar>                                           │
│     → Code-phrase: "Let me check available slots..."                         │
│                                                                              │
│  2. Reconfirming or Gathering User Name                                      │
│     → Tikrina <UserInformation> section                                      │
│                                                                              │
│  3. Reconfirming or Gathering Phone Number                                   │
│     → Skirtingai phone vs chat kanalams                                      │
│                                                                              │
│  4. Reconfirming or Gathering Email Address                                  │
│     → Phone: siunčia SMS, laukia atsakymo                                    │
│     → Chat: prašo įvesti                                                     │
│                                                                              │
│  5. Conversation Quality Guardrails                                          │
│     → One question per turn                                                  │
│     → Answer-first rule                                                      │
│     → No-repeat rule                                                         │
│                                                                              │
│  6. Reservation Routing                                                      │
│     → Tikrina ar ≥ 7 žmonių                                                  │
│     → Tikrina kupono tipą (bernvakario/mergvakario/šeimos/junior)            │
│     → Maršrutizacija į Scenario 1 arba 2                                     │
│                                                                              │
│  7. SMS Link Self-Booking Flow                                               │
│     → Siunčia SMS su nuoroda                                                 │
│     → Code-phrase: "Duokite man akimirką..."                                 │
│                                                                              │
│  8. Relaying to Manager                                                      │
│     → Patalpina į eilę                                                       │
│     → Laukia darbo valandų                                                   │
│                                                                              │
│  9. Switch Language                                                          │
│     → Default: Lietuvių                                                      │
│     → Switch pagal vartotojo žinutę                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       EXTERNAL INTEGRATIONS                                  │
│                                                                              │
│  • Booking System: https://ginkluklubas.lt/rezervacija/                     │
│  • SMS Gateway: SMS siuntimas vartotojui                                     │
│  • Email: bookings@newo.ai (large group notifications)                      │
│  • Manager Relay: info@akseler.lt                                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CONVERSATION END                                        │
│  • Scenario 20: Finish Conversation                                          │
│  • Įrašas į istoriją                                                         │
│  • Galimas callback jei nebaigta                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 DUOMENŲ TEKĖJIMO SCHEMA

### 1. Pokalbio Pradžia

```yaml
Trigger: Vartotojas paskambina / parašo
↓
CAMainFlow: ConversationStartedSkill.nslg
↓
Inicijuojama:
  - user_id
  - conversation_channel (phone/chat/sms)
  - session_start_time
  - business.currently_open (true/false)
↓
Injectuojama iš attributes.yaml:
  - project_attributes_private_dynamic_agent_persona (Tomas)
  - project_attributes_private_dynamic_business_context (Ginklų klubas info)
  - agent_creator_voice_channel_greeting_phrase ("Sveiki, čia Ginklų klubas...")
```

### 2. Intent Nustatymas

```yaml
Vartotojo žinutė: "Noriu rezervuoti laiką 5 žmonėms"
↓
CAMainFlow: Intent Classification (AI)
↓
Nuskaito: project_attributes_private_dynamic_itm_compiled
↓
Randa intentą: [L] Regular Reservation
↓
Mapping į scenarijų: Scenario 1
```

### 3. Scenarijaus Vykdymas

```yaml
Scenario 1: Regular Reservation via Link
↓
Step 1.2: Ar dovanų kuponas?
  ↓
  Jei taip → Reservation Routing procedūra
    ↓
    Tikrina: project_attributes_hospitality_large_group_reservation_minimum_party_size (7)
    ↓
    Jei < 7 → tęsti Scenario 1
    Jei ≥ 7 → Scenario 2
↓
Step 1.4-1.6: Renka informaciją
  ↓
  Naudoja procedūras iš ami_compiled
  ↓
  Klausimai iš: project_attributes_hospitality_regular_reservation_questions
↓
Step 1.7: SMS siuntimas
  ↓
  Code-phrase: "Duokite man akimirką..."
  ↓
  Siunčia į: user.provided_phone_number
  ↓
  Nuoroda: project_attributes_hospitality_reservation_url
           (https://ginkluklubas.lt/rezervacija/)
↓
Step 1.13: Patvirtinimas
  ↓
  Check-in notes: project_attributes_hospitality_regular_reservation_check_in_notes
                  ("Nepamirškite atsivešti dovanų kupono...")
```

### 4. Large Group Atvejis

```yaml
Trigger: Vartotojas sako " mus bus 10 žmonių"
↓
Reservation Routing procedūra
↓
Tikrina: adults >= 7
↓
Jei TAIP → Scenario 2
↓
Nuskaito: project_attributes_hospitality_large_group_reservation_email
          (info@akseler.lt)
↓
Nuskaito: project_attributes_hospitality_large_group_reservation_questions
          (tuščia šiuo atveju)
↓
Renka: vardą, telefoną, email, datą
↓
Sukuria email su visais duomenimis
↓
Siunčia į: info@akseler.lt
↓
Praneša vartotojui:
  Darbo metu: "Dabar iškart perduodu administracijai..."
  Ne darbo metu: "Šiuo metu nedirbame, bet perduosiu..."
```

### 5. Dovanų Kupono Atvejis

```yaml
Trigger: "Turiu dovanų kuponą"
↓
Reservation Routing
↓
Klausia: "Ammm... pasakykite greitai, iš kokio tiekėjo..."
↓
Jei "Gera Dovana":
  ↓
  Atsakymas: "Gera dovana partneriai nesijungia su mūsų kalendoriumi..."
  ↓
  Relay to Manager
↓
Jei Ginklų klubo kuponas:
  ↓
  Klausia tipo: bernvakario/mergvakario/šeimos/junior
  ↓
  Jei vienas iš šių → Scenario 2 (manual handling)
  ↓
  Jei kitas → Scenario 1 (link booking)
```

---

## 🔧 CRITICAL INTEGRATION POINTS

### 1. AMI Compilation

```
attributes.yaml:
  project_attributes_private_dynamic_ami_template
  ↓
  [Compilation Process]
  ↓
  project_attributes_private_dynamic_ami_compiled
  ↓
  Injected into CAMainFlow prompt
```

**AMI Template sudėtys:**
- 9 procedūrų aprašymai
- 7 scenarijų aprašymai  
- Lietuviškos frazės
- Business logic (7 žmonių riba, darbo valandos)

### 2. Business Context Injection

```
attributes.yaml:
  project_attributes_private_dynamic_business_context
  ↓
  Komponuojamas iš:
    - agent_creator_business_info_name
    - agent_creator_business_info_address
    - agent_creator_business_info_story
    - agent_creator_products_and_services
    - project_attributes_faq
  ↓
  Injected į kiekvieną AI promptą
```

### 3. Working Hours Check

```
attributes.yaml:
  agent_creator_business_info_working_hours
  ↓
  II-VI: 10:00-18:00
  VI: 10:00-17:00
  I, VII: Closed
  ↓
  CAMainFlow: _getWorkingHoursStatus.nslg
  ↓
  Nustato: business.currently_open (true/false)
  ↓
  Naudojama:
    - Relaying to Manager (skirtingos frazės)
    - Availability checking
```

### 4. Intent Type Map

```
attributes.yaml:
  project_attributes_private_dynamic_itm_compiled
  ↓
  11 intent types:
    - [L] Large Group Reservation
    - [L] Regular Reservation  
    - [L] Dovanų kuponas
    - [T] Reschedule or Modification
    - [T] Cancellation
    - [T] Manager or Human Request
    - [T] Gift Voucher Booking Technical Help
    - General Information Request
    - Spam Session
    - Test Session
    - Other type of session
  ↓
  Mapping į scenarijus
```

---

## 🎯 KODĖL TAIP VEIKIA

### 1. Separation of Concerns

```
Newo Backend (CAMainFlow):
  └─ Universalus orkestratorius (113 skillų)
     └─ Nežino specifinių verslo duomenų

attributes.yaml (Ginklu Klubas):
  └─ Verslo specifiniai duomenys
     └─ Injected į universalią sistemą

Result:
  └─ Tas pats CAMainFlow gali aptarnauti 100+ skirtingų verslų
     └─ Tiesiog keičiasi attributes.yaml turinys
```

### 2. Dynamic Compilation

```
Statinis kodas (CAMainFlow skills):
  └─ Nekinta tarp klientų
  └─ Apdoroja placeholderius: <||business_name||>, <||ami||>

Dinamiški duomenys (attributes.yaml):
  └─ Kinta kiekvienam klientui
  └─ Injected į placeholderius runtime

Result:
  └─ Vienas kodas, begalės konfigūracijų
```

### 3. Event-Driven Architecture

```
Vartotojo veiksmas:
  ↓
Trigger event (user_message, conversation_started)
  ↓
Event handler (CAMainFlow skill)
  ↓
Data injection (from attributes.yaml)
  ↓
AI processing (intent classification)
  ↓
Scenario execution
  ↓
External action (SMS, email, booking link)
```

---

## 📊 ARCHITEKTŪROS PRIVALUMAI

| Privalumas | Paaiškinimas |
|------------|--------------|
| **Reusability** | Tas pats CAMainFlow visiems klientams |
| **Customization** | Kiekvienas klientas turi unikalią attributes.yaml |
| **Scalability** | Naujas klientas = naujas attributes.yaml failas |
| **Maintainability** | Kliento pakeitimai neįtakoja kodo |
| **Multi-tenant** | Viena infrastruktūra, daug klientų |
| **Language Agnostic** | AMI gali būti bet kuria kalba (LT, EN, etc.) |

---

## 🎯 SANTRUMPA: KAIP SUSIJĘ FAILAI

```
┌─────────────────────────────────────────────────────────────┐
│                    JŪSŲ FAILAI                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ginklu-klubas-real-production-data.md                      │
│  └─ Išpakuoti duomenys iš attributes.yaml                    │
│     └─ Verslo logika, scenarijai, frazės                    │
│                                                              │
│  ginklu-klubas-maximal-detail.md                            │
│  └─ Detalūs scenarijų žingsniai, procedūros                 │
│     └─ Call flow detaliai                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ INJECTED INTO
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    NEWO BACKEND                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  newo-backend/naf/agents/ConvoAgent/flows/CAMainFlow/       │
│  └─ 113 universalūs skill failai                            │
│     └─ Nežino apie Ginklų klubą                             │
│                                                              │
│  newo-backend/attributes.yaml                               │
│  └─ Ginklų klubo konfigūracija                              │
│     └─ Injektuojama į CAMainFlow                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ RUNS ON
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    PRODUKCIJOS REZULTATAS                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Vartotojas skambina +37064069242                           │
│  ↓                                                          │
│  AI agentas Tomas atsako lietuviškai                        │
│  ↓                                                          │
│  Naudoja Ginklų klubo logiką ir kainas                      │
│  ↓                                                          │
│  Siunčia į https://ginkluklubas.lt/rezervacija/            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

**IŠVADA:** Ginklų klubas ir Newo backend susiję per **duomenų injekcijos** mechanizmą. Newo teikia universalų orkestratorių (CAMainFlow), o Ginklų klubas teikia verslo logiką (attributes.yaml). Kartu sukuriamas pilnai funkcionuojantis AI agentas.
