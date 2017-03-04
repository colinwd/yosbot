if [ -d "~/.yosenv" ]; then
    rm -rf "~/.yosenv"
fi

virtualenv -p python3.5 ~/.yosenv
