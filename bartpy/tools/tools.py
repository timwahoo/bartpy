from ..utils import cfl
import os
import subprocess
import tempfile as tmp

BART_PATH=os.environ['TOOLBOX_PATH'] + '/bart'
DEBUG=False
NAME=tmp.NamedTemporaryFile().name

def set_debug(status):
    global DEBUG
    DEBUG=status


def avg(input, bitmask, w=None):
    """
    Calculates (weighted) average along dimensions specified by bitmask.

    :param bitmask int:
    :param input array:
    :param w bool: weighted average

    """
    usage_string = "vg [-w] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'avg '
    flag_str = ''

    opt_args = f''

    multituples = []

    if w is not None:
        flag_str += f'-w '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def bench(T=None, S=None, s=None):
    """
    Performs a series of micro-benchmarks.

    :param T bool: varying number of threads
    :param S bool: varying problem size
    :param s long: select benchmarks

    """
    usage_string = "bench [-T] [-S] [-s d] [output]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'bench '
    flag_str = ''

    opt_args = f''

    multituples = []

    if T is not None:
        flag_str += f'-T '

    if S is not None:
        flag_str += f'-S '

    if s is not None:
        flag_str += f'-s {s} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def bin(label, src, l=None, o=None, R=None, C=None, r=None, c=None, a=None, A=None, O=None, x=None, M=None):
    """
    Binning

    :param label array:
    :param src array:
    :param l int: Bin according to labels: Specify cluster dimension
    :param o bool: Reorder according to labels
    :param R int: Quadrature Binning: Number of respiratory labels
    :param C int: Quadrature Binning: Number of cardiac labels
    :param r VEC2: (Respiration: Eigenvector index)
    :param c VEC2: (Cardiac motion: Eigenvector index)
    :param a int: Quadrature Binning: Moving average
    :param A int: (Quadrature Binning: Cardiac moving average window)
    :param O FLOAT_VEC2: Quadrature Binning: Angle offset for resp and card.
    :param x STRING: (Output filtered cardiac EOFs)
    :param M bool: Amplitude binning

    """
    usage_string = "bin [-l d] [-o] [-R d] [-C d] [-a d] [-O f:f] [-M] label src dst"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'bin '
    flag_str = ''

    opt_args = f''

    multituples = []

    if l is not None:
        flag_str += f'-l {l} '

    if o is not None:
        flag_str += f'-o '

    if R is not None:
        flag_str += f'-R {R} '

    if C is not None:
        flag_str += f'-C {C} '

    if r is not None:
        flag_str += f'-r {r} '

    if c is not None:
        flag_str += f'-c {c} '

    if a is not None:
        flag_str += f'-a {a} '

    if A is not None:
        flag_str += f'-A {A} '

    if O is not None:
        flag_str += f'-O {O} '

    if x is not None:
        flag_str += f'-x {x} '

    if M is not None:
        flag_str += f'-M '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}label {NAME}src {NAME}dst  "
    cfl.writecfl(NAME + 'label', label)
    cfl.writecfl(NAME + 'src', src)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'dst')
    return outputs

def bitmask(dim=None, b=None):
    """
    Convert between a bitmask and set of dimensions.

    :param dim tuple: None
    :param b bool: dimensions from bitmask use with exactly one argument

    """
    usage_string = "bitmask [-b] [dim1 ... dimN ]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'bitmask '
    flag_str = ''

    opt_args = f''

    multituples = []

    if dim != None:
        opt_args += f"{' '.join([str(arg) for arg in dim])} "

    if b is not None:
        flag_str += f'-b '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()}  "

    val = subprocess.Popen(cmd_str.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

    return [int(d) for d in val.split()] if len(val.split()) > 1 else int(val)

def cabs(input):
    """
    Absolute value of array (|<input>|).

    :param input array:

    """
    usage_string = "cabs input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'cabs '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def caldir(input, cal_size):
    """
    Estimates coil sensitivities from the k-space center using
a direct method (McKenzie et al.). The size of the fully-sampled
calibration region is automatically determined but limited by
{cal_size} (e.g. in the readout direction).

    :param cal_size int:
    :param input array:

    """
    usage_string = "caldir cal_size input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'caldir '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {cal_size} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def calmat(kspace, k=None, K=None, r=None, R=None, C=None):
    """
    Compute calibration matrix.

    :param kspace array:
    :param k list: kernel size
    :param K list: ()
    :param r list: Limits the size of the calibration region.
    :param R list: ()
    :param C bool: ()

    """
    usage_string = "calmat [-k d:d:d] [-r d:d:d] kspace calibration_matrix"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'calmat '
    flag_str = ''

    opt_args = f''

    multituples = []

    if k is not None:
        flag_str += f'-k {":".join([str(x) for x in k])} '

    if K is not None:
        flag_str += f'-K {":".join([str(x) for x in K])} '

    if r is not None:
        flag_str += f'-r {":".join([str(x) for x in r])} '

    if R is not None:
        flag_str += f'-R {":".join([str(x) for x in R])} '

    if C is not None:
        flag_str += f'-C '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}calibration_matrix  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'calibration_matrix')
    return outputs

def carg(input):
    """
    Argument (phase angle).

    :param input array:

    """
    usage_string = "carg input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'carg '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def casorati(input, dim, kern):
    """
    Casorati matrix with kernel (kern1, ..., kernN) along dimensions (dim1, ..., dimN).

    :param dim multituple:
    :param kern multituple:
    :param input array:

    """
    usage_string = "casorati dim1 kern1 ... dimN kernN input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'casorati '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    multituples.append(dim)
    
    multituples.append(kern)
    
    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def cc(kspace, p=None, M=None, r=None, R=None, A=None, S=None, G=None, E=None):
    """
    Performs coil compression.

    :param kspace array:
    :param p long: perform compression to N virtual channels
    :param M bool: output compression matrix
    :param r list: size of calibration region
    :param R list: (size of calibration region)
    :param A bool: use all data to compute coefficients
    :param S bool: type: SVD
    :param G bool: type: Geometric
    :param E bool: type: ESPIRiT

    """
    usage_string = "cc [-p d] [-M] [-r d:d:d] [-A] [-S] [-G] [-E] kspace coeff|proj_kspace"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'cc '
    flag_str = ''

    opt_args = f''

    multituples = []

    if p is not None:
        flag_str += f'-p {p} '

    if M is not None:
        flag_str += f'-M '

    if r is not None:
        flag_str += f'-r {":".join([str(x) for x in r])} '

    if R is not None:
        flag_str += f'-R {":".join([str(x) for x in R])} '

    if A is not None:
        flag_str += f'-A '

    if S is not None:
        flag_str += f'-S '

    if G is not None:
        flag_str += f'-G '

    if E is not None:
        flag_str += f'-E '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}coeff_proj_kspace  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'coeff_proj_kspace')
    return outputs

def ccapply(kspace, cc_matrix, p=None, u=None, t=None, S=None, G=None, E=None):
    """
    Apply coil compression forward/inverse operation.

    :param kspace array:
    :param cc_matrix array:
    :param p long: perform compression to N virtual channels
    :param u bool: apply inverse operation
    :param t bool: don't apply FFT in readout
    :param S bool: type: SVD
    :param G bool: type: Geometric
    :param E bool: type: ESPIRiT

    """
    usage_string = "ccapply [-p d] [-u] [-t] [-S] [-G] [-E] kspace cc_matrix proj_kspace"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ccapply '
    flag_str = ''

    opt_args = f''

    multituples = []

    if p is not None:
        flag_str += f'-p {p} '

    if u is not None:
        flag_str += f'-u '

    if t is not None:
        flag_str += f'-t '

    if S is not None:
        flag_str += f'-S '

    if G is not None:
        flag_str += f'-G '

    if E is not None:
        flag_str += f'-E '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}cc_matrix {NAME}proj_kspace  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'cc_matrix', cc_matrix)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'proj_kspace')
    return outputs

def cdf97(input, bitmask, i=None):
    """
    Perform a wavelet (cdf97) transform.

    :param bitmask int:
    :param input array:
    :param i bool: inverse

    """
    usage_string = "cdf97 [-i] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'cdf97 '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def circshift(input, dim, shift):
    """
    Perform circular shift along {dim} by {shift} elements.

    :param dim int:
    :param shift int:
    :param input array:

    """
    usage_string = "circshift dim shift input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'circshift '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dim} {shift} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def conj(input):
    """
    Compute complex conjugate.

    :param input array:

    """
    usage_string = "conj input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'conj '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def conv(input, kernel, bitmask):
    """
    Performs a convolution along selected dimensions.

    :param bitmask int:
    :param input array:
    :param kernel array:

    """
    usage_string = "conv bitmask input kernel output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'conv '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}kernel {NAME}output  "
    cfl.writecfl(NAME + 'input', input)
    cfl.writecfl(NAME + 'kernel', kernel)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def conway(input, P=None, n=None):
    """
    Conway's game of life.

    :param input array:
    :param P bool: periodic boundary conditions
    :param n int: nr. of iterations

    """
    usage_string = "conway [-P] [-n d] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'conway '
    flag_str = ''

    opt_args = f''

    multituples = []

    if P is not None:
        flag_str += f'-P '

    if n is not None:
        flag_str += f'-n {n} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def copy(input, output, dim=None, pos=None):
    """
    Copy an array (to a given position in the output file - which then must exist).

    :param input array:
    :param output INOUTFILE:
    :param dim multituple: None
    :param pos multituple: None

    """
    usage_string = "copy [dim1 pos1 ... dimN posN ] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'copy '
    flag_str = ''

    opt_args = f''

    multituples = []

    if dim != None:
        multituples.append(dim) 

    if pos != None:
        multituples.append(pos) 
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {output}  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def cpyphs(input):
    """
    Copy phase from <input> to <output>.

    :param input array:

    """
    usage_string = "cpyphs input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'cpyphs '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def creal(input):
    """
    Real value.

    :param input array:

    """
    usage_string = "creal input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'creal '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def crop(input, dimension, size):
    """
    Extracts a sub-array corresponding to the central part of {size} along {dimension}

    :param dimension int:
    :param size int:
    :param input array:

    """
    usage_string = "crop dimension size input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'crop '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dimension} {size} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def delta(dims, flags, size):
    """
    Kronecker delta.

    :param dims int:
    :param flags int:
    :param size long:

    """
    usage_string = "delta dims flags size out"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'delta '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dims} {flags} {size} {NAME}out  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'out')
    return outputs

def ecalib(kspace, t=None, c=None, k=None, K=None, r=None, R=None, m=None, S=None, W=None, I=None, _1=None, P=None, O=None, orthiter=None, b=None, V=None, C=None, g=None, p=None, n=None, v=None, a=None, d=None):
    """
    Estimate coil sensitivities using ESPIRiT calibration.
Optionally outputs the eigenvalue maps.

    :param kspace array:
    :param t float: This determined the size of the null-space.
    :param c float: Crop the sensitivities if the eigenvalue is smaller than crop_value.
    :param k list: kernel size
    :param K list: ()
    :param r list: Limits the size of the calibration region.
    :param R list: ()
    :param m int: Number of maps to compute.
    :param S bool: create maps with smooth transitions (Soft-SENSE).
    :param W bool: soft-weighting of the singular vectors.
    :param I bool: intensity correction
    :param _1 bool: perform only first part of the calibration
    :param P bool: Do not rotate the phase with respect to the first principal component
    :param O bool: ()
    :param orthiter int: ()
    :param b float: ()
    :param V bool: ()
    :param C bool: ()
    :param g bool: ()
    :param p float: ()
    :param n int: ()
    :param v float: Variance of noise in data.
    :param a bool: Automatically pick thresholds.
    :param d int: Debug level

    """
    usage_string = "calib [-t f] [-c f] [-k d:d:d] [-r d:d:d] [-m d] [-S] [-W] [-I] [-1] [-P] [-v f] [-a] [-d d] kspace sensitivities [ev-maps]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ecalib '
    flag_str = ''

    opt_args = f''

    multituples = []

    if t is not None:
        flag_str += f'-t {t} '

    if c is not None:
        flag_str += f'-c {c} '

    if k is not None:
        flag_str += f'-k {":".join([str(x) for x in k])} '

    if K is not None:
        flag_str += f'-K {":".join([str(x) for x in K])} '

    if r is not None:
        flag_str += f'-r {":".join([str(x) for x in r])} '

    if R is not None:
        flag_str += f'-R {":".join([str(x) for x in R])} '

    if m is not None:
        flag_str += f'-m {m} '

    if S is not None:
        flag_str += f'-S '

    if W is not None:
        flag_str += f'-W '

    if I is not None:
        flag_str += f'-I '

    if _1 is not None:
        flag_str += f'-1 '

    if P is not None:
        flag_str += f'-P '

    if O is not None:
        flag_str += f'-O '

    if orthiter is not None:
        flag_str += f'--orthiter {orthiter} '

    if b is not None:
        flag_str += f'-b {b} '

    if V is not None:
        flag_str += f'-V '

    if C is not None:
        flag_str += f'-C '

    if g is not None:
        flag_str += f'-g '

    if p is not None:
        flag_str += f'-p {p} '

    if n is not None:
        flag_str += f'-n {n} '

    if v is not None:
        flag_str += f'-v {v} '

    if a is not None:
        flag_str += f'-a '

    if d is not None:
        flag_str += f'-d {d} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}sensitivities {NAME}ev_maps  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'sensitivities'), cfl.readcfl(NAME + 'ev_maps')
    return outputs

