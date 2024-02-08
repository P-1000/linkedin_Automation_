import linkedin_json_data
import text_content_generator
import linkedin_prompts
import text_getter
import image_gen
import time
def main():

    file_path = "linkedin_topic.txt"  # Replace with the actual file path
    current_line = 0
    while True:
        next_line, current_line = text_getter.get_next_line_from_file(file_path, current_line)

        if next_line is not None:
            selected_text = next_line
            print(selected_text)
            print("")
            prompt =  linkedin_prompts.prompt.format(role_and_target_audience = selected_text)
            text_content = text_content_generator.openai_generate(prompt)
            print("generartd text content")
            print(" ")
            image_content = image_gen.create_image(selected_text)
            print("generated image content")
            print(" ")
            # linkedin_json_data.create_text_post(text_content)
            linkedin_json_data.register_upload_and_share_image(text_content, selected_text, image_content)
            # linkedin_json_data.register_upload_and_share_image(text_content, selected_text, "/Users/admin/Downloads/Linkedin Automation - 1/linkedin_image.jpg")
            time.sleep(31600)
        else:
            print("All Linkedin posts have been Published.")
            break
if __name__ == "__main__":
    main()