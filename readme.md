<div id="top"></div>

<div align="center">

  <h1 align="center">Automatic Traffic Management, Number plate recognition, Speeding car recognition and fine system</h1>

  <p align="center">
    An awesome README template to install and run this awesome computer vision project!
    
  </p>
  
  <p>Project Demo - https://www.youtube.com/watch?v=D6Qqi1Od_2k&ab_channel=Adhyayan</p>
</div>
<br />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<a href="https://www.linkedin.com/in/pradhan-adhyayan/">
  <img align="left" alt="Adhyayan's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
</a>

<br />

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

[![Full project demo][product-screenshot1]](https://www.youtube.com/watch?v=D6Qqi1Od_2k&ab_channel=Adhyayan)
<div align="center">
  
  ![product-screenshot1][product-screenshot2]
  ![product-screenshot1][product-screenshot3]
  ![product-screenshot1][product-screenshot1]

</div>

This platform is an end to end system for automatic Traffic Management, Number plate recognition, Speeding car recognition and fine system to prevail the advanced prototype of traffic in India -

1. A prototype database system (mysql) which contains license of individuals who owns a vehicle and info related to the vehicle and the number plate.
2. A well organized fine system for the people who are captured in cameras for overspeeding and for other traffic violation (incoming prototype). All are captured and fine is registered and message is send to their number with proof and the location.
3. A vehicle patrolling portal to see and keep track of all traffic incoming routes using traffic cams. Under this we have vehicle detection to detect the overspeeding vehicles, recognize their number plate and send them the fine. All are done in the backend without human interventions.
4. Second is the smart traffic management solution is an innovative approach to handle huge traffic in metro or other crowded cities. It uses the concept of density estimation of the traffic in various lane to vary the duration of the red and green light to ease the flow so that there won't be any jam. For example - if 90% of traffic in lane-01 and 10% of traffic in lane-02, in normal conditio green light stays for 45 sec. But in lane-02 as density of crowd is less there is no need for waiting for the empty street and increase the traffic in lane-01. So using this smart system lane-02 20 secs will be added to the more densly populated traffic lane.
5. Using computer vision technology which uses deep learning to recognize the number plate, to provide more accuracy to detect and recognize plate and fit those data in the database.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This section contains the requirement to create the project and also see the requirements.txt to see the complete listof modules

- [Python](https://www.python.org/)
- [Conda](https://docs.conda.io/en/latest/)
- [Tensorflow gpu 1.15](https://www.tensorflow.org/)
- [OpenCV python](https://www.tensorflow.org/)
- [Numpy](https://numpy.org/)
- [Tkinter UI](https://docs.python.org/3/library/tkinter.html)
- [MySql](https://www.mysql.com/)
- [Pushbullet](https://www.pushbullet.com/)
- [Chromedriver](https://chromedriver.chromium.org/downloads)

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

- installation of pushbullet
<p>Pushbullet is a free cross platform messaging tools which is used in the project to send the fine. It's has brilliant api documentation to experiment a lot of stuffs.</p>

```
1. Visit https://www.pushbullet.com/ and make an account.
2. Download the app from the google play store - https://play.google.com/store/apps/details?id=com.pushbullet.android&referrer=utm_source%3Dpushbullet.com. Make sure you login through the same email. After installation accept all the requirement asked in the app and proceed to explore the app.
3. Visit to https://www.pushbullet.com/ website and go the settings https://www.pushbullet.com/#settings. Skim to the Access Token area andclick on Create Access Token and save that token which will be used in the script (is mentioned below)

```

See the images to get an idea -
<div align="center">
  ![product-screenshot1][product-screenshot5]
  ![product-screenshot1][product-screenshot6]
  ![product-screenshot1][product-screenshot7]
</div>

- chromedriver installation for getting the exact location
<p>Chromedriver is required for getting the longitude and latitude of the place where overspeeding takes place. So that fine can be attached with the location and video proof.</p>

```
1. Open chrome and go to the settings. Click on the About Chrome and check the version.
2. Go this offical chromedriver link https://chromedriver.chromium.org/downloads and download that particular driver version.
3. Mine is Version 96.0.4664.45 so I downloaded the Version 96.0.4664.45 driver.

```

- create sql database beforehand just to start working.

```
1. Go to MySql Workbench and go to the localhost.
2. View your table (if already present) or create your own table as shown in the image below

```

See the image to get an idea of the mysql table-

![product-screenshot1][product-screenshot8]

### Installation

<h3>Folder Structure</h3>

<hr />
<pre>
 Automatic Traffic management/
┣ assets/
┃ ┣ data/
┃ ┃ ┣ chromedriver_win32/
┃ ┃ ┃ ┗ chromedriver.exe
┃ ┃ ┣ coco.names
┃ ┃ ┣ frozen_inference_graph.pb
┃ ┃ ┣ frozen_inference_graph_detect.pb
┃ ┃ ┣ myhaar.xml
┃ ┃ ┣ object-detection.pbtxt
┃ ┃ ┣ plates.json
┃ ┃ ┣ Vehicle_DB.db
┃ ┃ ┣ yolov3.cfg
┃ ┃ ┗ yolov3.weights
┃ ┣ images/
┃ ┃ ┗ cctv_Glf_icon.ico
┃ ┣ output/
┃ ┃ ┣ detected_object_output.mp4
┃ ┃ ┣ live_video.mp4
┃ ┃ ┗ speeding_5.png
┃ ┗ videos/
┃   ┣ cars.mp4
┃   ┣ speed_car_sound.mp4
┃   ┣ speed_car_sound.wav
┃   ┗ test3.mp4
┣ project_screenshots/
┃ ┣ 1.jpg
┃ ┣ 10.png
┃ ┣ 11.png
┃ ┣ 2.jpg
┃ ┣ 3.2.png
┃ ┣ 3.jpg
┃ ┣ 4.jpg
┃ ┣ 5.jpg
┃ ┣ 6.jpg
┃ ┣ 7.png
┃ ┣ 8.jpg
┃ ┗ 9.png
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
┃ ┣ alpr_video.cpython-37.pyc
┃ ┣ detection.cpython-37.pyc
┃ ┣ get_devices.cpython-37.pyc
┃ ┣ livevehicle.cpython-37.pyc
┃ ┣ plate_video.cpython-37.pyc
┃ ┣ traffic_detection.cpython-37.pyc
┃ ┗ traffic_light.cpython-37.pyc
┣ all_vehicle.py
┣ alpr_video.py
┣ base_station.py
┣ detection.py
┣ get_devices.py
┣ livevehicle.py
┣ plate_video.py
┣ readme.md
┣ requirements.txt
┣ send_challan.py
┣ traffic_detection.py
┣ traffic_light.py
┗ vehicle_video.py
</pre>

1. Clone this repo my making branch as Auto-Traffic-Control

2. Download the assets - https://drive.google.com/drive/folders/1n48ZKeYSlM2oW4kXVLzN0ytaH7sh__Ek?usp=sharing

3. Download the utils - https://drive.google.com/drive/folders/1LI5XxQiGVdn2bsYVTPYaEAaIj_Bnk6OI?usp=sharing

<p>The folder should/must look like the folder structure above</p>

4. Install all packages

   ```
   pip install -r requirements.txt

   ```

5. Make some <h3>necessary changes</h3> in the files

   ```
   1. Open alpr_video.py and go to the main_plate() function in mydb = mysql.connector.connect(user='user_name', password='password',host='localhost', database='db_name', auth_plugin='mysql_native_password'). Provide correct username, password, host, and databse name which you have created previously in pre-requisite section.

   2. After opening base_station.py  -

      a. go to the fine() function give your access token you copied from the pre-requisite section under installation of pushbullet <pushbullet-access-token> so it should look like

      os.system(f"python send_challan.py xxxxxyyyxx123 note {get_devices.get_device_api()}")

      b. Similarly go to the challan() and paste the same access-token there.

   3. Go to the get_devices.py and go to the header line in get_device_api() and paste the access-token <pushbullet-access-token>

   4. Similar to 01, Open send_challan.py and go to the challan() function in mydb = mysql.connector.connect(user='user_name', password='password',host='localhost', database='db_name', auth_plugin='mysql_native_password'). Provide correct username, password, host, and databse name which you have created previously in pre-requisite section.

   There are mysql command in various files please change if you are changing the column and row names while creating the table in the mysql workbench or follow the same method that are provided in the images in the pre-requisite section.

   ```

6. Run commands -

   ```
   1. conda activate virtual_env_name
   2. python base_station.py

   ```

7. Now the dashboard will open with various options. When a video frame opens to close it please enter letter "q" (smallcase) to exist from the frame to the dashboard or try clicking on ❌. And to exit from the program click on the exit button on the dashboard. You can follow https://www.youtube.com/watch?v=D6Qqi1Od_2k&ab_channel=Adhyayan to see the working.

8. All live images and screenshots captured during processing is stored in assets/output folder.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See <a href="https://github.com/Adhyayanpradhan/computer_vision/blob/a38e6584c474cb31722bb40590feefd5f80aae02/LICENSE">MIT LICENSE</a> for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

<div>
  <p>Adhyayan Pradhan-</p>
  <p>![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) - pradhanadhyayan@gmail.com</p>
  <p>
    Linkedin - https://www.linkedin.com/in/pradhan-adhyayan/<span>
    <a href="https://www.linkedin.com/in/pradhan-adhyayan/">
  <img align="left" alt="Adhyayan's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
    </a>
    </span>
  </p>
</div>
 

Project Link: [https://github.com/Adhyayanpradhan/computer_vision/tree/Auto-Traffic-Control](https://github.com/Adhyayanpradhan/computer_vision/tree/Auto-Traffic-Control)

<p align="right">(<a href="#top">back to top</a>)</p>

[product-screenshot1]: ./project_screenshots/1.jpg
[product-screenshot2]: ./project_screenshots/5.jpg
[product-screenshot3]: ./project_screenshots/8.jpg
[product-screenshot4]: ./project_screenshots/3.jpg
[product-screenshot5]: ./project_screenshots/3.jpg
[product-screenshot6]: ./project_screenshots/3.2.png
[product-screenshot7]: ./project_screenshots/4.jpg
[product-screenshot8]: ./project_screenshots/2.jpg
[linkedin-url]: https://www.linkedin.com/in/pradhan-adhyayan/
[license: mit]: https://github.com/Adhyayanpradhan/computer_vision/blob/a38e6584c474cb31722bb40590feefd5f80aae02/LICENSE