def ecaltwo(input, x, y, z, c=None, m=None, S=None, O=None, g=None):
    """
    Second part of ESPIRiT calibration.
Optionally outputs the eigenvalue maps.

    :param x long:
    :param y long:
    :param z long:
    :param input array:
    :param c float: Crop the sensitivities if the eigenvalue is smaller than crop_value.
    :param m long: Number of maps to compute.
    :param S bool: Create maps with smooth transitions (Soft-SENSE).
    :param O bool: ()
    :param g bool: ()

    """
    usage_string = "caltwo [-c f] [-m d] [-S] x y z input sensitivities [ev-maps]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ecaltwo '
    flag_str = ''

    opt_args = f''

    multituples = []

    if c is not None:
        flag_str += f'-c {c} '

    if m is not None:
        flag_str += f'-m {m} '

    if S is not None:
        flag_str += f'-S '

    if O is not None:
        flag_str += f'-O '

    if g is not None:
        flag_str += f'-g '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {x} {y} {z} {NAME}input {NAME}sensitivities {NAME}ev_maps  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'sensitivities'), cfl.readcfl(NAME + 'ev_maps')
    return outputs

def epg(C=None, M=None, H=None, F=None, S=None, B=None, _1=None, _2=None, b=None, o=None, r=None, e=None, f=None, s=None, n=None, u=None, v=None):
    """
    Simulate MR pulse sequence based on Extended Phase Graphs (EPG)

    :param C bool: CPMG
    :param M bool: fmSSFP
    :param H bool: Hyperecho
    :param F bool: FLASH
    :param S bool: Spinecho
    :param B bool: bSSFP
    :param _1 float: T1 [units of time]
    :param _2 float: T2 [units of time]
    :param b float: relative B1 [unitless]
    :param o float: off-resonance [units of inverse time]
    :param r float: repetition time [units of time]
    :param e float: echo time [units of time]
    :param f float: flip angle [degrees]
    :param s long: spoiling (0: ideal 1: conventional RF 2: random RF)
    :param n long: number of pulses
    :param u long: unknowns as bitmask (0: T1 1: T2 2: B1 3: off-res)
    :param v long: verbosity level

    """
    usage_string = "pg [-C] [-M] [-H] [-F] [-S] [-B] [-1 f] [-2 f] [-b f] [-o f] [-r f] [-e f] [-f f] [-s d] [-n d] [-u d] [-v d] signal intensity [configuration states] [(rel.) signal derivatives] [configuration derivatives]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'epg '
    flag_str = ''

    opt_args = f''

    multituples = []

    if C is not None:
        flag_str += f'-C '

    if M is not None:
        flag_str += f'-M '

    if H is not None:
        flag_str += f'-H '

    if F is not None:
        flag_str += f'-F '

    if S is not None:
        flag_str += f'-S '

    if B is not None:
        flag_str += f'-B '

    if _1 is not None:
        flag_str += f'-1 {_1} '

    if _2 is not None:
        flag_str += f'-2 {_2} '

    if b is not None:
        flag_str += f'-b {b} '

    if o is not None:
        flag_str += f'-o {o} '

    if r is not None:
        flag_str += f'-r {r} '

    if e is not None:
        flag_str += f'-e {e} '

    if f is not None:
        flag_str += f'-f {f} '

    if s is not None:
        flag_str += f'-s {s} '

    if n is not None:
        flag_str += f'-n {n} '

    if u is not None:
        flag_str += f'-u {u} '

    if v is not None:
        flag_str += f'-v {v} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}signal_intensity {NAME}configuration_states {NAME}_rel___signal_derivatives {NAME}configuration_derivatives  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'signal_intensity'), cfl.readcfl(NAME + 'configuration_states'), cfl.readcfl(NAME + '_rel___signal_derivatives'), cfl.readcfl(NAME + 'configuration_derivatives')
    return outputs

def estdelay(trajectory, data, R=None, p=None, n=None, r=None):
    """
    Estimate gradient delays from radial data.

    :param trajectory array:
    :param data array:
    :param R bool: RING method
    :param p int: [RING] Padding
    :param n int: [RING] Number of intersecting spokes
    :param r float: [RING] Central region size

    """
    usage_string = "tdelay [-R] [-p d] [-n d] [-r f] trajectory data [qf]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'estdelay '
    flag_str = ''

    opt_args = f''

    multituples = []

    if R is not None:
        flag_str += f'-R '

    if p is not None:
        flag_str += f'-p {p} '

    if n is not None:
        flag_str += f'-n {n} '

    if r is not None:
        flag_str += f'-r {r} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}trajectory {NAME}data {NAME}qf  "
    cfl.writecfl(NAME + 'trajectory', trajectory)
    cfl.writecfl(NAME + 'data', data)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'qf')
    return outputs

def estdims(traj):
    """
    Estimate image dimension from non-Cartesian trajectory.
Assume trajectory scaled to -DIM/2 to DIM/2 (ie dk=1/FOV=1)

    :param traj array:

    """
    usage_string = "tdims traj"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'estdims '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}traj  "
    cfl.writecfl(NAME + 'traj', traj)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def estshift(arg1, arg2, flags):
    """
    Estimate sub-pixel shift.

    :param flags int:
    :param arg1 array:
    :param arg2 array:

    """
    usage_string = "tshift flags arg1 arg2"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'estshift '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {flags} {NAME}arg1 {NAME}arg2  "
    cfl.writecfl(NAME + 'arg1', arg1)
    cfl.writecfl(NAME + 'arg2', arg2)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def estvar(kspace, k=None, K=None, r=None, R=None):
    """
    Estimate the noise variance assuming white Gaussian noise.

    :param kspace array:
    :param k list: kernel size
    :param K list: ()
    :param r list: Limits the size of the calibration region.
    :param R list: ()

    """
    usage_string = "tvar [-k d:d:d] [-r d:d:d] kspace"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'estvar '
    flag_str = ''

    opt_args = f''

    multituples = []

    if k is not None:
        flag_str += f'-k {":".join([str(x) for x in k])} '

    if K is not None:
        flag_str += f'-K {":".join([str(x) for x in K])} '

    if r is not None:
        flag_str += f'-r {":".join([str(x) for x in r])} '

    if R is not None:
        flag_str += f'-R {":".join([str(x) for x in R])} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def extract(input, dim, start, end):
    """
    Extracts a sub-array along dims from index start to (not including) end.

    :param dim multituple:
    :param start multituple:
    :param end multituple:
    :param input array:

    """
    usage_string = "xtract dim1 start1 end1 ... dimN startN endN input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'extract '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    multituples.append(dim)
    
    multituples.append(start)
    
    multituples.append(end)
    
    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fakeksp(image, kspace, sens, r=None):
    """
    Recreate k-space from image and sensitivities.

    :param image array:
    :param kspace array:
    :param sens array:
    :param r bool: replace measured samples with original values

    """
    usage_string = "fakeksp [-r] image kspace sens output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fakeksp '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}image {NAME}kspace {NAME}sens {NAME}output  "
    cfl.writecfl(NAME + 'image', image)
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'sens', sens)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fft(input, bitmask, u=None, i=None, n=None):
    """
    Performs a fast Fourier transform (FFT) along selected dimensions.

    :param bitmask long:
    :param input array:
    :param u bool: unitary
    :param i bool: inverse
    :param n bool: un-centered

    """
    usage_string = "fft [-u] [-i] [-n] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fft '
    flag_str = ''

    opt_args = f''

    multituples = []

    if u is not None:
        flag_str += f'-u '

    if i is not None:
        flag_str += f'-i '

    if n is not None:
        flag_str += f'-n '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fftmod(input, bitmask, b=None, i=None):
    """
    Apply 1 -1 modulation along dimensions selected by the {bitmask}.

    :param bitmask long:
    :param input array:
    :param b bool: (deprecated)
    :param i bool: inverse

    """
    usage_string = "fftmod [-i] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fftmod '
    flag_str = ''

    opt_args = f''

    multituples = []

    if b is not None:
        flag_str += f'-b '

    if i is not None:
        flag_str += f'-i '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fftrot(input, dim1, dim2, theta):
    """
    Performs a rotation using Fourier transform (FFT) along selected dimensions.

    :param dim1 int:
    :param dim2 int:
    :param theta float:
    :param input array:

    """
    usage_string = "fftrot dim1 dim2 theta input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fftrot '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dim1} {dim2} {theta} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fftshift(input, bitmask, b=None):
    """
    Apply fftshift along dimensions selected by the {bitmask}.

    :param bitmask long:
    :param input array:
    :param b bool: apply ifftshift

    """
    usage_string = "fftshift [-b] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fftshift '
    flag_str = ''

    opt_args = f''

    multituples = []

    if b is not None:
        flag_str += f'-b '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def filter(input, m=None, l=None, G=None, a=None):
    """
    Apply filter.

    :param input array:
    :param m int: median filter along dimension dim
    :param l int: length of filter
    :param G bool: geometric median
    :param a int: Moving average filter along dimension dim

    """
    usage_string = "filter [-m d] [-l d] [-G] [-a d] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'filter '
    flag_str = ''

    opt_args = f''

    multituples = []

    if m is not None:
        flag_str += f'-m {m} '

    if l is not None:
        flag_str += f'-l {l} '

    if G is not None:
        flag_str += f'-G '

    if a is not None:
        flag_str += f'-a {a} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def flatten(input):
    """
    Flatten array to one dimension.

    :param input array:

    """
    usage_string = "flatten input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'flatten '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def flip(input, bitmask):
    """
    Flip (reverse) dimensions specified by the {bitmask}.

    :param bitmask long:
    :param input array:

    """
    usage_string = "flip bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'flip '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fmac(input1, input2=None, A=None, C=None, s=None):
    """
    Multiply <input1> and <input2> and accumulate in <output>.
If <input2> is not specified, assume all-ones.

    :param input1 array:
    :param input2 array: None
    :param A bool: add to existing output (instead of overwriting)
    :param C bool: conjugate input2
    :param s long: squash dimensions selected by bitmask b

    """
    usage_string = "fmac [-A] [-C] [-s d] input1 [input2] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fmac '
    flag_str = ''

    opt_args = f''

    multituples = []

    if not isinstance(input2, type(None)):
        opt_args += 'NAME + {input2}'

    if A is not None:
        flag_str += f'-A '

    if C is not None:
        flag_str += f'-C '

    if s is not None:
        flag_str += f'-s {s} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input1 {NAME}output  "
    cfl.writecfl(NAME + 'input1', input1)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def fovshift(input, t=None, s=None):
    """
    Shifts FOV.

    :param input array:
    :param t array: k-space trajectory
    :param s FLOAT_VEC3: FOV shift

    """
    usage_string = "fovshift [-t file] [-s f:f:f] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'fovshift '
    flag_str = ''

    opt_args = f''

    multituples = []

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if s is not None:
        flag_str += f'-s {s} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def homodyne(input, dim, fraction, r=None, I=None, C=None, P=None, n=None):
    """
    Perform homodyne reconstruction along dimension dim.

    :param dim int:
    :param fraction float:
    :param input array:
    :param r float: Offset of ramp filter between 0 and 1. alpha=0 is a full ramp alpha=1 is a horizontal line
    :param I bool: Input is in image domain
    :param C bool: Clear unacquired portion of kspace
    :param P array: Use <phase_ref> as phase reference
    :param n bool: use uncentered ffts

    """
    usage_string = "homodyne [-r f] [-I] [-C] [-P file] [-n] dim fraction input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'homodyne '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r {r} '

    if I is not None:
        flag_str += f'-I '

    if C is not None:
        flag_str += f'-C '

    if not isinstance(P, type(None)):
        cfl.writecfl(NAME + 'P', P)
        flag_str += f'-P {NAME}P '

    if n is not None:
        flag_str += f'-n '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dim} {fraction} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

#def ictv(input, llambda, flags, flags, i=None, u=None):
def ictv(input, llambda, flags, i=None, u=None):
    """
    Infimal convolution of total variation along dims specified by flags.

    :param llambda float:
    :param flags int:
    :param flags int:
    :param input array:
    :param i int: max. iterations
    :param u float: rho in ADMM

    """
    usage_string = "ictv [-i d] [-u f] lambda flags flags input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ictv '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i {i} '

    if u is not None:
        flag_str += f'-u {u} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {llambda} {flags} {flags} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def index(dim, size):
    """
    Create an array counting from 0 to {size-1} in dimensions {dim}.

    :param dim int:
    :param size int:

    """
    usage_string = "index dim size name"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'index '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dim} {size} {NAME}name  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'name')
    return outputs

