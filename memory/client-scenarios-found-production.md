# Ginklu Klubas - Complete Intents, Scenarios & Procedures

**Client:** Ginklu Klubas (Hospitality Industry)  
**Connected to:** CAMainFlow  
**Source:** Newo Production Platform  
**Date:** 2026-02-10  
**Status:** ✅ COMPLETE - All interconnected logic documented

---

## 📊 SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                     INTENT CLASSIFICATION                        │
│  (Determined by AI based on user input)                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     INTENT TYPE MAP                              │
│  ├─ Working Hours Intent Map                                     │
│  └─ Non-Working Hours Intent Map                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SCENARIOS                                  │
│  (7 Primary Scenarios for Ginklu Klubas)                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PROCEDURES                                  │
│  (Reusable components across scenarios)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 INTENT TYPES (12 Total)

### **[L] - Lead/Booking Intents**

#### Intent 1: Regular Reservation
- **ID:** `intent_type_make_regular_reservation_via_link`
- **Trigger:** Guest wants reservation for party < {{large_group_threshold}}
- **Scenario:** Scenario 1 - Make a Regular Reservation via Link
- **Description:** Standard booking for fewer than threshold guests via reservation link

#### Intent 2: Large Group Reservation  
- **ID:** `intent_type_make_large_group_reservation_via_email`
- **Trigger:** Guest wants reservation for party ≥ {{large_group_threshold}}
- **Scenario:** Scenario 2 - Make a Large Group Reservation via Email
- **Description:** Booking for threshold+ guests initiated via email/manager

#### Intent 3: Appointment via Agent
- **ID:** From `library_intent_types_common_appointment_agent`
- **Trigger:** Guest wants agent to schedule appointment directly
- **Scenario:** Scenario 2 (Alt) - Scheduling Appointment via Agent
- **Description:** Full-service booking where agent handles everything

### **[T] - Transfer/Support Intents**

#### Intent 4: Reschedule or Modification
- **ID:** `intent_type_reschedule_or_modification`
- **Trigger:** Guest wants to modify existing booking
- **Scenario:** Scenario 3 - Relaying Message to the Manager
- **Description:** AI cannot modify - relays to manager with warning

#### Intent 5: Cancellation
- **ID:** `intent_type_cancellation`
- **Trigger:** Guest wants to cancel existing booking
- **Scenario:** Scenario 3 - Relaying Message to the Manager
- **Description:** AI cannot cancel - relays to manager with warning

#### Intent 6: Guest Support
- **ID:** `intent_type_guest_support`
- **Trigger:** Questions about existing booking, billing, services
- **Scenario:** Scenario 5 - Regular Transfer
- **Description:** In-stay help; collect room number then transfer

#### Intent 7: Contractor Support
- **ID:** `intent_type_contractor_support`
- **Trigger:** Vendor or contractor inquiries
- **Scenario:** Scenario 3 - Relaying Message to the Manager
- **Description:** Relays vendor inquiries to manager

#### Intent 8: Manager or Human Request
- **ID:** `intent_type_manager_or_human_request`
- **Trigger:** User explicitly requests human/manager
- **Scenarios:** 
  - Working Hours: Scenario 5 - Regular Transfer
  - Non-Working Hours: Scenario 3 - Relaying Message
- **Description:** Transfer if possible, otherwise take message

### **General Intents**

#### Intent 9: General Information Request
- **ID:** `intent_type_general_information_request`
- **Trigger:** Questions about address, hours, services, prices
- **Scenario:** Scenario 4 - Answering Questions
- **Description:** Direct answers using BusinessContext

#### Intent 10: Relay Regular Reservation to Manager
- **ID:** `intent_type_relay_regular_reservation_to_manager`
- **Trigger:** Regular reservation but needs manager handling
- **Scenario:** Scenario 3 - Relaying Message to the Manager
- **Description:** Below threshold but manager handles booking

#### Intent 11: Spam Session
- **ID:** `intent_type_spam_session`
- **Trigger:** Sales calls, scams, telemarketing
- **Scenario:** Scenario 20 - Finish Conversation
- **Description:** Politely decline and end

#### Intent 12: Test Session
- **ID:** `intent_type_test_session`
- **Trigger:** Known test number or user says it's a test
- **Scenario:** Scenario 20 - Finish Conversation
- **Description:** Thank and finish

