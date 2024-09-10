import sys
import subprocess

def print_help():
    print("Usage:")
    print("  kog h                     Show this help message")
    print("  kog all                   Run 'git add .'")
    print("  kog commit \"message\"    Run 'git commit -m \"message\"'")
    print("  kog commit -a             Run 'git commit --amend'")
    print("  kog sw fix                Run 'git checkout fix'")
    print("  kog sw -b fix             Run 'git checkout -b fix'")
    print("  kog push [branch]         Run 'git push -u origin [branch]' or 'git push -u origin current-branch'")

def execute_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_current_branch():
    try:
        result = subprocess.run('git rev-parse --abbrev-ref HEAD', check=True, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == 'h':
        print_help()
    elif command == 'all':
        execute_command('git add .')
    elif command == 'commit':
        if len(sys.argv) < 3:
            print("Error: No commit message provided.")
            print_help()
            sys.exit(1)
        message = sys.argv[2]
        if message == '-a':
            execute_command('git commit --amend')
        else:
            execute_command(f'git commit -m "{message}"')
    elif command == 'sw':
        if len(sys.argv) < 3:
            print("Error: No switch argument provided.")
            print_help()
            sys.exit(1)
        switch_arg = sys.argv[2]
        if switch_arg == '-b':
            if len(sys.argv) < 4:
                print("Error: No branch name provided.")
                print_help()
                sys.exit(1)
            branch_name = sys.argv[3]
            execute_command(f'git checkout -b {branch_name}')
        else:
            execute_command(f'git checkout {switch_arg}')
    elif command == 'push':
        if len(sys.argv) < 3:
            # No branch name provided, push the current branch
            branch_name = get_current_branch()
        else:
            branch_name = sys.argv[2]
        execute_command(f'git push -u origin {branch_name}')
    else:
        print(f"Unknown command: {command}")
        print_help()

if __name__ == '__main__':
    main()

# @REM D:\comd\