def invert(input):
    """
    Invert array (1 / <input>). The output is set to zero in case of divide by zero.

    :param input array:

    """
    usage_string = "invert input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'invert '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def itsense(sensitivities, kspace, pattern, alpha):
    """
    A simplified implementation of iterative sense reconstruction
with l2-regularization.

    :param alpha float:
    :param sensitivities array:
    :param kspace array:
    :param pattern array:

    """
    usage_string = "itsense alpha sensitivities kspace pattern output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'itsense '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {alpha} {NAME}sensitivities {NAME}kspace {NAME}pattern {NAME}output  "
    cfl.writecfl(NAME + 'sensitivities', sensitivities)
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'pattern', pattern)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def join(dimension, input, output, a=None):
    """
    Join input files along {dimensions}. All other dimensions must have the same size.
     Example 1: join 0 slice_001 slice_002 slice_003 full_data
     Example 2: join 0 `seq -f "slice_%%03g" 0 255` full_data

    :param dimension int:
    :param input tuple:
    :param output INOUTFILE:
    :param a bool: append - only works for cfl files!

    """
    usage_string = "join [-a] dimension input1 ... inputN output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'join '
    flag_str = ''

    opt_args = f''

    multituples = []

    if a is not None:
        flag_str += f'-a '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dimension} {' '.join([str(arg) for arg in input])} {output}  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def looklocker(input, t=None, D=None):
    """
    Compute T1 map from M_0, M_ss, and R_1*.

    :param input array:
    :param t float: Pixels with M0 values smaller than threshold are set to zero.
    :param D float: Time between the middle of inversion pulse and the first excitation.

    """
    usage_string = "looklocker [-t f] [-D f] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'looklocker '
    flag_str = ''

    opt_args = f''

    multituples = []

    if t is not None:
        flag_str += f'-t {t} '

    if D is not None:
        flag_str += f'-D {D} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def lrmatrix(input, d=None, i=None, m=None, f=None, j=None, k=None, N=None, s=None, l=None, u=None, v=None, H=None, p=None, n=None, g=None):
    """
    Perform (multi-scale) low rank matrix completion

    :param input array:
    :param o OUTFILE:
    :param d bool: perform decomposition instead ie fully sampled
    :param i int: maximum iterations.
    :param m long: which dimensions are reshaped to matrix columns.
    :param f long: which dimensions to perform multi-scale partition.
    :param j int: block size scaling from one scale to the next one.
    :param k long: smallest block size
    :param N bool: add noise scale to account for Gaussian noise.
    :param s bool: perform low rank + sparse matrix completion.
    :param l long: perform locally low rank soft thresholding with specified block size.
    :param u bool: ()
    :param v bool: ()
    :param H bool: (hogwild)
    :param p float: (rho)
    :param n bool: (no randshift)
    :param g bool: (use GPU)

    """
    usage_string = "lrmatrix [-d] [-i d] [-m d] [-f d] [-j d] [-k d] [-N] [-s] [-l d] [-o file] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'lrmatrix '
    flag_str = ''

    opt_args = f''

    multituples = []

    if d is not None:
        flag_str += f'-d '

    if i is not None:
        flag_str += f'-i {i} '

    if m is not None:
        flag_str += f'-m {m} '

    if f is not None:
        flag_str += f'-f {f} '

    if j is not None:
        flag_str += f'-j {j} '

    if k is not None:
        flag_str += f'-k {k} '

    if N is not None:
        flag_str += f'-N '

    if s is not None:
        flag_str += f'-s '

    if l is not None:
        flag_str += f'-l {l} '

    if u is not None:
        flag_str += f'-u '

    if v is not None:
        flag_str += f'-v '

    if H is not None:
        flag_str += f'-H '

    if p is not None:
        flag_str += f'-p {p} '

    if n is not None:
        flag_str += f'-n '

    if g is not None:
        flag_str += f'-g '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output {NAME}o  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def mandelbrot(s=None, n=None, t=None, z=None, r=None, i=None):
    """
    Compute mandelbrot set.

    :param s int: image size
    :param n int: nr. of iterations
    :param t float: threshold for divergence
    :param z float: zoom
    :param r float: offset real
    :param i float: offset imag

    """
    usage_string = "mandelbrot [-s d] [-n d] [-t f] [-z f] [-r f] [-i f] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'mandelbrot '
    flag_str = ''

    opt_args = f''

    multituples = []

    if s is not None:
        flag_str += f'-s {s} '

    if n is not None:
        flag_str += f'-n {n} '

    if t is not None:
        flag_str += f'-t {t} '

    if z is not None:
        flag_str += f'-z {z} '

    if r is not None:
        flag_str += f'-r {r} '

    if i is not None:
        flag_str += f'-i {i} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def measure(reference, input, mse=None, mse_mag=None, ssim=None, psnr=None):
    """
    

    :param reference array:
    :param input array:
    :param mse bool: mse
    :param mse_mag bool: mse of rss (over coil dim)
    :param ssim bool: ssim of rss (over coil dim) and mean over other dims
    :param psnr bool: psnr of rss (over coil dim) and mean over other dims

    """
    usage_string = "measure [--mse] [--mse-mag] [--ssim] [--psnr] reference input [output]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'measure '
    flag_str = ''

    opt_args = f''

    multituples = []

    if mse is not None:
        flag_str += f'--mse '

    if mse_mag is not None:
        flag_str += f'--mse-mag '

    if ssim is not None:
        flag_str += f'--ssim '

    if psnr is not None:
        flag_str += f'--psnr '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}reference {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'reference', reference)
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def mip(input, bitmask, m=None, a=None):
    """
    Maximum (minimum) intensity projection (MIP) along dimensions specified by bitmask.

    :param bitmask int:
    :param input array:
    :param m bool: minimum
    :param a bool: do absolute value first

    """
    usage_string = "mip [-m] [-a] bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'mip '
    flag_str = ''

    opt_args = f''

    multituples = []

    if m is not None:
        flag_str += f'-m '

    if a is not None:
        flag_str += f'-a '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def mnist(input, weights, ref_output, apply=None, train=None, gpu=None):
    """
    Trains or applies a MNIST network.
This network is to demonstrate how a neural network can be implemented in BART.

    :param input array:
    :param weights INOUTFILE:
    :param ref_output INOUTFILE:
    :param apply bool: apply nnet
    :param train bool: trains network
    :param gpu bool: run on gpu

    """
    usage_string = "mnist [-a,--apply] [-t,--train] [-g,--gpu] input weights ref/output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'mnist '
    flag_str = ''

    opt_args = f''

    multituples = []

    if apply is not None:
        flag_str += f'--apply '

    if train is not None:
        flag_str += f'--train '

    if gpu is not None:
        flag_str += f'--gpu '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {weights} {ref_output}  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def moba(kspace, TI_TE, r=None, L=None, P=None, F=None, G=None, bloch=None, m=None, l=None, i=None, reduction=None, T=None, j=None, u=None, C=None, s=None, B=None, b=None, d=None, N=None, f=None, p=None, J=None, M=None, O=None, g=None, multi_gpu=None, I=None, t=None, o=None, img_dims=None, k=None, kfilter_1=None, kfilter_2=None, e=None, n=None, no_alpha_min_exp_decay=None, sobolev_a=None, sobolev_b=None, fat_spec_0=None, scale_data=None, scale_psf=None, normalize_scaling=None, seq=None, sim=None, other=None):
    """
    Model-based nonlinear inverse reconstruction

    :param kspace array:
    :param TI_TE array:
    :param r SPECIAL: generalized regularization options (-rh for help)
    :param L bool: T1 mapping using model-based look-locker
    :param P bool: T1 mapping using reparameterized (M0 R1 alpha) model-based look-locker (TR required!)
    :param F bool: T2 mapping using model-based Fast Spin Echo
    :param G bool: T2* mapping using model-based multiple gradient echo
    :param bloch bool: Bloch model-based reconstruction
    :param m int: Select the MGRE model from enum  WF = 0 WFR2S WF2R2S R2S PHASEDIFF  [default: WFR2S]
    :param l int: toggle l1-wavelet or l2 regularization.
    :param i int: Number of Newton steps
    :param reduction float: reduction factor
    :param T float: damping on temporal frames
    :param j float: Minimum regularization parameter
    :param u float: ADMM rho [default: 0.01]
    :param C int: inner iterations
    :param s float: step size
    :param B float: lower bound for relaxation
    :param b FLOAT_VEC2: B0 field: spatial smooth level; scaling [default: 222.; 1.]
    :param d int: Debug level
    :param N bool: (normalize)
    :param f float: 
    :param p array: 
    :param J bool: Stack frames for joint recon
    :param M bool: Simultaneous Multi-Slice reconstruction
    :param O bool: (Output original maps from reconstruction without post processing)
    :param g bool: use gpu
    :param multi_gpu int: number of gpus to use
    :param I array: File for initialization
    :param t array: K-space trajectory
    :param o float: Oversampling factor for gridding [default: 1.]
    :param img_dims list: dimensions
    :param k bool: k-space edge filter for non-Cartesian trajectories
    :param kfilter_1 bool: k-space edge filter 1
    :param kfilter_2 bool: k-space edge filter 2
    :param e float: strength for k-space edge filter [default: 2e-3]
    :param n bool: (disable normalization of parameter maps for thresholding)
    :param no_alpha_min_exp_decay bool: (Use hard minimum instead of exponential decay towards alpha_min)
    :param sobolev_a float: (a in 1 + a * \Laplace^-b/2)
    :param sobolev_b float: (b in 1 + a * \Laplace^-b/2)
    :param fat_spec_0 bool: select fat spectrum from ISMRM fat-water tool
    :param scale_data float: scaling factor for data
    :param scale_psf float: (scaling factor for PSF)
    :param normalize_scaling bool: (normalize scaling by data / PSF)
    :param seq SUBOPT: configure sequence parameters
    :param sim SUBOPT: configure simulation parameters
    :param other SUBOPT: configure other parameters

    """
    usage_string = "moba [-r ...] [-L] [-P] [-F] [-G] [--bloch] [-m d] [-l d] [-i d] [-R,--reduction f] [-T f] [-j f] [-u f] [-C d] [-s f] [-B f] [-b f:f] [-d d] [-f f] [-p file] [-J] [-M] [-g] [--multi-gpu d] [-I file] [-t file] [-o f] [--img_dims d:d:d] [-k] [--kfilter-1] [--kfilter-2] [-e f] [--fat_spec_0] [--scale_data f] [--seq ...] [--sim ...] [--other ...] kspace TI/TE output [sensitivities]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'moba '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r {r} '

    if L is not None:
        flag_str += f'-L '

    if P is not None:
        flag_str += f'-P '

    if F is not None:
        flag_str += f'-F '

    if G is not None:
        flag_str += f'-G '

    if bloch is not None:
        flag_str += f'--bloch '

    if m is not None:
        flag_str += f'-m {m} '

    if l is not None:
        flag_str += f'-l {l} '

    if i is not None:
        flag_str += f'-i {i} '

    if reduction is not None:
        flag_str += f'--reduction {reduction} '

    if T is not None:
        flag_str += f'-T {T} '

    if j is not None:
        flag_str += f'-j {j} '

    if u is not None:
        flag_str += f'-u {u} '

    if C is not None:
        flag_str += f'-C {C} '

    if s is not None:
        flag_str += f'-s {s} '

    if B is not None:
        flag_str += f'-B {B} '

    if b is not None:
        flag_str += f'-b {b} '

    if d is not None:
        flag_str += f'-d {d} '

    if N is not None:
        flag_str += f'-N '

    if f is not None:
        flag_str += f'-f {f} '

    if not isinstance(p, type(None)):
        cfl.writecfl(NAME + 'p', p)
        flag_str += f'-p {NAME}p '

    if J is not None:
        flag_str += f'-J '

    if M is not None:
        flag_str += f'-M '

    if O is not None:
        flag_str += f'-O '

    if g is not None:
        flag_str += f'-g '

    if multi_gpu is not None:
        flag_str += f'--multi-gpu {multi_gpu} '

    if not isinstance(I, type(None)):
        cfl.writecfl(NAME + 'I', I)
        flag_str += f'-I {NAME}I '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if o is not None:
        flag_str += f'-o {o} '

    if img_dims is not None:
        flag_str += f'--img_dims {":".join([str(x) for x in img_dims])} '

    if k is not None:
        flag_str += f'-k '

    if kfilter_1 is not None:
        flag_str += f'--kfilter-1 '

    if kfilter_2 is not None:
        flag_str += f'--kfilter-2 '

    if e is not None:
        flag_str += f'-e {e} '

    if n is not None:
        flag_str += f'-n '

    if no_alpha_min_exp_decay is not None:
        flag_str += f'--no_alpha_min_exp_decay '

    if sobolev_a is not None:
        flag_str += f'--sobolev_a {sobolev_a} '

    if sobolev_b is not None:
        flag_str += f'--sobolev_b {sobolev_b} '

    if fat_spec_0 is not None:
        flag_str += f'--fat_spec_0 '

    if scale_data is not None:
        flag_str += f'--scale_data {scale_data} '

    if scale_psf is not None:
        flag_str += f'--scale_psf {scale_psf} '

    if normalize_scaling is not None:
        flag_str += f'--normalize_scaling '

    if seq is not None:
        flag_str += f'--seq {seq} '

    if sim is not None:
        flag_str += f'--sim {sim} '

    if other is not None:
        flag_str += f'--other {other} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}TI_TE {NAME}output {NAME}sensitivities  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'TI_TE', TI_TE)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output'), cfl.readcfl(NAME + 'sensitivities')
    return outputs

def mobafit(enc, echo_contrast_images, T=None, G=None, D=None, m=None, i=None, p=None, g=None):
    """
    Pixel-wise fitting of physical signal models.

    :param enc array:
    :param echo_contrast_images array:
    :param T bool: TSE
    :param G bool: MGRE
    :param D bool: diffusion
    :param m int: Select the MGRE model from enum  WF = 0 WFR2S WF2R2S R2S PHASEDIFF  [default: WFR2S]
    :param i int: Number of IRGNM steps
    :param p list: (patch size)
    :param g bool: use gpu

    """
    usage_string = "mobafit [-T] [-G] [-D] [-m d] [-i d] [-g] enc echo/contrast images [coefficients]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'mobafit '
    flag_str = ''

    opt_args = f''

    multituples = []

    if T is not None:
        flag_str += f'-T '

    if G is not None:
        flag_str += f'-G '

    if D is not None:
        flag_str += f'-D '

    if m is not None:
        flag_str += f'-m {m} '

    if i is not None:
        flag_str += f'-i {i} '

    if p is not None:
        flag_str += f'-p {":".join([str(x) for x in p])} '

    if g is not None:
        flag_str += f'-g '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}enc {NAME}echo_contrast_images {NAME}coefficients  "
    cfl.writecfl(NAME + 'enc', enc)
    cfl.writecfl(NAME + 'echo_contrast_images', echo_contrast_images)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'coefficients')
    return outputs

def morphop(binary_input, mask_size, e=None, d=None, o=None, c=None):
    """
    Perform morphological operators on binary data with odd mask sizes.

    :param mask_size int:
    :param binary_input array:
    :param e bool: EROSION (default)
    :param d bool: DILATION
    :param o bool: OPENING
    :param c bool: CLOSING

    """
    usage_string = "morphop [-e] [-d] [-o] [-c] mask_size binary input [binary output]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'morphop '
    flag_str = ''

    opt_args = f''

    multituples = []

    if e is not None:
        flag_str += f'-e '

    if d is not None:
        flag_str += f'-d '

    if o is not None:
        flag_str += f'-o '

    if c is not None:
        flag_str += f'-c '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {mask_size} {NAME}binary_input {NAME}binary_output  "
    cfl.writecfl(NAME + 'binary_input', binary_input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'binary_output')
    return outputs

