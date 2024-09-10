import sys

def print_help():
    print("Usage:")
    print("  Ko h          Show this help message")
    print("  Ko [command]  Execute a command")

def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == 'h':
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()

if __name__ == '__main__':
    main()
