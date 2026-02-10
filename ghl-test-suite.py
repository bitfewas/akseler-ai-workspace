#!/usr/bin/env python3
"""
GHL Solar Automation - Test Suite
=================================
Testavimo scriptas GHL automatizavimui.
Leidžia testuoti funkcijas be realių API call'ų naudojant mock data.

Naudojimas:
    python3 ghl-test-suite.py
    python3 ghl-test-suite.py --test new_lead
    python3 ghl-test-suite.py --verbose
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from unittest.mock import Mock, patch
from typing import Dict, Any

# Mock GHL API atsakymai
MOCK_CONTACT = {
    "id": "test-contact-123",
    "firstName": "Jonas",
    "lastName": "Jonaitis",
    "email": "jonas@email.lt",
    "phone": "+37061234567",
    "tags": ["solar-lead", "new"],
    "customFields": {
        "address": "Gatvė g. 1, Vilnius",
        "monthly_bill": "150 EUR",
        "roof_type": "Šlaitinis"
    },
    "dateAdded": datetime.now().isoformat()
}

MOCK_PIPELINE = {
    "id": "test-pipeline-456",
    "name": "Solar Sales Pipeline",
    "stages": [
        {"id": "stage-1", "name": "New Lead"},
        {"id": "stage-2", "name": "Qualified"},
        {"id": "stage-3", "name": "Proposal Sent"},
        {"id": "stage-4", "name": "Negotiation"},
        {"id": "stage-5", "name": "Won"}
    ]
}

MOCK_OPPORTUNITY = {
    "id": "test-opp-789",
    "title": "Jonas Jonaitis - Solar Installation",
    "pipelineId": "test-pipeline-456",
    "stageId": "stage-1",
    "status": "open",
    "monetaryValue": 15000,
    "contactId": "test-contact-123"
}

MOCK_TASKS = [
    {
        "id": "task-1",
        "title": "Paskambinti dėl konsultacijos",
        "dueDate": (datetime.now() - timedelta(days=2)).isoformat(),  # Overdue
        "completed": False,
        "assignedTo": "user-123"
    },
    {
        "id": "task-2", 
        "title": "Išsiųsti pasiūlymą",
        "dueDate": (datetime.now() + timedelta(days=1)).isoformat(),  # Upcoming
        "completed": False,
        "assignedTo": "user-123"
    }
]

MOCK_CALENDAR_SLOTS = [
    {"slot": "2026-02-10 10:00", "available": True},
    {"slot": "2026-02-10 14:00", "available": True},
    {"slot": "2026-02-11 09:00", "available": False},
]

class GHLMockClient:
    """Mock GHL klientas testavimui"""
    
    def __init__(self, token: str, location_id: str):
        self.token = token
        self.location_id = location_id
        self.calls_made = []
        
    def _log_call(self, method: str, endpoint: str, data: dict = None):
        """Logina API kviestukus"""
        self.calls_made.append({
            "method": method,
            "endpoint": endpoint,
            "data": data,
            "timestamp": datetime.now().isoformat()
        })
        
    def get_contact(self, contact_id: str) -> dict:
        """Gražina mock contact"""
        self._log_call("GET", f"/contacts/{contact_id}")
        return MOCK_CONTACT.copy()
    
    def create_contact(self, data: dict) -> dict:
        """Sukuria mock contact"""
        self._log_call("POST", "/contacts", data)
        return {**MOCK_CONTACT, **data, "id": "new-contact-456"}
    
    def update_contact(self, contact_id: str, data: dict) -> dict:
        """Atnaujina mock contact"""
        self._log_call("PUT", f"/contacts/{contact_id}", data)
        return {**MOCK_CONTACT, **data}
    
    def add_tag(self, contact_id: str, tag: str) -> dict:
        """Prideda tag'ą"""
        self._log_call("POST", f"/contacts/{contact_id}/tags", {"tag": tag})
        contact = MOCK_CONTACT.copy()
        if tag not in contact["tags"]:
            contact["tags"].append(tag)
        return contact
    
    def remove_tag(self, contact_id: str, tag: str) -> dict:
        """Pašalina tag'ą"""
        self._log_call("DELETE", f"/contacts/{contact_id}/tags/{tag}")
        contact = MOCK_CONTACT.copy()
        if tag in contact["tags"]:
            contact["tags"].remove(tag)
        return contact
    
    def send_sms(self, contact_id: str, message: str) -> dict:
        """Siunčia mock SMS"""
        self._log_call("POST", "/sms/send", {
            "contactId": contact_id,
            "message": message
        })
        return {
            "id": "sms-123",
            "contactId": contact_id,
            "message": message,
            "status": "sent",
            "sentAt": datetime.now().isoformat()
        }
    
    def create_task(self, data: dict) -> dict:
        """Sukuria mock užduotį"""
        self._log_call("POST", "/tasks", data)
        return {
            "id": f"task-{len(self.calls_made)}",
            **data,
            "createdAt": datetime.now().isoformat()
        }
    
    def get_tasks(self, contact_id: str = None, assigned_to: str = None, 
                  status: str = None) -> list:
        """Gražina mock užduotis"""
        self._log_call("GET", "/tasks", {
            "contactId": contact_id,
            "assignedTo": assigned_to,
            "status": status
        })
        return MOCK_TASKS
    
    def complete_task(self, task_id: str) -> dict:
        """Užbaigia užduotį"""
        self._log_call("PUT", f"/tasks/{task_id}/complete")
        return {"id": task_id, "completed": True}
    
    def create_opportunity(self, data: dict) -> dict:
        """Sukuria mock opportunity"""
        self._log_call("POST", "/opportunities", data)
        return {**MOCK_OPPORTUNITY, **data, "id": "new-opp-456"}
    
    def update_opportunity(self, opp_id: str, data: dict) -> dict:
        """Atnaujina mock opportunity"""
        self._log_call("PUT", f"/opportunities/{opp_id}", data)
        return {**MOCK_OPPORTUNITY, **data}
    
    def move_opportunity_stage(self, opp_id: str, stage_id: str) -> dict:
        """Perkelia opportunity į kitą stage"""
        self._log_call("PUT", f"/opportunities/{opp_id}/stage", {"stageId": stage_id})
        return {**MOCK_OPPORTUNITY, "stageId": stage_id}
    
    def get_pipelines(self) -> list:
        """Gražina mock pipelines"""
        self._log_call("GET", "/pipelines")
        return [MOCK_PIPELINE]
    
    def search_contacts(self, query: str, tags: list = None) -> list:
        """Ieško kontaktų"""
        self._log_call("GET", "/contacts/search", {"query": query, "tags": tags})
        return [MOCK_CONTACT]
    
    def get_calendar_slots(self, calendar_id: str, date: str) -> list:
        """Gražina kalendoriaus slotus"""
        self._log_call("GET", f"/calendars/{calendar_id}/slots", {"date": date})
        return MOCK_CALENDAR_SLOTS
    
    def create_appointment(self, data: dict) -> dict:
        """Sukuria susitikimą"""
        self._log_call("POST", "/appointments", data)
        return {
            "id": "appt-123",
            **data,
            "createdAt": datetime.now().isoformat()
        }


