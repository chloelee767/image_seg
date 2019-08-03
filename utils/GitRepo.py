import os
import shutil
import subprocess
import shlex
from pathlib import Path

def run_command(args,**kwargs):
    cp = subprocess.run(args,stdout = subprocess.PIPE,stderr= subprocess.STDOUT,universal_newlines=True,**kwargs)
    print(cp.stdout,cp.stderr)

class GitRepo:
    def __init__(self,ssh_url,repo_folder,keyfile,username,email):
        self.ssh_url = ssh_url
        self.keyfile = str(keyfile)
        
        if repo_folder:
            self.repo_folder = str(repo_folder)
        else:
            self.repo_folder = os.getcwd() + '/' + self.repo_name
       
        print(self.ssh_url,':',self.repo_folder)
        
        Path('/root/.ssh/').mkdir(parents=True,exist_ok=True)
        Path('/root/.ssh/known_hosts').touch(exist_ok=True)
        
        run_command(['git','config','--global','user.name',username])
        run_command(['git','config','--global','user.email', email])
    
    def clone(self,branch=None,reset=False):
        if reset and Path(self.repo_folder).exists(): 
            shutil.rmtree(self.repo_folder)
        Path(self.repo_folder).mkdir(exist_ok=True,parents=True)
        
        if not branch:
            branch = self.branch
            
        ssh_url = self.ssh_url
        run_command(f'eval "$(ssh-agent -s)" && ssh-add "{self.keyfile}" && ssh-keyscan github.com >> /root/.ssh/known_hosts && git clone --single-branch -b "{branch}" "{ssh_url}" "{self.repo_folder}"',shell=True)
        self.branch = branch
        
    def checkout(self,branch):
        run_command(['git','checkout','-b',branch],cwd = self.repo_folder)
        
        self.branch = branch
    
    def commit_and_push(self,msg):
        run_command('git add .', shell=True, cwd=self.repo_folder)
        run_command(['git','commit','-m',msg],cwd=self.repo_folder)
        run_command(f'eval "$(ssh-agent -s)" && ssh-add "{self.keyfile}" && ssh-keyscan github.com >> /root/.ssh/known_hosts && git push origin "{self.branch}"',cwd=self.repo_folder,shell=True)
