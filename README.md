# Prerequisites
```text
python 3.9+
pip-tools
make
```

# Updating project
```commandline
$ make lock
$ make install
```

# Run
create .env file and run
```commandline
$ docker compose up --build
```


# Explanation
I used csv file as database since this server will only run once :D but also
the data is not that big to set up a database