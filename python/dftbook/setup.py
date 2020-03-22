import subprocess

def setup_colab():
    '''Setup a colab environment.
    Installs quantum-espresso, ase, the QE python wrapper,
    '''
    print('Please be patient. This takes about 30 seconds.')
    print('Installing quantum espresso')
    subprocess.run(['apt-get', 'install', 'quantum-espresso'])

    print('Installing ASE')
    subprocess.run(['pip', 'install', 'ase'])

    print('Installing ase-espresso')
    subprocess.run(['pip', 'install', '--upgrade', 'git+git://github.com/ulissigroup/ase-espresso'])

    print('Installing pseudopotentials')
    subprocess.run(['mkdir', 'gbrv_pseudopotentials'])
    subprocess.run(['wget', '-P', './gbrv_pseudopotentials/', 'https://www.physics.rutgers.edu/gbrv/all_pbe_UPF_v1.5.tar.gz'])
    subprocess.run(['tar', 'xf', 'gbrv_pseudopotentials/all_pbe_UPF_v1.5.tar.gz', '-C', './gbrv_pseudopotentials/'])

    print('Renaming pseudopotentials')
    #Rename the GBRV pseudopotentials to Cu.UPF etc
    import glob
    import shutil
    import os
    ppfiles = glob.glob('gbrv_pseudopotentials/*_*.UPF')
    for ppfile in ppfiles:
        dir_name = os.path.dirname(ppfile)
        old_name = os.path.basename(ppfile)
        new_name = old_name.split('_')[0].capitalize() + '.UPF'

        shutil.move(ppfile, os.path.join(dir_name, new_name))

    #Tell ase-espresso where to get the pseudopotentials
    print('Almost there, setting environment pseudopotential path')
    os.environ['ESP_PSP_PATH'] = '/content/gbrv_pseudopotentials/'

    print('Setup is complete. Please visit https://github.com/jkitchin/dft-book-espresso to find the tutorials.')

    # import webbrowser
    #  webbrowser.open('https://drive.google.com/drive/folders/1fVOol26JssnCRXv_3EVgsbk3Z5jd60Nl')


def setup_ubuntu():
    '''Setup an Ubuntu environment.
    I have nowhere to test this.
    I assume you can just add "sudo" to the beginning of each command above.
    Alternatively, we can make it a script in the package that you just run at the command line.
    This probably needs some logic to not install every time it is run if not needed.
    Maybe also
    '''
    raise NotImplementedError('This is not supported yet. Can you help?')


def setup_nersc():
    '''Good idea?'''
    raise NotImplementedError('This is not supported yet. Can you help?')
