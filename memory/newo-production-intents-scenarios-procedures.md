# Newo.ai Production Intents, Scenarios & Procedures

**Generated:** 2026-02-10  
**Scope:** Production files only (excludes library aggregators)  
**Location:** `naf/agents/GeneralManagerAgent/flows/GMcanvasBuilderFlow/skills/`

---

## 📊 SUMMARY STATISTICS

| Category | Count | Location |
|----------|-------|----------|
| **Scenarios** | 78 | GMcanvasBuilderFlow/skills/scenario_*.nsl |
| **Procedures** | 28 | GMcanvasBuilderFlow/skills/procedure_*.nsl |
| **Intent Types** | 2* | CAMainFlow/skills/prompt_get_intent_type_map.nsl |
| **TOTAL** | **108** | |

*Intent Type Maps: Working Hours + Non-Working Hours variants

---

## 🎯 INTENT TYPE MAPS (CAMainFlow)

### File: `prompt_get_intent_type_map.nsl`

**Purpose:** Route to appropriate scenarios based on working hours

**Two Variants:**
1. **Working Hours:** `project_attributes_private_dynamic_itm_working_hours_compiled`
2. **Non-Working Hours:** `project_attributes_private_dynamic_itm_non_working_hours_compiled`

**Logic:**
```jinja2
{% if working_hours %}
    {{Return(val=GetCustomerAttribute(field="..._working_hours_compiled"))}}
{% else %}
    {{Return(val=GetCustomerAttribute(field="..._non_working_hours_compiled"))}}
{% endif %}
```

**Key Concept:** Different scenario availability based on business hours

---

## 🎬 SCENARIOS BY INDUSTRY (78 Total)

### 1. BEAUTY / SALON (9 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_beauty_introduction` | Initial greeting and service overview |
| `scenario_beauty_answering_questions` | Q&A about services, pricing, availability |
| `scenario_beauty_consultation` | Detailed consultation booking |
| `scenario_beauty_schedule_appointment_link` | Send booking link to customer |
| `scenario_beauty_schedule_appointment_manually` | Manual appointment scheduling |
| `scenario_beauty_regular_transfer` | Transfer to human agent |
| `scenario_beauty_relaying_message` | Message relay to manager/staff |
| `scenario_beauty_finish_conversation` | Proper call/chat closure |

### 2. CLEANING SERVICES (8 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_cleaning_introduction` | Service introduction |
| `scenario_cleaning_answering_questions` | FAQs about cleaning services |
| `scenario_cleaning_approximate_estimate` | Provide rough price estimates |
| `scenario_cleaning_send_booking_link` | Send self-service booking link |
| `scenario_cleaning_regular_transfer` | Transfer to sales/operations |
| `scenario_cleaning_relay_cleaning_request` | Relay specific cleaning requests |
| `scenario_cleaning_relay_message` | General message relay |
| `scenario_cleaning_finish_conversation` | Close interaction |

### 3. DENTAL / MEDICAL (8 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_dental_introduction` | Welcome and service overview |
| `scenario_dental_answering_questions` | Dental procedure Q&A |
| `scenario_dental_schedule_appointment_agent` | Agent schedules appointment |
| `scenario_dental_schedule_appointment_link` | Send online booking link |
| `scenario_dental_schedule_appointment_manually` | Manual scheduling process |
| `scenario_dental_regular_transfer` | Transfer to receptionist |
| `scenario_dental_relaying_message` | Message to dental staff |
| `scenario_dental_finish_conversation` | Call closure |

### 4. HOME SERVICES (8 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_home_service_introduction` | Service overview |
| `scenario_home_service_appointment_request` | Basic appointment request |
| `scenario_home_service_advanced_appointment_request` | Complex/multi-service booking |
| `scenario_home_service_answering_questions` | General Q&A |
| `scenario_home_service_regular_transfer` | Transfer to technician/sales |
| `scenario_home_service_relaying_message_to_the_manager` | Escalate to manager |
| `scenario_home_service_finish_conversation` | Proper closure |

