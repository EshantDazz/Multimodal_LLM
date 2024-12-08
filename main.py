import streamlit as st
from PIL import Image
import asyncio
from utils import save_uploaded_file, delete_image, encode_image
from llama_vision import return_ai_response


async def main():
    # Set page title and configuration
    st.set_page_config(page_title="Image and Prompt Processor", layout="wide")

    # Add a title and description
    st.title("✨ Image and Prompt Processing App")
    st.write("Upload an image and enter a prompt as your input!")

    # Initialize session state variables
    if "current_image_path" not in st.session_state:
        st.session_state.current_image_path = None
    if "encoded_image" not in st.session_state:
        st.session_state.encoded_image = None

    # Create two columns for inputs
    col1, col2 = st.columns(2)

    # Image upload in the first column
    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            try:
                # Save the uploaded file and store its path
                if not st.session_state.current_image_path:
                    filepath: str = await save_uploaded_file(uploaded_file)
                    st.session_state.current_image_path = filepath
                    st.session_state.encoded_image = await encode_image(filepath)
                    print(f"Saved image to: {filepath}")
                    print(
                        f"Encoded image length: {len(st.session_state.encoded_image) if st.session_state.encoded_image else 'None'}"
                    )

                # Display the uploaded image
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_container_width=True)
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
                st.session_state.current_image_path = None
                st.session_state.encoded_image = None

    # Text prompt in the second column
    with col2:
        st.subheader("Enter Prompt")
        user_prompt = st.text_area(
            "Type your prompt here...",
            height=150,
            placeholder="Enter your prompt or instructions...",
        )

        # Add a process button
        process_button = st.button("Process", type="primary")

    # Process and display results
    if process_button:
        if not st.session_state.encoded_image:
            st.error("Please upload an image first!")
            return
        if not user_prompt:
            st.error("Please enter a prompt!")
            return

        try:
            st.divider()
            st.subheader("Processing Results")

            with st.spinner("Generating response with Llama Vision "):
                content = await return_ai_response(
                    st.session_state.encoded_image, user_prompt
                )

            # Create an expander for the results
            with st.expander("See detailed results", expanded=True):
                st.write("🖼️ Image Analysis:")

                # Display combined analysis
                st.success(f"""
                Llama Vision Response:
                {content}
                """)

                # Prepare result text
                result_text = f"""
                Llama Vision Demo
                ===============================
                Image Details:
                - File path: {st.session_state.current_image_path}

                User Prompt:
                {user_prompt}

                AI Response:
                {content}
                """

                st.download_button(
                    label="Download Analysis Report",
                    data=result_text,
                    file_name="analysis_report.txt",
                    mime="text/plain",
                )

                # Delete the image after processing
                if st.session_state.current_image_path:
                    await delete_image(st.session_state.current_image_path)
                    st.session_state.current_image_path = None
                    st.session_state.encoded_image = None

        except Exception as e:
            st.error(f"Error during processing: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
