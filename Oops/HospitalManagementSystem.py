# ============================================================
# HOSPITAL MANAGEMENT SYSTEM
# A complete real-world OOP program covering every concept
# ============================================================

from abc import ABC, abstractmethod
from datetime import date, datetime
import random


# ============================================================
# STEP 1: ABSTRACT BASE CLASS — Defines the contract
# Every entity in our system MUST implement these methods.
# ============================================================

class MedicalEntity(ABC):
    """
    Abstract Base Class: the top of our entire hierarchy.
    Any class that represents a hospital entity MUST
    define get_role() and get_details().
    Cannot be instantiated directly.
    """

    @abstractmethod
    def get_role(self) -> str:
        """Return what role this entity plays."""
        pass

    @abstractmethod
    def get_details(self) -> str:
        """Return a formatted string of key details."""
        pass

    # Concrete method — available to ALL subclasses
    def introduce(self):
        print(f"[{self.get_role()}] {self.get_details()}")


# ============================================================
# STEP 2: PERSON — Abstract class with shared fields
# Inherits from MedicalEntity. Adds name, age, contact.
# Still abstract — get_role() and get_details() not defined.
# ============================================================

class Person(MedicalEntity):
    """
    Abstract intermediate class.
    All people (Patient, Doctor) share these fields.
    Demonstrates:
      - Inheritance from ABC
      - Class variable (institution_name)
      - Encapsulation (__contact)
      - @property and setter
      - Magic methods (__str__, __repr__, __eq__)
      - @staticmethod
    """

    # CLASS VARIABLE — shared by ALL Person instances
    institution_name = "ACTE General Hospital"
    _total_persons   = 0   # protected — internal counter

    def __init__(self, name: str, age: int, contact: str):
        # Validate before setting
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not Person.is_valid_age(age):
            raise ValueError(f"Invalid age: {age}. Must be 1–120.")

        # Instance variables
        self._name    = name.strip()          # protected
        self._age     = age
        self.__contact = contact              # PRIVATE (name-mangled)
        self._joined  = date.today()

        # Increment class counter
        Person._total_persons += 1

    # ── PROPERTIES (Getters) ──────────────────────────────────
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def contact(self):
        return self.__contact    # controlled read access

    # ── SETTERS WITH VALIDATION ──────────────────────────────
    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be blank")
        self._name = value.strip()

    @age.setter
    def age(self, value):
        if not Person.is_valid_age(value):
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @contact.setter
    def contact(self, value):
        if not Person.is_valid_contact(value):
            raise ValueError("Contact must be 10 digits")
        self.__contact = value

    # ── CLASS METHOD ──────────────────────────────────────────
    @classmethod
    def get_total_persons(cls):
        """Returns total people registered across the system."""
        return cls._total_persons

    @classmethod
    def set_institution(cls, name):
        """Change hospital name system-wide."""
        cls.institution_name = name

    # ── STATIC METHODS ────────────────────────────────────────
    @staticmethod
    def is_valid_age(age):
        """Pure utility — no self, no cls needed."""
        return isinstance(age, int) and 1 <= age <= 120

    @staticmethod
    def is_valid_contact(contact):
        return contact.isdigit() and len(contact) == 10

    # ── MAGIC METHODS ─────────────────────────────────────────
    def __str__(self):
        """Human-readable: used by print()"""
        return f"{self._name} (Age: {self._age}) — {self.institution_name}"

    def __repr__(self):
        """Developer-readable: used in REPL and debugging"""
        return f"{self.__class__.__name__}(name='{self._name}', age={self._age})"

    def __eq__(self, other):
        """Equality by name + age + contact"""
        if not isinstance(other, Person):
            return False
        return (self._name == other._name and
                self._age  == other._age  and
                self.__contact == other.contact)


# ============================================================
# STEP 3: PATIENT — Concrete class, inherits Person
# Adds patient-specific data and behaviour.
# ============================================================

