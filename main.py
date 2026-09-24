from dotenv import load_dotenv
import os
load_dotenv()

def main():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    print(f"ENV Variables: {GROQ_API_KEY}")


if __name__ == "__main__":
    main()
