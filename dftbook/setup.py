import subprocess

def setup_colab():
    '''Setup a colab environment.
    Installs quantum-espresso, ase, the QE python wrapper,
    '''
    subprocess.run(['apt-get', 'install', 'quantum-espresso'])
    subprocess.run(['pip', 'install', 'ase'])
    subprocess.run(['pip', 'install', '--upgrade', 'git+git://github.com/ulissigroup/ase-espresso'])

    subprocess.run(['mkdir', 'gbrv_pseudopotentials'])
    subprocess.run(['wget', '-P', './gbrv_pseudopotentials/', 'https://www.physics.rutgers.edu/gbrv/all_pbe_UPF_v1.5.tar.gz'])
    subprocess.run(['tar', 'xf', 'gbrv_pseudopotentials/all_pbe_UPF_v1.5.tar.gz', '-C', './gbrv_pseudopotentials/'])

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
    os.environ['ESP_PSP_PATH'] = '/content/gbrv_pseudopotentials/'

    print('Setup is complete. Please visit https://drive.google.com/drive/folders/1fVOol26JssnCRXv_3EVgsbk3Z5jd60Nl to find the tutorials.')

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