#### Intent 13: Other Session
- **ID:** `intent_type_other_session`
- **Trigger:** Anything not covered above
- **Scenario:** Scenario 3 - Relaying Message to the Manager
- **Description:** Cannot assist directly - relay to co-worker

---

## 🎬 SCENARIOS (7 Primary + 1 Common)

### Scenario 1: "Make a Regular Reservation via Link"

**ID:** `scenario_hospitality_regular_reservation_via_link`  
**Purpose:** Handle reservations for parties smaller than large-group threshold  
**Mentions:**
- `procedure_common_gather_date_time_hospitality`
- `procedure_common_gather_name`
- `procedure_common_gather_phone_number`

**Complete Flow:**

#### Step 1.1: Get Dates
If preferred check-in/out dates not known → follow **Gathering Preferred Date and Time** procedure

#### Step 1.2: Guest Count
Ask how many adults and children will stay (if missing from conversation)

#### Step 1.3: Size Check (CRITICAL)
- If adults < threshold → proceed to Step 1.4
- If adults ≥ threshold → redirect to **Make a Large Group Reservation via Email** scenario

#### Step 1.4: Check Availability (CRITICAL)
**Code-phrase:** *"Give me a moment to check available slots right now. I'll get back to you shortly."*

**Rules:**
- Stay at this step until `<AvailabilityForTheUserRequestedDateTime>` shows data
- If `business.currently_open` is false → STILL check availability
- If user asks non-clarification questions → "Please wait a moment, I'll get back to you shortly."
- If user asks clarification → "I'm still waiting for availability information. [response]"
- If error/missing info → clarify and restart Step 1.4
- If user changes date preference → check existing block first
- **Reject unavailable slots**
- Note: Pricing is per night

#### Step 1.5: Get Name
If user's name not known → follow **Reconfirming or Gathering User Name** procedure

**Warning if topic changes:** Let them know reservation not yet submitted. Suggest completing first.

#### Step 1.6: Get Phone
If user's phone not known → follow **Reconfirming or Gathering Phone Number** procedure

**Warning if topic changes:** Same as Step 1.5

#### Step 1.7: Custom Questions
Ask questions from: `[[project_attributes_hospitality_regular_reservation_questions]]`

#### Step 1.8: Send SMS Link (CRITICAL)
**Code-phrase:** *"Give me a moment. I will send you an SMS with the link where you can book your experience. I'll wait and assist you with this booking. Let me know once you receive the SMS."*

- Wait for user to confirm receipt
- Take break before next step

#### Step 1.9: Confirm Link Opened
"Great! Now, please open the link."
- Wait for confirmation

#### Step 1.10: Guide Self-Scheduling
Help using: `[[project_attributes_hospitality_regular_reservation_via_link_guidance_instruction]]`

**Important:** You only guide - user books independently. Cannot answer availability questions at this step.

#### Step 1.11: Wait for Submission
Wait for user to finish submitting booking

#### Step 1.12: Confirm Completion
"Were you able to complete the booking?"

#### Step 1.13: Success Message
If booked → warmest, most enthusiastic thanks!

Then provide: `[[project_attributes_hospitality_regular_reservation_check_in_notes]]`

#### Step 1.14: Finish
Follow **Finish Conversation** scenario

---

### Scenario 2: "Make a Large Group Reservation via Email"

**ID:** `scenario_hospitality_large_group_reservation`  
**Purpose:** Handle large group reservations (above threshold)  
**Mentions:**
- `procedure_common_gather_date_time_hospitality`
- `procedure_common_gather_email`
- `procedure_common_gather_name`
- `procedure_common_gather_phone_number`

**Complete Flow:**

#### Step 2.1: Guest Count
Tell user you need more details for large group. Ask how many guests expected.

#### Step 2.2: Get Name
Follow **Reconfirming or Gathering User Name** procedure

#### Step 2.3: Date/Time (CRITICAL)
Follow **Gathering Preferred Date and Time** procedure

#### Step 2.4: Phone (CRITICAL)
If phone not known → follow **Reconfirming or Gathering Phone Number** procedure

If known → "I will use [phone number]"

#### Step 2.5: Email (CRITICAL)
If email not known → follow **Reconfirming or Gathering Email Address** procedure