def multicfl(cfl, s=None):
    """
    Combine/Split multiple cfl files to one multi-cfl file.
In normal usage, the last argument is the combined multi-cfl,
with '-s', the first argument is the multi-cfl that is split up

    :param cfl tuple:
    :param s bool: separate

    """
    usage_string = "multicfl [-s] cfl1 ... cflN"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'multicfl '
    flag_str = ''

    opt_args = f''

    multituples = []

    if s is not None:
        flag_str += f'-s '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {' '.join([str(arg) for arg in cfl])}  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def nlinv(kspace, i=None, R=None, M=None, d=None, c=None, N=None, m=None, U=None, f=None, p=None, t=None, I=None, g=None, S=None, s=None, a=None, b=None, P=None, n=None, w=None, lowmem=None):
    """
    Jointly estimate image and sensitivities with nonlinear
inversion using {iter} iteration steps. Optionally outputs
the sensitivities.

    :param kspace array:
    :param i int: Number of Newton steps
    :param R float: (reduction factor)
    :param M float: (minimum for regularization)
    :param d int: Debug level
    :param c bool: Real-value constraint
    :param N bool: Do not normalize image with coil sensitivities
    :param m int: Number of ENLIVE maps to use in reconstruction
    :param U bool: Do not combine ENLIVE maps in output
    :param f float: restrict FOV
    :param p array: pattern / transfer function
    :param t array: kspace trajectory
    :param I array: File for initialization
    :param g bool: use gpu
    :param S bool: Re-scale image after reconstruction
    :param s int: (dimensions with constant sensitivities)
    :param a float: (a in 1 + a * \Laplace^-b/2)
    :param b float: (b in 1 + a * \Laplace^-b/2)
    :param P bool: (supplied psf is different for each coil)
    :param n bool: (non-Cartesian)
    :param w float: (inverse scaling of the data)
    :param lowmem bool: Use low-mem mode of the nuFFT

    """
    usage_string = "nlinv [-i d] [-d d] [-c] [-N] [-m d] [-U] [-f f] [-p file] [-t file] [-I file] [-g] [-S] [--lowmem] kspace output [sensitivities]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'nlinv '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i {i} '

    if R is not None:
        flag_str += f'-R {R} '

    if M is not None:
        flag_str += f'-M {M} '

    if d is not None:
        flag_str += f'-d {d} '

    if c is not None:
        flag_str += f'-c '

    if N is not None:
        flag_str += f'-N '

    if m is not None:
        flag_str += f'-m {m} '

    if U is not None:
        flag_str += f'-U '

    if f is not None:
        flag_str += f'-f {f} '

    if not isinstance(p, type(None)):
        cfl.writecfl(NAME + 'p', p)
        flag_str += f'-p {NAME}p '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if not isinstance(I, type(None)):
        cfl.writecfl(NAME + 'I', I)
        flag_str += f'-I {NAME}I '

    if g is not None:
        flag_str += f'-g '

    if S is not None:
        flag_str += f'-S '

    if s is not None:
        flag_str += f'-s {s} '

    if a is not None:
        flag_str += f'-a {a} '

    if b is not None:
        flag_str += f'-b {b} '

    if P is not None:
        flag_str += f'-P '

    if n is not None:
        flag_str += f'-n '

    if w is not None:
        flag_str += f'-w {w} '

    if lowmem is not None:
        flag_str += f'--lowmem '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}output {NAME}sensitivities  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output'), cfl.readcfl(NAME + 'sensitivities')
    return outputs

def nnet(input, weights, ref_output, apply=None, eval=None, train=None, gpu=None, batch_size=None, load=None, network=None, unet_segm=None, train_loss=None, valid_loss=None, valid_data=None, train_algo=None, adam=None, load_memory=None, export_graph=None):
    """
    Trains or applies a neural network.

    :param input array:
    :param weights INOUTFILE:
    :param ref_output INOUTFILE:
    :param apply bool: apply nnet
    :param eval bool: evaluate nnet
    :param train bool: trains network
    :param gpu bool: run on gpu
    :param batch_size long: size of mini batches
    :param load array: load weights for continuing training
    :param network SUBOPT: select neural network
    :param unet_segm SUBOPT: configure U-Net for segmentation
    :param train_loss SUBOPT: configure the training loss
    :param valid_loss SUBOPT: configure the validation loss
    :param valid_data SUBOPT: provide validation data
    :param train_algo SUBOPT: configure general training parmeters
    :param adam SUBOPT: configure Adam
    :param load_memory bool: load files into memory
    :param export_graph STRING: export graph for visualization

    """
    usage_string = "nnet [-a,--apply] [-e,--eval] [-t,--train] [-g,--gpu] [-b,--batch-size d] [-l,--load file] [-N,--network ...] [-U,--unet-segm ...] [--train-loss ...] [--valid-loss ...] [--valid-data ...] [-T,--train-algo ...] [--adam ...] [--load-memory] [--export-graph string] input weights ref/output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'nnet '
    flag_str = ''

    opt_args = f''

    multituples = []

    if apply is not None:
        flag_str += f'--apply '

    if eval is not None:
        flag_str += f'--eval '

    if train is not None:
        flag_str += f'--train '

    if gpu is not None:
        flag_str += f'--gpu '

    if batch_size is not None:
        flag_str += f'--batch-size {batch_size} '

    if not isinstance(load, type(None)):
        cfl.writecfl(NAME + 'load', load)
        flag_str += f'--load {NAME}load '

    if network is not None:
        flag_str += f'--network {network} '

    if unet_segm is not None:
        flag_str += f'--unet-segm {unet_segm} '

    if train_loss is not None:
        flag_str += f'--train-loss {train_loss} '

    if valid_loss is not None:
        flag_str += f'--valid-loss {valid_loss} '

    if valid_data is not None:
        flag_str += f'--valid-data {valid_data} '

    if train_algo is not None:
        flag_str += f'--train-algo {train_algo} '

    if adam is not None:
        flag_str += f'--adam {adam} '

    if load_memory is not None:
        flag_str += f'--load-memory '

    if export_graph is not None:
        flag_str += f'--export-graph {export_graph} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {weights} {ref_output}  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def noise(input, s=None, S=None, r=None, n=None):
    """
    Add noise with selected variance to input.

    :param input array:
    :param s int: random seed initialization
    :param S float: ()
    :param r bool: real-valued input
    :param n float: DEFAULT: 1.0

    """
    usage_string = "noise [-s d] [-r] [-n f] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'noise '
    flag_str = ''

    opt_args = f''

    multituples = []

    if s is not None:
        flag_str += f'-s {s} '

    if S is not None:
        flag_str += f'-S {S} '

    if r is not None:
        flag_str += f'-r '

    if n is not None:
        flag_str += f'-n {n} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def normalize(input, flags, b=None):
    """
    Normalize along selected dimensions.

    :param flags int:
    :param input array:
    :param b bool: l1

    """
    usage_string = "normalize [-b] flags input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'normalize '
    flag_str = ''

    opt_args = f''

    multituples = []

    if b is not None:
        flag_str += f'-b '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {flags} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def nrmse(reference, input, t=None, s=None):
    """
    Output normalized root mean square error (NRMSE),
i.e. norm(input - ref) / norm(ref)

    :param reference array:
    :param input array:
    :param t float: compare to eps
    :param s bool: automatic (complex) scaling

    """
    usage_string = "nrmse [-t f] [-s] reference input"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'nrmse '
    flag_str = ''

    opt_args = f''

    multituples = []

    if t is not None:
        flag_str += f'-t {t} '

    if s is not None:
        flag_str += f'-s '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}reference {NAME}input  "
    cfl.writecfl(NAME + 'reference', reference)
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def nufft(traj, input, a=None, i=None, d=None, D=None, t=None, r=None, c=None, l=None, m=None, P=None, s=None, g=None, _1=None, lowmem=None):
    """
    Perform non-uniform Fast Fourier Transform.

    :param traj array:
    :param input array:
    :param a bool: adjoint
    :param i bool: inverse
    :param d list: dimensions
    :param D list: ()
    :param t bool: Toeplitz embedding for inverse NUFFT
    :param r bool: turn-off Toeplitz embedding for inverse NUFFT
    :param c bool: Preconditioning for inverse NUFFT
    :param l float: l2 regularization
    :param m int: ()
    :param P bool: periodic k-space
    :param s bool: DFT
    :param g bool: GPU (only inverse)
    :param _1 bool: use/return oversampled grid
    :param lowmem bool: Use low-mem mode of the nuFFT

    """
    usage_string = "nufft [-a] [-i] [-d d:d:d] [-t] [-r] [-c] [-l f] [-P] [-s] [-g] [-1] [--lowmem] traj input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'nufft '
    flag_str = ''

    opt_args = f''

    multituples = []

    if a is not None:
        flag_str += f'-a '

    if i is not None:
        flag_str += f'-i '

    if d is not None:
        flag_str += f'-d {":".join([str(x) for x in d])} '

    if D is not None:
        flag_str += f'-D {":".join([str(x) for x in D])} '

    if t is not None:
        flag_str += f'-t '

    if r is not None:
        flag_str += f'-r '

    if c is not None:
        flag_str += f'-c '

    if l is not None:
        flag_str += f'-l {l} '

    if m is not None:
        flag_str += f'-m {m} '

    if P is not None:
        flag_str += f'-P '

    if s is not None:
        flag_str += f'-s '

    if g is not None:
        flag_str += f'-g '

    if _1 is not None:
        flag_str += f'-1 '

    if lowmem is not None:
        flag_str += f'--lowmem '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}traj {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'traj', traj)
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def onehotenc(input, r=None, i=None):
    """
    Transforms class labels to one-hot-encoded classes


    :param input array:
    :param r bool: get class label by maximum entry
    :param i int: select dimension

    """
    usage_string = "onehotenc [-r] [-i d] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'onehotenc '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r '

    if i is not None:
        flag_str += f'-i {i} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def ones(dims, dim):
    """
    Create an array filled with ones with {dims} dimensions of size {dim1} to {dimn}.

    :param dims long:
    :param dim tuple:

    """
    usage_string = "ones dims dim1 ... dimN output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ones '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dims} {' '.join([str(arg) for arg in dim])} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def pattern(kspace, s=None):
    """
    Compute sampling pattern from kspace

    :param kspace array:
    :param s int: Squash dimensions selected by bitmask

    """
    usage_string = "pattern [-s d] kspace pattern"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'pattern '
    flag_str = ''

    opt_args = f''

    multituples = []

    if s is not None:
        flag_str += f'-s {s} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}pattern  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'pattern')
    return outputs

