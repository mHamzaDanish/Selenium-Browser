from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome          import ChromeDriverManager
from selenium.common.exceptions        import *
import os, ast

##============= Read Config File =====================#
f                                = open(r"config.txt",'r')
Config                           = f.read()
Config_v                         = ast.literal_eval(Config)
chrome_exe_path                  = Config_v['chrome_exe_path']
f.close()
##====================== End =============================#

warnings.filterwarnings('ignore')
root_current_dir_path      = os.getcwd()

try:
    driver.quit()
except:
    try:driver.close()
    except:pass
    
##============= Function =====================#
def openBrowser(chrome_profile_path):
    try:
        run_chrome = f'chrome.exe --remote-debugging-port=8989 --user-data-dir="{chrome_profile_path}"'
        os.system(f"start cmd.exe @cmd /k {run_chrome} && exit || exit ")
        return True
    except Exceception as e:
        return False
    
    
def create_folder(path,name):
    path = os.path.join(path,name)
    try:
        os.mkdir(path)
    except:
        pass
    return path

def clear_terminal():
    try:
        os.system('cls')
    except:
        pass
    

chrome_path = fr'{root_current_dir_path}\chrome_profile'
current_dir_path                 = os.getcwd()
chrome_profile_path              = create_folder(current_dir_path,'chrome_profile')
os.chdir(chrome_exe_path) 
status                           = openBrowser(chrome_profile_path)

opt                             = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver                          = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
