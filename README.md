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

run:

```
python main.py  -c  "while [ 1 -eq 1 ]; do echo 2; sleep 1; done" -p "/Users/ruifengyun/github/"
```

stdout:

```
2018-07-29 10:32:35 - Executing `while [ 1 -eq 1 ]; do echo 2018年 7月29日 星期日 10时32分35秒 CST; sleep 1; done`
2018年 7月29日 星期日 10时32分35秒 CST
2018年 7月29日 星期日 10时32分35秒 CST
2018年 7月29日 星期日 10时32分35秒 CST
2018-07-29 10:32:41 - Modified directory: /Users/ruifengyun/github/watchrun/.git
2018-07-29 10:32:41 - Terminated (return code: -15)
2018-07-29 10:32:41 - Restarting `while [ 1 -eq 1 ]; do echo 2018年 7月29日 星期日 10时32分35秒 CST; sleep 1; done`
2018年 7月29日 星期日 10时32分35秒 CST
2018-07-29 10:32:41 - Modified directory: /Users/ruifengyun/github/watchrun/.git
2018-07-29 10:32:41 - Restarting `while [ 1 -eq 1 ]; do echo 2018年 7月29日 星期日 10时32分35秒 CST; sleep 1; done`
2018-07-29 10:32:41 - Terminated (return code: -15)
```
