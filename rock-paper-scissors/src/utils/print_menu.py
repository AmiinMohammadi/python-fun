from typing import List 
def print_menu(action_list:List[str]):
    print("\n————————————————————————")
    print("ACTIONS:")
    for action in action_list:
        print(f"-> {action}")
    print("————————————————————————")


if __name__ == "__main__":
    print_menu()
