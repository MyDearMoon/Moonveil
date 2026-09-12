def main():
    correct_flag = "CTF{moonveil_is_cool}"

    print("Moonveil CTF Challenge")
    flag = input("Enter the flag: ").strip()

    if flag == correct_flag:
        print("Correct! You found the flag.")
    else:
        print("Incorrect flag.")

if __name__ == "__main__":
    main()