
import biotite.structure.io as bsio
import esm
import sys
import torch
import string

# Following from: https://github.com/doricke/Software-Toolboxes/tree/master/OpenPython 
from InputFile import InputFile;
from FastaIterator import FastaIterator;
from FastaSequence import FastaSequence;

# **Authors:** Darrell O. Ricke, Ph.D. (Darrell.Ricke@ll.mit.edu)
# 
# **RAMS request ID 1022407**
# 
# **Overview:**
# This provides an iterator for a FASTA sequence library file to ESMFold.
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


###############################################################################
if ( __name__ == "__main__" ) and (len(sys.argv) >= 2):
  model = esm.pretrained.esmfold_v1()
  model = model.eval().cuda()

  test = FastaIterator()
  test.setFileName ( sys.argv[1] )
  test.openFile ()

  scores_file = OutputFile( sys.argv[1] + "_score.txt" )
  while ( test.isEndOfFile () == 0 ):
    fasta = test.nextSequence ()
    if ( fasta.sequence != "" ):
      sequence = fasta.getSequence()
      with torch.no_grad():
        output = model.infer_pdb( sequence )

      with open(fasta.getName() + ".pdb", "w") as f:
        f.write(output)
        print(fasta.getName() + ".pdb")

      struct = bsio.load_structure(fasta.getName() + ".pdb", extra_fields=["b_factor"])
      print("pLDDT: ", struct.b_factor.mean())
      score_txt = fasta.getName() + "\tpLDDT:\t" + str( struct.b_factor.mean() ) + "\n"
      scores_file.write( score_txt )

  test.closeFile ()
  scores_file.closeFile()

