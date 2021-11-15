<div id="top"></div>

-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">

  <h1 align="center">Millitary Rescue and criminal Tracking</h1>

  <p align="center">
    An awesome guide to install and run this awesome computer vision project!
    
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Full project demo][product-screenshot1]](https://www.youtube.com/watch?v=mTAQe_-H1AE&ab_channel=BinaryBlock)
[![product-screenshot1][product-screenshot2]]
[![product-screenshot1][product-screenshot3]]
[![product-screenshot1][product-screenshot4]]

This Hybrid AI platform for military, rescue and criminal tracking drone + AI platform is a prototype version for fighting crime and help in security. The drone is equipped with an onboard camera which can -

1. Provide live footage of the area it is scanning.
2. While Scanning the area it can detect people and other objects using object detection algorithm. I have used YOLO V3 for the real time object detection. Hugely used to rescue people in landslides, fire and keep an eagle eye on the sky for terrorists and naxalites.
3. It's enabled with ip camera's system that can detect known faces and alert when unknown face is detected.
4. The project has a great feature of gun detection. Due to increase of gun violence, it may detect gun with an accuracy of more than 60% and will notify. This I have trained using ssd_mobilenet_v1_coco model.
5. Last but not the least the drone can scan the area and show the 3d model of the scene.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This section contains the requirement to create the project

- [Python](https://www.python.org/)
- [Conda](https://docs.conda.io/en/latest/)
- [Tensorflow gpu 1.15](https://www.tensorflow.org/)
- [OpenCV python](https://www.tensorflow.org/)
- [Numpy](https://numpy.org/)
- [Tkinter UI](https://docs.python.org/3/library/tkinter.html)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Please follow the detailed instruction to run this project on your local.

### Prerequisites

Before running the project to have a virtual env to run this file. I used conda for this particular project

- conda (once conda is installed you can either use conda or pip )
  ```
  https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307
  ```
- install pip using conda

  ```
  1. Run "conda create -n venv_name" and "conda activate venv_name", where venv_name is the name of your virtual environment.

  2. Run "conda install pip". This will install pip to your venv directory.
  ```

### Installation

<h3>Folder Structure</h3>

<hr />
<pre>
  Millitary/
  ┣ assets/
  ┃ ┣ data/
  ┃ ┃ ┣ coco.names
  ┃ ┃ ┣ frozen_inference_graph_new.pb
  ┃ ┃ ┣ object-detection.pbtxt
  ┃ ┃ ┣ yolov3.cfg
  ┃ ┃ ┗ yolov3.weights
  ┃ ┣ images/
  ┃ ┃ ┣ adhyayan.jpg
  ┃ ┃ ┣ biden.jpg
  ┃ ┃ ┗ sosgot_Eoy_icon.ico
  ┃ ┣ security_videos/
  ┃ ┗ videos/
  ┃   ┗ gun4.mp4
  ┣ project_screenshots/
  ┃ ┣ 1.jpg
  ┃ ┣ 4.jpg
  ┃ ┣ 7.jpg
  ┃ ┗ project_screenshot.png
  ┣ utils/
  ┃ ┣ __pycache__/
  ┃ ┃ ┣ autoaugment_utils.cpython-36.pyc
  ┃ ┃ ┣ config_util.cpython-36.pyc
  ┃ ┃ ┣ context_manager.cpython-36.pyc
  ┃ ┃ ┣ dataset_util.cpython-36.pyc
  ┃ ┃ ┣ json_utils.cpython-36.pyc
  ┃ ┃ ┣ label_map_util.cpython-36.pyc
  ┃ ┃ ┣ label_map_util.cpython-37.pyc
  ┃ ┃ ┣ learning_schedules.cpython-36.pyc
  ┃ ┃ ┣ metrics.cpython-36.pyc
  ┃ ┃ ┣ model_util.cpython-36.pyc
  ┃ ┃ ┣ np_box_list.cpython-36.pyc
  ┃ ┃ ┣ np_box_list_ops.cpython-36.pyc
  ┃ ┃ ┣ np_box_mask_list.cpython-36.pyc
  ┃ ┃ ┣ np_box_mask_list_ops.cpython-36.pyc
  ┃ ┃ ┣ np_box_ops.cpython-36.pyc
  ┃ ┃ ┣ np_mask_ops.cpython-36.pyc
  ┃ ┃ ┣ object_detection_evaluation.cpython-36.pyc
  ┃ ┃ ┣ ops.cpython-36.pyc
  ┃ ┃ ┣ patch_ops.cpython-36.pyc
  ┃ ┃ ┣ per_image_evaluation.cpython-36.pyc
  ┃ ┃ ┣ shape_utils.cpython-36.pyc
  ┃ ┃ ┣ spatial_transform_ops.cpython-36.pyc
  ┃ ┃ ┣ static_shape.cpython-36.pyc
  ┃ ┃ ┣ variables_helper.cpython-36.pyc
  ┃ ┃ ┣ visualization_utils.cpython-36.pyc
  ┃ ┃ ┣ visualization_utils.cpython-37.pyc
  ┃ ┃ ┣ __init__.cpython-36.pyc
  ┃ ┃ ┗ __init__.cpython-37.pyc
  ┃ ┣ autoaugment_utils.py
  ┃ ┣ category_util.py
  ┃ ┣ category_util_test.py
  ┃ ┣ config_util.py
  ┃ ┣ config_util_test.py
  ┃ ┣ context_manager.py
  ┃ ┣ context_manager_test.py
  ┃ ┣ dataset_util.py
  ┃ ┣ dataset_util_test.py
  ┃ ┣ json_utils.py
  ┃ ┣ json_utils_test.py
  ┃ ┣ label_map_util.py
  ┃ ┣ label_map_util_test.py
  ┃ ┣ learning_schedules.py
  ┃ ┣ learning_schedules_test.py
  ┃ ┣ metrics.py
  ┃ ┣ metrics_test.py
  ┃ ┣ model_util.py
  ┃ ┣ model_util_test.py
  ┃ ┣ np_box_list.py
  ┃ ┣ np_box_list_ops.py
  ┃ ┣ np_box_list_ops_test.py
  ┃ ┣ np_box_list_test.py
  ┃ ┣ np_box_mask_list.py
  ┃ ┣ np_box_mask_list_ops.py
  ┃ ┣ np_box_mask_list_ops_test.py
  ┃ ┣ np_box_mask_list_test.py
  ┃ ┣ np_box_ops.py
  ┃ ┣ np_box_ops_test.py
  ┃ ┣ np_mask_ops.py
  ┃ ┣ np_mask_ops_test.py
  ┃ ┣ object_detection_evaluation.py
  ┃ ┣ object_detection_evaluation_test.py
  ┃ ┣ ops.py
  ┃ ┣ ops_test.py
  ┃ ┣ patch_ops.py
  ┃ ┣ patch_ops_test.py
  ┃ ┣ per_image_evaluation.py
  ┃ ┣ per_image_evaluation_test.py
  ┃ ┣ per_image_vrd_evaluation.py
  ┃ ┣ per_image_vrd_evaluation_test.py
  ┃ ┣ shape_utils.py
  ┃ ┣ shape_utils_test.py
  ┃ ┣ spatial_transform_ops.py
  ┃ ┣ spatial_transform_ops_test.py
  ┃ ┣ static_shape.py
  ┃ ┣ static_shape_test.py
  ┃ ┣ test_case.py
  ┃ ┣ test_utils.py
  ┃ ┣ test_utils_test.py
  ┃ ┣ variables_helper.py
  ┃ ┣ variables_helper_test.py
  ┃ ┣ visualization_utils.py
  ┃ ┣ visualization_utils_test.py
  ┃ ┣ vrd_evaluation.py
  ┃ ┣ vrd_evaluation_test.py
  ┃ ┗ __init__.py
  ┣ __pycache__/
  ┃ ┗ gun_video.cpython-37.pyc
  ┣ crime_scene3D.html
  ┣ gun_video.py
  ┣ index.html
  ┣ military_base_station.py
  ┣ readme.md
  ┗ requirements.txt
</pre>

1. Clone the repo

   ```

   ```

2. Download the assets - https://drive.google.com/drive/folders/1YD6N5vjX6-95shmVPnpbs3z9-2Rs1ej-?usp=sharing

3. Download the utils - https://drive.google.com/drive/folders/10j0ZyqQHVQMLgsgikJ0oEMKovV9wia1q?usp=sharing

<p>The folder should look like the folder structure above</p>

4. Install all packages

   ```
   pip install requirements.txt

   ```

5. Make some changes in the files

   ```
   1. Open military_base_station.py file and you can do following changes -
        a. In face_id(), in cv2.VideoCapture(0) 0 is default for the inbuild front camera of the laptop. You can change it to 1 if you are attaching another camera through USB or connecting FPV goggle video transmitter (from a quadcopter) to the laptop through USB. In detection() and video(), vs = VideoStream(src=0).start() follows the same rule.

        b. Attach two images in image_one and image_two_image respectively in face_id() function and replace name of those faces who will get access in known_face_names list

        c. Change full path of the two html files in crime_scene() and scene() function after "file:///"+ "real path" webbrowser.open('file://' + os.path.realpath(filename)). Or just click on the html file and copy the url from the browser and paste it in the above functions.
   ```

6. Run commands -

   ```
   1. conda activate virtual_env_name
   2. python military_base_station.py

   ```

7. Now the dashboard will open with various options. When a video frame opens to close it please enter letter "q" (smallcase) to exist from the frame to the dashboard. And to exit from the program click on the exit button on the dashboard.

8. All live images and screenshots captured during processing is stored in assets/security_videos folder.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See <a href="https://github.com/Adhyayanpradhan/computer_vision/blob/a38e6584c474cb31722bb40590feefd5f80aae02/LICENSE">MIT LICENSE</a> for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Adhyayan Pradhan- pradhanadhyayan@gmail.com

Project Link: [https://github.com/Adhyayanpradhan/computer_vision/tree/master/Millitary](https://github.com/Adhyayanpradhan/computer_vision/tree/master/Millitary)

<p align="right">(<a href="#top">back to top</a>)</p>

<p align="right">(<a href="#top">back to top</a>)</p>

[product-screenshot1]: ./project_screenshots/project_screenshot.png
[product-screenshot2]: ./project_screenshots/1.jpg
[product-screenshot3]: ./project_screenshots/2.jpg
[product-screenshot4]: ./project_screenshots/3.jpg
[linkedin-url]: https://www.linkedin.com/in/pradhan-adhyayan/
