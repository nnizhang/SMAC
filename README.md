# SMAC: Learning Selective Mutual Attention and Contrast for RGB-D Saliency Detection

paper link: [https://arxiv.org/abs/2010.05537](https://arxiv.org/abs/2010.05537)

## Citing our work
If you think our work is helpful, please cite 
```
@misc{liu2020learning,
      title={Learning Selective Mutual Attention and Contrast for RGB-D Saliency Detection}, 
      author={Nian Liu and Ni Zhang and Ling Shao and Junwei Han},
      year={2020},
      eprint={2010.05537},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## The Proposed RGB-D Salient Object Detection Dataset
### ReDWeb-S

We construct a new large-scale challenging dataset ReDWeb-S and it has totally 3179 images with various real-world scenes and high-quality depth maps. We split the dataset into a training set with 2179 RGB-D image pairs and a testing set with the remaining 1000 image pairs.

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/dataset_examp2.png)

The proposed dataset link can be found here. [[baidu pan](https://pan.baidu.com/s/1yRlptJ7MXgCFd9WUloWI6Q) fetch code: rp8b | [Google drive](https://drive.google.com/file/d/1PM8wo8xFrHK2oVpYz_9aON6Imc_SM5Cl/view?usp=sharing)]

### Dataset Statistics and Comparisons

We analyze the proposed ReDWeb-S datset from several statistical aspects and also conduct a comparison between ReDWeb-S and other existing RGB-D SOD datasets.

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/table.png)

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/scene_object_stat.png)
Fig.1. Top 60% scene and object category distributions of our proposed ReDWeb-S dataset.

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/GC_IC.png)
Fig.2. Comparison of nine RGB-D SOD dataset in terms of the distributions of global contrast and interior contrast.

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/center_bias.png)
Fig.3. Comparsion of the average annotation maps for nine RGB-D SOD benchmark datasets.

![avatar](https://github.com/nnizhang/SMAC/blob/main/figures/object_size.png)

Fig.4. Comparsion of the distribution of object size for nine RGB-D SOD benchmark datasets.

## SOTA Results on Our Proposed Dataset

We provide other SOTA RGB-D methods' results and scores on our proposed dataset. You can directly download all results [[here](https://pan.baidu.com/s/1GUyvRjiQpwCGjsDNR2I3YQ) ov08].
**No.** | **Pub.** | **Name** | **Title** | **Download**    
:-: | :-: | :-: | :- | :-: | 
01 | **ECCV2020** | **PGAR** | Progressively Guided Alternate Refinement Network for RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1R-zqn-aKCITT13jIRqNZ9w), mwtr
02 | **ECCV2020** | **HDFNet** | Hierarchical Dynamic Filtering Network for RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1UOBIdE8-GkcpIYg-hhQwCg), b98z
03| **ECCV2020** | **DANet** | A Single Stream Network for Robust and Real-time RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1DU_0V8xjhcxDs1ekgHtWxg), 1luj
04 | **ECCV2020** | **CoNet** | Accurate RGB-D Salient Object Detection via Collaborative Learning | [results](https://pan.baidu.com/s/1P891fV3brwLK6dtiKg46Tg), bqq6
05 | **ECCV2020** | **CMWNet** | Cross-Modal Weighting Network for RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1xpXgZ2DYGM0Vq0aXMWCBug), ztv9
06 | **ECCV2020** | **cmMS** | RGB-D Salient Object Detection with Cross-Modality Modulation and Selection | [results](https://pan.baidu.com/s/10QnVC-XV1lGruIPzS9bWmw), kwe5
07 | **ECCV2020** | **BBS-Net** | BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network | [results](https://pan.baidu.com/s/1x6gF4qVvoP7dImfSnIXHYg), ya5v
08 | **ECCV2020** | **ATSA** | Asymmetric Two-Stream Architecture for Accurate RGB-D Saliency Detection | [results](https://pan.baidu.com/s/1nxxcjYxyrfsMEu5EC-BiHA), k750
09 | **CVPR2020** | **S2MA** | Learning Selective Self-Mutual Attention for RGB-D Saliency Detection | [results](https://pan.baidu.com/s/1uYmvq8iGYOV4moJrCAv16Q), g0pgx
10 | **CVPR2020** | **JL-DCF** | JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1woqURqUdD2Yj_m0gFsna2w), xh9p
11 | **CVPR2020** | **UCNet** | UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders | [results](https://pan.baidu.com/s/1Y0Th92bJi6O1F34rQctRww), 6o93
12 | **CVPR2020** | **A2dele** | A2dele: Adaptive and Attentive Depth Distiller for Efficient RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/19hCRw_FH29itQX9NHXpG1Q), swv5
13 | **CVPR2020** | **SSF-RGBD** | 	Select, Supplement and Focus for RGB-D Saliency Detection | [results](https://pan.baidu.com/s/1ybSdHz6QIKrL6h5hkvtOEw), oshl
14 | **TIP2020** | **DisenFusion** | RGBD Salient Object Detection via Disentangled Cross-Modal Fusion | [results](https://pan.baidu.com/s/1LNabG-hL3uOeXzXuyKX_qQ), h3hc
15 | **TNNLS2020** | **D3Net** | D3Net:Rethinking RGB-D Salient Object Detection: Models, Datasets, and Large-Scale Benchmarks | [results](https://pan.baidu.com/s/1_mmi1tz2XSs2YtDJegHnvA), tetn
16 | **ICCV2019** | **DMRA** | Depth-induced multi-scale recurrent attention network for saliency detection | [results](https://pan.baidu.com/s/1UHlRvz-_8poJmeAvD5B7wg), kqq4
17 | **CVPR2019** | **CPFP** | Depth-induced multi-scale recurrent attention network for saliency detection | [results](https://pan.baidu.com/s/1RZjrImrV8vuXHT6sxZ4Xnw), 0v2c 
18 | **TIP2019** | **TANet** | Three-stream attention-aware network for RGB-D salient object detection | [results](https://pan.baidu.com/s/1LS5WoS0xGpGLtgG2ajr_jA), hsy9 
19 | **CVPR2018** | **PCF** | Progressively Complementarity-Aware Fusion Network for RGB-D Salient Object Detection | [results](https://pan.baidu.com/s/1nUo0z4hjSy80FFI97t3INQ), qzhm 
20 | **PR2019** | **MMCI** | Multi-modal fusion network with multiscale multi-path and cross-modal interactions for RGB-D salient object detection | [results](https://pan.baidu.com/s/1WLhbJVMO_Qu9DpMgkJU6iw), c90m 
21 | **TCyb2017** | **CTMF** | CNNs-based RGB-D saliency detection via cross-view transfer and multiview fusion | [results](https://pan.baidu.com/s/1VuiMYFP_zwc6jceHIgoLMQ), i0zb 
22 | **Access2019** | **AFNet** | Adaptive fusion for rgb-d salient object detection | [results](https://pan.baidu.com/s/1PY6nUe_JIjNyh6_M7v-V4A), 54zc
23 | **TIP2017** | **DF** | Rgbd salient object detection via deep fusion | [results](https://pan.baidu.com/s/1SOdNZeDhtXaBMwhfebxngA), d7sc
24 | **ICME2016** | **SE** | Salient object detection for rgb-d image via saliency evolution | [results](https://pan.baidu.com/s/1WWLmuP53yFEHkKDwL2GRzQ), h10s
25 | **SPL2016** | **DCMC** | Saliency detection for stereoscopic images based on depth confidence analysis and multiple cues fusion | [results](https://pan.baidu.com/s/1O8is3axC7Ssr88a8QnxeWQ), 18po
26 | **CVPR2016** | **LBE** | Local background enclosure for rgb-d salient object detection | [results](https://pan.baidu.com/s/1X30QiJ0mE9diQwhQIqMD2A), iiz5

**Methods** | **S-measure** | **maxF** | **E-measure** | **MAE**     
:-: | :-: | :-: | :-: | :-: |
S2MA | 0.711 | 0.696 | 0.781 | 0.139
JL-DCF | 0.734 | 0.727 | 0.805 | 0.128
UCNet | 0.713 | 0.71 | 0.794 | 0.13
A2dele | 0.641 | 0.603 | 0.672 | 0.16
SSF-RGBD | 0.595 | 0.558 | 0.71 | 0.189
DisenFusion | 0.675 | 0.658 | 0.76 | 0.16
D3Net | 0.689 | 0.673 | 0.768 | 0.149
DMRA | 0.592 | 0.579 | 0.721 | 0.188
CPFP | 0.685 | 0.645 | 0.744 | 0.142
TANet | 0.656 | 0.623 | 0.741 | 0.165 
PCF | 0.655 | 0.627 | 0.743 | 0.166 
MMCI | 0.660 | 0.641 | 0.754 | 0.176 
CTMF | 0.641 | 0.607 | 0.739 | 0.204 
AFNet | 0.546 | 0.549 | 0.693 | 0.213
DF | 0.595 | 0.579 | 0.683 | 0.233
SE | 0.435 | 0.393 | 0.587 | 0.283
DCMC | 0.427 | 0.348 | 0.549 | 0.313
LBE | 0.637 | 0.629 | 0.73 | 0.253

## Acknowledgement
We thank all annotators for helping us constructing the proposed dataset. Our proposed dataset is based on the [ReDWeb](https://openaccess.thecvf.com/content_cvpr_2018/papers/Xian_Monocular_Relative_Depth_CVPR_2018_paper.pdf) dataset, which is a state-of-the-art dataset proposed for monocular image depth estimation. We also thank the authors for providing the ReDWeb dataset.

## Contact
If you have any questions, please feel free to contact me. (nnizhang.1995@gmail.com)







