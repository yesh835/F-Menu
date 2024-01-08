import subprocess

import time

def load_proxies():
    print("❗Loading proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n❗Proxies loaded successfully❗")
    print("\n=====================")
    time.sleep(0.5)
    print("❗Activating proxies❗")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\n🟢Proxies activated🟢")
    time.sleep(0.5)

with open('Tools/proxies.txt') as f:
    proxies = f.readlines()
    
load_proxies()




def execute_script(script_name):
    try:
        subprocess.call(["python", f"Tools/{script_name}.py"])
    except Exception as e:
        print(f"Error executing the script: {e}")

    input("\nPress any key to return to the menu...")
    display_menu()

def display_menu():
    options = [
        "TokenBruteforce",
        "FN IPsniffer",
        "UsernameScrape",
        "WebhookDestoryer",
        "Login Bruteforce",
        "DOSAttack",
        "Gmail BruteForce",
        "GcSpammer",
        "massreport",
        "TokenDecrypt",
        "ImageLogger",
        "Quit",
    ]

    # Add border around the menu
    border =  "=" * 90

    print(f"{asciibyme}\n{border}")
    print("💫  Choose your posion  💫".center(65))
    for idx, option in enumerate(options, 1):
        print(f"[{idx}] {option}".ljust(23), end="")

        if  idx %  4  == 0:  # After every 3 options, start a new line
            print()

    print(f"{border}\n")

    # Set prompt color to pink
    prompt = Colorate.Vertical(Colors.pink, "[input] > ")
    choice = input(prompt)

    try:
        script_name = options[int(choice) - 1]
        if script_name == "TokenBruteforce":
            execute_script("TokenBruteforce")
        elif script_name == "FN IPsniffer":
            execute_script("FN IPsniffer")
        elif script_name == "UsernameScrape":
            execute_script("UsernameScrape")
        elif script_name == "DOSAttack":
            execute_script("DOSAttack")
        elif script_name == "Gmail BruteForce":
            execute_script("Gmail BruteForce")
        elif script_name == "TokenDecrypt":
            execute_script("TokenDecrypt")
        elif script_name == "GcSpammer":
            execute_script("GcSpammer")
        elif script_name == "massreport":
            execute_script("massreport")
        elif script_name == "Login Bruteforce":
            execute_script("Login Bruteforce")
        elif script_name == "ImageLogger":
            execute_script("ImageLogger")
        # Add the rest of the scripts here with their respective filenames
        elif script_name == "Quit":
            print("Exiting the menu...")
        else:
            print("Invalid choice. Please select a valid option.")
            display_menu()
    except Exception as e:
        print("Invalid choice. Please select a valid option.")
        display_menu()

if __name__ == "__main__":
    display_menu()