class Patient(Person):
    """
    Concrete class for patients.
    Demonstrates:
      - super() in constructor
      - Private attribute with controlled access
      - @property for read-only ID
      - Business methods
    """

    _patient_counter = 1000   # class variable for ID generation

    def __init__(self, name: str, age: int,
                 contact: str, diagnosis: str):
        super().__init__(name, age, contact)   # calls Person.__init__

        # Generate unique patient ID
        Patient._patient_counter += 1
        self.__patient_id    = f"PAT-{Patient._patient_counter}"
        self._diagnosis      = diagnosis
        self.__medical_records = []          # private list
        self._bill_amount    = 0.0
        self._is_admitted    = True

    # ── READ-ONLY property ────────────────────────────────────
    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def diagnosis(self):
        return self._diagnosis

    @property
    def bill(self):
        return self.__medical_records

    # ── BUSINESS METHODS ──────────────────────────────────────
    def add_record(self, record: str, cost: float = 0.0):
        """Add a medical record entry and cost to the bill."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"[{timestamp}] {record}"
        self.__medical_records.append(entry)
        self._bill_amount += cost
        print(f"  📋 Record added for {self._name}: {record}")

    def get_bill_summary(self):
        """Show complete bill breakdown."""
        print(f"\n{'='*50}")
        print(f"  BILL SUMMARY — {self._name} ({self.__patient_id})")
        print(f"{'='*50}")
        print(f"  Diagnosis  : {self._diagnosis}")
        for rec in self.__medical_records:
            print(f"  {rec}")
        print(f"{'─'*50}")
        gst = self._bill_amount * 0.05
        print(f"  Subtotal   : ₹{self._bill_amount:,.2f}")
        print(f"  GST (5%)   : ₹{gst:,.2f}")
        print(f"  TOTAL      : ₹{(self._bill_amount + gst):,.2f}")
        print(f"{'='*50}")

    def discharge(self):
        self._is_admitted = False
        print(f"  🏠 {self._name} discharged from hospital.")

    # ── Implement abstract methods from MedicalEntity ─────────
    def get_role(self):
        return "Patient"

    def get_details(self):
        status = "Admitted" if self._is_admitted else "Discharged"
        return (f"{self._name} | ID: {self.__patient_id} | "
                f"Diagnosis: {self._diagnosis} | Status: {status}")

    # ── Magic method ──────────────────────────────────────────
    def __len__(self):
        """len(patient) → number of medical records"""
        return len(self.__medical_records)


# ============================================================
# STEP 4: DOCTOR — Abstract class, inherits Person
# Still abstract because treat_patient() is not defined.
# ============================================================

class Doctor(Person):
    """
    Abstract class for all types of doctors.
    Demonstrates:
      - Abstract method leaving implementation to children
      - Super() in constructor
      - Class-level doctor counter
    """

    _doctor_counter = 2000

    def __init__(self, name: str, age: int, contact: str,
                 specialization: str, consultation_fee: float):
        super().__init__(name, age, contact)

        Doctor._doctor_counter += 1
        self.__doctor_id       = f"DOC-{Doctor._doctor_counter}"
        self._specialization   = specialization
        self._consultation_fee = consultation_fee
        self.__schedule        = []     # private schedule

    @property
    def doctor_id(self):
        return self.__doctor_id

    @property
    def specialization(self):
        return self._specialization

    @property
    def consultation_fee(self):
        return self._consultation_fee

    def add_to_schedule(self, appointment):
        self.__schedule.append(appointment)

    def view_schedule(self):
        print(f"\n📅 Schedule for Dr. {self._name}:")
        if not self.__schedule:
            print("  No appointments scheduled.")
            return
        for i, appt in enumerate(self.__schedule, 1):
            print(f"  {i}. {appt}")

    # ── ABSTRACT METHOD — child classes MUST override this ────
    @abstractmethod
    def treat_patient(self, patient: Patient) -> float:
        """
        Treat a patient and return the charge.
        EVERY type of doctor treats differently.
        """
        pass

    # ── CONCRETE method all doctors share ─────────────────────
    def prescribe(self, patient: Patient, medicine: str, days: int):
        cost = days * 150    # ₹150 per day prescription
        record = f"Prescription by Dr.{self._name}: {medicine} for {days} days"
        patient.add_record(record, cost)
        print(f"  💊 Dr. {self._name} prescribed {medicine} to {patient.name}")

    # ── Implement abstract methods from MedicalEntity ─────────
    def get_role(self):
        return f"Doctor ({self._specialization})"

    def get_details(self):
        return (f"Dr. {self._name} | ID: {self.__doctor_id} | "
                f"Specialization: {self._specialization} | "
                f"Fee: ₹{self._consultation_fee:,.0f}")

    def __str__(self):
        return f"Dr. {self._name} — {self._specialization}"

    def __repr__(self):
        return f"Doctor(name='Dr.{self._name}', spec='{self._specialization}')"


# ============================================================
# STEP 5: SPECIALIST — Inherits Doctor (concrete)
# Overrides treat_patient with specialist logic.
# ============================================================

class Specialist(Doctor):
    """
    A specialist doctor. Charges extra premium fee.
    Demonstrates:
      - Single inheritance from Doctor
      - Method overriding of treat_patient()
      - super() to call parent method
    """

    def __init__(self, name, age, contact,
                 specialization, consultation_fee, premium_percent=20):
        super().__init__(name, age, contact, specialization, consultation_fee)
        self.__premium_percent = premium_percent

    @property
    def total_fee(self):
        return self.consultation_fee * (1 + self.__premium_percent / 100)

    # ── OVERRIDE: treat_patient ───────────────────────────────
    def treat_patient(self, patient: Patient) -> float:
        """Specialist treatment — charges consultation + premium."""
        charge = self.total_fee
        record = (f"Specialist consultation with Dr. {self.name} "
                  f"({self.specialization}) — Premium visit")
        patient.add_record(record, charge)
        print(f"  🩺 Dr. {self.name} (Specialist) treated {patient.name} "
              f"— Charge: ₹{charge:,.2f}")
        return charge

    def get_role(self):
        return f"Specialist ({self.specialization})"


# ============================================================
# STEP 6: SURGEON — Inherits Doctor (concrete)
# Overrides treat_patient with surgery logic.
# ============================================================

class Surgeon(Doctor):
    """
    A surgeon. Higher charges, specific surgery method.
    Demonstrates:
      - Another concrete child of Doctor
      - Different override of treat_patient()
      - Additional surgery-specific method
    """

    def __init__(self, name, age, contact,
                 specialization, consultation_fee, surgery_base_fee):
        super().__init__(name, age, contact, specialization, consultation_fee)
        self.__surgery_base_fee = surgery_base_fee
        self.__surgeries_done   = 0

    @property
    def surgeries_done(self):
        return self.__surgeries_done

    # ── OVERRIDE: treat_patient ───────────────────────────────
    def treat_patient(self, patient: Patient) -> float:
        """Surgeon treats with pre-op consultation only."""
        charge = self.consultation_fee
        record = (f"Pre-operative consultation with Surgeon "
                  f"Dr. {self.name} ({self.specialization})")
        patient.add_record(record, charge)
        print(f"  🩹 Dr. {self.name} (Surgeon) assessed {patient.name} "
              f"— Pre-op charge: ₹{charge:,.2f}")
        return charge

    def perform_surgery(self, patient: Patient, surgery_name: str,
                        complexity: str = "routine") -> float:
        """Perform surgery — surgeon-specific method."""
        multiplier = {"routine": 1.0, "complex": 1.8, "emergency": 2.5}
        charge = self.__surgery_base_fee * multiplier.get(complexity, 1.0)

        record = (f"Surgery: {surgery_name} performed by Dr. {self.name} "
                  f"[{complexity.upper()}] — ₹{charge:,.2f}")
        patient.add_record(record, charge)
        self.__surgeries_done += 1

        print(f"\n  🏥 SURGERY PERFORMED")
        print(f"     Patient   : {patient.name}")
        print(f"     Surgeon   : Dr. {self.name}")
        print(f"     Procedure : {surgery_name} ({complexity})")
        print(f"     Charge    : ₹{charge:,.2f}")
        return charge

    def get_role(self):
        return f"Surgeon ({self.specialization})"


# ============================================================
# STEP 7: RESEARCHER — Separate ABC (for Multiple Inheritance)
# ============================================================

class Researcher(ABC):
    """
    Independent abstract class for research capabilities.
    Will be combined with Doctor via Multiple Inheritance.
    """

    def __init__(self, research_area: str, institution: str):
        self._research_area  = research_area
        self._institution    = institution
        self.__publications  = []

    def publish_paper(self, title: str):
        self.__publications.append(title)
        print(f"  📄 Published: '{title}' by {self._research_area} researcher")

    @property
    def publication_count(self):
        return len(self.__publications)

    @abstractmethod
    def conduct_research(self) -> str:
        pass


# ============================================================
# STEP 8: RESEARCH DOCTOR — MULTIPLE INHERITANCE
# Inherits from BOTH Doctor AND Researcher
# ============================================================

class ResearchDoctor(Doctor, Researcher):
    """
    Demonstrates MULTIPLE INHERITANCE.
    A ResearchDoctor is both a Doctor and a Researcher.
    MRO (Method Resolution Order): ResearchDoctor → Doctor → Researcher
    """

    def __init__(self, name, age, contact,
                 specialization, consultation_fee,
                 research_area, institution):
        # Call Doctor's __init__
        Doctor.__init__(self, name, age, contact,
                        specialization, consultation_fee)
        # Call Researcher's __init__
        Researcher.__init__(self, research_area, institution)

    # ── OVERRIDE: treat_patient ───────────────────────────────
    def treat_patient(self, patient: Patient) -> float:
        """Research doctors apply evidence-based treatment."""
        charge = self.consultation_fee * 1.15   # research premium
        record = (f"Evidence-based consultation with Research Dr. {self.name} "
                  f"(Research: {self._research_area})")
        patient.add_record(record, charge)
        print(f"  🔬 Dr. {self.name} (Research Doctor) treated "
              f"{patient.name} — Charge: ₹{charge:,.2f}")
        return charge

    # ── OVERRIDE: conduct_research ────────────────────────────
    def conduct_research(self) -> str:
        result = (f"Dr. {self.name} researching '{self._research_area}' "
                  f"at {self._institution}")
        print(f"  🧪 {result}")
        return result

    def get_role(self):
        return f"Research Doctor ({self.specialization})"


# ============================================================
# STEP 9: APPOINTMENT — Operator Overloading + Magic Methods
# ============================================================

class Appointment:
    """
    Booking between a Patient and a Doctor.
    Demonstrates:
      - __str__, __repr__
      - __eq__, __lt__ (comparison for sorting)
      - __bool__ (truthiness)
    """

    _appt_counter = 5000

    def __init__(self, patient: Patient, doctor: Doctor,
                 appointment_date: str, priority: int = 2):
        Appointment._appt_counter += 1
        self.__appt_id   = f"APPT-{Appointment._appt_counter}"
        self.patient     = patient
        self.doctor      = doctor
        self.appt_date   = appointment_date
        self.priority    = priority   # 1=urgent, 2=normal, 3=routine
        self.__confirmed = False

    def confirm(self):
        self.__confirmed = True
        self.doctor.add_to_schedule(self)
        print(f"  ✅ Appointment {self.__appt_id} confirmed: "
              f"{self.patient.name} → {self.doctor.name} on {self.appt_date}")

    def cancel(self):
        self.__confirmed = False
        print(f"  ❌ Appointment {self.__appt_id} cancelled.")

    # ── MAGIC METHODS ──────────────────────────────────────────

    def __str__(self):
        status = "Confirmed" if self.__confirmed else "Pending"
        return (f"Appt {self.__appt_id}: {self.patient.name} with "
                f"{self.doctor.name} on {self.appt_date} [{status}]")

    def __repr__(self):
        return (f"Appointment(id='{self.__appt_id}', "
                f"patient='{self.patient.name}', "
                f"doctor='{self.doctor.name}')")

    def __eq__(self, other):
        """Two appointments are equal if same patient + doctor + date."""
        if not isinstance(other, Appointment):
            return False
        return (self.patient   == other.patient and
                self.doctor    == other.doctor  and
                self.appt_date == other.appt_date)

    def __lt__(self, other):
        """Used for sorting: lower priority number = higher urgency."""
        return self.priority < other.priority

    def __bool__(self):
        """An appointment is 'truthy' only if confirmed."""
        return self.__confirmed


# ============================================================
# STEP 10: HOSPITAL — Brings everything together
# ============================================================

class Hospital:
    """
    Manages the entire hospital operation.
    Demonstrates:
      - Class variables (shared across all Hospital instances)
      - @classmethod factory method
      - Polymorphism: treating patients via common interface
      - __len__, __contains__, __str__
    """

    _total_hospitals = 0
    _all_hospitals   = []

    def __init__(self, name: str, city: str, beds: int):
        Hospital._total_hospitals += 1
        self.__hospital_id = f"HOSP-{Hospital._total_hospitals:03d}"
        self.__name        = name
        self.__city        = city
        self.__beds        = beds

        self.__patients     = []
        self.__doctors      = []
        self.__appointments = []

        # Update Person's class variable so all instances know hospital name
        Person.set_institution(f"{name}, {city}")

        Hospital._all_hospitals.append(self)
        print(f"🏥 Hospital '{name}' opened in {city} — ID: {self.__hospital_id}")

    # ── CLASS METHOD: factory ─────────────────────────────────
    @classmethod
    def get_total_hospitals(cls):
        return cls._total_hospitals

    @classmethod
    def find_hospital(cls, hospital_id):
        return next((h for h in cls._all_hospitals
                     if h.__hospital_id == hospital_id), None)

    # ── STATIC METHOD: utility ────────────────────────────────
    @staticmethod
    def generate_report_header(title):
        line = "═" * 55
        return f"\n{line}\n  {title}\n{line}"

    # ── ADMISSION ─────────────────────────────────────────────
    def admit_patient(self, patient: Patient):
        if len(self.__patients) >= self.__beds:
            print(f"  ❌ No beds available at {self.__name}")
            return False
        self.__patients.append(patient)
        print(f"  🛏️  {patient.name} admitted to {self.__name}")
        return True

    def add_doctor(self, doctor: Doctor):
        self.__doctors.append(doctor)
        print(f"  👨‍⚕️  Dr. {doctor.name} joined {self.__name}")

    def book_appointment(self, patient: Patient,
                         doctor: Doctor, date: str,
                         priority: int = 2) -> Appointment:
        appt = Appointment(patient, doctor, date, priority)
        appt.confirm()
        self.__appointments.append(appt)
        return appt

    # ── POLYMORPHISM in action ────────────────────────────────
    def run_consultation(self, appointment: Appointment):
        """
        POLYMORPHISM:
        We call treat_patient() on every doctor the same way.
        Python figures out WHICH version to run based on actual type.
        Specialist → Specialist.treat_patient()
        Surgeon    → Surgeon.treat_patient()
        ResearchDoctor → ResearchDoctor.treat_patient()
        """
        if not appointment:    # uses __bool__
            print("  ⚠️  Appointment not confirmed — cannot run consultation")
            return

        print(f"\n  🩺 Consultation starting...")
        charge = appointment.doctor.treat_patient(appointment.patient)
        return charge

    # ── REPORTS ───────────────────────────────────────────────
    def generate_full_report(self):
        print(self.generate_report_header(
            f"HOSPITAL REPORT — {self.__name}, {self.__city}"
        ))

        # Patients
        print(f"\n  📋 PATIENTS ({len(self.__patients)} admitted):")
        for p in self.__patients:
            p.introduce()           # calls MedicalEntity.introduce()
            print(f"     Records: {len(p)}")  # uses __len__

        # Doctors
        print(f"\n  👨‍⚕️  DOCTORS ({len(self.__doctors)} on staff):")
        for d in self.__doctors:
            d.introduce()           # polymorphic — each type prints differently

        # Appointments sorted by priority
        sorted_appts = sorted(self.__appointments)   # uses __lt__
        print(f"\n  📅 APPOINTMENTS ({len(sorted_appts)} total):")
        for appt in sorted_appts:
            print(f"     {appt}")   # uses __str__

        print(f"\n  🏥 Total registered persons: {Person.get_total_persons()}")
        print("═" * 55)

    # ── MAGIC METHODS for Hospital ────────────────────────────
    def __len__(self):
        """len(hospital) → number of current patients"""
        return len(self.__patients)

    def __contains__(self, person):
        """'patient in hospital' → True/False"""
        return person in self.__patients or person in self.__doctors

    def __str__(self):
        return f"{self.__name}, {self.__city} ({len(self)} patients)"

    def __repr__(self):
        return f"Hospital(id='{self.__hospital_id}', name='{self.__name}')"


# ============================================================
# MAIN PROGRAM — Run the entire system
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("  HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 55)

    # ─────────────────────────────────────────────────────────
    # 1. CREATE HOSPITAL (class variables update globally)
    # ─────────────────────────────────────────────────────────
    print("\n[ SETTING UP HOSPITAL ]")
    hospital = Hospital("ACTE General Hospital", "Bengaluru", beds=100)

    # ─────────────────────────────────────────────────────────
    # 2. CREATE DOCTORS (different types — polymorphism)
    # ─────────────────────────────────────────────────────────
    print("\n[ HIRING DOCTORS ]")

    # Specialist — inherits Doctor
    cardiologist = Specialist(
        name             = "Arjun Mehta",
        age              = 45,
        contact          = "9876543210",
        specialization   = "Cardiology",
        consultation_fee = 1500,
        premium_percent  = 25
    )

    # Surgeon — inherits Doctor
    surgeon = Surgeon(
        name             = "Priya Nair",
        age              = 40,
        contact          = "9876501234",
        specialization   = "Orthopaedics",
        consultation_fee = 2000,
        surgery_base_fee = 80000
    )

    # ResearchDoctor — Multiple Inheritance (Doctor + Researcher)
    research_doctor = ResearchDoctor(
        name             = "Kabir Rahman",
        age              = 50,
        contact          = "9876509999",
        specialization   = "Oncology",
        consultation_fee = 2500,
        research_area    = "Cancer Genomics",
        institution      = "IISc Bengaluru"
    )

    hospital.add_doctor(cardiologist)
    hospital.add_doctor(surgeon)
    hospital.add_doctor(research_doctor)

    # ─────────────────────────────────────────────────────────
    # 3. ADMIT PATIENTS
    # ─────────────────────────────────────────────────────────
    print("\n[ ADMITTING PATIENTS ]")

    patient1 = Patient(
        name      = "Aman Kumar",
        age       = 35,
        contact   = "9000000001",
        diagnosis = "Chest Pain"
    )

    patient2 = Patient(
        name      = "Riya Sharma",
        age       = 28,
        contact   = "9000000002",
        diagnosis = "Knee Fracture"
    )

    patient3 = Patient(
        name      = "Zoya Patel",
        age       = 52,
        contact   = "9000000003",
        diagnosis = "Lymphoma"
    )

    hospital.admit_patient(patient1)
    hospital.admit_patient(patient2)
    hospital.admit_patient(patient3)

    # ─────────────────────────────────────────────────────────
    # 4. MAGIC METHODS IN ACTION
    # ─────────────────────────────────────────────────────────
    print("\n[ MAGIC METHODS DEMO ]")
    print(f"  str(patient1) → {patient1}")            # __str__
    print(f"  repr(patient1)→ {repr(patient1)}")       # __repr__
    print(f"  str(surgeon)  → {surgeon}")             # __str__ (inherited from Person)
    print(f"  repr(surgeon) → {repr(surgeon)}")        # __repr__
    print(f"  len(hospital) → {len(hospital)} patients")  # __len__
    print(f"  patient1 in hospital → {patient1 in hospital}")  # __contains__
    print(f"  surgeon in hospital  → {surgeon in hospital}")

    # ─────────────────────────────────────────────────────────
    # 5. BOOK APPOINTMENTS
    # ─────────────────────────────────────────────────────────
    print("\n[ BOOKING APPOINTMENTS ]")

    appt1 = hospital.book_appointment(
        patient1, cardiologist, "2026-10-15", priority=1   # urgent
    )
    appt2 = hospital.book_appointment(
        patient2, surgeon, "2026-10-15", priority=2        # normal
    )
    appt3 = hospital.book_appointment(
        patient3, research_doctor, "2026-10-16", priority=2
    )

    # __eq__ demo
    appt_dup = Appointment(patient1, cardiologist, "2026-10-15")
    appt_dup.confirm()
    print(f"\n  appt1 == appt_dup → {appt1 == appt_dup}")  # True (__eq__)
    print(f"  appt1 == appt2   → {appt1 == appt2}")        # False

    # ─────────────────────────────────────────────────────────
    # 6. POLYMORPHISM — all doctors treat via same interface
    # ─────────────────────────────────────────────────────────
    print("\n[ RUNNING CONSULTATIONS — POLYMORPHISM ]")
    print("  (same call 'treat_patient()' → different behaviour per doctor type)\n")

    hospital.run_consultation(appt1)   # Specialist.treat_patient()
    hospital.run_consultation(appt2)   # Surgeon.treat_patient()
    hospital.run_consultation(appt3)   # ResearchDoctor.treat_patient()

    # ─────────────────────────────────────────────────────────
    # 7. DOCTOR-SPECIFIC METHODS
    # ─────────────────────────────────────────────────────────
    print("\n[ DOCTOR-SPECIFIC ACTIONS ]")

    # Surgeon performs surgery — surgery-specific method
    surgeon.perform_surgery(
        patient2, "Knee Replacement", complexity="complex"
    )

    # Cardiologist prescribes medicine — inherited from Doctor
    cardiologist.prescribe(patient1, "Aspirin 75mg + Clopidogrel", days=30)

    # Research doctor publishes and researches — from Researcher
    research_doctor.publish_paper("Genomic Markers in Stage III Lymphoma")
    research_doctor.conduct_research()

    # ─────────────────────────────────────────────────────────
    # 8. ABSTRACTION — introduce() via MedicalEntity
    # ─────────────────────────────────────────────────────────
    print("\n[ ABSTRACTION — introduce() via MedicalEntity ]")
    print("  (get_role() and get_details() differ per class)\n")
    for entity in [patient1, cardiologist, surgeon, research_doctor]:
        entity.introduce()

    # ─────────────────────────────────────────────────────────
    # 9. ENCAPSULATION — controlled access
    # ─────────────────────────────────────────────────────────
    print("\n[ ENCAPSULATION DEMO ]")

    # Valid contact update through setter
    patient1.contact = "9111111111"
    print(f"  Contact updated: {patient1.contact}")

    # Invalid update caught by setter
    try:
        patient1.age = 200          # ❌ setter rejects this
    except ValueError as e:
        print(f"  ❌ Setter validation: {e}")

    # Cannot access private attributes directly
    try:
        _ = patient1.__medical_records   # ❌ name mangled
    except AttributeError:
        print(f"  ❌ Private attribute __medical_records not accessible directly")

    # But the property gives controlled read access:
    print(f"  ✅ Records count via len() = {len(patient1)}")

    # ─────────────────────────────────────────────────────────
    # 10. CLASS VARIABLES — shared across all instances
    # ─────────────────────────────────────────────────────────
    print("\n[ CLASS VARIABLES DEMO ]")
    print(f"  Institution (set once, seen by all): {Person.institution_name}")
    print(f"  Total persons registered          : {Person.get_total_persons()}")
    print(f"  Total hospitals opened            : {Hospital.get_total_hospitals()}")
    print(f"  Surgeries performed by Dr. Priya  : {surgeon.surgeries_done}")

    # ─────────────────────────────────────────────────────────
    # 11. BILL SUMMARIES
    # ─────────────────────────────────────────────────────────
    print("\n[ PATIENT BILL SUMMARIES ]")
    patient1.get_bill_summary()
    patient2.get_bill_summary()
    patient3.get_bill_summary()

    # ─────────────────────────────────────────────────────────
    # 12. DOCTOR SCHEDULES
    # ─────────────────────────────────────────────────────────
    surgeon.view_schedule()

    # ─────────────────────────────────────────────────────────
    # 13. FULL HOSPITAL REPORT
    # ─────────────────────────────────────────────────────────
    hospital.generate_full_report()

    # ─────────────────────────────────────────────────────────
    # 14. DISCHARGE — final step
    # ─────────────────────────────────────────────────────────
    print("\n[ DISCHARGING PATIENTS ]")
    patient1.discharge()
    patient2.discharge()