def phantom(s=None, S=None, k=None, t=None, c=None, a=None, m=None, G=None, T=None, NIST=None, SONAR=None, N=None, B=None, x=None, g=None, _3=None, b=None, r=None, rotation_angle=None, rotation_steps=None):
    """
    Image and k-space domain phantoms.

    :param s int: nc sensitivities
    :param S int: Output nc sensitivities
    :param k bool: k-space
    :param t array: trajectory
    :param c bool: ()
    :param a bool: ()
    :param m bool: ()
    :param G bool: geometric object phantom
    :param T bool: tubes phantom
    :param NIST bool: NIST phantom (T2 sphere)
    :param SONAR bool: Diagnostic Sonar phantom
    :param N int: Random tubes phantom and number
    :param B bool: BART logo
    :param x int: dimensions in y and z
    :param g int: select geometry for object phantom
    :param _3 bool: 3D
    :param b bool: basis functions for geometry
    :param r int: random seed initialization
    :param rotation_angle float: Angle of Rotation
    :param rotation_steps int: Number of rotation steps

    """
    usage_string = "phantom [-s d] [-S d] [-k] [-t file] [-G] [-T] [--NIST] [--SONAR] [-N d] [-B] [-x d] [-g d] [-3] [-b] [-r d] [--rotation-angle f] [--rotation-steps d] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'phantom '
    flag_str = ''

    opt_args = f''

    multituples = []

    if s is not None:
        flag_str += f'-s {s} '

    if S is not None:
        flag_str += f'-S {S} '

    if k is not None:
        flag_str += f'-k '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if c is not None:
        flag_str += f'-c '

    if a is not None:
        flag_str += f'-a '

    if m is not None:
        flag_str += f'-m '

    if G is not None:
        flag_str += f'-G '

    if T is not None:
        flag_str += f'-T '

    if NIST is not None:
        flag_str += f'--NIST '

    if SONAR is not None:
        flag_str += f'--SONAR '

    if N is not None:
        flag_str += f'-N {N} '

    if B is not None:
        flag_str += f'-B '

    if x is not None:
        flag_str += f'-x {x} '

    if g is not None:
        flag_str += f'-g {g} '

    if _3 is not None:
        flag_str += f'-3 '

    if b is not None:
        flag_str += f'-b '

    if r is not None:
        flag_str += f'-r {r} '

    if rotation_angle is not None:
        flag_str += f'--rotation-angle {rotation_angle} '

    if rotation_steps is not None:
        flag_str += f'--rotation-steps {rotation_steps} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def pics(kspace, sensitivities, l=None, r=None, R=None, c=None, s=None, i=None, t=None, n=None, N=None, g=None, G=None, p=None, I=None, b=None, e=None, H=None, D=None, F=None, J=None, T=None, W=None, d=None, O=None, o=None, u=None, C=None, q=None, f=None, m=None, w=None, S=None, L=None, K=None, B=None, P=None, a=None, M=None, lowmem=None, psf_import=None, wavelet=None):
    """
    Parallel-imaging compressed-sensing reconstruction.


    :param kspace array:
    :param sensitivities array:
    :param psf_export OUTFILE:
    :param l SPECIAL: toggle l1-wavelet or l2 regularization.
    :param r float: regularization parameter
    :param R SPECIAL: generalized regularization options (-Rh for help)
    :param c bool: real-value constraint
    :param s float: iteration stepsize
    :param i int: max. number of iterations
    :param t array: k-space trajectory
    :param n bool: disable random wavelet cycle spinning
    :param N bool: do fully overlapping LLR blocks
    :param g bool: use GPU
    :param G int: use GPU device gpun
    :param p array: pattern or weights
    :param I bool: select IST
    :param b int: Lowrank block size
    :param e bool: Scale stepsize based on max. eigenvalue
    :param H bool: (hogwild)
    :param D bool: (ADMM dynamic step size)
    :param F bool: (fast)
    :param J bool: (ADMM residual balancing)
    :param T array: (truth file)
    :param W array: Warm start with <img>
    :param d int: Debug level
    :param O int: (reweighting)
    :param o float: (reweighting)
    :param u float: ADMM rho
    :param C int: ADMM max. CG iterations
    :param q float: (cclambda)
    :param f float: restrict FOV
    :param m bool: select ADMM
    :param w float: inverse scaling of the data
    :param S bool: re-scale the image after reconstruction
    :param L int: batch-mode
    :param K bool: randshift for NUFFT
    :param B array: temporal (or other) basis
    :param P float: Basis Pursuit formulation || y- Ax ||_2 <= eps
    :param a bool: select Primal Dual
    :param M bool: Simultaneous Multi-Slice reconstruction
    :param lowmem bool: Use low-mem mode of the nuFFT
    :param psf_import array: Import PSF from file
    :param wavelet STRING: wavelet type (haar dau2 cdf44)

    """
    usage_string = "pics [-l ...] [-r f] [-R ...] [-c] [-s f] [-i d] [-t file] [-n] [-N] [-g] [-G d] [-p file] [-I] [-b d] [-e] [-W file] [-d d] [-u f] [-C d] [-f f] [-m] [-w f] [-S] [-L d] [-K] [-B file] [-P f] [-a] [-M] [-U,--lowmem] [--psf_export file] [--psf_import file] [--wavelet string] kspace sensitivities output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'pics '
    flag_str = ''

    opt_args = f''

    multituples = []

    if l is not None:
        flag_str += f'-l {l} '

    if r is not None:
        flag_str += f'-r {r} '

    if R is not None:
        flag_str += f'-R {R} '

    if c is not None:
        flag_str += f'-c '

    if s is not None:
        flag_str += f'-s {s} '

    if i is not None:
        flag_str += f'-i {i} '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if n is not None:
        flag_str += f'-n '

    if N is not None:
        flag_str += f'-N '

    if g is not None:
        flag_str += f'-g '

    if G is not None:
        flag_str += f'-G {G} '

    if not isinstance(p, type(None)):
        cfl.writecfl(NAME + 'p', p)
        flag_str += f'-p {NAME}p '

    if I is not None:
        flag_str += f'-I '

    if b is not None:
        flag_str += f'-b {b} '

    if e is not None:
        flag_str += f'-e '

    if H is not None:
        flag_str += f'-H '

    if D is not None:
        flag_str += f'-D '

    if F is not None:
        flag_str += f'-F '

    if J is not None:
        flag_str += f'-J '

    if not isinstance(T, type(None)):
        cfl.writecfl(NAME + 'T', T)
        flag_str += f'-T {NAME}T '

    if not isinstance(W, type(None)):
        cfl.writecfl(NAME + 'W', W)
        flag_str += f'-W {NAME}W '

    if d is not None:
        flag_str += f'-d {d} '

    if O is not None:
        flag_str += f'-O {O} '

    if o is not None:
        flag_str += f'-o {o} '

    if u is not None:
        flag_str += f'-u {u} '

    if C is not None:
        flag_str += f'-C {C} '

    if q is not None:
        flag_str += f'-q {q} '

    if f is not None:
        flag_str += f'-f {f} '

    if m is not None:
        flag_str += f'-m '

    if w is not None:
        flag_str += f'-w {w} '

    if S is not None:
        flag_str += f'-S '

    if L is not None:
        flag_str += f'-L {L} '

    if K is not None:
        flag_str += f'-K '

    if not isinstance(B, type(None)):
        cfl.writecfl(NAME + 'B', B)
        flag_str += f'-B {NAME}B '

    if P is not None:
        flag_str += f'-P {P} '

    if a is not None:
        flag_str += f'-a '

    if M is not None:
        flag_str += f'-M '

    if lowmem is not None:
        flag_str += f'--lowmem '

    if not isinstance(psf_import, type(None)):
        cfl.writecfl(NAME + 'psf_import', psf_import)
        flag_str += f'--psf_import {NAME}psf_import '

    if wavelet is not None:
        flag_str += f'--wavelet {wavelet} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}sensitivities {NAME}output {NAME}psf_export  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'sensitivities', sensitivities)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def pocsense(kspace, sensitivities, i=None, r=None, l=None, g=None, o=None, m=None):
    """
    Perform POCSENSE reconstruction.

    :param kspace array:
    :param sensitivities array:
    :param i int: max. number of iterations
    :param r float: regularization parameter
    :param l int: toggle l1-wavelet or l2 regularization
    :param g bool: ()
    :param o float: ()
    :param m float: ()

    """
    usage_string = "pocsense [-i d] [-r f] [-l d] kspace sensitivities output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'pocsense '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i {i} '

    if r is not None:
        flag_str += f'-r {r} '

    if l is not None:
        flag_str += f'-l {l} '

    if g is not None:
        flag_str += f'-g '

    if o is not None:
        flag_str += f'-o {o} '

    if m is not None:
        flag_str += f'-m {m} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}sensitivities {NAME}output  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'sensitivities', sensitivities)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def poisson(Y=None, Z=None, y=None, z=None, C=None, v=None, V=None, e=None, D=None, T=None, m=None, R=None, s=None):
    """
    Computes Poisson-disc sampling pattern.

    :param Y int: size dimension 1
    :param Z int: size dimension 2
    :param y float: acceleration dim 1
    :param z float: acceleration dim 2
    :param C int: size of calibration region
    :param v bool: variable density
    :param V float: (variable density)
    :param e bool: elliptical scanning
    :param D float: ()
    :param T int: ()
    :param m bool: ()
    :param R int: ()
    :param s int: random seed

    """
    usage_string = "poisson [-Y d] [-Z d] [-y f] [-z f] [-C d] [-v] [-e] [-s d] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'poisson '
    flag_str = ''

    opt_args = f''

    multituples = []

    if Y is not None:
        flag_str += f'-Y {Y} '

    if Z is not None:
        flag_str += f'-Z {Z} '

    if y is not None:
        flag_str += f'-y {y} '

    if z is not None:
        flag_str += f'-z {z} '

    if C is not None:
        flag_str += f'-C {C} '

    if v is not None:
        flag_str += f'-v '

    if V is not None:
        flag_str += f'-V {V} '

    if e is not None:
        flag_str += f'-e '

    if D is not None:
        flag_str += f'-D {D} '

    if T is not None:
        flag_str += f'-T {T} '

    if m is not None:
        flag_str += f'-m '

    if R is not None:
        flag_str += f'-R {R} '

    if s is not None:
        flag_str += f'-s {s} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def pol2mask(poly, X=None, Y=None):
    """
    Compute masks from polygons.

    :param poly array:
    :param X int: size dimension 0
    :param Y int: size dimension 1

    """
    usage_string = "pol2mask [-X d] [-Y d] poly output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'pol2mask '
    flag_str = ''

    opt_args = f''

    multituples = []

    if X is not None:
        flag_str += f'-X {X} '

    if Y is not None:
        flag_str += f'-Y {Y} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}poly {NAME}output  "
    cfl.writecfl(NAME + 'poly', poly)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def poly(L, N, a_):
    """
    Evaluate polynomial p(x) = a_1 + a_2 x + a_3 x^2 ... a_(N+1) x^N at x = {0, 1, ... , L - 1} where a_i are floats.

    :param L int:
    :param N int:
    :param a_ tuple:

    """
    usage_string = "poly L N a_1 ... a_N output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'poly '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {L} {N} {' '.join([str(arg) for arg in a_])} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def reconet(kspace, sensitivities, weights, ref_out, train=None, eval=None, apply=None, gpu=None, load=None, batch_size=None, iterations=None, normalize=None, network=None, resnet_block=None, varnet_block=None, unet=None, data_consistency=None, initial_reco=None, shared_weights=None, no_shared_weights=None, shared_lambda=None, no_shared_lambda=None, rss_norm=None, trajectory=None, pattern=None, adjoint=None, psf=None, export=None, mask=None, valid_data=None, train_loss=None, valid_loss=None, train_algo=None, adam=None, iPALM=None, load_memory=None, lowmem=None, test=None, export_graph=None, B=None):
    """
    Trains or appplies a neural network for reconstruction.

    :param kspace array:
    :param sensitivities array:
    :param weights INOUTFILE:
    :param ref_out INOUTFILE:
    :param train bool: train reconet
    :param eval bool: evaluate reconet
    :param apply bool: apply reconet
    :param gpu bool: run on gpu
    :param load array: load weights for continuing training
    :param batch_size long: size of mini batches
    :param iterations long: number of unrolled iterations
    :param normalize bool: normalize data with maximum magnitude of adjoint reconstruction
    :param network SUBOPT: select neural network
    :param resnet_block SUBOPT: configure residual block
    :param varnet_block SUBOPT: configure variational block
    :param unet SUBOPT: configure U-Net block
    :param data_consistency SUBOPT: configure data-consistency method
    :param initial_reco SUBOPT: configure initialization
    :param shared_weights bool: share weights across iterations
    :param no_shared_weights bool: share weights across iterations
    :param shared_lambda bool: share lambda across iterations
    :param no_shared_lambda bool: share lambda across iterations
    :param rss_norm bool: scale output image to rss normalization
    :param trajectory array: trajectory
    :param pattern array: sampling pattern / psf in kspace
    :param adjoint INOUTFILE: (validation data adjoint (load or export))
    :param psf INOUTFILE: (psf (load or export))
    :param export bool: (export psf and adjoint reconstruction)
    :param mask array: mask for computation of loss
    :param valid_data SUBOPT: provide validation data
    :param train_loss SUBOPT: configure the training loss
    :param valid_loss SUBOPT: configure the validation loss
    :param train_algo SUBOPT: configure general training parmeters
    :param adam SUBOPT: configure Adam
    :param iPALM SUBOPT: configure iPALM
    :param load_memory bool: copy training data into memory
    :param lowmem bool: reduce memory usage by checkpointing
    :param test bool: very small network for tests
    :param export_graph STRING: export graph for visualization
    :param B array: (temporal (or other) basis)

    """
    usage_string = "reconet [-t,--train] [-e,--eval] [-a,--apply] [-g,--gpu] [-l,--load file] [-b,--batch-size d] [-I,--iterations d] [-n,--normalize] [-N,--network ...] [--resnet-block ...] [--varnet-block ...] [--unet ...] [--data-consistency ...] [--initial-reco ...] [--shared-weights] [--no-shared-weights] [--shared-lambda] [--no-shared-lambda] [--rss-norm] [--trajectory file] [--pattern file] [--mask file] [--valid-data ...] [--train-loss ...] [--valid-loss ...] [-T,--train-algo ...] [--adam ...] [--iPALM ...] [--load-memory] [--lowmem] [--test] [--export-graph string] kspace sensitivities weights ref/out"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'reconet '
    flag_str = ''

    opt_args = f''

    multituples = []

    if train is not None:
        flag_str += f'--train '

    if eval is not None:
        flag_str += f'--eval '

    if apply is not None:
        flag_str += f'--apply '

    if gpu is not None:
        flag_str += f'--gpu '

    if not isinstance(load, type(None)):
        cfl.writecfl(NAME + 'load', load)
        flag_str += f'--load {NAME}load '

    if batch_size is not None:
        flag_str += f'--batch-size {batch_size} '

    if iterations is not None:
        flag_str += f'--iterations {iterations} '

    if normalize is not None:
        flag_str += f'--normalize '

    if network is not None:
        flag_str += f'--network {network} '

    if resnet_block is not None:
        flag_str += f'--resnet-block {resnet_block} '

    if varnet_block is not None:
        flag_str += f'--varnet-block {varnet_block} '

    if unet is not None:
        flag_str += f'--unet {unet} '

    if data_consistency is not None:
        flag_str += f'--data-consistency {data_consistency} '

    if initial_reco is not None:
        flag_str += f'--initial-reco {initial_reco} '

    if shared_weights is not None:
        flag_str += f'--shared-weights '

    if no_shared_weights is not None:
        flag_str += f'--no-shared-weights '

    if shared_lambda is not None:
        flag_str += f'--shared-lambda '

    if no_shared_lambda is not None:
        flag_str += f'--no-shared-lambda '

    if rss_norm is not None:
        flag_str += f'--rss-norm '

    if not isinstance(trajectory, type(None)):
        cfl.writecfl(NAME + 'trajectory', trajectory)
        flag_str += f'--trajectory {NAME}trajectory '

    if not isinstance(pattern, type(None)):
        cfl.writecfl(NAME + 'pattern', pattern)
        flag_str += f'--pattern {NAME}pattern '

    if adjoint is not None:
        flag_str += f'--adjoint {adjoint} '

    if psf is not None:
        flag_str += f'--psf {psf} '

    if export is not None:
        flag_str += f'--export '

    if not isinstance(mask, type(None)):
        cfl.writecfl(NAME + 'mask', mask)
        flag_str += f'--mask {NAME}mask '

    if valid_data is not None:
        flag_str += f'--valid-data {valid_data} '

    if train_loss is not None:
        flag_str += f'--train-loss {train_loss} '

    if valid_loss is not None:
        flag_str += f'--valid-loss {valid_loss} '

    if train_algo is not None:
        flag_str += f'--train-algo {train_algo} '

    if adam is not None:
        flag_str += f'--adam {adam} '

    if iPALM is not None:
        flag_str += f'--iPALM {iPALM} '

    if load_memory is not None:
        flag_str += f'--load-memory '

    if lowmem is not None:
        flag_str += f'--lowmem '

    if test is not None:
        flag_str += f'--test '

    if export_graph is not None:
        flag_str += f'--export-graph {export_graph} '

    if not isinstance(B, type(None)):
        cfl.writecfl(NAME + 'B', B)
        flag_str += f'-B {NAME}B '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}sensitivities {weights} {ref_out}  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'sensitivities', sensitivities)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def repmat(input, dimension, repetitions):
    """
    Repeat input array multiple times along a certain dimension.

    :param dimension int:
    :param repetitions int:
    :param input array:

    """
    usage_string = "repmat dimension repetitions input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'repmat '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dimension} {repetitions} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def reshape(input, flags, dim):
    """
    Reshape selected dimensions.

    :param flags long:
    :param dim tuple:
    :param input array:

    """
    usage_string = "reshape flags dim1 ... dimN input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'reshape '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {flags} {' '.join([str(arg) for arg in dim])} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def resize(input, dim, size, c=None):
    """
    Resizes an array along dimensions to sizes by truncating or zero-padding. Please see doc/resize.txt for examples.

    :param dim multituple:
    :param size multituple:
    :param input array:
    :param c bool: center

    """
    usage_string = "resize [-c] dim1 size1 ... dimN sizeN input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'resize '
    flag_str = ''

    opt_args = f''

    multituples = []

    if c is not None:
        flag_str += f'-c '
    cmd_str += flag_str + opt_args + '  '

    multituples.append(dim)
    
    multituples.append(size)
    
    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def rmfreq(traj, k, N=None, M=None):
    """
    Remove angle-dependent frequency

    :param traj array:
    :param k array:
    :param N int: Number of harmonics [Default: 5]
    :param M STRING: Contrast modulation file

    """
    usage_string = "rmfreq [-N d] [-M string] traj k k_cor"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'rmfreq '
    flag_str = ''

    opt_args = f''

    multituples = []

    if N is not None:
        flag_str += f'-N {N} '

    if M is not None:
        flag_str += f'-M {M} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}traj {NAME}k {NAME}k_cor  "
    cfl.writecfl(NAME + 'traj', traj)
    cfl.writecfl(NAME + 'k', k)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'k_cor')
    return outputs

