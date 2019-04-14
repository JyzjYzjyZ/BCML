import argparse
import configparser
import os
import glob

from bcml import install, uninstall, update, export, reorder

def main():
    datadir = os.path.join(os.getenv('LOCALAPPDATA'), 'bcml')
    os.makedirs(datadir, exist_ok=True)

    cemudir = ''
    cdirfile = os.path.join(datadir,'.cdir')
    if not os.path.exists(cdirfile):
        while not os.path.exists(os.path.join(cemudir, 'Cemu.exe')):
            cemudir = input('For first time use, please specify the folder where Cemu is installed:\n> ')
        with open(cdirfile, 'w') as cdir:
            cdir.write(os.path.abspath(cemudir))
    else:
        with open(cdirfile, 'r') as cdir:
            cemudir = cdir.readline()

    parser : argparse.ArgumentParser = argparse.ArgumentParser(prog='bcml')
    parser.add_argument('-d', '--directory', help = 'Specify path to Cemu graphicPacks folder, if different from saved', default = os.path.join(cemudir, 'graphicPacks'), type = str)
    parser.add_argument('-v', '--verbose', help = 'Verbose output covering every file processed', action='store_true')
    subparsers = parser.add_subparsers(dest='command', help='Command for BCML to perform')
    subparsers.required = False

    p_install = subparsers.add_parser('install')
    p_install.add_argument('mod', help = 'Path to a ZIP or RAR archive containing a BOTW mod in Cemu 1.15+ format')
    p_install.add_argument('-p', '--priority', help = 'Mod load priority, default 100', default = '100', type = int)
    p_install.add_argument('--nomerge', help = 'Do not automatically merge pack files', action = 'store_true')
    p_install.add_argument('-s', '--shrink', help = 'Update RSTB entries for files which haven\'t grown', action="store_true")
    p_install.add_argument('-l', '--leave', help = 'Do not remove RSTB entries for file sizes which cannot be calculated', action="store_true")

    p_uninstall = subparsers.add_parser('uninstall', description = 'Uninstaller for BCML-managed mods')

    p_reorder = subparsers.add_parser('reorder', description = 'Change priority for BCML-managed mod')

    p_update = subparsers.add_parser('update', description = 'Refreshes RSTB and merged packs for BCML-managed mods')
    p_update.add_argument('--nomerge', 'Skip updating merged packs', action='store_true')

    p_export = subparsers.add_parser('export')
    p_export.add_argument('output', help = 'Path to the mod ZIP that BCML should create')
    p_export.add_argument('-o', '--onlymerges', help = 'Only include the merged RSTB and packs, not all installed content', action = 'store_true')
    formats = p_export.add_mutually_exclusive_group()
    formats.add_argument('-s', '--sdcafiine', help = 'Export in SDCafiine format instead of graphicPack', action = 'store_true')
    formats.add_argument('-m', '--mlc', help = 'Export in the MLC content format instead of graphicPack', action = 'store_true')
    p_export.add_argument('-t', '--title', help = 'The TitleID to use for SDCafiine or mlc export, default 00050000101C9400 (US version)', default = '00050000101C9400', type = str)

    args = parser.parse_args()

    print('##############################################')
    print('##    Breath of the Wild Cemu Mod Loader    ##')
    print('##             Version 0.993                ##')
    print('##------------------------------------------##')
    print('##     (c) 2019 Nicene Nerd - GPLv3+        ##')
    print('## 7za.exe (c) 2019 Ignor Pavolv - LGPLv3+  ##')
    print('##############################################')
    print()

    if args.command == 'install':
        args.mod = os.path.abspath(args.mod)
        install.main(args)
        os._exit(0)
    elif args.command == 'uninstall':
        uninstall.main(args)
        os._exit(0)
    elif args.command == 'export':
        args.output = os.path.abspath(args.output)
        export.main(args)
        os._exit(0)
    elif args.command == 'update':
        update.main(args)
        os._exit(0)
    elif args.command == 'reorder':
        reorder.main(args)
        os._exit(0)
    else:
        mods = {}
        print('No command given, listing mods currently installed:')
        print()
        for i, rulef in enumerate(glob.iglob(os.path.join(args.directory, 'BotwMod*/rules.txt'))):
            rules = configparser.ConfigParser()
            rules.read(rulef)
            mods[i] = {
                'name' : rules['Definition']['name'],
                'priority' : rules['Definition']['fsPriority'],
                'path' : os.path.dirname(rulef)
            }
            if mods[i]['name'] == 'BCML': continue
            print(f'{mods[i]["name"]} — Priority: {mods[i]["priority"]}')

if __name__ == "__main__":
    main()