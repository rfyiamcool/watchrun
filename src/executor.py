# coding: utf-8

import os
import sys
import signal
import subprocess
import threading
import logging


class Executor():
    def __init__(self, command):
        self.__command = command
        self.__process = None

    def __command_reader(self):
        # Poll process for new output until finished
        while True:
            nextline = self.__process.stdout.readline()
            if nextline == '' and self.__process.poll() != None:
                break

            sys.stdout.write(nextline)
            sys.stdout.flush()

        logging.debug("Terminated (return code: %s)" % self.__process.returncode)

    def restart(self):
        if self.kill():
            logging.debug("Restarting `%s`" % self.__command)
        else:
            logging.debug("Executing `%s`" % self.__command)

        self.__process = subprocess.Popen(self.__command, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, preexec_fn=os.setsid)
        threading.Thread(target=self.__command_reader).start()

    def kill(self):
        if self.__process:
            try:
                os.killpg(os.getpgid(self.__process.pid), signal.SIGTERM)
                self.__process.wait()
                return True
            except OSError:
                logging.debug("No process to kill")

        return False