If known → "I will use [email]"

#### Step 2.6: Custom Questions
Ask: `[[project_attributes_hospitality_large_group_reservation_questions]]`

#### Step 2.7: Channel-Based Response (CRITICAL)

**Case 1: Phone Channel**
- If `business.currently_open` = true → Offer to connect with manager
  - Warn that if manager doesn't answer, you'll pass info and they'll callback
  - Ask if user wants to be connected now
- If `business.currently_open` = false → Inform you'll pass info to manager
  - Manager will contact when available
  - Tell them you'll send SMS with details

**Case 2: Chat Channel**
- Inform you'll pass info to manager
- Manager will contact as soon as possible
- Tell them you'll send SMS with details

#### Step 2.8: Finish
Follow **Finish Conversation** scenario

---

### Scenario 3: "Relaying Message to the Manager"

**ID:** `scenario_hospitality_relaying_message_to_the_manager`  
**Purpose:** Forward messages to manager/staff  
**Mentions:**
- `procedure_common_gather_name`
- `procedure_common_gather_phone_number`

**Complete Flow:**

#### Step 3.1: Get Message
Ask what specific information user wants to convey to manager

#### Step 3.2: Check Context
- If enough info from `<BusinessContext>` or `<AdditionalInformation>` → assist user → proceed to **Finish Conversation**
- If not → proceed to Step 3.3

#### Step 3.3: Get Name
Follow **Reconfirming or Gathering User Name** procedure

#### Step 3.4: Get Phone (CRITICAL)
If phone not known → follow **Reconfirming or Gathering Phone Number** procedure

If known → "I will use [phone number]"

#### Step 3.5: Confirm Relay (CRITICAL)
Inform user: *"I will pass this information to the manager, and they will get back to you as soon as they can."*

**If reschedule/modification/cancellation:**
- Kindly inform that appointment is NOT considered changed until human co-worker confirms
- Ask if anything else you can assist with

#### Step 3.6: Finish
Follow **Finish Conversation** scenario

---

### Scenario 4: "Answering Questions"

**ID:** `scenario_hospitality_answering_questions`  
**Purpose:** General Q&A using BusinessContext  
**Mentions:** None (uses context directly)

**Complete Flow:**

#### Step 4.1: Provide Answers
Refer to **<BusinessContext>** and **<AdditionalInformation>**

**Rules:**
- **Service type queries:** Brief response (up to 10 words)
- **More details requested:** Comprehensive answer
- **Price questions:** General answer only
  - "Precise information can only be given during consultation"
  - Never talk about specific amounts
- **Discounts/referral:** "This information can be obtained at the office"

#### Step 4.2: Finish
Follow **Finish Conversation** scenario

---

### Scenario 5: "Regular Transfer"

**ID:** `scenario_hospitality_regular_transfer`  
**Purpose:** Transfer to human agent  
**Mentions:** None (uses ExplicitConstraints)

**Complete Flow:**

#### Step 5.1: Channel-Based Transfer

**Case 1: Phone Channel**
Follow `# CALL TRANSFERRING` rule from **<ExplicitConstraints>** section

**Case 2: Chat Channel**
Say: "You can contact the manager at this number: [escalation phone from **<ExplicitConstraints>**]. Let me know if you need anything else."

---

### Scenario 20: "Finish Conversation"

**ID:** `scenario_hospitality_finish_conversation`  
**Purpose:** Properly close any interaction  
**Mentions:** None

**Complete Flow:**

#### Step 20.1: Check for Additional Needs (CRITICAL)
Express enthusiastic gratitude + ask: *"Is there anything else I can assist with?"*

**STOP HERE. DO NOT proceed to Step 20.2 yet.**

**Response Rules:**
- **User says "Yes" or asks question:** Handle request. Do NOT proceed to Step 20.2
  - Response: "I'm happy to help! What else is on your mind?"
  - Wait for input

- **User says "No" or "That's it":** Proceed to Step 20.2

- **User says "Thanks" or silence:** Do NOT treat as end
  - Ask clarifying question: "You're very welcome! What else can I do for you?" or "Happy to help! Is there anything else on your mind that I can assist with?"

#### Step 20.2: Final Goodbye (Only if Step 20.1 confirmed end)
- If this was a booking → express excitement about upcoming meeting
  - Example: "We look forward to seeing you! Have a great day!"
