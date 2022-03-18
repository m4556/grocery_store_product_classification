#  ****Grocery store item classification****
A model for the grocery items recognition in store shelves. Image classification is performed using three different types of deep convolutional neural networks in order to classify groceries of fruits, vegetables, and dairy.

 # ****Dataset****
Dataset consists of natural images of grocery items. All natural images was taken with a smartphone camera in different grocery stores.There are 5125 natural images from 81 different classes of fruits, vegetables, and carton items (e.g. milk, yoghurt). Dataset is split to train, validaton and test and it was rearanged to fit the goal of the project. The original dataset is from https://github.com/marcusklasson/GroceryStoreDataset

 #  ***Models*** 
 Xception, MobileNet and VGG19 were used, with archived accuracy in range 94%-97%.

 #  ***Citation*** 
 
> @inproceedings{klasson2019hierarchical,
  title={A Hierarchical Grocery Store Image Dataset with Visual and Semantic Labels},
  author={Klasson, Marcus and Zhang, Cheng and Kjellstr{\"o}m, Hedvig},
  booktitle={IEEE Winter Conference on Applications of Computer Vision (WACV)},
  year={2019}
}
