import subprocess
import os
import pwd
import sys

def run_as_user(command, username):
    pw_record = pwd.getpwnam(username)
    user_uid = pw_record.pw_uid
    user_gid = pw_record.pw_gid

    env = os.environ.copy()
    env['HOME'] = pw_record.pw_dir
    env['LOGNAME'] = username
    env['PWD'] = os.getcwd()
    env['USER'] = username

    process = subprocess.Popen(command, preexec_fn=demote(user_uid, user_gid), env=env, start_new_session=True)
    return process

def demote(user_uid, user_gid):
    def result():
        os.setgid(user_gid)
        os.setuid(user_uid)
    return result

def main():
    if len(sys.argv) < 4:
        print("Usage: starterscript.py username venv-python-path python-script [arg1 arg2 ...]")
        sys.exit(1)

    username = sys.argv[1]
    venv_python_path = sys.argv[2]
    python_script = sys.argv[3]
    script_args = sys.argv[4:]

    command_to_run = [venv_python_path, python_script] + script_args
    run_as_user(command_to_run, username)

if __name__ == '__main__':
    main()
