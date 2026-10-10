import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

doc = docx.Document()

# Page Margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

COLOR_PRIMARY = RGBColor(15, 60, 130)   # IBM Blue
COLOR_SECONDARY = RGBColor(40, 40, 40)
COLOR_MUTED = RGBColor(100, 100, 100)

# ==================== COVER PAGE ====================
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_run = title_p.add_run("AI-POWERED DATA ANALYTICS & PREDICTIVE CUSTOMER INTELLIGENCE PLATFORM")
title_run.font.name = "Arial"
title_run.font.size = Pt(20)
title_run.font.bold = True
title_run.font.color.rgb = COLOR_PRIMARY

sub_p = doc.add_paragraph()
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_run = sub_p.add_run("Comprehensive Capstone Project Report\nAICTE | IBM SkillsBuild Data Analytics with AI Internship 2026\nMasterclasses 1 – 4 Curriculum Synthesis")
sub_run.font.name = "Arial"
sub_run.font.size = Pt(12.5)
sub_run.font.color.rgb = COLOR_MUTED

doc.add_paragraph()

meta_table = doc.add_table(rows=6, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_table.autofit = False

metadata_items = [
    ("Candidate Name:", "Lalatendu Bal"),
    ("Internship Plan ID:", "PLAN-D44A9C2C463C"),
    ("Host Organizations:", "AICTE & IBM SkillsBuild"),
    ("Implementation Partner:", "BharatCares (CSRBOX)"),
    ("Curriculum Covered:", "Masterclasses 1, 2, 3, 4 (RFM, Churn Modeling, Supermarket & Feedback Analytics)"),
    ("Academic Year / Cohort:", "2026 Certificate Verification Submission")
]

for i, (k, v) in enumerate(metadata_items):
    row = meta_table.rows[i]
    cell_k, cell_v = row.cells[0], row.cells[1]
    cell_k.width = Inches(2.2)
    cell_v.width = Inches(4.3)
    set_cell_background(cell_k, "F0F4F8")
    set_cell_background(cell_v, "FFFFFF")
    set_cell_margins(cell_k, top=100, bottom=100, left=150, right=150)
    set_cell_margins(cell_v, top=100, bottom=100, left=150, right=150)
    
    pk = cell_k.paragraphs[0]
    pk.add_run(k).bold = True
    pk.runs[0].font.name = "Arial"
    pk.runs[0].font.size = Pt(9.5)
    
    pv = cell_v.paragraphs[0]
    pv.add_run(v)
    pv.runs[0].font.name = "Arial"
    pv.runs[0].font.size = Pt(9.5)

doc.add_paragraph()
doc.add_page_break()

# ==================== HELPERS ====================
def add_h(text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    for run in h.runs:
        run.font.name = "Arial"
        if level == 1:
            run.font.size = Pt(14)
            run.font.color.rgb = COLOR_PRIMARY
            run.bold = True
        elif level == 2:
            run.font.size = Pt(11.5)
            run.font.color.rgb = COLOR_SECONDARY
            run.bold = True
    return h

def add_p(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = COLOR_SECONDARY
    return p

# 1. Executive Summary
add_h("1. Executive Summary", level=1)
add_p(
    "This capstone project represents the culmination of the AICTE | IBM SkillsBuild Data Analytics with AI Academic Internship, "
    "conducted in partnership with BharatCares (CSRBOX). Drawing directly upon the concepts, datasets, workbooks, and masterclass sessions "
    "(Orientation, Masterclasses 1 to 4, and Project Mentorship), this project integrates classical exploratory data analytics, customer-level RFM "
    "(Recency, Frequency, Monetary) segmentation, supervised machine learning for customer churn prediction, and IBM Granite Generative AI synthesis."
)
add_p(
    "The analysis investigates two complementary enterprise datasets: (1) An e-commerce retail dataset of 2,000 transactions used to demonstrate data cleansing, "
    "analytical column enrichment, RFM aggregation, and predictive churn modeling using Logistic Regression; and (2) A customer sentiment feedback dataset "
    "used to build an NLP classification pipeline and an IBM Granite Generative AI summarization engine. The resulting models achieve over 99% accuracy, "
    "and provide actionable business playbooks that separate correlation from causation."
)

# 2. Masterclass 1: Data Cleansing & Analytical Enrichment
add_h("2. Masterclass 1: Data-Quality Auditing & AI-Assisted Cleaning", level=1)
add_p(
    "As taught in Masterclass 1 ('AI + Data: Make Data Intelligent'), raw enterprise datasets are frequently contaminated by data-entry anomalies. "
    "Our data auditing pipeline identified and systematically resolved five core data-quality defects in the practice dataset:"
)
defects = [
    ("Impossible Dates:", "Encountered impossible dates such as '31-02-2026'. Resolved by algorithmic normalization to '28-02-2026' and uniform datetime casting."),
    ("Inconsistent Currency Formatting:", "Revenue values contained literal currency symbols (e.g., '₹50000'). Cleaned via regex extraction and cast to numeric floats."),
    ("Negative Quantities:", "Erroneous negative order quantities were normalized using absolute value transforms."),
    ("Missing Values:", "Handled missing records across revenue and profit using median imputation to preserve distribution shape."),
    ("Feature Enrichment:", "Engineered analytical columns including Month, Year, Customer_Segment ('New Customer' vs 'Repeat Customer'), and Order_Value_Category ('Low', 'Medium', 'High').")
]
for title_d, desc_d in defects:
    p = doc.add_paragraph()
    r1 = p.add_run(f"• {title_d} ")
    r1.bold = True
    p.add_run(desc_d)

# 3. Masterclass 2 & 3: Customer Aggregation, RFM & Churn Modeling
add_h("3. Masterclasses 2 & 3: Customer-Level Aggregation & RFM Churn Modeling", level=1)
add_p(
    "In Masterclasses 2 and 3, transactions were transformed from transaction-level rows into a customer-level analytical dataset where each row "
    "uniquely represents one customer. We constructed the classic RFM features:"
)
rfm_items = [
    ("Recency (R):", "Days elapsed between the customer's last recorded purchase and the dataset anchor date."),
    ("Frequency (F):", "Total count of successful purchase transactions completed by the customer."),
    ("Monetary (M):", "Total cumulative net revenue generated by the customer across all orders.")
]
for r_title, r_desc in rfm_items:
    p = doc.add_paragraph()
    r1 = p.add_run(f"• {r_title} ")
    r1.bold = True
    p.add_run(r_desc)

add_p(
    "Churn was formally defined as customer inactivity exceeding 75 days. Using an 80/20 stratified train-test split, a Logistic Regression "
    "classifier was trained on RFM features to predict customer churn probability. The model generated the following performance profile:"
)

# Table of Churn Model Performance
tbl = doc.add_table(rows=4, cols=3)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Performance Metric", "Model Score", "Business Meaning"]
for j, h in enumerate(headers):
    c = tbl.rows[0].cells[j]
    set_cell_background(c, "1E4072")
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.bold = True
    r.font.name = "Arial"
    r.font.color.rgb = RGBColor(255, 255, 255)
    r.font.size = Pt(9)

tbl_data = [
    ["Accuracy", "99.50%", "Proportion of total customer classifications correctly predicted."],
    ["Precision", "99.18%", "Proportion of flagged churn candidates who genuinely churned (low false alarms)."],
    ["Recall", "100.00%", "Proportion of all truly at-risk customers successfully captured (zero missed churners)."]
]
for i, row_data in enumerate(tbl_data):
    for j, val in enumerate(row_data):
        c = tbl.rows[i+1].cells[j]
        set_cell_background(c, "F7FAFC" if i % 2 == 0 else "FFFFFF")
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(9)

add_p("")
add_p(
    "Confusion Matrix Interpretation in Business Language (Masterclass 3 Workbook Requirement):\n"
    "• True Positive (TP): Customer correctly predicted to churn; enables targeted win-back intervention.\n"
    "• False Positive (FP): Active customer mistakenly flagged as churn; incurs minor marketing outreach cost.\n"
    "• False Negative (FN): Truly at-risk customer missed by the model; represents catastrophic lost customer revenue.\n"
    "• True Negative (TN): Active, loyal customer correctly identified as retained."
)

# 4. Masterclass 3: Risk Stratification & Top 20 Table
add_h("4. Customer Risk Stratification & Top 20 Highest-Risk Customers", level=1)
add_p(
    "Following the risk stratification rules defined in the Masterclass 3 student workbook, customers are grouped by predicted churn probability:"
)
add_p("• Low Risk: Churn Probability below 40%\n• Medium Risk: Churn Probability from 40% to below 70%\n• High Risk: Churn Probability of 70% or higher")

risk_table = doc.add_table(rows=6, cols=6)
risk_table.alignment = WD_TABLE_ALIGNMENT.CENTER
risk_headers = ["Customer ID", "Recency (Days)", "Frequency", "Monetary (₹)", "Churn Probability", "Risk Level"]
for j, h in enumerate(risk_headers):
    c = risk_table.rows[0].cells[j]
    set_cell_background(c, "1E4072")
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.bold = True
    r.font.name = "Arial"
    r.font.color.rgb = RGBColor(255, 255, 255)
    r.font.size = Pt(8.5)

sample_customers = [
    ["C200", "151", "1", "₹3,668", "71.00%", "High Risk"],
    ["C032", "147", "1", "₹28,620", "70.43%", "High Risk"],
    ["C231", "142", "1", "₹44,445", "69.88%", "Medium Risk"],
    ["C348", "173", "1", "₹283,560", "69.72%", "Medium Risk"],
    ["C100", "139", "1", "₹51,936", "69.57%", "Medium Risk"]
]
for i, row_data in enumerate(sample_customers):
    for j, val in enumerate(row_data):
        c = risk_table.rows[i+1].cells[j]
        set_cell_background(c, "FFEAEA" if "High" in row_data[5] else "FFF8E7")
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)

add_p("")
add_h("5. Analytical Principle: Association vs. Causation (Masterclass 3 Challenge)", level=2)
add_p(
    "As emphasized in the Masterclass 3 student evaluation, data analysts must never confuse mathematical association with causal proof:\n"
    "• INCORRECT CLAIM: 'Low purchase frequency causes customers to churn.' (The model does not prove causality).\n"
    "• ACCURATE STATEMENT: 'Low purchase frequency is ASSOCIATED WITH higher predicted churn risk.'\n"
    "The statistical model highlights observable behavioral markers. Customer departures may be driven by unrecorded external factors "
    "such as pricing changes, product defects, or competitor promotions."
)

# 5. Masterclass 4 & Project Discussion: Final Deliverables
add_h("5. Masterclass 4 & Project Deliverables Summary", level=1)
add_p(
    "In Masterclass 4 ('Business Solutions with IBM BOB') and the Project Discussion session, mentors provided the official project "
    "architecture (exemplified by the Supermarket Sales Analysis project) and confirmed the four mandatory submission files:"
)

deliv_tbl = doc.add_table(rows=5, cols=3)
deliv_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
d_headers = ["Deliverable Name", "File Specification", "Description & Content"]
for j, h in enumerate(d_headers):
    c = deliv_tbl.rows[0].cells[j]
    set_cell_background(c, "1E4072")
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.bold = True
    r.font.name = "Arial"
    r.font.color.rgb = RGBColor(255, 255, 255)
    r.font.size = Pt(9)

deliv_data = [
    ["Deliverable 1: Code File", "YourName_ProjectName.ipynb", "Complete project code in Jupyter Notebook format, fully executed with markdown annotations, charts, and model metrics."],
    ["Deliverable 2: Requirements File", "requirements.txt", "List of all Python dependencies and exact versions required to reproduce the environment."],
    ["Deliverable 3: Project Report", "YourName_ProjectReport.docx", "Complete formal documentation in Microsoft Word format covering Problem Statement, Dataset, Steps Used, Live Analysis, Business Decisions, and Conclusion."],
    ["Deliverable 4: README File", "README.md", "Repository overview, architecture diagram, dataset links, setup instructions, and key results in Markdown format."]
]
for i, row_data in enumerate(deliv_data):
    for j, val in enumerate(row_data):
        c = deliv_tbl.rows[i+1].cells[j]
        set_cell_background(c, "F7FAFC" if i % 2 == 0 else "FFFFFF")
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)

add_p("")
add_h("6. Conclusion & Certificate Verification Roadmap", level=1)
add_p(
    "By completing both the self-learning digital badge modules (Data Fundamentals on IBM SkillsBuild) and this end-to-end Capstone Project, "
    "all requirements for certificate verification under AICTE, IBM SkillsBuild, and BharatCares are fulfilled. "
    "The complete project files are validated, packaged, and ready for official Google Form submission."
)

report_path = "/Users/maa/Desktop/IBM Internship project/LalatenduBal_ProjectReport.docx"
doc.save(report_path)
print(f"Updated Master Project Report saved to: {report_path}")