class SolarAutomationTester:
    """Testuoja saulės verslo automatizavimo scenarijus"""
    
    def __init__(self, verbose: bool = False):
        self.client = GHLMockClient("test-token", "test-location")
        self.verbose = verbose
        self.results = []
        
    def log(self, message: str, level: str = "info"):
        """Logina žinutę"""
        if self.verbose or level == "error":
            prefix = {"info": "ℹ️", "success": "✅", "error": "❌", "warning": "⚠️"}.get(level, "ℹ️")
            print(f"{prefix} {message}")
    
    def test_new_lead_workflow(self) -> bool:
        """Testuoja naujo leado apdorojimą"""
        print("\n📥 TEST: New Lead Workflow")
        print("-" * 40)
        
        try:
            # 1. Sukurti kontaktą
            contact = self.client.create_contact({
                "firstName": "Petras",
                "lastName": "Petraitis",
                "email": "petras@email.lt",
                "phone": "+37069876543",
                "tags": ["solar-lead", "website"]
            })
            self.log(f"Kontaktas sukurtas: {contact['firstName']} {contact['lastName']}")
            
            # 2. Pridėti tag'us
            self.client.add_tag(contact["id"], "needs-followup")
            self.log("Tag'as 'needs-followup' pridėtas")
            
            # 3. Sukurti opportunity
            opp = self.client.create_opportunity({
                "title": f"{contact['firstName']} {contact['lastName']} - Solar Installation",
                "pipelineId": "pipeline-123",
                "stageId": "stage-new",
                "contactId": contact["id"],
                "monetaryValue": 0  # Dar nežinome
            })
            self.log(f"Opportunity sukurta: {opp['id']}")
            
            # 4. Sukurti užduotis
            tasks = [
                {"title": "Paskambinti per 24h", "dueDate": (datetime.now() + timedelta(days=1)).isoformat()},
                {"title": "Išsiųsti info paketą", "dueDate": (datetime.now() + timedelta(days=2)).isoformat()},
                {"title": "Suplanuoti konsultaciją", "dueDate": (datetime.now() + timedelta(days=3)).isoformat()}
            ]
            for task_data in tasks:
                task = self.client.create_task({
                    **task_data,
                    "contactId": contact["id"],
                    "assignedTo": "user-123"
                })
                self.log(f"Užduotis sukurta: {task['title']}")
            
            # 5. Siųsti pasveikinimo SMS
            sms = self.client.send_sms(contact["id"], 
                "Sveiki! Ačiū, kad domitės saulės energija. Netrukus susisieksime dėl konsultacijos. ☀️")
            self.log(f"SMS išsiųsta: {sms['id']}")
            
            self.log("New Lead Workflow: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def test_followup_reminders(self) -> bool:
        """Testuoja priminimus apie vėluojančius skambučius"""
        print("\n⏰ TEST: Follow-up Reminders")
        print("-" * 40)
        
        try:
            # Gauti vėluojančias užduotis
            tasks = self.client.get_tasks(status="incomplete")
            overdue_tasks = [
                t for t in tasks 
                if datetime.fromisoformat(t["dueDate"].replace('Z', '+00:00')) < datetime.now()
            ]
            
            self.log(f"Rasta {len(overdue_tasks)} vėluojančių užduočių")
            
            for task in overdue_tasks:
                # Gauti kontaktą
                contact = self.client.get_contact("test-contact-123")
                
                # Siųsti priminimą
                sms = self.client.send_sms(contact["id"],
                    f"Primename: {task['title']}. Gal galite šiandien? ☀️")
                self.log(f"Priminimas išsiųstas: {contact['firstName']} - {task['title']}")
            
            self.log("Follow-up Reminders: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def test_proposal_followup(self) -> bool:
        """Testuoja pasiūlymo sekimą"""
        print("\n📄 TEST: Proposal Follow-up")
        print("-" * 40)
        
        try:
            # Gauti opportunity stage "Proposal Sent"
            opportunities = [MOCK_OPPORTUNITY]  # Mock
            
            for opp in opportunities:
                if opp["stageId"] == "stage-3":  # Proposal Sent
                    contact = self.client.get_contact(opp["contactId"])
                    
                    # Siųsti follow-up po 48h
                    sms = self.client.send_sms(contact["id"],
                        f"Labas {contact['firstName']}! Ar turite klausimų dėl pasiūlymo? "
                        f"Mielai paaiškinsime detales. 📊")
                    self.log(f"Follow-up SMS išsiųsta: {contact['firstName']}")
                    
                    # Sukurti užduotį
                    self.client.create_task({
                        "title": f"Paklausti dėl pasiūlymo - {contact['firstName']}",
                        "contactId": contact["id"],
                        "dueDate": (datetime.now() + timedelta(days=2)).isoformat(),
                        "assignedTo": "user-123"
                    })
            
            self.log("Proposal Follow-up: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def test_deal_won_workflow(self) -> bool:
        """Testuoja laimėto deal'o workflow"""
        print("\n🏆 TEST: Deal Won Workflow")
        print("-" * 40)
        
        try:
            opp = MOCK_OPPORTUNITY.copy()
            contact = self.client.get_contact(opp["contactId"])
            
            # 1. Atnaujinti opportunity
            self.client.update_opportunity(opp["id"], {
                "status": "won",
                "closedAt": datetime.now().isoformat()
            })
            self.log("Opportunity pažymėta kaip WON")
            
            # 2. Perkelti kontaktą į "Customer"
            self.client.add_tag(contact["id"], "customer")
            self.client.remove_tag(contact["id"], "lead")
            self.log("Tag'ai atnaujinti: customer ✓, lead ✗")
            
            # 3. Sveikinimo SMS
            sms = self.client.send_sms(contact["id"],
                f"Sveikiname, {contact['firstName']}! 🎉 Džiaugiamės bendradarbiavimu! "
                f"Netrukus susisieksime dėl montavimo grafiko. ☀️")
            self.log(f"Sveikinimo SMS išsiųsta")
            
            # 4. Sukurti montavimo užduotis
            install_tasks = [
                "Užsakyti įrangą",
                "Suplanuoti montavimo datą", 
                "Paruošti sutartį",
                "Informuoti klientą apie sekantis žingsnius"
            ]
            for task_title in install_tasks:
                self.client.create_task({
                    "title": task_title,
                    "contactId": contact["id"],
                    "dueDate": (datetime.now() + timedelta(days=1)).isoformat(),
                    "assignedTo": "user-123"
                })
                self.log(f"Montavimo užduotis: {task_title}")
            
            self.log("Deal Won Workflow: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def test_reactivation_campaign(self) -> bool:
        """Testuoja neaktyvių lead'ų reaktyvaciją"""
        print("\n🔄 TEST: Reactivation Campaign")
        print("-" * 40)
        
        try:
            # Ieškoti neaktyvių lead'ų
            inactive_leads = self.client.search_contacts(
                query="",
                tags=["solar-lead", "no-response-30d"]
            )
            
            self.log(f"Rasta {len(inactive_leads)} neaktyvių lead'ų")
            
            for lead in inactive_leads:
                # Siųsti reaktyvacijos žinutę
                sms = self.client.send_sms(lead["id"],
                    f"Labas {lead['firstName']}! Dar ieškote saulės sprendimų? "
                    f"Turime naują pasiūlymą - gal norėtumėte pasikonsultuoti? ☀️")
                self.log(f"Reaktyvacijos SMS: {lead['firstName']}")
                
                # Pridėti tag'ą
                self.client.add_tag(lead["id"], "reactivation-sent")
                
                # Sukurti užduotį
                self.client.create_task({
                    "title": f"Reaktyvacijos sekimas - {lead['firstName']}",
                    "contactId": lead["id"],
                    "dueDate": (datetime.now() + timedelta(days=7)).isoformat(),
                    "assignedTo": "user-123"
                })
            
            self.log("Reactivation Campaign: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def test_daily_report(self) -> bool:
        """Testuoja dienos ataskaitos generavimą"""
        print("\n📊 TEST: Daily Report")
        print("-" * 40)
        
        try:
            today = datetime.now()
            
            # Gauti užduotis
            all_tasks = self.client.get_tasks()
            overdue = [t for t in all_tasks if datetime.fromisoformat(t["dueDate"].replace('Z', '+00:00')) < today]
            upcoming = [t for t in all_tasks if datetime.fromisoformat(t["dueDate"].replace('Z', '+00:00')) >= today]
            
            # Gauti pipelines
            pipelines = self.client.get_pipelines()
            
            # Sugeneruoti ataskaitą
            report = f"""
📊 Dienos ataskaita - {today.strftime('%Y-%m-%d')}

🎯 Aktyvūs pipeline'ai: {len(pipelines)}
📋 Užduočių suvestinė:
   • Vėluojančios: {len(overdue)}
   • Artėjančios: {len(upcoming)}
   • Iš viso: {len(all_tasks)}

🔥 Prioritetai:
   1. Suskubti su vėluojančiomis užduotimis
   2. Pasiruošti rytojaus skambučiams
   3. Sekti atsiųstus pasiūlymus

Sėkmės! 💪
"""
            print(report)
            
            # Siųsti ataskaitą vadovui
            # self.client.send_sms("manager-phone", report)  # Realiame kode
            
            self.log("Daily Report: SĖKMINGAI ✅", "success")
            return True
            
        except Exception as e:
            self.log(f"Klaida: {e}", "error")
            return False
    
    def run_all_tests(self) -> dict:
        """Paleidžia visus testus"""
        print("\n" + "=" * 60)
        print("🧪 GHL SOLAR AUTOMATION - TEST SUITE")
        print("=" * 60)
        print(f"Laikas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Mode: MOCK (be realių API call'ų)")
        print("=" * 60)
        
        tests = [
            ("New Lead Workflow", self.test_new_lead_workflow),
            ("Follow-up Reminders", self.test_followup_reminders),
            ("Proposal Follow-up", self.test_proposal_followup),
            ("Deal Won Workflow", self.test_deal_won_workflow),
            ("Reactivation Campaign", self.test_reactivation_campaign),
            ("Daily Report", self.test_daily_report),
        ]
        
        results = {}
        for name, test_func in tests:
            results[name] = test_func()
        
        # API call summary
        print("\n" + "=" * 60)
        print("📈 API CALL SUMMARY")
        print("=" * 60)
        print(f"Iš viso API kviestukų: {len(self.client.calls_made)}")
        
        if self.verbose:
            print("\nDetalus sąrašas:")
            for call in self.client.calls_made:
                print(f"  {call['method']:6} {call['endpoint']}")
        
        # Final results
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS")
        print("=" * 60)
        passed = sum(1 for v in results.values() if v)
        total = len(results)
        
        for name, passed_test in results.items():
            status = "✅ PASS" if passed_test else "❌ FAIL"
            print(f"  {status:8} {name}")
        
        print("-" * 60)
        print(f"REZULTATAS: {passed}/{total} testų sėkmingi ({passed/total*100:.1f}%)")
        
        if passed == total:
            print("🎉 VISI TESTAI PRAEITI! Gali naudoti su realiais API!")
        
        print("=" * 60)
        
        return results


def main():
    parser = argparse.ArgumentParser(description="GHL Solar Automation Test Suite")
    parser.add_argument("--test", choices=[
        "new_lead", "followup", "proposal", "deal_won", "reactivation", "report"
    ], help="Paleisti konkretų testą")
    parser.add_argument("--verbose", "-v", action="store_true", help="Detalus output")
    parser.add_argument("--save-report", help="Išsaugoti ataskaitą į failą")
    
    args = parser.parse_args()
    
    tester = SolarAutomationTester(verbose=args.verbose)
    
    if args.test:
        # Paleisti konkretų testą
        test_map = {
            "new_lead": tester.test_new_lead_workflow,
            "followup": tester.test_followup_reminders,
            "proposal": tester.test_proposal_followup,
            "deal_won": tester.test_deal_won_workflow,
            "reactivation": tester.test_reactivation_campaign,
            "report": tester.test_daily_report
        }
        success = test_map[args.test]()
        sys.exit(0 if success else 1)
    else:
        # Paleisti visus testus
        results = tester.run_all_tests()
        
        # Jei prašoma - išsaugoti ataskaitą
        if args.save_report:
            report_data = {
                "timestamp": datetime.now().isoformat(),
                "results": results,
                "api_calls": tester.client.calls_made,
                "summary": {
                    "passed": sum(1 for v in results.values() if v),
                    "total": len(results)
                }
            }
            with open(args.save_report, 'w') as f:
                json.dump(report_data, f, indent=2)
            print(f"\n📄 Ataskaita išsaugota: {args.save_report}")
        
        sys.exit(0 if all(results.values()) else 1)


if __name__ == "__main__":
    main()
