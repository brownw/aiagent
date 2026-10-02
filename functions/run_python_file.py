import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))
        
        # Validate that the target directory stays within the allowed working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        root, ext = os.path.splitext(file_path_abs)
        if ext != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]
        if args:
            command.extend(args)

        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            timeout=30
        )

        #print(f"Executed command: {result}")
        output = ""
        if result.returncode != 0:
            output += f'Process exited with return code {result.returncode}'
        if not result.stdout and not result.stderr:
            output += 'No output produced'
        else:
            if result.stdout:
                output += f'STDOUT:\n{result.stdout}'
            if result.stderr:
                output += f'STDERR:\n{result.stderr}'
        return output.strip() if output else "No output produced"

    except Exception as e:
        return f"Error: executing Python file: {e}"