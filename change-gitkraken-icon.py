# Changes the gitkraken icon 
def main():
    gitkraken_file = '/var/lib/snapd/desktop/applications/gitkraken_gitkraken.desktop'
    with open(gitkraken_file, 'r') as f:
        lines = f.readlines()
    with open(gitkraken_file, 'w') as f:
        for line in lines:
            line = line.replace('Icon=gitkraken', 'Icon=/home/cade/snap/gitkraken/gitkraken_glo.png')
            f.write(line)


if __name__ == "__main__":
    main()