def rof(input, llambda, flags):
    """
    Perform total variation denoising along dims <flags>.

    :param llambda float:
    :param flags int:
    :param input array:

    """
    usage_string = "rof lambda flags input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'rof '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {llambda} {flags} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def roistat(roi, input, b=None, C=None, S=None, M=None, D=None, E=None, V=None):
    """
    Compute ROI statistics.

    :param roi array:
    :param input array:
    :param b bool: Bessel's correction i.e. 1 / (n - 1)
    :param C bool: voxel count
    :param S bool: sum
    :param M bool: mean
    :param D bool: standard deviation
    :param E bool: energy
    :param V bool: variance

    """
    usage_string = "roistat [-b] [-C] [-S] [-M] [-D] [-E] [-V] roi input [output]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'roistat '
    flag_str = ''

    opt_args = f''

    multituples = []

    if b is not None:
        flag_str += f'-b '

    if C is not None:
        flag_str += f'-C '

    if S is not None:
        flag_str += f'-S '

    if M is not None:
        flag_str += f'-M '

    if D is not None:
        flag_str += f'-D '

    if E is not None:
        flag_str += f'-E '

    if V is not None:
        flag_str += f'-V '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}roi {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'roi', roi)
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def rss(input, bitmask):
    """
    Calculates root of sum of squares along selected dimensions.

    :param bitmask int:
    :param input array:

    """
    usage_string = "rss bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'rss '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def rtnlinv(kspace, i=None, R=None, M=None, d=None, c=None, N=None, m=None, U=None, f=None, p=None, t=None, I=None, C=None, g=None, S=None, a=None, b=None, T=None, w=None, x=None, A=None, s=None):
    """
    Jointly estimate a time-series of images and sensitivities with nonlinear
inversion using {iter} iteration steps. Optionally outputs
the sensitivities.

    :param kspace array:
    :param i int: Number of Newton steps
    :param R float: (reduction factor)
    :param M float: (minimum for regularization)
    :param d int: Debug level
    :param c bool: Real-value constraint
    :param N bool: Do not normalize image with coil sensitivities
    :param m int: Number of ENLIVE maps to use in reconstruction
    :param U bool: Do not combine ENLIVE maps in output
    :param f float: restrict FOV
    :param p array: pattern / transfer function
    :param t array: kspace trajectory
    :param I array: File for initialization
    :param C array: (File for initialization with image space sensitivities)
    :param g bool: use gpu
    :param S bool: Re-scale image after reconstruction
    :param a float: (a in 1 + a * \Laplace^-b/2)
    :param b float: (b in 1 + a * \Laplace^-b/2)
    :param T float: temporal damping [default: 0.9]
    :param w float: (inverse scaling of the data)
    :param x list: Explicitly specify image dimensions
    :param A bool: (Alternative scaling)
    :param s bool: (Simultaneous Multi-Slice reconstruction)

    """
    usage_string = "rtnlinv [-i d] [-d d] [-c] [-N] [-m d] [-U] [-f f] [-p file] [-t file] [-I file] [-g] [-S] [-T f] [-x d:d:d] kspace output [sensitivities]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'rtnlinv '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i {i} '

    if R is not None:
        flag_str += f'-R {R} '

    if M is not None:
        flag_str += f'-M {M} '

    if d is not None:
        flag_str += f'-d {d} '

    if c is not None:
        flag_str += f'-c '

    if N is not None:
        flag_str += f'-N '

    if m is not None:
        flag_str += f'-m {m} '

    if U is not None:
        flag_str += f'-U '

    if f is not None:
        flag_str += f'-f {f} '

    if not isinstance(p, type(None)):
        cfl.writecfl(NAME + 'p', p)
        flag_str += f'-p {NAME}p '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if not isinstance(I, type(None)):
        cfl.writecfl(NAME + 'I', I)
        flag_str += f'-I {NAME}I '

    if not isinstance(C, type(None)):
        cfl.writecfl(NAME + 'C', C)
        flag_str += f'-C {NAME}C '

    if g is not None:
        flag_str += f'-g '

    if S is not None:
        flag_str += f'-S '

    if a is not None:
        flag_str += f'-a {a} '

    if b is not None:
        flag_str += f'-b {b} '

    if T is not None:
        flag_str += f'-T {T} '

    if w is not None:
        flag_str += f'-w {w} '

    if x is not None:
        flag_str += f'-x {":".join([str(x) for x in x])} '

    if A is not None:
        flag_str += f'-A '

    if s is not None:
        flag_str += f'-s '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}output {NAME}sensitivities  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output'), cfl.readcfl(NAME + 'sensitivities')
    return outputs

def sake(kspace, i=None, s=None, o=None):
    """
    Use SAKE algorithm to recover a full k-space from undersampled
data using low-rank matrix completion.

    :param kspace array:
    :param i int: number of iterations
    :param s float: rel. size of the signal subspace
    :param o float: ()

    """
    usage_string = "ke [-i d] [-s f] kspace output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'sake '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i {i} '

    if s is not None:
        flag_str += f'-s {s} '

    if o is not None:
        flag_str += f'-o {o} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}output  "
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def saxpy(input1, input2, scale):
    """
    Multiply input1 with scale factor and add input2.

    :param scale CFL:
    :param input1 array:
    :param input2 array:

    """
    usage_string = "xpy scale input1 input2 output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'saxpy '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {scale} {NAME}input1 {NAME}input2 {NAME}output  "
    cfl.writecfl(NAME + 'input1', input1)
    cfl.writecfl(NAME + 'input2', input2)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def scale(input, factor):
    """
    Scale array by {factor}. The scale factor can be a complex number.

    :param factor CFL:
    :param input array:

    """
    usage_string = "cale factor input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'scale '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {factor} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def sdot(input1, input2):
    """
    Compute dot product along selected dimensions.

    :param input1 array:
    :param input2 array:

    """
    usage_string = "dot input1 input2"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'sdot '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input1 {NAME}input2  "
    cfl.writecfl(NAME + 'input1', input1)
    cfl.writecfl(NAME + 'input2', input2)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def show(input, m=None, d=None, s=None, f=None):
    """
    Outputs values or meta data.

    :param input array:
    :param m bool: show meta data
    :param d int: show size of dimension
    :param s STRING: use <sep> as the separator
    :param f STRING: use <format> as the format. Default: %%+.6e%%+.6ei

    """
    usage_string = "how [-m] [-d d] [-s string] [-f string] input"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'show '
    flag_str = ''

    opt_args = f''

    multituples = []

    if m is not None:
        flag_str += f'-m '

    if d is not None:
        flag_str += f'-d {d} '

    if s is not None:
        flag_str += f'-s {s} '

    if f is not None:
        flag_str += f'-f {f} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def signal(F=None, B=None, T=None, M=None, G=None, fat=None, I=None, s=None, _0=None, _1=None, _2=None, _3=None, r=None, e=None, f=None, t=None, n=None, b=None, av_spokes=None):
    """
    Analytical simulation tool.

    :param F bool: FLASH
    :param B bool: bSSFP
    :param T bool: TSE
    :param M bool: MOLLI
    :param G bool: MGRE
    :param fat bool: Simulate additional fat component.
    :param I bool: inversion recovery
    :param s bool: inversion recovery starting from steady state
    :param _0 FLOAT_VEC3: range of off-resonance frequency (Hz)
    :param _1 FLOAT_VEC3: range of T1s (s)
    :param _2 FLOAT_VEC3: range of T2s (s)
    :param _3 FLOAT_VEC3: range of Mss
    :param r float: repetition time
    :param e float: echo time
    :param f float: flip ange
    :param t float: T1 relax period (second) for MOLLI
    :param n long: number of measurements
    :param b long: number of heart beats for MOLLI
    :param av_spokes int: Number of averaged consecutive spokes

    """
    usage_string = "ignal [-F] [-B] [-T] [-M] [-G] [--fat] [-I] [-s] [-0 f:f:f] [-1 f:f:f] [-2 f:f:f] [-3 f:f:f] [-r f] [-e f] [-f f] [-t f] [-n d] [-b d] [--av-spokes d] basis-functions"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'signal '
    flag_str = ''

    opt_args = f''

    multituples = []

    if F is not None:
        flag_str += f'-F '

    if B is not None:
        flag_str += f'-B '

    if T is not None:
        flag_str += f'-T '

    if M is not None:
        flag_str += f'-M '

    if G is not None:
        flag_str += f'-G '

    if fat is not None:
        flag_str += f'--fat '

    if I is not None:
        flag_str += f'-I '

    if s is not None:
        flag_str += f'-s '

    if _0 is not None:
        flag_str += f'-0 {_0} '

    if _1 is not None:
        flag_str += f'-1 {_1} '

    if _2 is not None:
        flag_str += f'-2 {_2} '

    if _3 is not None:
        flag_str += f'-3 {_3} '

    if r is not None:
        flag_str += f'-r {r} '

    if e is not None:
        flag_str += f'-e {e} '

    if f is not None:
        flag_str += f'-f {f} '

    if t is not None:
        flag_str += f'-t {t} '

    if n is not None:
        flag_str += f'-n {n} '

    if b is not None:
        flag_str += f'-b {b} '

    if av_spokes is not None:
        flag_str += f'--av-spokes {av_spokes} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}basis_functions  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'basis_functions')
    return outputs

def sim(dB1=None, T1=None, T2=None, ROT=None, ODE=None, STM=None, split_dim=None, seq=None, other=None):
    """
    simulation tool

    :param dB1 dM0: None
    :param T1 FLOAT_VEC3: range of T1 values
    :param T2 FLOAT_VEC3: range of T2 values
    :param ROT bool: homogeneously discretized simulation based on rotational matrices
    :param ODE bool: full ordinary differential equation solver based simulation (default)
    :param STM bool: state-transition matrix based simulation
    :param split_dim bool: Split output in x y and z dimensional parts
    :param seq SUBOPT: configure sequence parameter
    :param other SUBOPT: configure other parameters

    """
    usage_string = "im [-1,--T1 f:f:f] [-2,--T2 f:f:f] [--ROT] [--ODE] [--STM] [--split-dim] [--seq ...] [--other ...] signal: Mxy [Partial derivatives: dR1, dM0, dR2, dB1]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'sim '
    flag_str = ''

    opt_args = f''

    multituples = []

    if dB1 != None:
            opt_args += '{dB1}'

    if T1 is not None:
        flag_str += f'--T1 {T1} '

    if T2 is not None:
        flag_str += f'--T2 {T2} '

    if ROT is not None:
        flag_str += f'--ROT '

    if ODE is not None:
        flag_str += f'--ODE '

    if STM is not None:
        flag_str += f'--STM '

    if split_dim is not None:
        flag_str += f'--split-dim '

    if seq is not None:
        flag_str += f'--seq {seq} '

    if other is not None:
        flag_str += f'--other {other} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}signal__Mxy  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'signal__Mxy')
    return outputs

