import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000/api"

st.set_page_config(page_title="Student Management", page_icon="🎓", layout="wide")

st.title("🎓 Student Management Portal")

# Helper function to fetch all records
def fetch_all():
    try:
        res = requests.get(f"{BASE_URL}/students", timeout=3)
        if res.status_code == 200:
            return res.json().get("data", [])
    except requests.exceptions.ConnectionError:
        return None
    return []

students_data = fetch_all()

# Top Metric Cards
if students_data:
    df_raw = pd.DataFrame(students_data)
    df_raw.columns = [str(col).upper() for col in df_raw.columns]

    total_count = len(df_raw)
    active_courses = df_raw["COURSE"].nunique() if "COURSE" in df_raw.columns else 0
    total_fee = pd.to_numeric(df_raw.get("FEE", 0), errors="coerce").fillna(0).sum()

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Students", total_count)
    m2.metric("Active Courses", active_courses)
    m3.metric("Total Fee Collected", f"₹{total_fee:,.2f}")
    st.divider()

# Navigation Tabs
tab_view, tab_add, tab_update, tab_delete = st.tabs(
    ["📋 All Students", "➕ Add Student", "✏️ Update Student", "🗑️ Delete Student"]
)

# ---------------- Tab 1: All Students ----------------
with tab_view:
    head_col, btn_col = st.columns([5, 1])
    head_col.subheader("Enrolled Students")
    if btn_col.button("🔄 Refresh"):
        st.rerun()

    if students_data is None:
        st.error("⚠️ Backend offline. Ensure FastAPI is running on http://127.0.0.1:8000")
    elif len(students_data) == 0:
        st.info("No records found in the database.")
    else:
        df = pd.DataFrame(students_data)
        df.columns = [str(col).upper() for col in df.columns]

        search = st.text_input("🔍 Filter by Name or Course", placeholder="Type to search...")
        if search:
            mask = df["NAME"].astype(str).str.contains(search, case=False, na=False) | \
                   df["COURSE"].astype(str).str.contains(search, case=False, na=False)
            df = df[mask]

        st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------- Tab 2: Add Student ----------------
with tab_add:
    st.subheader("Register New Student")
    with st.form("create_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Student Name (3-15 chars)")
        course = c2.text_input("Course Name (3-15 chars)")
        fee = st.number_input("Course Fee (₹)", min_value=1.0, value=5000.0, step=500.0)

        if st.form_submit_button("Submit"):
            name_clean = name.strip()
            course_clean = course.strip()
            if len(name_clean) < 3 or len(name_clean) > 15:
                st.warning("Name must be between 3 and 15 characters.")
            elif len(course_clean) < 3 or len(course_clean) > 15:
                st.warning("Course must be between 3 and 15 characters.")
            else:
                payload = {"name": name_clean, "course": course_clean, "fee": float(fee)}
                try:
                    res = requests.post(f"{BASE_URL}/student", json=payload)
                    if res.status_code == 201:
                        st.success(f"Student '{name_clean}' added successfully!")
                    else:
                        st.error(f"Failed: {res.text}")
                except Exception:
                    st.error("Server connection failed.")

# ---------------- Tab 3: Update Student ----------------
with tab_update:
    st.subheader("Edit Student Record")
    u_col1, _ = st.columns([1, 2])
    target_id = u_col1.number_input("Enter Student ID to Edit", min_value=1, step=1, key="target_id")

    if u_col1.button("Fetch Details"):
        try:
            res = requests.get(f"{BASE_URL}/students/{target_id}")
            data = res.json().get("data")
            if data:
                st.session_state["edit_data"] = {str(k).upper(): v for k, v in data.items()}
            else:
                st.session_state["edit_data"] = None
                st.warning(f"Student ID {target_id} not found.")
        except Exception:
            st.error("Connection failed.")

    cached = st.session_state.get("edit_data")
    if cached:
        with st.form("edit_form"):
            col1, col2 = st.columns(2)
            up_name = col1.text_input("Name", value=str(cached.get("NAME", "")))
            up_course = col2.text_input("Course", value=str(cached.get("COURSE", "")))
            up_fee = st.number_input("Fee (₹)", min_value=1.0, value=float(cached.get("FEE", 1000.0)), step=500.0)

            if st.form_submit_button("Save Changes"):
                payload = {"name": up_name.strip(), "course": up_course.strip(), "fee": float(up_fee)}
                try:
                    res = requests.put(f"{BASE_URL}/students/{target_id}", json=payload)
                    if res.status_code == 200:
                        st.success(f"Student ID {target_id} updated!")
                        st.session_state["edit_data"] = None
                    else:
                        st.error(f"Update failed: {res.text}")
                except Exception:
                    st.error("Connection failed.")

# ---------------- Tab 4: Delete Student ----------------
with tab_delete:
    st.subheader("Remove Student Record")
    d_id = st.number_input("Enter Student ID to Delete", min_value=1, step=1, key="d_id")
    confirm = st.checkbox(f"Confirm deletion of ID #{d_id}")

    if st.button("Delete Student", type="primary"):
        if not confirm:
            st.warning("Please check the confirmation box first.")
        else:
            try:
                res = requests.delete(f"{BASE_URL}/students/{d_id}")
                if res.status_code == 200:
                    st.success(f"Student ID {d_id} deleted successfully.")
                else:
                    st.error(f"Failed: {res.text}")
            except Exception:
                st.error("Server connection failed.")