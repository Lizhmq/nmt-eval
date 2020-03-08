## NMT Eval

仓库包含NMT几种常见指标BLEU,ROUGE-L,ROUGE-1,ROUGE-2的评估脚本。引用代码来自Github/tensorflow/nmt.

将输出文件和标准文件处理成每行一个样本，以空格分开的格式，运行以下命令则输出BLEU(default max-n-gram=2),ROUGE值：

```
python3 main.py -out <outfile> -ref <reffile>
```

#### process_xx.py

process_rl.py是处理[Reinforcement-Learning](https://code.byted.org/lizhuo.joe/paraphrase-generation)代码decode输出的脚本，RL解码输出以每个样本一个文件的形式存储在一个目录中，这个脚本将输出处理为按行的同一文件中：

```
python3 nmt_eval/process_rl.py -out_dir path/to/rouge_dec_dir -ref_dir path/to/rouge_ref -out_output <outfile> -ref_output <reffile> -size 30000
# size是测试数据的期望大小，处理完成时检查是否一致
```

process_dips.py是处理[DiPS](https://code.byted.org/lizhuo.joe/paraphrase-generation)代码decode输出的脚本，DiPS的输出是npy文件，包含了source和对应的多条target输出，一个样本如下：

```
array([['What are the important topics to be prepared for the CAT ?',
        'What are the important topics to prepare for CAT ?'],
       ['What are the important topics to be prepared for the CAT ?',
        'Which is the best topic for CAT ?'],
       ['What are the important topics to be prepared for the CAT ?',
        'What are the best topics for cat preparation ?'],
       ['What are the important topics to be prepared for the CAT ?',
        'What are the essential topics for preparing CAT ?']],
      dtype='<U248')
```

```
python3 nmt_eval/process_dips.py -res_file <resfile> -out_output <outfile> -ref_output <reffile>
```

#### 训练结果

训练的模型太大，这里给出下载[链接](https://pkueducn-my.sharepoint.com/:u:/g/personal/1600012911_pku_edu_cn/EQDhu-bxEWRFjxDiBCxA8VMBe1JKDAf8i4iYViQ8IzAp_A?e=WwGORR)（包含RL的八个模型[pretrain+finetuning]和DiPS的四个模型共1.6G），decoding结果在files目录。
