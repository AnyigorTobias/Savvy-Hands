

def detect_file_type(file_path):
    """This function detects the type of file

    Args:
        file_path (_type_): this argument shoulf be a file path

    Returns:
        _type_: this is a string 
    """
    if (file_path.startswith('https://www.youtube')):
        
        file_type = 'youtube'

    elif (file_path.startswith('https://')):
        file_type = "web_doc"
    
    else:
        file_type = 'unknown'
        
    return file_type



print(detect_file_type('https://www.youtube.com/watch?v=ae-CV2KfoN0&t=2s'))