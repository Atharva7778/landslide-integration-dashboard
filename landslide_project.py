import time
from datetime import datetime

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Landslide | Integration Lab",
    page_icon="🌍",
    layout="wide"
)

# ---------- HEADER ----------
st.title("🌍 Landslide Integration & Testing Lab")
st.caption(
    "Drone-based landslide monitoring | "
    "Software prototype v1.0"
)

st.info(
    "PROTOTYPE MODE: Detection is simulated for testing. "
    "No real AI model or drone hardware is connected."
)

# ---------- STATUS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Model", "Simulation")

with col2:
    st.metric("Drone Connection", "Not connected")

with col3:
    st.metric("Testing Mode", "Active")

st.divider()

# ---------- MAIN WORKSPACE ----------
left, right = st.columns([1, 1])

with left:
    st.subheader("01 · Image Input")

    uploaded_file = st.file_uploader(
        "Upload a hillside or landslide image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(
            image,
            caption="Uploaded test image",
            use_container_width=True
        )
        st.success("Image received successfully.")
    else:
        st.warning("Upload an image to begin testing.")

with right:
    st.subheader("02 · Integration Test")

    scenario = st.selectbox(
        "Select a test scenario",
        [
            "Simulated landslide detection",
            "Simulated no-detection case",
            "Simulated communication failure"
        ]
    )

    st.write(
        "This test checks the software response logic. "
        "It does not determine whether the image contains "
        "a real landslide."
    )

    run_test = st.button(
        "▶ Run Integration Test",
        type="primary",
        use_container_width=True
    )

    if run_test:
        if uploaded_file is None:
            st.error("Please upload an image first.")
        else:
            start = time.perf_counter()

            # Simulated system behaviour
            if scenario == "Simulated landslide detection":
                result = "Detection event simulated"
                response = "Alert logic triggered"
                status = "PASS"

            elif scenario == "Simulated no-detection case":
                result = "No-detection event simulated"
                response = "No alert triggered"
                status = "PASS"

            else:
                result = "Communication failure simulated"
                response = "Response unavailable"
                status = "FAIL"

            latency_ms = (
                time.perf_counter() - start
            ) * 1000

            st.session_state["last_test"] = {
                "time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "scenario": scenario,
                "result": result,
                "response": response,
                "status": status,
                "latency": latency_ms
            }

# ---------- RESULTS ----------
st.divider()
st.subheader("03 · Test Results")

test = st.session_state.get("last_test")

if test:
    a, b, c = st.columns(3)

    with a:
        st.metric("Test Status", test["status"])

    with b:
        st.metric(
            "Software Execution Time",
            f'{test["latency"]:.3f} ms'
        )

    with c:
        st.metric("Hardware Status", "Not connected")

    st.write("**Scenario:**", test["scenario"])
    st.write("**Event:**", test["result"])
    st.write("**Expected response:**", test["response"])
    st.write("**Test timestamp:**", test["time"])

    st.caption(
        "Timing covers only the local simulation logic. "
        "It excludes image analysis, network transmission, "
        "and physical hardware response."
    )

    report = (
        "LANDSLIDE INTEGRATION TEST REPORT\n"
        f'Timestamp: {test["time"]}\n'
        f'Scenario: {test["scenario"]}\n'
        f'Status: {test["status"]}\n'
        f'Event: {test["result"]}\n'
        f'Response: {test["response"]}\n'
        f'Simulation time: {test["latency"]:.3f} ms\n'
        "AI: Simulated\n"
        "Drone hardware: Not connected\n"
    )

    st.download_button(
        "Download Test Report",
        data=report,
        file_name="integration_test_report.txt",
        mime="text/plain"
    )
else:
    st.write(
        "No test has been run yet. Upload an image "
        "and select a test scenario above."
    )

# ---------- FOOTER ----------
st.divider()
st.caption(
    "Systems Integration & Testing | "
    "Drone-Based Landslide Detection Project"
)