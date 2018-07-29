# watchrun

restart your program when program directory or files are changed

## Usage

```
usage: main.py [-h] [-d DEBUG] [-p PATH] [-e [FILE_EXT [FILE_EXT ...]]] -c
               COMMAND

Restarts process when any files / directory changes

optional arguments:
  -h, --help            show this help message and exit
  -d DEBUG, --debug DEBUG
                        Debug mode
  -p PATH, --path PATH  Which directory to watch for changes
  -e [FILE_EXT [FILE_EXT ...]], --extension [FILE_EXT [FILE_EXT ...]]
                        Which file extensions to listen for
  -c COMMAND, --command COMMAND
                        Command to be executed
```

## Example

```
python main.py  -c  "while [ 1 -eq 1 ]; do echo 2; sleep 1; done" -p "/Users/ruifengyun/github/"
```

