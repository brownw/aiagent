import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_dir_abs, file_path))
        
        # Validate that the target file path stays within the allowed working directory
        valid_target_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
        if not valid_target_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Ensure the parent directory exists
        parent_dir = os.path.dirname(target_file_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        
        # Write content to the file
        with open(target_file_path, 'w') as file:
            file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"