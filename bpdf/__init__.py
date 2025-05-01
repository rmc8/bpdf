import os
from logging import getLogger

from fpdf import FPDF

logger = getLogger(__name__)


class Client:
    def __init__(self, font_path, config):
        self.font_path = font_path
        self.font_name_for_fpdf = "LoraItalic"
        self.config = config

    def run(self, text: str):
        """
        Create a PDF containing the specified text.

        Args:
            text (str): Text to include in the PDF.
        """
        pdf = FPDF()
        pdf.add_page()

        # 1. Register the font with add_font()
        if not os.path.exists(self.font_path):
            logger.error(f"Font file '{self.font_path}' not found.")
            logger.error("Please place the font file at the specified path.")
            logger.info("Using default Arial font instead.")
            font_added_successfully = False
        else:
            try:
                pdf.add_font(self.font_name_for_fpdf, "", str(self.font_path))
                font_added_successfully = True
            except Exception as e:
                logger.error(f"Failed to load font '{self.font_path}': {e}")
                logger.error(
                    "Please ensure the font file is a valid TrueType/OpenType font."
                )
                logger.info("Using default Arial font instead.")
                font_added_successfully = False

        # 2. Use the registered font name with set_font()
        FONT_SIZE = self.config.get("font_size", 16)
        line_height = FONT_SIZE * self.config.get("line_height", 1.2)
        if font_added_successfully:
            pdf.set_font(self.font_name_for_fpdf, "", FONT_SIZE)
        else:
            pdf.set_font("Arial", size=FONT_SIZE)

        # 3. Add text with multi_cell()
        try:
            pdf.multi_cell(0, line_height, text)
        except Exception as e:
            logger.error(f"Error occurred while adding text: {e}")
            logger.error("This might be a text encoding issue.")
        # 4. Add a blank page
        pdf.add_page()
        # 5. Save the PDF to a file with output()
        os.makedirs("output", exist_ok=True)
        output_filename = "output/output.pdf"  # Define output filename
        pdf.output(output_filename)
        logger.info(f"PDF successfully created: {output_filename}")
