import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Ephemeral IAM Guard",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #f4f7fb;
        --panel: #ffffff;
        --panel-2: #eef4fb;
        --panel-3: #0f172a;
        --text: #0f172a;
        --muted: #5b6475;
        --line: #d9e2ec;
        --primary: #0f766e;
        --primary-2: #06b6d4;
        --accent: #f97316;
        --success-bg: #dcfce7;
        --success-text: #166534;
        --warn-bg: #fef3c7;
        --warn-text: #92400e;
        --danger-bg: #fee2e2;
        --danger-text: #991b1b;
        --shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        --radius-xl: 24px;
        --radius-lg: 18px;
        --radius-md: 14px;
    }

    html, body, [class*="css"] {
        font-family: 'Manrope', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(6,182,212,0.10), transparent 22%),
            radial-gradient(circle at left bottom, rgba(249,115,22,0.08), transparent 24%),
            linear-gradient(180deg, #f8fbff 0%, #f4f7fb 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1350px;
        padding-top: 1.2rem;
        padding-bottom: 1.5rem;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        background: rgba(255,255,255,0.88);
        border: 1px solid rgba(15,23,42,0.06);
        border-radius: 22px;
        padding: 1rem 1.2rem;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
    }

    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }

    .brand-icon {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        background: linear-gradient(135deg, #0f766e, #06b6d4);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.4rem;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(6, 182, 212, 0.22);
    }

    .brand-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.1rem;
    }

    .brand-sub {
        font-size: 0.9rem;
        color: var(--muted);
    }

    .top-pill {
        display: inline-block;
        padding: 0.48rem 0.85rem;
        border-radius: 999px;
        background: #ecfeff;
        color: #155e75;
        border: 1px solid #bae6fd;
        font-size: 0.82rem;
        font-weight: 700;
        margin-left: 0.4rem;
    }

    .panel {
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(15,23,42,0.07);
        border-radius: var(--radius-xl);
        padding: 1.2rem;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
    }

    .panel-dark {
        background: linear-gradient(135deg, #0f172a, #162033);
        color: #f8fafc;
        border-radius: var(--radius-xl);
        padding: 1.2rem;
        box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.85rem;
    }

    .section-title-light {
        font-size: 1rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.85rem;
    }

    .muted {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.6;
    }

    .mini-card {
        background: linear-gradient(180deg, #ffffff, #f7fbff);
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        min-height: 110px;
    }

    .mini-label {
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.45rem;
    }

    .mini-value {
        color: var(--text);
        font-size: 1.05rem;
        font-weight: 800;
        line-height: 1.35;
    }

    .mini-desc {
        color: var(--muted);
        font-size: 0.86rem;
        margin-top: 0.35rem;
        line-height: 1.45;
    }

    .decision-box {
        border-radius: 20px;
        padding: 1rem 1.1rem;
        text-align: center;
        font-weight: 800;
        font-size: 1rem;
        margin-bottom: 1rem;
    }

    .approved {
        background: var(--success-bg);
        color: var(--success-text);
        border: 1px solid #86efac;
    }

    .conditional {
        background: var(--warn-bg);
        color: var(--warn-text);
        border: 1px solid #fcd34d;
    }

    .denied {
        background: var(--danger-bg);
        color: var(--danger-text);
        border: 1px solid #fca5a5;
    }

    .info-grid {
        background: #f8fbff;
        border: 1px solid #dbe7f3;
        border-radius: 18px;
        padding: 1rem;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        gap: 0.8rem;
        padding: 0.6rem 0;
        border-bottom: 1px dashed #d7e3ef;
        font-size: 0.94rem;
    }

    .info-row:last-child {
        border-bottom: none;
    }

    .info-key {
        color: var(--muted);
        font-weight: 600;
    }

    .info-value {
        color: var(--text);
        font-weight: 700;
        text-align: right;
    }

    .badge {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        margin: 0.18rem;
        border-radius: 999px;
        background: #e6fffb;
        border: 1px solid #b5f5ec;
        color: #115e59;
        font-size: 0.82rem;
        font-weight: 700;
    }

    .badge-dark {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        margin: 0.18rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.14);
        color: #e2e8f0;
        font-size: 0.82rem;
        font-weight: 700;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    .stTextInput > div > div,
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 1px solid #d5e0ea !important;
        border-radius: 16px !important;
        min-height: 48px;
        box-shadow: none !important;
    }

    input, textarea, [data-baseweb="input"] input {
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
        caret-color: #0f172a !important;
        font-size: 15px !important;
    }

    input::placeholder, textarea::placeholder {
        color: #94a3b8 !important;
        -webkit-text-fill-color: #94a3b8 !important;
    }

    .stTextInput label, .stSelectbox label {
        color: #334155 !important;
        font-weight: 700 !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        border-radius: 16px;
        padding: 0.85rem 1rem;
        font-size: 0.98rem;
        font-weight: 800;
        border: none;
        background: linear-gradient(135deg, #0f766e, #06b6d4);
        color: white;
        box-shadow: 0 12px 24px rgba(6, 182, 212, 0.22);
    }

    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #0f766e, #06b6d4) !important;
    }

    .stProgress > div > div {
        background-color: #dbeafe !important;
    }

    .hint-box {
        background: #fff7ed;
        border: 1px solid #fed7aa;
        color: #9a3412;
        border-radius: 18px;
        padding: 0.95rem 1rem;
        font-size: 0.9rem;
        line-height: 1.55;
    }

    .footer-note {
        text-align: center;
        color: var(--muted);
        font-size: 0.83rem;
        padding-top: 0.4rem;
    }

    @media (max-width: 900px) {
        .topbar {
            flex-direction: column;
            align-items: flex-start;
        }
    }
    </style>
    """, unsafe_allow_html=True)

POLICY_MATRIX = {
    "Developer": ["Staging VM", "Test S3 Bucket", "Dev Database"],
    "DevOps": ["Staging VM", "Test S3 Bucket", "Dev Database", "CI/CD Runner"],
    "Security Analyst": ["IAM Logs", "Cloud Audit Trail", "Security Group Rules"],
    "Intern": ["Test S3 Bucket"]
}

def evaluate_access(role, resource, location, device, time_of_day, justification):
    allowed = resource in POLICY_MATRIX.get(role, [])
    risk_score = 0

    if location not in ["Coimbatore", "India"]:
        risk_score += 2
    if device == "Unmanaged":
        risk_score += 2
    if time_of_day in ["Night", "Late Night"]:
        risk_score += 1
    if len(justification.strip()) < 10:
        risk_score += 1

    if not allowed:
        return "Denied", "Role-policy mismatch", risk_score

    if risk_score >= 4:
        return "Denied", "High contextual risk detected", risk_score
    elif risk_score >= 2:
        return "Conditional", "MFA or manager approval required", risk_score
    else:
        return "Approved", "Temporary least-privilege access granted", risk_score

def generate_temp_credential():
    now = datetime.now()
    expiry = now + timedelta(minutes=15)
    return {
        "issued_at": now.strftime("%d-%m-%Y %H:%M:%S"),
        "expires_at": expiry.strftime("%d-%m-%Y %H:%M:%S"),
        "session_id": f"STS-{now.strftime('%H%M%S')}",
        "duration": "15 minutes"
    }

def decision_class(status):
    if status == "Approved":
        return "approved"
    elif status == "Conditional":
        return "conditional"
    return "denied"

load_css()

st.markdown("""
<div class="topbar">
    <div class="brand-wrap">
        <div class="brand-icon">🔐</div>
        <div>
            <div class="brand-title">Ephemeral IAM Guard</div>
            <div class="brand-sub">Context-aware temporary cloud access console</div>
        </div>
    </div>
    <div>
        <span class="top-pill">Zero Standing Privilege</span>
        <span class="top-pill">Ephemeral Sessions</span>
        <span class="top-pill">Dynamic Trust Review</span>
    </div>
</div>
""", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4, gap="large")
with k1:
    st.markdown("""
    <div class="mini-card">
        <div class="mini-label">Policy Engine</div>
        <div class="mini-value">Role + Context</div>
        <div class="mini-desc">Maps user role to allowed resources before issuing access.</div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown("""
    <div class="mini-card">
        <div class="mini-label">Session Window</div>
        <div class="mini-value">15 Min Max</div>
        <div class="mini-desc">Access is temporary and auto-expires without standing privilege.</div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown("""
    <div class="mini-card">
        <div class="mini-label">Signals</div>
        <div class="mini-value">Location / Device / Time</div>
        <div class="mini-desc">Context is scored to decide approval, denial, or conditional flow.</div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown("""
    <div class="mini-card">
        <div class="mini-label">Decision Mode</div>
        <div class="mini-value">Least Privilege</div>
        <div class="mini-desc">Only the minimum mapped resource can be granted temporarily.</div>
    </div>
    """, unsafe_allow_html=True)

left, right = st.columns([1, 1.25], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Request Access</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">Submit a short-lived access request for a cloud resource. The engine evaluates role mapping and trust signals before issuing a session.</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("iam_form"):
        role = st.selectbox("User Role", ["Developer", "DevOps", "Security Analyst", "Intern"])
        resource = st.selectbox("Ephemeral Resource", ["Staging VM", "Test S3 Bucket", "Dev Database", "CI/CD Runner", "IAM Logs", "Cloud Audit Trail", "Security Group Rules"])
        location = st.selectbox("Access Location", ["Coimbatore", "India", "Other Country"])
        device = st.selectbox("Device Type", ["Managed", "Unmanaged"])
        time_of_day = st.selectbox("Request Time", ["Morning", "Afternoon", "Evening", "Night", "Late Night"])
        sensitivity = st.selectbox("Resource Sensitivity", ["Low", "Medium", "High"])
        justification = st.text_input("Business Justification", "Need temporary access for deployment validation")
        submitted = st.form_submit_button("Run Access Evaluation")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="panel-dark">
        <div class="section-title-light">Policy Preview</div>
        <div style="margin-top:0.25rem;">
            <span class="badge-dark">Short-lived credentials</span>
            <span class="badge-dark">Continuous verification</span>
            <span class="badge-dark">Risk-based decision</span>
            <span class="badge-dark">Auto revocation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Live Decision Workspace</div>', unsafe_allow_html=True)

    if submitted:
        status, reason, risk_score = evaluate_access(role, resource, location, device, time_of_day, justification)
        creds = generate_temp_credential()

        st.markdown(f'<div class="decision-box {decision_class(status)}">{status} — {reason}</div>', unsafe_allow_html=True)

        a1, a2, a3 = st.columns(3, gap="medium")
        with a1:
            st.markdown(f"""
            <div class="mini-card">
                <div class="mini-label">Risk Score</div>
                <div class="mini-value">{risk_score}/5</div>
                <div class="mini-desc">Calculated from request context and justification strength.</div>
            </div>
            """, unsafe_allow_html=True)
        with a2:
            st.markdown(f"""
            <div class="mini-card">
                <div class="mini-label">Selected Role</div>
                <div class="mini-value">{role}</div>
                <div class="mini-desc">Used for role-policy mapping and least-privilege checks.</div>
            </div>
            """, unsafe_allow_html=True)
        with a3:
            st.markdown(f"""
            <div class="mini-card">
                <div class="mini-label">Resource Sensitivity</div>
                <div class="mini-value">{sensitivity}</div>
                <div class="mini-desc">Shown as request metadata in the evaluation workspace.</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        x1, x2 = st.columns(2, gap="large")
        with x1:
            st.markdown("""
            <div class="section-title">Decision Details</div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="info-grid">
                <div class="info-row"><div class="info-key">Decision</div><div class="info-value">{status}</div></div>
                <div class="info-row"><div class="info-key">Reason</div><div class="info-value">{reason}</div></div>
                <div class="info-row"><div class="info-key">Requested Resource</div><div class="info-value">{resource}</div></div>
                <div class="info-row"><div class="info-key">Location</div><div class="info-value">{location}</div></div>
                <div class="info-row"><div class="info-key">Device</div><div class="info-value">{device}</div></div>
                <div class="info-row"><div class="info-key">Time</div><div class="info-value">{time_of_day}</div></div>
            </div>
            """, unsafe_allow_html=True)

        with x2:
            st.markdown("""
            <div class="section-title">Temporary Session</div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="info-grid">
                <div class="info-row"><div class="info-key">Session ID</div><div class="info-value">{creds["session_id"]}</div></div>
                <div class="info-row"><div class="info-key">Issued At</div><div class="info-value">{creds["issued_at"]}</div></div>
                <div class="info-row"><div class="info-key">Expires At</div><div class="info-value">{creds["expires_at"]}</div></div>
                <div class="info-row"><div class="info-key">Max Duration</div><div class="info-value">{creds["duration"]}</div></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if status == "Approved":
            score_value = 86
        elif status == "Conditional":
            score_value = 58
        else:
            score_value = 24

        st.markdown('<div class="section-title">Trust Confidence</div>', unsafe_allow_html=True)
        st.progress(score_value)

        d1, d2 = st.columns(2, gap="large")
        with d1:
            st.markdown('<div class="section-title">Allowed Resources</div>', unsafe_allow_html=True)
            st.markdown("".join([f'<span class="badge">{item}</span>' for item in POLICY_MATRIX.get(role, [])]), unsafe_allow_html=True)
        with d2:
            st.markdown('<div class="section-title">Security Controls</div>', unsafe_allow_html=True)
            principles = ["MFA step-up", "Least privilege", "Session expiry", "Context review"]
            st.markdown("".join([f'<span class="badge">{item}</span>' for item in principles]), unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="hint-box">
            Fill the request form and run the evaluation to view the access decision, contextual risk, and temporary session metadata.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        p1, p2 = st.columns(2, gap="large")
        with p1:
            st.markdown("""
            <div class="mini-card">
                <div class="mini-label">Why this layout</div>
                <div class="mini-value">Operator-first workflow</div>
                <div class="mini-desc">The request form stays on the left while the results workspace updates on the right.</div>
            </div>
            """, unsafe_allow_html=True)
        with p2:
            st.markdown("""
            <div class="mini-card">
                <div class="mini-label">Security posture</div>
                <div class="mini-value">Zero-trust inspired</div>
                <div class="mini-desc">Access is granted only after policy fit and contextual trust are evaluated together.</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer-note">Ephemeral IAM demo interface for hackathons, cloud security showcases, and zero-trust access prototypes.</div>', unsafe_allow_html=True)
