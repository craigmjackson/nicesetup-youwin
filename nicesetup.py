#!/usr/bin/env python3
import shutil
import os
import subprocess
import sys


TOPLEVEL_DIR = os.path.join(os.path.dirname(__file__))
HOME = os.environ["HOME"]
STOP_ON_FAIL = True
USER = os.environ["USER"]


def run_command(command, cwd=None, fatal=True):
    if cwd:
        process = subprocess.Popen(command, shell=True, cwd=cwd)
    else:
        process = subprocess.Popen(command, shell=True)
    process.communicate()
    if process.returncode == 0:
        return True
    if STOP_ON_FAIL:
        if not fatal:
            sys.exit(1)
    return False


def copy_file(src, dest):
    try:
        shutil.copyfile(src, dest)
    except Exception:
        print("Could not copy \"" + src + "\" to \"" + dest + "\"")
        if STOP_ON_FAIL:
            sys.exit(1)
        return False


def install_nano():
    package_dir = os.path.join(TOPLEVEL_DIR, "nano")
    nanorc_src = os.path.join(package_dir, "nanorc")
    nanorc_dest = os.path.join(HOME, ".nanorc")
    shutil.copyfile(nanorc_src, nanorc_dest)


def install_git():
    run_command("sudo apt -y install git")


def install_tmux():
    package_dir = os.path.join(TOPLEVEL_DIR, "tmux")
    tmux_conf_src = os.path.join(package_dir, "tmux.conf")
    tmux_conf_dest = os.path.join(HOME, ".tmux.conf")
    tpm_dir = os.path.join(HOME, ".tmux", "plugins", "tpm")
    if not os.path.exists(tpm_dir):
        run_command("git clone https://github.com/tmux-plugins/tpm " +
                    "~/.tmux/plugins/tpm")
    else:
        print("Directory \"" + tpm_dir + "\" already exists.  Delete it if " +
              "you want to reinstall tmux plugin manager.")
    run_command("sudo apt -y install tmux", fatal=False)
    copy_file(tmux_conf_src, tmux_conf_dest)


def install_curl():
    run_command("sudo apt -y install curl")


def install_zsh():
    package_dir = os.path.join(TOPLEVEL_DIR, "zsh")
    zshrc_src = os.path.join(package_dir, "zshrc")
    zshrc_dest = os.path.join(HOME, ".zshrc")
    ohmyzsh_dir = os.path.join(HOME, ".oh-my-zsh")
    run_command("sudo apt -y install zsh")
    run_command("sudo chsh -s $(which zsh) " + USER)
    if not os.path.exists(ohmyzsh_dir):
        run_command("sh -c \"$(curl -fsSL https://raw.github.com/" +
                    "robbyrussell/oh-my-zsh/master/tools/install.sh)\"")
    else:
        print("Directory \"" + ohmyzsh_dir + "\" already exists.  " +
              "Delete it if you want to reinstall oh my zsh.")
    copy_file(zshrc_src, zshrc_dest)


def install_node():
    tarball = "node-v20.10.0-linux-x64.tar.xz"
    src_dir = "/tmp/node-v20.10.0-linux-x64"
    run_command("wget https://nodejs.org/dist/v20.10.0/" + tarball, cwd="/tmp")
    run_command("tar xf /tmp/" + tarball, cwd="/tmp")
    run_command("sudo /bin/cp -R " + src_dir + "/bin/* /usr/local/bin/")
    run_command("sudo /bin/cp -R " + src_dir + "/include/* " +
                "/usr/local/include/")
    run_command("sudo /bin/cp -R " + src_dir + "/lib/* /usr/local/lib/")
    run_command("sudo /bin/cp -R " + src_dir + "/share/* /usr/local/share/")
    run_command("rm -rf " + src_dir)
    run_command("rm -f /tmp/" + tarball + "*")


def install_rsync():
    run_command("sudo apt -y install rsync")


