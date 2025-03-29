"""
This module contains all the data related to exams.
It provides functions to retrieve and search through the exam data.
"""

# List of exam categories with their subcategories
EXAM_CATEGORIES = [
    {
        "id": "engineering",
        "name": "Engineering Entrance Exams",
        "description": "Exams for admission to undergraduate and postgraduate engineering programs",
        "icon_class": "fa-cogs",
        "subcategories": [
            {"id": "eng_national", "name": "National Level"},
            {"id": "eng_state", "name": "State Level"},
            {"id": "eng_private", "name": "Private Universities"}
        ]
    },
    {
        "id": "medical",
        "name": "Medical Entrance Exams",
        "description": "Exams for admission to MBBS, BDS, AYUSH and other medical courses",
        "icon_class": "fa-stethoscope",
        "subcategories": [
            {"id": "med_national", "name": "National Level"},
            {"id": "med_state", "name": "State Level"},
            {"id": "med_super", "name": "Super Speciality"}
        ]
    },
    {
        "id": "management",
        "name": "Management Entrance Exams",
        "description": "Exams for admission to MBA and other management courses",
        "icon_class": "fa-briefcase",
        "subcategories": [
            {"id": "mba_national", "name": "National Level"},
            {"id": "mba_state", "name": "State Level"},
            {"id": "mba_institute", "name": "Institute Level"}
        ]
    },
    {
        "id": "law",
        "name": "Law Entrance Exams",
        "description": "Exams for admission to undergraduate and postgraduate law programs",
        "icon_class": "fa-gavel",
        "subcategories": [
            {"id": "law_national", "name": "National Level"},
            {"id": "law_state", "name": "State Level"}
        ]
    },
    {
        "id": "upsc",
        "name": "UPSC Exams",
        "description": "Civil Services and other examinations conducted by UPSC",
        "icon_class": "fa-landmark",
        "subcategories": [
            {"id": "upsc_civil", "name": "Civil Services"},
            {"id": "upsc_defense", "name": "Defense Services"},
            {"id": "upsc_others", "name": "Other UPSC Exams"}
        ]
    },
    {
        "id": "state_psc",
        "name": "State PSC Exams",
        "description": "Civil Services examinations conducted by State Public Service Commissions",
        "icon_class": "fa-university",
        "subcategories": []
    },
    {
        "id": "banking",
        "name": "Banking Exams",
        "description": "Exams for recruitment in public and private sector banks",
        "icon_class": "fa-money-bill-wave",
        "subcategories": [
            {"id": "bank_po", "name": "Probationary Officers"},
            {"id": "bank_clerk", "name": "Clerks"},
            {"id": "bank_specialist", "name": "Specialist Officers"}
        ]
    },
    {
        "id": "ssc",
        "name": "SSC Exams",
        "description": "Staff Selection Commission exams for various government posts",
        "icon_class": "fa-users",
        "subcategories": []
    },
    {
        "id": "railways",
        "name": "Railway Exams",
        "description": "Exams for recruitment in Indian Railways",
        "icon_class": "fa-train",
        "subcategories": [
            {"id": "rrb_ntpc", "name": "RRB NTPC"},
            {"id": "rrb_group_d", "name": "RRB Group D"},
            {"id": "rrb_alp", "name": "RRB ALP & Technician"}
        ]
    },
    {
        "id": "defense",
        "name": "Defense Exams",
        "description": "Exams for recruitment in Indian Armed Forces",
        "icon_class": "fa-shield-alt",
        "subcategories": [
            {"id": "def_army", "name": "Indian Army"},
            {"id": "def_navy", "name": "Indian Navy"},
            {"id": "def_airforce", "name": "Indian Air Force"}
        ]
    },
    {
        "id": "teaching",
        "name": "Teaching Exams",
        "description": "Exams for recruitment as teachers in schools and colleges",
        "icon_class": "fa-chalkboard-teacher",
        "subcategories": [
            {"id": "teach_net", "name": "UGC NET/JRF"},
            {"id": "teach_tet", "name": "TET Exams"},
            {"id": "teach_stet", "name": "State TETs"}
        ]
    },
    {
        "id": "abroad",
        "name": "Study Abroad Exams",
        "description": "Exams for admission to universities abroad",
        "icon_class": "fa-globe",
        "subcategories": [
            {"id": "abroad_general", "name": "General Exams"},
            {"id": "abroad_subject", "name": "Subject Specific"}
        ]
    }
]

