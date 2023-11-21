import os

os.system("pip install -r requirements.txt")

api_key = str(input("Please, insert your API key: "))
with open("config.py", "w") as config_file:
    config_file.write(f"API_KEY ='{api_key}'")

print(f"\n\n\nFrom now on execute the app.py file unless you want to change API key...\n")
os.system("python app.py")