def install_neovim():
    package_dir = os.path.join(TOPLEVEL_DIR, "nvim")
    tarball = "nvim-linux64.tar.gz"
    luals_tarball = "lua-language-server-3.7.3-linux-x64.tar.gz"
    luals_src = "/tmp/luals"
    src_dir = "/tmp/nvim-linux64"
    user_config = os.path.join(HOME, ".config")
    user_config_nvim = os.path.join(user_config, "nvim")
    user_config_nvim_src = os.path.join(package_dir, "config", "nvim")
    user_local_share = os.path.join(HOME, ".local", "share")
    user_local_share_nvim = os.path.join(user_local_share, "nvim")
    user_local_share_nvim_src = os.path.join(package_dir,
                                             "local", "share", "nvim")
    run_command("wget https://github.com/neovim/neovim/releases/latest/" +
                "download/nvim-linux64.tar.gz", cwd="/tmp")
    run_command("tar xf /tmp/" + tarball, cwd="/tmp")
    if os.path.exists("/usr/local/bin/nvim"):
        run_command("sudo mv /usr/local/bin/nvim /usr/local/nvim.orig")
    run_command("sudo /bin/cp -R " + src_dir + "/bin/* /usr/local/bin/")
    run_command("sudo /bin/cp -R " + src_dir + "/lib/* /usr/local/lib/")
    run_command("sudo /bin/cp -R " + src_dir + "/man/* /usr/local/man/")
    run_command("sudo /bin/cp -R " + src_dir + "/share/* /usr/local/share/")
    run_command("rm -rf " + src_dir)
    run_command("rm -f /tmp/" + tarball + "*")
    run_command("mkdir -p " + user_config_nvim)
    run_command("mkdir -p " + user_local_share_nvim)
    run_command("rsync -az --delete " + user_config_nvim_src + "/ " +
                user_config_nvim + "/")
    run_command("rsync -az --delete " + user_local_share_nvim_src + "/ " +
                user_local_share_nvim + "/")
    run_command("sudo npm i -g bash-language-server")
    run_command("sudo npm i -g vscode-langservers-extracted")
    run_command("sudo npm i -g @microsoft/compose-language-service")
    run_command("wget https://github.com/LuaLS/lua-language-server/" +
                "releases/download/3.7.3/" +
                "lua-language-server-3.7.3-linux-x64.tar.gz", cwd="/tmp")
    run_command("mkdir -p /tmp/luals")
    run_command("tar xf /tmp/" + luals_tarball, cwd="/tmp/luals")
    run_command("sudo /bin/cp -R " + luals_src + "/* /usr/local/")
    run_command("sudo mkdir -p /usr/local/log")
    run_command("sudo chmod -R 777 /usr/local/log")
    run_command("rm -rf " + luals_src)
    run_command("rm -f /tmp/" + luals_tarball + "*")
    run_command("sudo npm i -g @vue/language-server")
    run_command("sudo npm i -g yaml-language-server")
    run_command("sudo apt -y install python3-neovim")
    run_command("sudo apt -y install python3-venv")
    run_command("sudo apt -y install python3-pylsp")
    for filename in ["vim", "vi"]:
        if os.path.exists("/usr/bin/vim"):
            if not os.path.islink("/usr/bin/" + filename):
                run_command("sudo mv /usr/bin/" + filename +
                            " /usr/bin/" + filename + ".orig")
                run_command("sudo ln -sf /usr/local/bin/nvim /usr/bin/" +
                            filename)
            else:
                if os.readlink("/usr/bin/" +
                               filename) != "/usr/local/bin/nvim":
                    run_command("sudo rm /usr/bin/" + filename)
                    run_command("sudo ln -sf /usr/local/bin/nvim " +
                                "/usr/bin/" + filename)


def main():
    install_nano()
    install_git()
    install_tmux()
    install_curl()
    install_zsh()
    install_node()
    install_rsync()
    install_neovim()

if __name__ == "__main__":
    main()

