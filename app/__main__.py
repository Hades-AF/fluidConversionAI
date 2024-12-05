from app.file_text_filtering import process_text_file
from app.openai_utility import openai_processing


def main():
    print("Welcome to the Fluid Conversion AI!")
    while True:
        try:
            file_name = input("Enter the file name to process (or 'exit' to quit): ").strip()
            if file_name.lower() == 'exit':
                print("Exiting the application. Goodbye!")
                break

            content = process_text_file(file_name)
            openai_processing(content)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()