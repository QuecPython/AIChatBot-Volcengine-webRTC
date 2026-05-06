# QuecPython AI ChatBot English Documentation

## Table of Contents

- [Introduction](#Introduction)

- [Features](#Features)

- [Quick Start](#Quick-Start)
    - [Prerequisites](#Prerequisites)
    
    - [Installation](#Installation)
    
    - [Running the Application](#Running-the-Application)
    
- [Directory Structure](#Directory-Structure)

- [Contributing](#Contributing)

- [License](#License)

- [Support](#Support)

## Introduction

QuecPython has launched an AI chatbot solution based on Doubao webRTC\. This solution is based on Volcengine RTC library and can only use firmware that supports TiktokRTC functionality.

The module models supporting this feature are as follows:

|Series|Model|
|---|---|
|EC600M|EC600MCN\_LE|
|EC800M|EC800MCN\_LE, EC800MCN\_GB|
|EG810M|EG810MCN\_GA\_VOLTE|

## Features

- Support for agent switching\.

- Support for voice timbre switching\.

- Support for ASR subtitles\.

- Support for TTS subtitles\.

- Support for voice interruption/barge\-in\.

- Support for server address switching\.

- Support for voice wake\-up\.

- Written in Python language, facilitating secondary development\.

## Quick Start

### Prerequisites

Before you begin, please ensure you have the following prerequisites:

- **Hardware:**

    - EC600MCNLE QuecPython Standard Development Board \(including antenna, Type\-C data cable, etc\.\)

        > - Click to view the development board [Schematic](https://images.quectel.com/python/2023/05/EC600X_EVB_V3.2-SCH.pdf) and [Silkscreen Diagram](https://images.quectel.com/python/2023/05/EC600X_EVB_V3.2-%E4%B8%9D%E5%8D%B0.pdf) documentation\.
        > 
        > - [QuecMall Purchase Link](https://www.quecmall.com/goods-detail/2c90800c916a8eb501918d85528b017b)
        > 
    
- Computer \(Windows 7, Windows 10, or Windows 11\)
  
- LCD Display
  
    - Model: ST7789
        - Resolution: 240×240
    
    - Speaker

        - Any speaker with 2\-5W power will work

        - [QuecMall Purchase Link](https://www.quecmall.com/goods-detail/2c90800c9488358b01956aa656680239)

- **Software:**

    - USB driver for QuecPython module: [QuecPython\_USB\_Driver\_Win10\_ASR](https://images.quectel.com/python/2023/04/Quectel_Windows_USB_DriverA_Customer_V1.1.13.zip)

    - Debugging tool [QPYcom](https://images.quectel.com/python/2022/12/QPYcom_V3.6.0.zip)

    - QuecPython [Firmware](https://github.com/QuecPython/AIChatBot-Volcengine-webRTC/releases/download/v1.0.0/EC600MCNLER06A01M08_OCPU_QPY_TEST0213.zip)

    - Python text editor \(e\.g\., [VSCode](https://code.visualstudio.com/), [Pycharm](https://www.jetbrains.com/pycharm/download/)\)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/QuecPython/AIChatBot-Volcengine-webRTC.git
    cd AIChatBot-Volcengine-webRTC
    ```

2. **Install USB driver**

3. **Flash firmware:**
Follow the [instructions](https://developer.quectel.com/doc/quecpython/Getting_started/en/4G/flash_firmware.html) to flash the firmware onto the development board\.

> Note: The Volcengine conversation token in the firmware is for temporary testing purposes and may be revoked at any time\. For usage experience, please contact Quectel technical support\.
> If you have your own Volcengine token, you can directly configure it through the `tiktok.config` interface\.
> 
> 

### Running the Application

1. **Hardware connection:**
Connect the hardware as shown in the following diagram:

    1. Connect the speaker to the pin headers marked `SPK+` and `SPK-` in the diagram\.

    2. Connect the LCD screen to the pin headers marked with `LCD`\.

    3. Insert an available Nano SIM card in the indicated position\.

    4. Connect the antenna to the antenna connector marked `LTE`\.

    5. Use a Type\-C data cable to connect the development board to the computer\.

2. **Download code to the device:**

    - Launch the QPYcom debugging tool\.

    - Connect the data cable to the computer\.

    - Press the **PWRKEY** button on the development board to start the device\.

    - Follow the [instructions](https://developer.quectel.com/doc/quecpython/Getting_started/en/4G/first_python.html#Transferring-the-Script-File-to-the-Module) to import all files in the `code` folder into the module\&\#39;s file system, preserving the directory structure\.

3. **Run the application:**
    - Select the `File` tab\.
    
    - Select the `ai_main.py` script\.
    
    - Right\-click and select `Run` or use the `Run` shortcut button to execute the script\.
    
4. **Reference runtime logs:**

```python
import example
>>> example.exec('/usr/ai_main.py')
window show over
volume: 6
>>> lte network normal
ai task running
# Press KEY1 to enter the agent
rtc_queue key event 1
start rtc
TIKTOK_RTC_EVENT_START
TIKTOK_RTC_EVENT_TTS_TEXT Hello
TIKTOK_RTC_EVENT_TTS_TEXT Hello there
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I can
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I can help
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I can help you
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I can help you with
TIKTOK_RTC_EVENT_TTS_TEXT Is there anything I can help you with?
# Press KEY2 to exit the agent
rtc_queue key event 2
stop rtc
```

## Directory Structure

```plaintext
solution-AI/
├── code/
│   ├── ai_main.py
│   ├── datetime.py
│   ├── ...
│   └── img/
│       ├── battery/
│       │   ├── bat_00.png
│       │   ├── bat_01.png
│       │   └── ...
│       ├── signal/
│       │   ├── signal_00.png
│       │   ├── signal_01.png
│       │   └── ...
│       ├── image1.png
│       ├── image2.png
│       └── ...
├── examples/
│   └── examples_ai.py
├── docs/zh/media/
│           └── wire_connection.jpg
├── EC600MCNLER06A01M08_OCPU_QPY_TEST0213.zip
├── LICENSE
├── readme.md
└── readme_zh.md
```

## Contributing

We welcome contributions to improve this project\! Please follow these steps to contribute:

1. Fork this repository\.

2. Create a new branch \(`git checkout -b feature/your-feature`\)\.

3. Commit your changes \(`git commit -m 'Add your feature'`\)\.

4. Push to the branch \(`git push origin feature/your-feature`\).

5. Open a Pull Request\.

## License

This project uses the Apache license\. Please refer to the LICENSE file for details\.

## Support

If you have any questions or need support, please refer to the [QuecPython Documentation](https://developer.quectel.com/doc/quecpython/en/index.html) or open an issue in this repository\.
