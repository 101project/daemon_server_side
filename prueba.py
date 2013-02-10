#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import shlex

directory = "/home/user/Documents/"
lista = os.listdir(directory)
directorios = []
archivosIMP = []
for d in lista:
    if os.path.isdir(directory + d):
        directorios.append(os.path.join(directory, d))

for path in directorios:
    archivos = os.listdir(path)
    for archivo in archivos:
        if os.path.isfile(path + "/" + archivo):
            archivosIMP.append(os.path.join(path, archivo))

#print archivosIMP

impresoras = []
pathVPN = "/etc/openvpn/ccd/"
clientes = os.listdir(pathVPN)
for cliente in clientes:
    if not "." in cliente:
        if os.path.isfile(pathVPN + cliente):
            f = open(pathVPN + cliente)
            line = f.readline()
            f.close()
            linea = shlex.split(line)
            impresoras.append(linea[3][1:])
#print impresoras

for impresora in impresoras:
    estado = subprocess.Popen(["lpstat", "-p", impresora], stdout=subprocess.PIPE)
    out, err = estado.communicate()
    if "Ready" in out:
        for archivo in archivosIMP:
            if impresora in archivo:
                impresion = subprocess.Popen(["lp", "-d", impresora, archivo], stdout=subprocess.PIPE)
                OUT, ERR = impresion.communicate()
                print OUT
            else:
                print archivo
    else:
        print "No está disponible la impresora"