def slice(input, dim, pos):
    """
    Extracts a slice from positions along dimensions.

    :param dim multituple:
    :param pos multituple:
    :param input array:

    """
    usage_string = "lice dim1 pos1 ... dimN posN input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'slice '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    multituples.append(dim)
    
    multituples.append(pos)
    
    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def spow(input, exponent):
    """
    Raise array to the power of {exponent}. The exponent can be a complex number.

    :param exponent CFL:
    :param input array:

    """
    usage_string = "pow exponent input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'spow '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {exponent} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def sqpics(kspace, sensitivities, l=None, r=None, R=None, s=None, i=None, t=None, n=None, g=None, p=None, I=None, b=None, e=None, H=None, F=None, T=None, W=None, d=None, u=None, C=None, f=None, m=None, w=None, S=None):
    """
    Parallel-imaging compressed-sensing reconstruction.

    :param kspace array:
    :param sensitivities array:
    :param l SPECIAL: toggle l1-wavelet or l2 regularization.
    :param r float: regularization parameter
    :param R SPECIAL: generalized regularization options (-Rh for help)
    :param s float: iteration stepsize
    :param i int: max. number of iterations
    :param t array: k-space trajectory
    :param n bool: disable random wavelet cycle spinning
    :param g bool: use GPU
    :param p array: pattern or weights
    :param I bool: (select IST)
    :param b int: Lowrank block size
    :param e bool: Scale stepsize based on max. eigenvalue
    :param H bool: (hogwild)
    :param F bool: (fast)
    :param T array: (truth file)
    :param W array: Warm start with <img>
    :param d int: Debug level
    :param u float: ADMM rho
    :param C int: ADMM max. CG iterations
    :param f float: restrict FOV
    :param m bool: Select ADMM
    :param w float: scaling
    :param S bool: Re-scale the image after reconstruction

    """
    usage_string = "qpics [-l ...] [-r f] [-R ...] [-s f] [-i d] [-t file] [-n] [-g] [-p file] [-b d] [-e] [-W file] [-d d] [-u f] [-C d] [-f f] [-m] [-w f] [-S] kspace sensitivities output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'sqpics '
    flag_str = ''

    opt_args = f''

    multituples = []

    if l is not None:
        flag_str += f'-l {l} '

    if r is not None:
        flag_str += f'-r {r} '

    if R is not None:
        flag_str += f'-R {R} '

    if s is not None:
        flag_str += f'-s {s} '

    if i is not None:
        flag_str += f'-i {i} '

    if not isinstance(t, type(None)):
        cfl.writecfl(NAME + 't', t)
        flag_str += f'-t {NAME}t '

    if n is not None:
        flag_str += f'-n '

    if g is not None:
        flag_str += f'-g '

    if not isinstance(p, type(None)):
        cfl.writecfl(NAME + 'p', p)
        flag_str += f'-p {NAME}p '

    if I is not None:
        flag_str += f'-I '

    if b is not None:
        flag_str += f'-b {b} '

    if e is not None:
        flag_str += f'-e '

    if H is not None:
        flag_str += f'-H '

    if F is not None:
        flag_str += f'-F '

    if not isinstance(T, type(None)):
        cfl.writecfl(NAME + 'T', T)
        flag_str += f'-T {NAME}T '

    if not isinstance(W, type(None)):
        cfl.writecfl(NAME + 'W', W)
        flag_str += f'-W {NAME}W '

    if d is not None:
        flag_str += f'-d {d} '

    if u is not None:
        flag_str += f'-u {u} '

    if C is not None:
        flag_str += f'-C {C} '

    if f is not None:
        flag_str += f'-f {f} '

    if m is not None:
        flag_str += f'-m '

    if w is not None:
        flag_str += f'-w {w} '

    if S is not None:
        flag_str += f'-S '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}kspace {NAME}sensitivities {NAME}output  "
    cfl.writecfl(NAME + 'kspace', kspace)
    cfl.writecfl(NAME + 'sensitivities', sensitivities)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def squeeze(input):
    """
    Remove singleton dimensions of array.

    :param input array:

    """
    usage_string = "queeze input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'squeeze '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def ssa(src, w=None, z=None, m=None, n=None, r=None, g=None):
    """
    Perform SSA-FARY or Singular Spectrum Analysis. <src>: [samples, coordinates]

    :param src array:
    :param w int: Window length
    :param z bool: Zeropadding [Default: True]
    :param m int: Remove mean [Default: True]
    :param n int: Normalize [Default: False]
    :param r int: Rank for backprojection. r < 0: Throw away first r components. r > 0: Use only first r components.
    :param g long: Bitmask for Grouping (long value!)

    """
    usage_string = "[-w d] [-z] [-m d] [-n d] [-r d] [-g d] src EOF [S] [backprojection]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'ssa '
    flag_str = ''

    opt_args = f''

    multituples = []

    if w is not None:
        flag_str += f'-w {w} '

    if z is not None:
        flag_str += f'-z '

    if m is not None:
        flag_str += f'-m {m} '

    if n is not None:
        flag_str += f'-n {n} '

    if r is not None:
        flag_str += f'-r {r} '

    if g is not None:
        flag_str += f'-g {g} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}src {NAME}EOF {NAME}S {NAME}backprojection  "
    cfl.writecfl(NAME + 'src', src)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'EOF'), cfl.readcfl(NAME + 'S'), cfl.readcfl(NAME + 'backprojection')
    return outputs

def std(input, bitmask):
    """
    Compute standard deviation along selected dimensions specified by the {bitmask}

    :param bitmask long:
    :param input array:

    """
    usage_string = "td bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'std '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def svd(input, e=None):
    """
    Compute singular-value-decomposition (SVD).

    :param input array:
    :param e bool: econ

    """
    usage_string = "vd [-e] input U S VH"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'svd '
    flag_str = ''

    opt_args = f''

    multituples = []

    if e is not None:
        flag_str += f'-e '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}U {NAME}S {NAME}VH  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'U'), cfl.readcfl(NAME + 'S'), cfl.readcfl(NAME + 'VH')
    return outputs

def tgv(input, llambda, flags):
    """
    Perform total generalized variation denoising along dims specified by flags.

    :param llambda float:
    :param flags int:
    :param input array:

    """
    usage_string = "tgv lambda flags input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'tgv '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {llambda} {flags} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def threshold(input, llambda, H=None, W=None, L=None, D=None, B=None, j=None, b=None):
    """
    Perform (soft) thresholding with parameter lambda.

    :param llambda float:
    :param input array:
    :param H bool: hard thresholding
    :param W bool: daubechies wavelet soft-thresholding
    :param L bool: locally low rank soft-thresholding
    :param D bool: divergence-free wavelet soft-thresholding
    :param B bool: thresholding with binary output
    :param j int: joint soft-thresholding
    :param b int: locally low rank block size

    """
    usage_string = "threshold [-H] [-W] [-L] [-D] [-B] [-j d] [-b d] lambda input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'threshold '
    flag_str = ''

    opt_args = f''

    multituples = []

    if H is not None:
        flag_str += f'-H '

    if W is not None:
        flag_str += f'-W '

    if L is not None:
        flag_str += f'-L '

    if D is not None:
        flag_str += f'-D '

    if B is not None:
        flag_str += f'-B '

    if j is not None:
        flag_str += f'-j {j} '

    if b is not None:
        flag_str += f'-b {b} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {llambda} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def toimg(input, g=None, c=None, w=None, d=None, m=None, W=None):
    """
    Create magnitude images as png or proto-dicom.
The first two non-singleton dimensions will
be used for the image, and the other dimensions
will be looped over.

    :param input array:
    :param g float: gamma level
    :param c float: contrast level
    :param w float: window level
    :param d bool: write to dicom format (deprecated use extension .dcm)
    :param m bool: re-scale each image
    :param W bool: use dynamic windowing

    """
    usage_string = "toimg [-g f] [-c f] [-w f] [-d] [-m] [-W] input output prefix"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'toimg '
    flag_str = ''

    opt_args = f''

    multituples = []

    if g is not None:
        flag_str += f'-g {g} '

    if c is not None:
        flag_str += f'-c {c} '

    if w is not None:
        flag_str += f'-w {w} '

    if d is not None:
        flag_str += f'-d '

    if m is not None:
        flag_str += f'-m '

    if W is not None:
        flag_str += f'-W '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output_prefix  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output_prefix')
    return outputs

def traj(x=None, y=None, d=None, e=None, a=None, t=None, m=None, l=None, g=None, r=None, G=None, H=None, s=None, D=None, o=None, R=None, q=None, Q=None, O=None, _3=None, c=None, E=None, z=None, C=None, V=None):
    """
    Computes k-space trajectories.

    :param x int: readout samples
    :param y int: phase encoding lines
    :param d int: full readout samples
    :param e int: number of echoes
    :param a int: acceleration
    :param t int: turns
    :param m int: SMS multiband factor
    :param l bool: aligned partition angle
    :param g bool: golden angle in partition direction
    :param r bool: radial
    :param G bool: golden-ratio sampling
    :param H bool: halfCircle golden-ratio sampling
    :param s int: tiny golden angle
    :param D bool: projection angle in [0 360°) else in [0 180°)
    :param o float: oversampling factor
    :param R float: rotate
    :param q FLOAT_VEC3: gradient delays: x y xy
    :param Q FLOAT_VEC3: (gradient delays: z xz yz)
    :param O bool: correct transverse gradient error for radial tajectories
    :param _3 bool: 3D
    :param c bool: asymmetric trajectory [DC sampled]
    :param E bool: multi-echo multi-spoke trajectory
    :param z VEC2: Undersampling in z-direction.
    :param C array: custom_angle file [phi + i * psi]
    :param V array: (custom_gdelays)

    """
    usage_string = "traj [-x d] [-y d] [-d d] [-e d] [-a d] [-t d] [-m d] [-l] [-g] [-r] [-G] [-H] [-s d] [-D] [-o f] [-R f] [-q f:f:f] [-O] [-3] [-c] [-E] [-z d:d] [-C file] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'traj '
    flag_str = ''

    opt_args = f''

    multituples = []

    if x is not None:
        flag_str += f'-x {x} '

    if y is not None:
        flag_str += f'-y {y} '

    if d is not None:
        flag_str += f'-d {d} '

    if e is not None:
        flag_str += f'-e {e} '

    if a is not None:
        flag_str += f'-a {a} '

    if t is not None:
        flag_str += f'-t {t} '

    if m is not None:
        flag_str += f'-m {m} '

    if l is not None:
        flag_str += f'-l '

    if g is not None:
        flag_str += f'-g '

    if r is not None:
        flag_str += f'-r '

    if G is not None:
        flag_str += f'-G '

    if H is not None:
        flag_str += f'-H '

    if s is not None:
        flag_str += f'-s {s} '

    if D is not None:
        flag_str += f'-D '

    if o is not None:
        flag_str += f'-o {o} '

    if R is not None:
        flag_str += f'-R {R} '

    if q is not None:
        flag_str += f'-q {q} '

    if Q is not None:
        flag_str += f'-Q {Q} '

    if O is not None:
        flag_str += f'-O '

    if _3 is not None:
        flag_str += f'-3 '

    if c is not None:
        flag_str += f'-c '

    if E is not None:
        flag_str += f'-E '

    if z is not None:
        flag_str += f'-z {z} '

    if not isinstance(C, type(None)):
        cfl.writecfl(NAME + 'C', C)
        flag_str += f'-C {NAME}C '

    if not isinstance(V, type(None)):
        cfl.writecfl(NAME + 'V', V)
        flag_str += f'-V {NAME}V '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def transpose(input, dim1, dim2):
    """
    Transpose dimensions {dim1} and {dim2}.

    :param dim1 int:
    :param dim2 int:
    :param input array:

    """
    usage_string = "transpose dim1 dim2 input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'transpose '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dim1} {dim2} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def twixread(dat_file, x=None, r=None, y=None, z=None, s=None, v=None, c=None, n=None, a=None, A=None, L=None, P=None, M=None, d=None):
    """
    Read data from Siemens twix (.dat) files.

    :param dat_file array:
    :param x long: number of samples (read-out)
    :param r long: radial lines
    :param y long: phase encoding steps
    :param z long: partition encoding steps
    :param s long: number of slices
    :param v long: number of averages
    :param c long: number of channels
    :param n long: number of repetitions
    :param a long: total number of ADCs
    :param A bool: automatic [guess dimensions]
    :param L bool: use linectr offset
    :param P bool: use partctr offset
    :param M bool: MPI mode
    :param d int: Debug level

    """
    usage_string = "twixread [-x d] [-r d] [-y d] [-z d] [-s d] [-v d] [-c d] [-n d] [-a d] [-A] [-L] [-P] [-M] [-d d] dat file output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'twixread '
    flag_str = ''

    opt_args = f''

    multituples = []

    if x is not None:
        flag_str += f'-x {x} '

    if r is not None:
        flag_str += f'-r {r} '

    if y is not None:
        flag_str += f'-y {y} '

    if z is not None:
        flag_str += f'-z {z} '

    if s is not None:
        flag_str += f'-s {s} '

    if v is not None:
        flag_str += f'-v {v} '

    if c is not None:
        flag_str += f'-c {c} '

    if n is not None:
        flag_str += f'-n {n} '

    if a is not None:
        flag_str += f'-a {a} '

    if A is not None:
        flag_str += f'-A '

    if L is not None:
        flag_str += f'-L '

    if P is not None:
        flag_str += f'-P '

    if M is not None:
        flag_str += f'-M '

    if d is not None:
        flag_str += f'-d {d} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}dat_file {NAME}output  "
    cfl.writecfl(NAME + 'dat_file', dat_file)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def upat(Y=None, Z=None, y=None, z=None, c=None):
    """
    Create a sampling pattern.

    :param Y long: size Y
    :param Z long: size Z
    :param y int: undersampling y
    :param z int: undersampling z
    :param c int: size of k-space center

    """
    usage_string = "upat [-Y d] [-Z d] [-y d] [-z d] [-c d] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'upat '
    flag_str = ''

    opt_args = f''

    multituples = []

    if Y is not None:
        flag_str += f'-Y {Y} '

    if Z is not None:
        flag_str += f'-Z {Z} '

    if y is not None:
        flag_str += f'-y {y} '

    if z is not None:
        flag_str += f'-z {z} '

    if c is not None:
        flag_str += f'-c {c} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def var(input, bitmask):
    """
    Compute variance along selected dimensions specified by the {bitmask}

    :param bitmask long:
    :param input array:

    """
    usage_string = "var bitmask input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'var '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def vec(val):
    """
    Create a vector of values.

    :param val tuple:

    """
    usage_string = "vec val1 ... valN output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'vec '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {' '.join([str(arg) for arg in val])} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def version(t=None, V=None):
    """
    Print BART version. The version string is of the form
TAG or TAG-COMMITS-SHA as produced by 'git describe'. It
specifies the last release (TAG), and (if git is used)
the number of commits (COMMITS) since this release and
the abbreviated hash of the last commit (SHA). If there
are local changes '-dirty' is added at the end.

    :param t STRING: Check minimum version
    :param V bool: Output verbose info

    """
    usage_string = "version [-t string] [-V]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'version '
    flag_str = ''

    opt_args = f''

    multituples = []

    if t is not None:
        flag_str += f'-t {t} '

    if V is not None:
        flag_str += f'-V '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()}  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