# Detailed exam data
EXAMS_DATA = [
    # ENGINEERING ENTRANCE EXAMS - NATIONAL LEVEL
    {
        "id": "jee_main",
        "name": "JEE Main",
        "full_name": "Joint Entrance Examination (Main)",
        "category": "engineering",
        "subcategory": "eng_national",
        "description": "JEE Main is the national level undergraduate engineering entrance exam conducted for admission to NITs, IIITs, CFTIs and other engineering institutions.",
        "conducting_body": "National Testing Agency (NTA)",
        "frequency": "Twice a year (January and April sessions)",
        "eligibility": "Candidates who have passed class 12th or equivalent examination with Physics, Chemistry, and Mathematics as compulsory subjects.",
        "age_limit": "No age limit",
        "exam_pattern": "Computer Based Test (CBT) with Multiple Choice Questions (MCQs) and Numerical Value Questions. The exam consists of 3 papers: Paper 1 for B.E./B.Tech, Paper 2A for B.Arch, and Paper 2B for B.Planning.",
        "syllabus": "Physics, Chemistry, and Mathematics for Paper 1. Mathematics, Aptitude Test, and Drawing Test for Paper 2A. Mathematics, Aptitude Test, and Planning-Based Questions for Paper 2B.",
        "application_procedure": "Online application through the NTA JEE Main website. Registration typically opens 2-3 months before the exam.",
        "important_dates": {
            "application_start": "Generally in September (for January session) and February (for April session)",
            "application_end": "Generally in October (for January session) and March (for April session)",
            "exam_date": "January and April",
            "result_date": "Approximately 10-15 days after the exam"
        },
        "website": "https://jeemain.nta.nic.in/",
        "preparation_tips": [
            "Focus on NCERT textbooks for building strong concepts",
            "Solve previous years' question papers",
            "Take regular mock tests",
            "Create short notes for revision",
            "Focus on formula-based and conceptual questions"
        ]
    },
    {
        "id": "jee_advanced",
        "name": "JEE Advanced",
        "full_name": "Joint Entrance Examination (Advanced)",
        "category": "engineering",
        "subcategory": "eng_national",
        "description": "JEE Advanced is the second stage of JEE for admission to the 23 Indian Institutes of Technology (IITs) across the country.",
        "conducting_body": "One of the IITs (rotational basis)",
        "frequency": "Once a year",
        "eligibility": "Top 2,50,000 rank holders in JEE Main. Candidates can attempt JEE Advanced maximum twice in consecutive years.",
        "age_limit": "Candidates should have been born on or after October 1, 1998 (for the general category)",
        "exam_pattern": "Computer Based Test (CBT) with two papers (Paper 1 and Paper 2), each of 3 hours duration. The exam includes MCQs, numerical value questions, and match-the-following type questions.",
        "syllabus": "Advanced concepts in Physics, Chemistry, and Mathematics",
        "application_procedure": "Online registration through the JEE Advanced website after qualifying JEE Main.",
        "important_dates": {
            "application_start": "Generally in May",
            "application_end": "Generally in May (approximately 10 days after JEE Main results)",
            "exam_date": "Generally in June",
            "result_date": "Generally in June (approximately 10-15 days after the exam)"
        },
        "website": "https://jeeadv.ac.in/",
        "preparation_tips": [
            "Start advanced preparation after mastering JEE Main concepts",
            "Focus on understanding the application of concepts",
            "Practice previous years' papers extensively",
            "Attempt mock tests with increasing difficulty",
            "Work on speed and accuracy"
        ]
    },
    # MEDICAL ENTRANCE EXAMS - NATIONAL LEVEL
    {
        "id": "neet_ug",
        "name": "NEET UG",
        "full_name": "National Eligibility cum Entrance Test (Undergraduate)",
        "category": "medical",
        "subcategory": "med_national",
        "description": "NEET UG is the single entrance examination for admission to MBBS, BDS, AYUSH, and other medical courses in India.",
        "conducting_body": "National Testing Agency (NTA)",
        "frequency": "Once a year",
        "eligibility": "Candidates who have passed class 12th or equivalent examination with Physics, Chemistry, and Biology/Biotechnology as compulsory subjects.",
        "age_limit": "Minimum 17 years as on December 31 of the year of admission",
        "exam_pattern": "Pen and paper-based test with 180 Multiple Choice Questions (MCQs) from Physics, Chemistry, and Biology (Botany & Zoology). Duration is 3 hours.",
        "syllabus": "Physics, Chemistry, and Biology (Botany & Zoology) based on NCERT curriculum of classes 11 and 12.",
        "application_procedure": "Online application through the NTA NEET website. Registration typically opens 2-3 months before the exam.",
        "important_dates": {
            "application_start": "Generally in December",
            "application_end": "Generally in January",
            "exam_date": "Generally in May",
            "result_date": "Generally in June"
        },
        "website": "https://neet.nta.nic.in/",
        "preparation_tips": [
            "Master NCERT textbooks thoroughly",
            "Create concise notes for quick revision",
            "Practice MCQs regularly",
            "Take sectional tests to identify weak areas",
            "Manage time effectively during preparation"
        ]
    },
    # UPSC EXAMS
    {
        "id": "upsc_cse",
        "name": "UPSC CSE",
        "full_name": "UPSC Civil Services Examination",
        "category": "upsc",
        "subcategory": "upsc_civil",
        "description": "The Civil Services Examination is conducted by UPSC for recruitment to various Civil Services of the Government of India, including IAS, IPS, and IFS.",
        "conducting_body": "Union Public Service Commission (UPSC)",
        "frequency": "Once a year",
        "eligibility": "Indian citizens who have a bachelor's degree from a recognized university.",
        "age_limit": "21-32 years for General category (with relaxations for reserved categories)",
        "exam_pattern": "Three-stage examination: Preliminary (objective), Mains (written), and Interview (personality test).",
        "syllabus": "Preliminary: General Studies and CSAT. Mains: Essay, General Studies Papers (I, II, III, IV), Optional Subject Papers (I, II).",
        "application_procedure": "Online application through the UPSC website. Registration typically opens in February-March.",
        "important_dates": {
            "application_start": "Generally in February",
            "application_end": "Generally in March",
            "prelims_exam_date": "Generally in May-June",
            "mains_exam_date": "Generally in September",
            "interview_date": "Generally in March-May (of the following year)",
            "final_result_date": "Generally in May-June (of the following year)"
        },
        "website": "https://www.upsc.gov.in/",
        "preparation_tips": [
            "Create a comprehensive study plan",
            "Read newspapers daily for current affairs",
            "Make notes for quick revision",
            "Practice answer writing for Mains",
            "Regularly attempt mock tests"
        ]
    },
    # BANKING EXAMS
    {
        "id": "sbi_po",
        "name": "SBI PO",
        "full_name": "State Bank of India Probationary Officer",
        "category": "banking",
        "subcategory": "bank_po",
        "description": "SBI PO is a national level exam conducted for recruitment of Probationary Officers in State Bank of India.",
        "conducting_body": "State Bank of India (SBI)",
        "frequency": "Once a year",
        "eligibility": "Graduates in any discipline from a recognized university.",
        "age_limit": "21-30 years (with relaxations for reserved categories)",
        "exam_pattern": "Three phases: Preliminary Exam, Main Exam, and Group Exercise & Interview.",
        "syllabus": "Preliminary: English Language, Quantitative Aptitude, and Reasoning Ability. Mains: Reasoning & Computer Aptitude, Data Analysis & Interpretation, General/Economy/Banking Awareness, and English Language.",
        "application_procedure": "Online application through the SBI career website. Registration typically opens once a year.",
        "important_dates": {
            "application_start": "Generally in April",
            "application_end": "Generally in May",
            "prelims_exam_date": "Generally in July",
            "mains_exam_date": "Generally in August",
            "interview_date": "Generally in September-October",
            "final_result_date": "Generally in November"
        },
        "website": "https://sbi.co.in/web/careers",
        "preparation_tips": [
            "Focus on building speed and accuracy",
            "Practice quantitative aptitude and reasoning daily",
            "Stay updated with banking current affairs",
            "Attempt previous years' papers",
            "Take mock tests regularly"
        ]
    },
    # SSC EXAMS
    {
        "id": "ssc_cgl",
        "name": "SSC CGL",
        "full_name": "Staff Selection Commission Combined Graduate Level",
        "category": "ssc",
        "subcategory": "",
        "description": "SSC CGL is conducted for recruitment to various Group B and Group C posts in various Ministries/ Departments/ Organizations of the Government of India.",
        "conducting_body": "Staff Selection Commission (SSC)",
        "frequency": "Once a year",
        "eligibility": "Graduates in any discipline from a recognized university.",
        "age_limit": "18-32 years (varies for different posts, with relaxations for reserved categories)",
        "exam_pattern": "Four tiers: Tier 1 and Tier 2 (Computer Based Tests), Tier 3 (Descriptive Paper), and Tier 4 (Computer Proficiency Test/Skill Test).",
        "syllabus": "Tier 1: General Intelligence & Reasoning, General Awareness, Quantitative Aptitude, and English Comprehension. Tier 2: Quantitative Abilities, English Language & Comprehension, Statistics, and General Studies (Finance & Economics).",
        "application_procedure": "Online application through the SSC website. Registration typically opens once a year.",
        "important_dates": {
            "application_start": "Generally in October",
            "application_end": "Generally in November",
            "tier_1_exam_date": "Generally in February-March",
            "tier_2_exam_date": "Generally in June",
            "tier_3_exam_date": "Generally in September",
            "tier_4_exam_date": "Generally in December",
            "final_result_date": "Generally in March (of the following year)"
        },
        "website": "https://ssc.nic.in/",
        "preparation_tips": [
            "Focus on the basics of all subjects",
            "Practice numerical ability and reasoning regularly",
            "Improve English grammar and vocabulary",
            "Stay updated with current affairs",
            "Take timed mock tests to improve speed"
        ]
    },
    # DEFENCE EXAMS
    {
        "id": "cds",
        "name": "CDS",
        "full_name": "Combined Defence Services",
        "category": "defense",
        "subcategory": "def_army",
        "description": "CDS is conducted for admission to the Indian Military Academy, Indian Naval Academy, Air Force Academy, and Officers Training Academy.",
        "conducting_body": "Union Public Service Commission (UPSC)",
        "frequency": "Twice a year",
        "eligibility": "Graduates for IMA, INA, and AFA. Graduates/Final year students for OTA.",
        "age_limit": "19-24 years for IMA, INA, and AFA. 19-25 years for OTA.",
        "exam_pattern": "Written exam followed by SSB Interview. Written exam consists of English, General Knowledge, and Elementary Mathematics (except for OTA).",
        "syllabus": "English: Comprehension, Error Detection, Synonyms, Antonyms, etc. General Knowledge: Current Affairs, History, Geography, etc. Elementary Mathematics: Arithmetic, Algebra, Trigonometry, Geometry, Statistics, etc.",
        "application_procedure": "Online application through the UPSC website. Registration opens twice a year.",
        "important_dates": {
            "application_start": "Generally in November (for April exam) and June (for November exam)",
            "application_end": "Generally in December (for April exam) and July (for November exam)",
            "exam_date": "Generally in April and November",
            "ssb_interview": "3-4 months after the written exam",
            "final_result_date": "Generally 6-7 months after the written exam"
        },
        "website": "https://www.upsc.gov.in/",
        "preparation_tips": [
            "Focus on building strong fundamentals in all subjects",
            "Stay updated with current affairs",
            "Practice mathematics regularly",
            "Improve English communication skills",
            "Prepare for physical fitness tests"
        ]
    }
]

# Helper functions to work with the exam data

def get_exam_categories():
    """
    Returns the list of all exam categories.
    """
    return EXAM_CATEGORIES

def get_exams_by_category(category_id):
    """
    Returns a list of exams for a specific category.
    """
    return [exam for exam in EXAMS_DATA if exam['category'] == category_id]

def get_exams_by_subcategory(subcategory_id):
    """
    Returns a list of exams for a specific subcategory.
    """
    return [exam for exam in EXAMS_DATA if 'subcategory' in exam and exam['subcategory'] == subcategory_id]

def get_exam_details(exam_id):
    """
    Returns the details of a specific exam.
    """
    for exam in EXAMS_DATA:
        if exam['id'] == exam_id:
            return exam
    return None

def search_exams(query):
    """
    Searches for exams by name or description.
    """
    query = query.lower()
    results = []
    
    for exam in EXAMS_DATA:
        # Check if query matches with exam name, full name, or description
        if (query in exam['name'].lower() or 
            ('full_name' in exam and query in exam['full_name'].lower()) or 
            query in exam['description'].lower()):
            results.append(exam)
    
    return results