### 5. HOSPITALITY / HOTELS (7 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_hospitality_introduction` | Welcome guests |
| `scenario_hospitality_answering_questions` | Amenities, services Q&A |
| `scenario_hospitality_large_group_reservation` | Group booking handling |
| `scenario_hospitality_regular_reservation_via_link` | Standard booking link |
| `scenario_hospitality_regular_transfer` | Transfer to reservations |
| `scenario_hospitality_relaying_message_to_the_manager` | Manager escalation |
| `scenario_hospitality_finish_conversation` | Call/chat end |

### 6. RESTAURANT / FOOD (12 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_restaurant_introduction` | Welcome and menu overview |
| `scenario_restaurant_answering_questions` | Menu, hours, location Q&A |
| `scenario_restaurant_regular_reservation_default` | Standard reservation |
| `scenario_restaurant_regular_reservation_link` | Reservation via link |
| `scenario_restaurant_large_reservation_default` | Large party booking |
| `scenario_restaurant_live_show_reservation_link` | Event reservations |
| `scenario_restaurant_food_order_link` | Online ordering link |
| `scenario_restaurant_modifying_reservation` | Change existing booking |
| `scenario_restaurant_canceling_reservation` | Cancellation handling |
| `scenario_restaurant_managing_reservation_email` | Email confirmation |
| `scenario_restaurant_regular_transfer` | Transfer to host/hostess |
| `scenario_restaurant_relaying_message` | Message to staff |
| `scenario_restaurant_finish_conversation` | Closure |

### 7. SALES / B2B (13 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_sales_introduction` | Product/service intro |
| `scenario_sales_consultation_and_lead_qualification` | Discovery call |
| `scenario_sales_pre_sale_consultation` | Technical consultation |
| `scenario_sales_lead_qualification` | Qualify prospects |
| `scenario_sales_appointment_via_calendar` | Schedule via calendar link |
| `scenario_sales_appointment_via_link` | Schedule via booking link |
| `scenario_sales_sale_via_link` | Direct sales link |
| `scenario_sales_send_product_link` | Share product info |
| `scenario_sales_partner_registration` | Partner onboarding |
| `scenario_sales_generate` | Generate leads |
| `scenario_sales_regular_transfer` | Transfer to sales rep |
| `scenario_sales_relay_message` | Message to sales team |
| `scenario_sales_finish_conversation` | Close sales call |

### 8. CATERING (6 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_catering_introduction` | Service overview |
| `scenario_catering_answering_questions` | Menu, pricing Q&A |
| `scenario_catering_order_default` | Standard order process |
| `scenario_catering_regular_transfer` | Transfer to catering manager |
| `scenario_catering_relaying_message` | Message relay |
| `scenario_catering_finish_conversation` | Order closure |

### 9. COMMON / SHARED (7 scenarios)

| Scenario ID | Purpose |
|-------------|---------|
| `scenario_common_schedule_appointment_agent` | Generic appointment booking |
| `scenario_restaurant_regular_reservation_link_no_slots_checking` | Link booking without availability check |

---

## 🔧 PROCEDURES (28 Total)

### Common Procedures (Universal)

| Procedure ID | Purpose | Industry |
|--------------|---------|----------|
| `procedure_common_asking_about_services` | Inquire about service needs | All |
| `procedure_common_gather_name` | Collect customer name | All |
| `procedure_common_gather_first_and_last_name` | Full name collection | All |
| `procedure_common_gather_phone_number` | Phone number collection | All |
| `procedure_common_gather_email` | Email address collection | All |
| `procedure_common_gather_physical_address` | Street address | All |
| `procedure_common_gather_zip_code` | ZIP/postal code | All |
| `procedure_common_gather_date_of_birth` | DOB collection | Medical |
| `procedure_common_gather_language` | Preferred language | All |

### Availability Procedures (Industry-Specific)

| Procedure ID | Purpose | Industry |
|--------------|---------|----------|
| `procedure_common_gather_availability_default` | Generic availability | All |
| `procedure_common_gather_availability_home_service` | Home service specific | Home Services |
| `procedure_common_gather_availability_hospitality` | Hotel/restaurant | Hospitality |

### Date/Time Procedures (By Industry)

