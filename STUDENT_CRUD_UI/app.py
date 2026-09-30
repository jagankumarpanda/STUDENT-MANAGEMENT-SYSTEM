
import streamlit as st
import requests
import pandas as pd

# ==================================================
# CONFIGURATION
# ==================================================

BASE_URL = "https://student-management-system-uxo9.onrender.com/api"

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide",
)

# ==================================================
# SIMPLE PROFESSIONAL STYLING
# ==================================================

st.markdown(
    """
    <style>

    /* Page */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Header */
    .app-header {
        background-color: #1976d2;
        padding: 22px 28px;
        border-radius: 12px;
        margin-bottom: 22px;
    }

    .app-title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .app-subtitle {
        color: #e3f2fd;
        font-size: 0.95rem;
        margin-top: 5px;
    }

    /* Metric cards */
    .metric-card {
        background-color: white;
        padding: 18px 20px;
        border-radius: 10px;
        border: 1px solid #e1e7ef;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }

    .metric-label {
        color: #64748b;
        font-size: 0.9rem;
    }

    .metric-value {
        color: #1565c0;
        font-size: 1.6rem;
        font-weight: 700;
        margin-top: 4px;
    }

    /* Section heading */
    .section-title {
        color: #1e293b;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 12px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        background-color: white;
        padding: 5px;
        border-radius: 10px;
        border: 1px solid #e1e7ef;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 7px;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background-color: #e3f2fd;
        color: #1565c0;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 7px;
        font-weight: 500;
    }

    /* Inputs */
    .stTextInput input,
    .stNumberInput input {
        border-radius: 7px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.8rem;
        padding: 25px 0 5px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# HELPER FUNCTIONS
# ==================================================

def fetch_all():
    try:
        response = requests.get(
            f"{BASE_URL}/students",
            timeout=10
        )

        if response.status_code == 200:
            return response.json().get("data", [])

        return None

    except requests.exceptions.RequestException:
        return None


def fetch_student(student_id):
    try:
        response = requests.get(
            f"{BASE_URL}/students/{student_id}",
            timeout=10
        )

        if response.status_code == 200:
            return response.json().get("data")

        return None

    except requests.exceptions.RequestException:
        return None


# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <div class="app-header">
        <div class="app-title">🎓 Student Management System</div>
        <div class="app-subtitle">
            Manage student records, courses and fee information
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# FETCH DATA
# ==================================================

students_data = fetch_all()

if students_data is None:
    st.error("⚠️ Unable to connect to the backend. Please try again.")
    st.stop()

# ==================================================
# METRICS
# ==================================================

df_raw = pd.DataFrame(students_data)

if not df_raw.empty:

    df_raw.columns = [
        str(column).upper()
        for column in df_raw.columns
    ]

    total_students = len(df_raw)

    active_courses = (
        df_raw["COURSE"].nunique()
        if "COURSE" in df_raw.columns
        else 0
    )

    total_fee = (
        pd.to_numeric(
            df_raw["FEE"],
            errors="coerce"
        )
        .fillna(0)
        .sum()
        if "FEE" in df_raw.columns
        else 0
    )

else:

    total_students = 0
    active_courses = 0
    total_fee = 0


m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">👨‍🎓 Total Students</div>
            <div class="metric-value">{total_students}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">📚 Active Courses</div>
            <div class="metric-value">{active_courses}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">💰 Total Fees</div>
            <div class="metric-value">₹{total_fee:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ==================================================
# TABS
# ==================================================

tab_view, tab_add, tab_update, tab_delete = st.tabs(
    [
        "📋 Students",
        "➕ Add Student",
        "✏️ Update Student",
        "🗑️ Delete Student",
    ]
)

# ==================================================
# STUDENTS TAB
# ==================================================

with tab_view:

    st.markdown(
        '<div class="section-title">📋 Student Records</div>',
        unsafe_allow_html=True,
    )

    search_col, refresh_col = st.columns([5, 1])

    with search_col:

        search = st.text_input(
            "Search",
            placeholder="🔍 Search by name or course...",
            label_visibility="collapsed",
        )

    with refresh_col:

        if st.button(
            "🔄 Refresh",
            use_container_width=True
        ):
            st.rerun()

    if not students_data:

        st.info(
            "No student records found. Add a student to get started."
        )

    else:

        df = pd.DataFrame(students_data)

        df.columns = [
            str(column).upper()
            for column in df.columns
        ]

        if search:

            mask = (
                df["NAME"]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                df["COURSE"]
                .astype(str)
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            )

            df = df[mask]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

# ==================================================
# ADD STUDENT
# ==================================================

with tab_add:

    st.markdown(
        '<div class="section-title">➕ Register New Student</div>',
        unsafe_allow_html=True,
    )

    with st.form(
        "create_form",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Student Name",
                placeholder="Enter student name",
            )

        with col2:

            course = st.text_input(
                "Course Name",
                placeholder="Enter course name",
            )

        fee = st.number_input(
            "Course Fee (₹)",
            min_value=1.0,
            value=5000.0,
            step=500.0,
        )

        submitted = st.form_submit_button(
            "➕ Add Student",
            use_container_width=True,
        )

        if submitted:

            name_clean = name.strip()
            course_clean = course.strip()

            if not 3 <= len(name_clean) <= 15:

                st.warning(
                    "Student name must contain 3–15 characters."
                )

            elif not 3 <= len(course_clean) <= 15:

                st.warning(
                    "Course name must contain 3–15 characters."
                )

            else:

                payload = {
                    "name": name_clean,
                    "course": course_clean,
                    "fee": float(fee),
                }

                try:

                    response = requests.post(
                        f"{BASE_URL}/student",
                        json=payload,
                        timeout=10,
                    )

                    if response.status_code == 201:

                        st.success(
                            f"✅ Student '{name_clean}' added successfully!"
                        )

                    else:

                        st.error(
                            f"Failed to add student: {response.text}"
                        )

                except requests.exceptions.RequestException:

                    st.error(
                        "Unable to connect to the backend."
                    )

# ==================================================
# UPDATE STUDENT
# ==================================================

with tab_update:

    st.markdown(
        '<div class="section-title">✏️ Update Student</div>',
        unsafe_allow_html=True,
    )

    if students_data:

        df_students = pd.DataFrame(students_data)

        df_students.columns = [
            str(column).upper()
            for column in df_students.columns
        ]

        student_options = {
            f"{row['ID']} — {row['NAME']} ({row['COURSE']})":
            int(row["ID"])
            for _, row in df_students.iterrows()
        }

        selected_student = st.selectbox(
            "Select Student",
            list(student_options.keys()),
        )

        selected_id = student_options[selected_student]

        if st.button(
            "Fetch Student Details",
            use_container_width=True
        ):

            student = fetch_student(selected_id)

            if student:

                st.session_state["edit_data"] = student

            else:

                st.error(
                    "Unable to find the selected student."
                )

        cached = st.session_state.get("edit_data")

        if cached:

            with st.form("edit_form"):

                col1, col2 = st.columns(2)

                with col1:

                    up_name = st.text_input(
                        "Student Name",
                        value=str(
                            cached.get("NAME", "")
                        ),
                    )

                with col2:

                    up_course = st.text_input(
                        "Course",
                        value=str(
                            cached.get("COURSE", "")
                        ),
                    )

                up_fee = st.number_input(
                    "Course Fee (₹)",
                    min_value=1.0,
                    value=float(
                        cached.get("FEE", 1000.0)
                    ),
                    step=500.0,
                )

                save = st.form_submit_button(
                    "💾 Save Changes",
                    use_container_width=True,
                )

                if save:

                    payload = {
                        "name": up_name.strip(),
                        "course": up_course.strip(),
                        "fee": float(up_fee),
                    }

                    try:

                        response = requests.put(
                            f"{BASE_URL}/students/{selected_id}",
                            json=payload,
                            timeout=10,
                        )

                        if response.status_code == 200:

                            st.success(
                                f"✅ Student ID {selected_id} updated successfully!"
                            )

                            st.session_state.pop(
                                "edit_data",
                                None
                            )

                            st.rerun()

                        else:

                            st.error(
                                f"Update failed: {response.text}"
                            )

                    except requests.exceptions.RequestException:

                        st.error(
                            "Unable to connect to the backend."
                        )

    else:

        st.info(
            "No students available to update."
        )

# ==================================================
# DELETE STUDENT
# ==================================================

with tab_delete:

    st.markdown(
        '<div class="section-title">🗑️ Delete Student</div>',
        unsafe_allow_html=True,
    )

    if students_data:

        df_students = pd.DataFrame(students_data)

        df_students.columns = [
            str(column).upper()
            for column in df_students.columns
        ]

        student_options = {
            f"{row['ID']} — {row['NAME']} ({row['COURSE']})":
            int(row["ID"])
            for _, row in df_students.iterrows()
        }

        selected_student = st.selectbox(
            "Select Student to Delete",
            list(student_options.keys()),
            key="delete_student",
        )

        selected_id = student_options[selected_student]

        confirm = st.checkbox(
            f"I confirm that I want to delete Student ID #{selected_id}"
        )

        if st.button(
            "🗑️ Delete Student",
            type="primary",
            use_container_width=True,
        ):

            if not confirm:

                st.warning(
                    "Please confirm the deletion first."
                )

            else:

                try:

                    response = requests.delete(
                        f"{BASE_URL}/students/{selected_id}",
                        timeout=10,
                    )

                    if response.status_code == 200:

                        st.success(
                            f"✅ Student ID {selected_id} deleted successfully!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            f"Delete failed: {response.text}"
                        )

                except requests.exceptions.RequestException:

                    st.error(
                        "Unable to connect to the backend."
                    )

    else:

        st.info(
            "No students available to delete."
        )

# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        Student Management System • FastAPI • MySQL • Docker • Cloud
    </div>
    """,
    unsafe_allow_html=True,
)
