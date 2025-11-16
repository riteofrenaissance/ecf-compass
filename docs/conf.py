git clone --depth 1 https://github.com/riteofrenaissance/ecf-compass.git . 
git fetch origin --force --prune --prune-tags --depth 50 refs/heads/main:refs/remotes/origin/main 
git checkout --force origin/main 
cat readthedocs.yaml 
asdf global python 3.13.3 
python -mvirtualenv $READTHEDOCS_VIRTUALENV_PATH 
python -m pip install --upgrade --no-cache-dir pip setuptools 
python -m pip install --upgrade --no-cache-dir sphinx 