import streamlit as st
import requests

st.set_page_config(page_title="AI Data Extractor", layout="centered")

st.title("📊 AI Data Extraction System")

st.write("Upload your PDF / CSV / Excel file to process data automatically.")

# File Upload
uploaded_file = st.file_uploader("Upload File", type=["pdf", "csv", "xlsx"])

if uploaded_file is not None:
    st.success("File uploaded successfully ✅")

    if st.button("Process File 🚀"):
        with st.spinner("Processing..."):

            files = {"file": uploaded_file.getvalue()}
            response = requests.post(
                "http://127.0.0.1:8001/process/",
                files={"file": uploaded_file}
            )

            if response.status_code == 200:
                data = response.json()

                st.success(data["message"])

                if "errors" in data and data["errors"]:
                    st.warning("⚠️ Validation Errors:")
                    for err in data["errors"]:
                        st.write(err)

                # Download Button 🔥
                with open("output.csv", "rb") as f:
                    st.download_button(
                        label="📥 Download Output CSV",
                        data=f,
                        file_name="output.csv",
                        mime="text/csv"
                    )

            else:
                st.error("Something went wrong ❌")