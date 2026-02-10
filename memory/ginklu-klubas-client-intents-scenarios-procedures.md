# Ginklu Klubas - Intents, Scenarios & Procedures

**Client:** Ginklu Klubas  
**Connected to:** CAMainFlow  
**Status:** [REIKIA UŽPILDYTI IŠ NEWO ADMIN]

---

## 🎯 INTENT TYPE MAP

### Working Hours Intent Map
**Location in Newo:** `project_attributes_private_dynamic_itm_working_hours_compiled`

```json
{
  "intent_types": [
    {
      "idn": "[REIKIA UŽPILDYTI]",
      "title": "[Pavyzdys: Narystės užklausa]",
      "description": "[Klientas klausia apie narystę]",
      "scenarios": ["[REIKIA UŽPILDYTI]"]
    }
  ]
}
```

### Non-Working Hours Intent Map
**Location in Newo:** `project_attributes_private_dynamic_itm_non_working_hours_compiled`

```json
{
  "intent_types": [
    {
      "idn": "[REIKIA UŽPILDYTI]",
      "title": "[Pavyzdys: Palikite žinutę]",
      "description": "[Uždaros valandos - siūlome palikti žinutę]",
      "scenarios": ["[REIKIA UŽPILDYTI]"]
    }
  ]
}
```

---

## 🎬 SCENARIOS

### Location in Newo: `project_attributes_private_dynamic_ami_compiled`

#### Scenario 1: [REIKIA UŽPILDYTI]
```json
{
  "idn": "[REIKIA UŽPILDYTI - pvz: scenario_ginklu_klubas_membership_inquiry]",
  "title": "## **Scenario 1:** [Pavadinimas]",
  "body": "### **Step 1.1:** [Žingsnis]\n\n### **Step 1.2:** [Kitas žingsnis]",
  "description": "[Scenarijaus aprašymas]",
  "mentions": [
    {"type": "procedures", "item_idn": "[REIKIA UŽPILDYTI]"}
  ],
  "is_from_library": true,
  "origin_idn": ""
}
```

#### Scenario 2: [REIKIA UŽPILDYTI]
```json
{
  "idn": "[REIKIA UŽPILDYTI]",
  "title": "## **Scenario 2:** [Pavadinimas]",
  "body": "### **Step 2.1:** [Žingsnis]",
  "description": "[Aprašymas]",
  "mentions": [],
  "is_from_library": true,
  "origin_idn": ""
}
```

---

## 🔧 PROCEDURES

### Location in Newo: `project_attributes_private_dynamic_procedures_compiled`

#### Procedure 1: [REIKIA UŽPILDYTI]
```json
{
  "idn": "[REIKIA UŽPILDYTI - pvz: procedure_ginklu_klubas_gather_membership_type]",
  "title": "## **Procedure:** [Pavadinimas]",
  "body": "### **Step:** [Žingsnis]",
  "description": "[Aprašymas]",
  "is_from_library": true
}
```

---

## 📋 INSTRUKCIJOS KAIP GAUTI DUOMENIS

### 1. Prisijungti prie Newo Admin
- URL: [Newo admin panel URL]
- Project: Ginklu Klubas

### 2. Rasti Project Attributes
Eiti į: `Project Settings → Attributes → Private Dynamic`

### 3. Reikalingi laukai:
| Lauko pavadinimas | Turinys |
|-------------------|---------|
| `project_attributes_private_dynamic_itm_working_hours_compiled` | Working hours Intent Type Map |
| `project_attributes_private_dynamic_itm_non_working_hours_compiled` | Non-working hours Intent Type Map |
| `project_attributes_private_dynamic_ami_compiled` | Scenarios (AMI = Agent Main Instruction) |
| `project_attributes_private_dynamic_procedures_compiled` | Procedures |

### 4. Eksportuoti JSON
Kopijuoti kiekvieno lauko reikšmę ir įklijuoti į šį failą

---

## 🔄 KAIP TAI VEIKIA CAMainFlow

```
Vartotojo žinutė
    ↓
CAMainFlow: prompt_get_intent_type_map.nsl
    ↓
Gaunamas Intent Type Map (working/non-working hours)
    ↓
Intent klasifikacija
    ↓
Scenario pasirinkimas pagal intent
    ↓
CAMainFlow: prompt_get_scenarios_procedures.nsl
    ↓
Gaunami Ginklu Klubas scenarijai ir procedūros
    ↓
AI agentas seka scenario žingsnius
    ↓
Jei reikia - kviečia procedures
```

---

## ⚠️ PASTABA

**Šis failas yra TEMPLATE.** Realūs Ginklu Klubas duomenys saugomi Newo platformoje project_attributes laukuose. Juos galima gauti tik per Newo admin panel.

**Kai gausi realius duomenis:**
1. Kopijuoti JSON iš `project_attributes_private_dynamic_*` laukų
2. Įklijuoti į šį failą vietoje `[REIKIA UŽPILDYTI]`
3. Išsaugoti ir commit į git

---

**Paskutinis atnaujinimas:** 2026-02-10 (laukiama realių duomenų iš Newo)
