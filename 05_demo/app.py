import streamlit as st
from ultralytics import YOLO
from PIL import Image

MODEL_PATH = "best.pt"


@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


st.set_page_config(
    page_title="Car Damage Detection",
    layout="centered"
)

model = load_model()


# Header
st.markdown(
    "<h1 style='text-align: center;'>Car Damage Detection</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>"
    "YOLO11n trained on the car damage dataset for dent and scratch detection."
    "</p>",
    unsafe_allow_html=True
)

st.divider()


# Image Upload
uploaded_file = st.file_uploader(
    "Upload a car image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.markdown("---")


    # Detection Button
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        detect_button = st.button(
            "Detect Damage",
            use_container_width=True
        )


    if detect_button:

        with st.spinner("Detecting damage..."):

            results = model.predict(
                source=image,
                imgsz=640,
                conf=0.25,
                verbose=False
            )

        result = results[0]

        st.markdown("---")

        st.markdown(
            "<h2 style='text-align: center;'>Detection Results</h2>",
            unsafe_allow_html=True
        )

        annotated_image = result.plot()

        st.image(
            annotated_image,
            channels="BGR",
            use_container_width=True
        )

        boxes = result.boxes


        if boxes is not None and len(boxes) > 0:

            st.markdown("---")

            st.subheader("Detected Damage")

            for cls, conf in zip(
                boxes.cls.tolist(),
                boxes.conf.tolist()
            ):

                class_name = model.names[int(cls)]

                st.write(
                    f"**{class_name.upper()}** — "
                    f"Confidence: **{conf:.2f}**"
                )

        else:

            st.markdown("---")

            st.info("No damage detected.")