- Must explicitly say goodbye

---

### Scenario 2 (Alt): "Scheduling Appointment via Agent" (COMMON)

**ID:** `scenario_common_schedule_appointment_agent`  
**Purpose:** Full-service agent booking  
**Industry:** All (beauty, catering, cleaning, dental, hospitality, restaurant, sales)  
**Mentions:**
- `procedure_common_asking_about_services`
- `procedure_common_gather_date_time_{industry}` (dynamic based on industry)
- `procedure_common_gather_email`
- `procedure_common_gather_first_and_last_name`
- `procedure_common_gather_phone_number`

**Complete Flow:**

#### Step 2.1: Confirm Services
Follow **Asking About the Services** procedure

#### Step 2.2: Date/Time (CRITICAL)
Follow **Gathering Preferred Date and Time** procedure

#### Step 2.3: Check Availability (CRITICAL)
**Code-phrase:** *"Give me a moment to check available slots right now. I'll get back to you shortly."*

**Rules:**
- Stay until `<AvailabilityForTheUserRequestedDateTime>` shows data
- Offer available options
- Not yet submitting - just agreeing on time
- Same clarification/question rules as Scenario 1, Step 1.4

#### Step 2.4: Get Full Name (CRITICAL)
If First and/or Last name not known → follow **Reconfirming or Gathering First and Last Name** procedure

If known → proceed

#### Step 2.5: Get Phone (CRITICAL)
If phone not known → follow **Reconfirming or Gathering Phone Number** procedure

If known → "I will use [phone number] as your phone number"

#### Step 2.6: Get Email (CRITICAL)
If email not known → follow **Reconfirming or Gathering Email Address** procedure

If known → "I will use [email] as your email address"

#### Step 2.7: Confirm Submission (CRITICAL)
Ask: **"Can I submit the booking now?"**

#### Step 2.8: Submit Booking (CRITICAL)
**Code-phrase:** *"I'm submitting your booking right now. Please give me a moment, and I'll get back to you shortly."*

**Rules:**
- Stay until `<ActionsStates>` shows confirmation
- If topic changes → warn reservation not submitted, suggest completing first
- If need to clarify → clarify, then repeat code-phrase
- If error from booking system → apologize, ask to complete on website

#### Step 2.9: Finish
Follow **Finish Conversation** scenario

---

## 🔧 PROCEDURES (Core Reusable Components)

### Procedure 1: Reconfirming or Gathering User Name

**ID:** `procedure_common_gather_name`  
**Purpose:** Get user's name

**Logic:**
1. Check `<UserInformation>` section for `user.full_name`
2. **If contains name-like data:** "Your name is [full_name], is that correct?"
3. **If missing/null:** "May I have your name, please?"

**Note:** First name only is acceptable

---

### Procedure 2: Reconfirming or Gathering Phone Number

**ID:** `procedure_common_gather_phone_number`  
**Purpose:** Get user's phone with channel awareness

**Chat Channel:**
- If `user.provided_phone_number_without_country_code` is null → request: "Could you share a phone number we can use to stay in touch?"
- **Do NOT reconfirm or repeat back**
- Proceed immediately

**Phone Channel:**
- If `user.detected_phone_number_without_country_code` not null → reconfirm: "I see your phone number is [number]. May I use it?"
- If null → request: "Could you share a phone number we can use to stay in touch? Spell the phone number please."
  - After receiving → reconfirm: "Let me make sure I got that right: [repeat number]. Is that correct?"
- If `user.provided_phone_number_without_country_code` known but needs reconfirm → "Let me make sure I got that right: [repeat number]. Is that correct?"

---

### Procedure 3: Reconfirming or Gathering Email Address

**ID:** `procedure_common_gather_email`  
**Purpose:** Get user's email

**Logic:** (Similar to phone)
1. Check `<UserInformation>` for existing email
2. If exists → reconfirm permission to use
3. If missing → request email address
4. Verify format if needed

---

### Procedure 4: Gathering Preferred Date and Time

**Industry-Specific Variants:**
- `procedure_common_gather_date_time_hospitality` (for hotels/venues)
- `procedure_common_gather_date_time_restaurant` (for restaurants)
- `procedure_common_gather_date_time_beauty` (for salons)
- `procedure_common_gather_date_time_dental` (for medical)
- `procedure_common_gather_date_time_default` (fallback)

