if [ -d "~/.yosenv" ]; then
    rm -rf "~/.yosenv"
fi

virtualenv -p python3.6 ~/.yosenv
