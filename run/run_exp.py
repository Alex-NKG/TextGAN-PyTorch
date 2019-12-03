# -*- coding: utf-8 -*-
# @Author       : William
# @Project      : TextGAN-william
# @FileName     : run_exp.py
# @Time         : Created at 2019-07-26
# @Blog         : http://zhiweil.ml/
# @Description  : 
# Copyrights (C) 2018. All Rights Reserved.

import sys
from subprocess import call
import os

# Executables
executable = '/home/zhiwei/.virtualenvs/zhiwei/bin/python'
rootdir = '../'

run_model = 'catgan'
device = 0

ora_pretrain = [0, 1, 1]
gen_pretrain = [0, 1, 1]
use_all_real_fake = [int(True), int(False), int(True)]
ADV_train_epoch = [0, 2000, 2000]

for i in range(21):
    job_id = i % 3
    args = [
        '--device', device,
        '--run_model', run_model,
        '--ora_pretrain', ora_pretrain[job_id],
        '--gen_pretrain', gen_pretrain[job_id],
        '--adv_epoch', ADV_train_epoch[job_id],
        '--use_all_real_fake', use_all_real_fake[job_id],
    ]

    args = list(map(str, args))
    my_env = os.environ.copy()
    call([executable, 'main.py'] + args, env=my_env, cwd=rootdir)