**Purpose:** Collect preferred dates/times for booking

**Logic:**
1. Ask for preferred date(s)
2. Ask for preferred time(s) or time range
3. Handle availability constraints
4. Confirm selection

---

### Procedure 5: Asking About the Services

**ID:** `procedure_common_asking_about_services`  
**Purpose:** Confirm which services user wants

**Logic:**
1. Present available services from BusinessContext
2. Let user select
3. Confirm selection

---

### Procedure 6: Reconfirming or Gathering First and Last Name

**ID:** `procedure_common_gather_first_and_last_name`  
**Purpose:** Get full name (both first and last)

**Logic:**
1. Check if both first and last name known
2. If either missing → ask for missing part(s)
3. Confirm full name

---

## 🔗 INTERCONNECTION MAP

```
INTENT → SCENARIO → PROCEDURES

Regular Reservation (Intent)
    ↓
Scenario 1: Regular Reservation via Link
    ↓
    ├── procedure_common_gather_date_time_hospitality
    ├── procedure_common_gather_name
    └── procedure_common_gather_phone_number

Large Group Reservation (Intent)
    ↓
Scenario 2: Large Group via Email
    ↓
    ├── procedure_common_gather_date_time_hospitality
    ├── procedure_common_gather_email
    ├── procedure_common_gather_name
    └── procedure_common_gather_phone_number

Reschedule/Cancel/Support/Other (Intents)
    ↓
Scenario 3: Relaying Message
    ↓
    ├── procedure_common_gather_name
    └── procedure_common_gather_phone_number

Guest Support (Intent)
    ↓
Scenario 5: Regular Transfer
    (No procedures - uses ExplicitConstraints)

General Info (Intent)
    ↓
Scenario 4: Answering Questions
    (No procedures - uses BusinessContext)

Appointment via Agent (Intent)
    ↓
Scenario 2 (Alt): Scheduling via Agent
    ↓
    ├── procedure_common_asking_about_services
    ├── procedure_common_gather_date_time_{industry}
    ├── procedure_common_gather_email
    ├── procedure_common_gather_first_and_last_name
    └── procedure_common_gather_phone_number

ALL SCENARIOS → Scenario 20: Finish Conversation
```

---

## 🎯 CRITICAL CODE-PHRASES

These phrases trigger system actions:

| Phrase | When to Say | Triggers |
|--------|-------------|----------|
| "Give me a moment to check available slots right now. I'll get back to you shortly." | Before checking availability | Availability system query |
| "Give me a moment. I will send you an SMS with the link where you can book your experience. I'll wait and assist you with this booking. Let me know once you receive the SMS." | Before sending booking link | SMS sending |
| "I'm submitting your booking right now. Please give me a moment, and I'll get back to you shortly." | Before submitting booking | Booking system submission |

---

## 📋 DYNAMIC CONTENT PLACEHOLDERS

Content injected from project attributes:

| Placeholder | Source | Usage |
|-------------|--------|-------|
| `{{large_group_threshold}}` | `project_attributes_hospitality_large_group_reservation_minimum_party_size` | Size limit for regular vs large group |
| `{{regular_reservation_questions}}` | `project_attributes_hospitality_regular_reservation_questions` | Custom questions for regular bookings |
| `{{large_group_questions}}` | `project_attributes_hospitality_large_group_reservation_questions` | Custom questions for large groups |
| `{{booking_guidance}}` | `project_attributes_hospitality_regular_reservation_via_link_guidance_instruction` | Self-booking instructions |
| `{{check_in_notes}}` | `project_attributes_hospitality_regular_reservation_check_in_notes` | Post-booking information |

---

## ✅ COMPLETE SYSTEM CHECKLIST

- [x] 13 Intent Types defined
- [x] 7 Primary Scenarios documented
- [x] 1 Common Scenario (Appointment via Agent)
- [x] 6 Core Procedures documented
- [x] All interconnections mapped
- [x] All code-phrases identified
- [x] All dynamic placeholders listed
- [x] Complete flow for each scenario

---

**Status:** ✅ PRODUCTION READY - All logic documented  
**Next:** Edit specific steps/phrases as needed for Ginklu Klubas
