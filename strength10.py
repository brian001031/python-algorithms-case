
import argparse
import matplotlib as mp
mp.use('Agg')

import matplotlib.pyplot as plt
import numpy
import scipy
import pyparsing



#parse command-line argument
parse = argparse.ArgumentParser(usage=__doc__)
parse.add_argument("--order",type=int,default =3 ,help="Bessel fuction")
parse.add_argument("--output",default ="strength.png" ,help="output image file ")
args = parse.parse_args()


plt.plot([0,12,75])
plt.ylabel('some number yLabel')


plt.savefig(args.output,dpi=97)
plt.show()

print('strength Test')







