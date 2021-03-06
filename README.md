# toteGrasping
Dataset for robotic grasping in dense cluster

## Overview
This repository is the supplementary materials of the paper "GraspFusionNet: a two-stage multi-parameter grasp detection network based on RGB–XYZ fusion in dense clutter."[Video](https://youtu.be/aFGE-4iL2w8) by Liu et al. In this repo, we provide  code of how to show grasp.

## Results
### Known objects
<p>
	<img src ="results/known/000011_color.png" width="160" />
	<img src ="results/known/000110_color.png" width="160" />
	<img src ="results/known/000135_color.png" width="160" />
	<img src ="results/known/000148_color.png" width="160" />
	<img src ="results/known/000176_color.png" width="160" />
</p>
<p>
	<img src ="results/known/000011_3d.png" width="160" /> 
	<img src ="results/known/000110_3d.png" width="160" />
	<img src ="results/known/000135_3d.png" width="160" />
	<img src ="results/known/000148_depth.png" width="160" />
	<img src ="results/known/000176_3d.png" width="160" />
</p>

### Novel objects
<p>
	<img src ="results/novel/01_2d.png" width="160" />
	<img src ="results/novel/02_2d.png" width="160" />
	<img src ="results/novel/03_2d.png" width="160" />
	<img src ="results/novel/04_2d.png" width="160" />
	<img src ="results/novel/05_2d.png" width="160" />
</p>
<p>
	<img src ="results/novel/01_3d.png" width="160" /> 
	<img src ="results/novel/02_3d.png" width="160" />
	<img src ="results/novel/03_3d.png" width="160" />
	<img src ="results/novel/04_3d.png" width="160" />
	<img src ="results/novel/05_3d.png" width="160" />
</p>


## Datasets
Download links for our grasping dataset  can be found on our [toteGrasping](https://www.dropbox.com/sh/bi1link0bhoga5v/AABO4KXf7E1sjMASope9ay0za?dl=0).

### Datasets Structure
* toteGrasping
	* toteGrasping/heightmap_color
		* toteGrasping/heightmap_color/%0.6d.png: color heightmap.
  	* toteGrasping/heightmap_depth
		* toteGrasping/heightmap_depth/%0.6d_combine.npy: xyz heightmap, in meter.
  	* toteGrasping/label_gPPN
		* toteGrasping/label_gPPN/%0.6d_bad|good.npy: good (x,y,1,angle,width,depth),angle:deg,width:mm,depth:meter/10000..
  	* toteGrasping/label_gRPN
		* toteGrasping/label_gRPN/%0.6d.png: pixel wise label, graspable or non-graspable.
		* toteGrasping/label_gRPN/%0.6d.npy: pixel wise label, angle,width,depth.
  	* toteGrasping/label_show
		* toteGrasping/label_show/%0.6d.png: original grasp label.
  	* toteGrasping/train-split.txt: traing data
  	* toteGrasping/test-split.txt:  test data

## Contact
If you have any questions, please let me know:  sjtu-wenhai[at]sjtu[dot]edu[dot]cn

