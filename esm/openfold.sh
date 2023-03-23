#!/bin/bash 

# **Authors:** Darrell O. Ricke, Ph.D. (Darrell.Ricke@ll.mit.edu)
#              Adam Michaleas          (Adam.Micheas@ll.mit.edu)
# 
# **RAMS request ID 1022407**
# 
# **Overview:**
# This is a Singularity container of Evolutionary Scale Modeling (ESM) / ESMFold tool - https://github.com/facebookresearch/esm
# 
# **Citation:** None
# 
# **Disclaimer:**
# DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
# 
# This material is based upon work supported by the Department of the Air Force under 
# Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or 
# recommendations expressed in this material are those of the author(s) and do not 
# necessarily reflect the views of the Department of the Air Force.
# 
# © 2023 Massachusetts Institute of Technology.
# 
# Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)
# 
# The software/firmware is provided to you on an As-Is basis
# 
# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS 
# Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, 
# U.S. Government rights in this work are defined by DFARS 252.227-7013 or 
# DFARS 252.227-7014 as detailed above. Use of this work other than as specifically 
# authorized by the U.S. Government may violate any copyrights that exist in this work.
#
# **License:**
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# ESMFold machine learning Singularity recipe

  export FORCE_CUDA="1"
  export CUDA_VISIBLE_DEVICES=0
  export CUDA_HOME=/usr/local/cuda

  cd /S/
  git clone https://github.com/aqlaboratory/openfold.git
  cd openfold
  export PATH="/usr/local/anaconda3/bin/:$PATH"
  conda env create --file environment.yml
  bash scripts/install_third_party_dependencies.sh
  bash scripts/activate_conda_env.sh
  python3 setup.py install
  bash scripts/install_hh_suite.sh

  chmod 777 *.py