def walsh(input, r=None, R=None, b=None, B=None):
    """
    Estimate coil sensitivities using walsh method (use with ecaltwo).

    :param input array:
    :param r list: Limits the size of the calibration region.
    :param R list: ()
    :param b list: Block size.
    :param B list: ()

    """
    usage_string = "walsh [-r d:d:d] [-b d:d:d] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'walsh '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r {":".join([str(x) for x in r])} '

    if R is not None:
        flag_str += f'-R {":".join([str(x) for x in R])} '

    if b is not None:
        flag_str += f'-b {":".join([str(x) for x in b])} '

    if B is not None:
        flag_str += f'-B {":".join([str(x) for x in B])} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def wave(maps, wave, kspace, r=None, b=None, i=None, s=None, c=None, t=None, e=None, g=None, f=None, H=None, v=None, w=None, l=None):
    """
    Perform a wave-caipi reconstruction.

Conventions:
  * (sx, sy, sz) - Spatial dimensions.
  * wx           - Extended FOV in READ_DIM due to
                   wave's voxel spreading.
  * (nc, md)     - Number of channels and ESPIRiT's 
                   extended-SENSE model operator
                   dimensions (or # of maps).
Expected dimensions:
  * maps    - ( sx, sy, sz, nc, md)
  * wave    - ( wx, sy, sz,  1,  1)
  * kspace  - ( wx, sy, sz, nc,  1)
  * output  - ( sx, sy, sz,  1, md)

    :param maps array:
    :param wave array:
    :param kspace array:
    :param r float: Soft threshold lambda for wavelet or locally low rank.
    :param b int: Block size for locally low rank.
    :param i int: Maximum number of iterations.
    :param s float: Step size for iterative method.
    :param c float: Continuation value for IST/FISTA.
    :param t float: Tolerance convergence condition for iterative method.
    :param e float: Maximum eigenvalue of normal operator if known.
    :param g bool: use GPU
    :param f bool: Reconstruct using FISTA instead of IST.
    :param H bool: Use hogwild in IST/FISTA.
    :param v bool: Split result to real and imaginary components.
    :param w bool: Use wavelet.
    :param l bool: Use locally low rank across the real and imaginary components.

    """
    usage_string = "wave [-r f] [-b d] [-i d] [-s f] [-c f] [-t f] [-e f] [-g] [-f] [-H] [-v] [-w] [-l] maps wave kspace output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'wave '
    flag_str = ''

    opt_args = f''

    multituples = []

    if r is not None:
        flag_str += f'-r {r} '

    if b is not None:
        flag_str += f'-b {b} '

    if i is not None:
        flag_str += f'-i {i} '

    if s is not None:
        flag_str += f'-s {s} '

    if c is not None:
        flag_str += f'-c {c} '

    if t is not None:
        flag_str += f'-t {t} '

    if e is not None:
        flag_str += f'-e {e} '

    if g is not None:
        flag_str += f'-g '

    if f is not None:
        flag_str += f'-f '

    if H is not None:
        flag_str += f'-H '

    if v is not None:
        flag_str += f'-v '

    if w is not None:
        flag_str += f'-w '

    if l is not None:
        flag_str += f'-l '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}maps {NAME}wave {NAME}kspace {NAME}output  "
    cfl.writecfl(NAME + 'maps', maps)
    cfl.writecfl(NAME + 'wave', wave)
    cfl.writecfl(NAME + 'kspace', kspace)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def wavelet(input, bitmask, dim=None, a=None, H=None, D=None, C=None):
    """
    Perform wavelet transform.

    :param bitmask int:
    :param input array:
    :param dim tuple: None
    :param a bool: adjoint (specify dims)
    :param H bool: type: Haar
    :param D bool: type: Dau2
    :param C bool: type: CDF44

    """
    usage_string = "wavelet [-a] [-H] [-D] [-C] bitmask [dim1 ... dimN ] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'wavelet '
    flag_str = ''

    opt_args = f''

    multituples = []

    if dim != None:
        opt_args += f"{' '.join([str(arg) for arg in dim])} "

    if a is not None:
        flag_str += f'-a '

    if H is not None:
        flag_str += f'-H '

    if D is not None:
        flag_str += f'-D '

    if C is not None:
        flag_str += f'-C '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {bitmask} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def wavepsf(c=None, x=None, y=None, r=None, a=None, t=None, g=None, s=None, n=None):
    """
    Generate a wave PSF in hybrid space.
- Assumes the first dimension is the readout dimension.
- Only generates a 2 dimensional PSF.
- Use reshape and fmac to generate a 3D PSF.

3D PSF Example:
bart wavepsf        -x 768 -y 128 -r 0.1 -a 3000 -t 0.00001 -g 0.8 -s 17000 -n 6 wY
bart wavepsf -c -x 768 -y 128 -r 0.1 -a 3000 -t 0.00001 -g 0.8 -s 17000 -n 6 wZ
bart reshape 7 wZ 768 1 128 wZ wZ
bart fmac wY wZ wYZ

    :param c bool: Set to use a cosine gradient wave
    :param x int: Number of readout points
    :param y int: Number of phase encode points
    :param r float: Resolution of phase encode in cm
    :param a int: Readout duration in microseconds.
    :param t float: ADC sampling rate in seconds
    :param g float: Maximum gradient amplitude in Gauss/cm
    :param s float: Maximum gradient slew rate in Gauss/cm/second
    :param n int: Number of cycles in the gradient wave

    """
    usage_string = "wavepsf [-c] [-x d] [-y d] [-r f] [-a d] [-t f] [-g f] [-s f] [-n d] output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'wavepsf '
    flag_str = ''

    opt_args = f''

    multituples = []

    if c is not None:
        flag_str += f'-c '

    if x is not None:
        flag_str += f'-x {x} '

    if y is not None:
        flag_str += f'-y {y} '

    if r is not None:
        flag_str += f'-r {r} '

    if a is not None:
        flag_str += f'-a {a} '

    if t is not None:
        flag_str += f'-t {t} '

    if g is not None:
        flag_str += f'-g {g} '

    if s is not None:
        flag_str += f'-s {s} '

    if n is not None:
        flag_str += f'-n {n} '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def whiten(input, ndata, o=None, c=None, n=None):
    """
    Apply multi-channel noise pre-whitening on <input> using noise data <ndata>.
Optionally output whitening matrix and noise covariance matrix

    :param input array:
    :param ndata array:
    :param o array: use external whitening matrix <optmat_in>
    :param c array: use external noise covariance matrix <covar_in>
    :param n bool: normalize variance to 1 using noise data <ndata>

    """
    usage_string = "whiten [-o file] [-c file] [-n] input ndata output [optmat_out] [covar_out]"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'whiten '
    flag_str = ''

    opt_args = f''

    multituples = []

    if not isinstance(o, type(None)):
        cfl.writecfl(NAME + 'o', o)
        flag_str += f'-o {NAME}o '

    if not isinstance(c, type(None)):
        cfl.writecfl(NAME + 'c', c)
        flag_str += f'-c {NAME}c '

    if n is not None:
        flag_str += f'-n '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}ndata {NAME}output {NAME}optmat_out {NAME}covar_out  "
    cfl.writecfl(NAME + 'input', input)
    cfl.writecfl(NAME + 'ndata', ndata)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output'), cfl.readcfl(NAME + 'optmat_out'), cfl.readcfl(NAME + 'covar_out')
    return outputs

def window(input, flags, H=None):
    """
    Apply Hamming (Hann) window to <input> along dimensions specified by flags

    :param flags long:
    :param input array:
    :param H bool: Hann window

    """
    usage_string = "window [-H] flags input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'window '
    flag_str = ''

    opt_args = f''

    multituples = []

    if H is not None:
        flag_str += f'-H '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {flags} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def wshfl(maps, wave, phi, reorder, table, R=None, b=None, i=None, j=None, s=None, e=None, F=None, O=None, t=None, g=None, K=None, H=None, v=None):
    """
    Perform a wave-shuffling reconstruction.

Conventions:
  * (sx, sy, sz) - Spatial dimensions.
  * wx           - Extended FOV in READ_DIM due to
                   wave's voxel spreading.
  * (nc, md)     - Number of channels and ESPIRiT's 
                   extended-SENSE model operator
                   dimensions (or # of maps).
  * (tf, tk)     - Turbo-factor and the rank
                   of the temporal basis used in
                   shuffling.
  * ntr          - Number of TRs, or the number of
                   (ky, kz) points acquired of one
                   echo image.
  * n            - Total number of (ky, kz) points
                   acquired. This is equal to the
                   product of ntr and tf.

Descriptions:
  * reorder is an (n by 3) index matrix such that
    [ky, kz, t] = reorder(i, :) represents the
    (ky, kz) kspace position of the readout line
    acquired at echo number (t), and 0 <= ky < sy,
    0 <= kz < sz, 0 <= t < tf).
  * table is a (wx by nc by n) matrix such that
    table(:, :, k) represents the kth multichannel
    kspace line.

Expected dimensions:
  * maps    - (   sx, sy, sz, nc, md,  1,  1)
  * wave    - (   wx, sy, sz,  1,  1,  1,  1)
  * phi     - (    1,  1,  1,  1,  1, tf, tk)
  * output  - (   sx, sy, sz,  1, md,  1, tk)
  * reorder - (    n,  3,  1,  1,  1,  1,  1)
  * table   - (   wx, nc,  n,  1,  1,  1,  1)

    :param maps array:
    :param wave array:
    :param phi array:
    :param reorder array:
    :param table array:
    :param R SPECIAL: Generalized regularization options. (-Rh for help)
    :param b int: Block size for locally low rank.
    :param i int: Maximum number of iterations.
    :param j int: Maximum number of CG iterations in ADMM.
    :param s float: ADMM Rho value.
    :param e float: Eigenvalue to scale step size. (Optional.)
    :param F array: Go from shfl-coeffs to data-table. Pass in coeffs path.
    :param O array: Initialize reconstruction with guess.
    :param t float: Tolerance convergence condition for FISTA.
    :param g bool: Use GPU.
    :param K bool: Go from data-table to shuffling basis k-space.
    :param H bool: Use hogwild.
    :param v bool: Split coefficients to real and imaginary components.

    """
    usage_string = "wshfl [-R ...] [-b d] [-i d] [-j d] [-s f] [-e f] [-F file] [-O file] [-t f] [-g] [-K] [-H] [-v] maps wave phi reorder table output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'wshfl '
    flag_str = ''

    opt_args = f''

    multituples = []

    if R is not None:
        flag_str += f'-R {R} '

    if b is not None:
        flag_str += f'-b {b} '

    if i is not None:
        flag_str += f'-i {i} '

    if j is not None:
        flag_str += f'-j {j} '

    if s is not None:
        flag_str += f'-s {s} '

    if e is not None:
        flag_str += f'-e {e} '

    if not isinstance(F, type(None)):
        cfl.writecfl(NAME + 'F', F)
        flag_str += f'-F {NAME}F '

    if not isinstance(O, type(None)):
        cfl.writecfl(NAME + 'O', O)
        flag_str += f'-O {NAME}O '

    if t is not None:
        flag_str += f'-t {t} '

    if g is not None:
        flag_str += f'-g '

    if K is not None:
        flag_str += f'-K '

    if H is not None:
        flag_str += f'-H '

    if v is not None:
        flag_str += f'-v '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}maps {NAME}wave {NAME}phi {NAME}reorder {NAME}table {NAME}output  "
    cfl.writecfl(NAME + 'maps', maps)
    cfl.writecfl(NAME + 'wave', wave)
    cfl.writecfl(NAME + 'phi', phi)
    cfl.writecfl(NAME + 'reorder', reorder)
    cfl.writecfl(NAME + 'table', table)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def zeros(dims, dim):
    """
    Create a zero-filled array with {dims} dimensions of size {dim1} to {dimn}.

    :param dims long:
    :param dim tuple:

    """
    usage_string = "zeros dims dim1 ... dimN output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'zeros '
    flag_str = ''

    opt_args = f''

    multituples = []
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {dims} {' '.join([str(arg) for arg in dim])} {NAME}output  "

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

def zexp(input, i=None):
    """
    Point-wise complex exponential.

    :param input array:
    :param i bool: imaginary

    """
    usage_string = "zexp [-i] input output"

    cmd_str = f'{BART_PATH} '
    cmd_str += 'zexp '
    flag_str = ''

    opt_args = f''

    multituples = []

    if i is not None:
        flag_str += f'-i '
    cmd_str += flag_str + opt_args + '  '

    cmd_str += f"{' '.join([' '.join([str(x) for x in arg]) for arg in zip(*multituples)]).strip()} {NAME}input {NAME}output  "
    cfl.writecfl(NAME + 'input', input)

    if DEBUG:
        print(cmd_str)


    os.system(cmd_str)

    outputs = cfl.readcfl(NAME + 'output')
    return outputs

