import pymupdf


# =========================================================
# EXTRACT TEXT FROM PDF
# =========================================================

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF resume.

    Parameters
    ----------
    pdf_file : Streamlit UploadedFile
        Uploaded PDF file.

    Returns
    -------
    str
        Extracted text from all pages.

    Raises
    ------
    ValueError
        If no readable text is found.

    RuntimeError
        If the PDF cannot be opened or processed.
    """

    # =====================================================
    # 1. VALIDATE FILE
    # =====================================================

    if pdf_file is None:

        raise ValueError(
            "Please upload a resume PDF."
        )

    try:

        # =================================================
        # 2. READ PDF BYTES
        # =================================================

        pdf_bytes = pdf_file.read()

        if not pdf_bytes:

            raise ValueError(
                "The uploaded PDF is empty."
            )

        # =================================================
        # 3. OPEN PDF
        # =================================================

        pdf_document = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        if pdf_document.page_count == 0:

            pdf_document.close()

            raise ValueError(
                "The PDF does not contain any pages."
            )

        # =================================================
        # 4. EXTRACT TEXT FROM EVERY PAGE
        # =================================================

        pages = []

        for page_number, page in enumerate(
            pdf_document
        ):

            try:

                page_text = page.get_text(
                    "text"
                )

                if page_text and page_text.strip():

                    pages.append(
                        page_text.strip()
                    )

            except Exception:
                # Skip a problematic page rather than
                # stopping the entire resume analysis.
                continue

        # =================================================
        # 5. CLOSE PDF
        # =================================================

        pdf_document.close()

        # =================================================
        # 6. COMBINE ALL PAGES
        # =================================================

        final_text = "\n\n".join(
            pages
        ).strip()

        # =================================================
        # 7. CHECK FOR READABLE TEXT
        # =================================================

        if not final_text:

            raise ValueError(
                "No readable text was found in this PDF. "
                "The resume may be scanned or image-based."
            )

        return final_text

    except ValueError:
        raise

    except Exception as error:

        raise RuntimeError(
            f"Unable to read the PDF: {error}"
        )