| Procedure ID | Purpose |
|--------------|---------|
| `procedure_common_gather_date_time_default` | Generic scheduling |
| `procedure_common_gather_date_time_beauty` | Salon appointments |
| `procedure_common_gather_date_time_catering` | Catering events |
| `procedure_common_gather_date_time_cleaning` | Cleaning bookings |
| `procedure_common_gather_date_time_dental` | Medical appointments |
| `procedure_common_gather_date_time_hospitality` | Hotel reservations |
| `procedure_common_gather_date_time_restaurant` | Restaurant bookings |
| `procedure_common_gather_date_time_sales` | Sales meetings |

### Industry-Specific Procedures

| Procedure ID | Purpose | Industry |
|--------------|---------|----------|
| `procedure_beauty_pricing` | Service pricing | Beauty |
| `procedure_cleaning_gather_frequency` | Cleaning frequency | Cleaning |
| `procedure_dental_gathering_insurance` | Insurance info | Dental |

---

## 🏗️ ARCHITECTURE PATTERNS

### 1. Scenario Structure (JSON Format)

```json
{
    "idn": "unique_scenario_identifier",
    "title": "Human-readable title",
    "body": "Step-by-step instructions (markdown)",
    "description": "Summary for AI context",
    "mentions": [
        {"type": "procedures", "item_idn": "procedure_id"},
        {"type": "scenarios", "item_idn": "other_scenario_id"}
    ],
    "is_from_library": true,
    "origin_idn": ""
}
```

### 2. Procedure Structure

Similar to scenarios but focused on single-task completion:
- Gather specific information
- Perform specific action
- Reusable across multiple scenarios

### 3. Intent Type Map Structure

```json
{
    "intent_types": [
        {
            "idn": "intent_id",
            "title": "Intent Name",
            "description": "When to use",
            "scenarios": ["scenario_id_1", "scenario_id_2"]
        }
    ]
}
```

---

## 🔄 DATA FLOW

```
1. User Input
   ↓
2. Intent Classification (Intent Type Map)
   ↓
3. Scenario Selection (based on intent + working hours)
   ↓
4. Step Execution (scenario body)
   ↓
5. Procedure Calls (when mentioned)
   ↓
6. Completion / Handoff
```

---

## 📁 FILE LOCATIONS

### Core Files (CAMainFlow)
- `naf/agents/ConvoAgent/flows/CAMainFlow/skills/prompt_get_intent_type_map.nsl`
- `naf/agents/ConvoAgent/flows/CAMainFlow/skills/prompt_get_scenarios_procedures.nsl`
- `naf/agents/ConvoAgent/flows/CAAssessmentFlow/skills/collect_quality_metrics_scenario_following.nsl`

### Industry Content (GeneralManagerAgent)
- `naf/agents/GeneralManagerAgent/flows/GMcanvasBuilderFlow/skills/scenario_*.nsl`
- `naf/agents/GeneralManagerAgent/flows/GMcanvasBuilderFlow/skills/procedure_*.nsl`

### Migration Helpers (Legacy)
- `naf/agents/GeneralManagerAgent/flows/GMmainFlow/skills/_migration_3_0_0_helper_parse_intent_types.nsl`
- `naf/agents/GeneralManagerAgent/flows/GMmainFlow/skills/_migration_3_8_0_removing_language_procedure.nsl`

---

## 🔍 KEY INSIGHTS

1. **Industry Coverage:** 9 major industries (Beauty, Cleaning, Dental, Home Services, Hospitality, Restaurant, Sales, Catering)

2. **Scenario Reuse:** Common patterns across industries (Introduction → Q&A → Booking → Transfer → Finish)

3. **Procedure Granularity:** Procedures are atomic tasks, scenarios orchestrate them

4. **Working Hours Awareness:** Different scenario sets for working vs non-working hours

5. **Mention System:** Scenarios reference procedures and other scenarios by ID

6. **Assessment Integration:** `collect_quality_metrics_scenario_following` evaluates AI compliance

---

## 📈 STATISTICS BY CATEGORY

| Category | Count | Percentage |
|----------|-------|------------|
| Sales/B2B | 13 | 16.7% |
| Restaurant | 12 | 15.4% |
| Home Services | 8 | 10.3% |
| Dental | 8 | 10.3% |
| Cleaning | 8 | 10.3% |
| Beauty | 9 | 11.5% |
| Hospitality | 7 | 9.0% |
| Catering | 6 | 7.7% |
| Common/Shared | 7 | 9.0% |

---

**End of Analysis**
