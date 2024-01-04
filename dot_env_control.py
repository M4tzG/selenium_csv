from dotenv import dotenv_values

def read_env_file(filepath):
    env_values = dotenv_values(filepath)
    env_dict = dict(env_values)
    return env_dict
    
DOT_ENV_PATH = '.env'
ENV = read_env_file(DOT_ENV_PATH)
